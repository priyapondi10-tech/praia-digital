#!/usr/bin/env python3
"""Dependency-free structural validation for this GitHub Pages project."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit, unquote
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://priyapondi10-tech.github.io/praia-digital/'
PREFIX = '/praia-digital/'

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids, self.refs, self.canonicals = set(), [], []
        self.h1, self.lang, self.description, self.title = 0, '', '', ''
        self.in_title = False
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.add(a['id'])
        if tag == 'html': self.lang = a.get('lang', '')
        if tag == 'h1': self.h1 += 1
        if tag == 'title': self.in_title = True
        if tag == 'meta' and a.get('name') == 'description': self.description = a.get('content', '')
        if tag == 'link' and a.get('rel') == 'canonical': self.canonicals.append(a.get('href', ''))
        if tag in ('a', 'link') and a.get('href'): self.refs.append(a['href'])
        if tag in ('img', 'script') and a.get('src'): self.refs.append(a['src'])
    def handle_endtag(self, tag):
        if tag == 'title': self.in_title = False
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
    if not rel or path.endswith('/'): target = target / 'index.html'
    return target

def main():
    pages = {p: Page(p.read_text(encoding='utf-8')) for p in ROOT.rglob('*.html')}
    errors, titles, descriptions, expected = [], set(), set(), set()
    for path, page in pages.items():
        rel, url = path.relative_to(ROOT), live_url(path)
        if page.h1 != 1 or page.lang != 'en': errors.append(f'{rel}: require one H1 and lang=en')
        if not page.title: errors.append(f'{rel}: missing title')
        if path.name != '404.html':
            expected.add(url)
            if page.canonicals != [url]: errors.append(f'{rel}: incorrect canonical')
            if not page.description: errors.append(f'{rel}: missing description')
            if page.title in titles or page.description in descriptions: errors.append(f'{rel}: duplicate metadata')
            titles.add(page.title); descriptions.add(page.description)
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
    for error in errors: print('ERROR:', error)
    print(f'Checked {len(pages)} HTML files, {len(expected)} canonical content pages; {len(errors)} errors.')
    return bool(errors)

if __name__ == '__main__': sys.exit(main())
