#!/usr/bin/env python3
"""Dependency-free structure, navigation, editorial, and Markdown target checks."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit, unquote
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://priyapondi10-tech.github.io/praia-digital/'
PREFIX = '/praia-digital/'
SLUGS = ('web-design-development', 'seo-content', 'digital-marketing', 'website-care')
SERVICES = {BASE + 'services/' + slug + '/' for slug in SLUGS}
REQUIRED = {'fit', 'deliverables', 'process', 'prepare', 'questions', 'related'}

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids, self.duplicates, self.refs, self.canonicals = set(), [], [], []
        self.h1, self.lang, self.description, self.title = 0, '', '', ''
        self.in_title = self.in_main = self.in_shortcuts = False
        self.nav_depth = self.sections = self.summaries = self.faqs = 0
        self.main_links, self.shortcuts, self.section_ids = [], [], set()
        self.has_summary = False
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            if a['id'] in self.ids: self.duplicates.append(a['id'])
            self.ids.add(a['id'])
        if tag == 'html': self.lang = a.get('lang', '')
        if tag == 'h1': self.h1 += 1
        if tag == 'title': self.in_title = True
        if tag == 'main': self.in_main = True
        if tag == 'nav':
            self.nav_depth += 1
            if a.get('aria-label') == 'Service shortcuts': self.in_shortcuts = True
        if tag == 'meta' and a.get('name') == 'description': self.description = a.get('content', '')
        if tag == 'link' and a.get('rel') == 'canonical': self.canonicals.append(a.get('href', ''))
        if tag in ('a', 'link') and a.get('href'): self.refs.append(a['href'])
        if tag in ('img', 'script') and a.get('src'): self.refs.append(a['src'])
        if tag == 'a' and a.get('href'):
            if self.in_shortcuts: self.shortcuts.append(a['href'])
            if self.in_main and self.nav_depth == 0: self.main_links.append(a['href'])
        if self.in_main:
            classes = a.get('class', '').split()
            if tag == 'section':
                self.sections += 1
                self.section_ids.add(a.get('id', ''))
            if tag == 'p' and 'section-intro' in classes: self.summaries += 1
            if 'summary-box' in classes: self.has_summary = True
            if tag == 'details': self.faqs += 1
    def handle_endtag(self, tag):
        if tag == 'title': self.in_title = False
        if tag == 'main': self.in_main = False
        if tag == 'nav':
            self.nav_depth -= 1
            self.in_shortcuts = False
    def handle_data(self, data):
        if self.in_title: self.title += data

def live_url(path):
    rel = path.relative_to(ROOT).as_posix()
    return BASE + (rel[:-10] if rel.endswith('index.html') else rel)

def local_path(url):
    path = unquote(urlsplit(url).path)
    if not path.startswith(PREFIX): return None
    rel = path[len(PREFIX):]
    target = ROOT / rel
    return target / 'index.html' if not rel or path.endswith('/') else target

def main():
    pages = {p: Page(p.read_text(encoding='utf-8')) for p in ROOT.rglob('*.html')}
    errors, titles, descriptions, expected = [], set(), set(), set()
    for path, page in pages.items():
        rel, url = path.relative_to(ROOT), live_url(path)
        if page.h1 != 1 or page.lang != 'en': errors.append(f'{rel}: require one H1 and lang=en')
        if page.duplicates: errors.append(f'{rel}: duplicate IDs {page.duplicates}')
        if not page.title: errors.append(f'{rel}: missing title')
        if path.name != '404.html':
            expected.add(url)
            if page.canonicals != [url]: errors.append(f'{rel}: incorrect canonical')
            if not page.description: errors.append(f'{rel}: missing description')
            if page.title in titles or page.description in descriptions: errors.append(f'{rel}: duplicate metadata')
            titles.add(page.title); descriptions.add(page.description)
            shortcuts = {urljoin(url, ref).split('#')[0] for ref in page.shortcuts}
            if shortcuts != SERVICES: errors.append(f'{rel}: incomplete service shortcuts')
        if url in SERVICES:
            related = {urljoin(url, ref).split('#')[0] for ref in page.main_links} & (SERVICES - {url})
            if len(related) < 2: errors.append(f'{rel}: require two contextual related services')
            if not REQUIRED <= page.section_ids: errors.append(f'{rel}: missing required sections')
            if page.summaries != page.sections: errors.append(f'{rel}: require a summary per section')
            if not page.has_summary or page.faqs < 2: errors.append(f'{rel}: require service summary and two FAQs')
        for ref in page.refs:
            target_url = urljoin(url, ref)
            parsed = urlsplit(target_url)
            if parsed.scheme not in ('http', 'https') or parsed.netloc != urlsplit(BASE).netloc: continue
            target = local_path(target_url)
            if target is None or not target.is_file(): errors.append(f'{rel}: missing local target {ref}'); continue
            if parsed.fragment and target in pages and unquote(parsed.fragment) not in pages[target].ids:
                errors.append(f'{rel}: missing fragment {ref}')
    sitemap = {e.text for e in ET.parse(ROOT / 'sitemap.xml').findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')}
    if sitemap != expected: errors.append('Sitemap does not match public content pages')
    markdown = list(ROOT.rglob('*.md'))
    for path in markdown:
        for ref in re.findall(r'\[[^\]]+\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
            parsed = urlsplit(ref)
            if parsed.scheme or parsed.netloc or not parsed.path: continue
            target = (path.parent / unquote(parsed.path)).resolve()
            if not target.exists(): errors.append(f'{path.relative_to(ROOT)}: missing Markdown target {ref}')
    for error in errors: print('ERROR:', error)
    print(f'Checked {len(pages)} HTML files, {len(expected)} canonical pages, {len(markdown)} Markdown files; {len(errors)} errors.')
    return bool(errors)

if __name__ == '__main__': sys.exit(main())
