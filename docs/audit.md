# Live website audit

## Audit summary

**Summary:** the new starter site was fully reachable; the audit-driven revision adds useful service detail, explicit section summaries, persistent service shortcuts, and contextual cross-links. A fresh live crawl verified the improvements.

On **2026-11-15**, Firecrawl crawled the initial `starter-v1` deployment and then the improved `audited-v2` deployment. Both crawls returned all six expected content pages with HTTP 200. No missing content pages, orphan pages, or broken in-scope anchor targets/fragments were observed. This is an audit of a newly created starter website, not a pre-existing Praia Digital site or business.

## Source revisions and deployment evidence

**Summary:** the initial and improved versions were checked only after their corresponding GitHub Pages builds completed.

| Version | Source commit | Pages build | Built at UTC |
| --- | --- | --- | --- |
| Initial `starter-v1` | [7eb448e](https://github.com/priyapondi10-tech/praia-digital/commit/7eb448ed202a41cb106e23e58631deac06fdac44) | `1371600331` | `2026-11-15T11:05:54Z` |
| Improved `audited-v2` | [3347045](https://github.com/priyapondi10-tech/praia-digital/commit/334704598c5328fa18a8c2733969c0884177dc81) | `1371609451` | `2026-11-15T11:10:37Z` |

Pages serves `main` from `/` at [the public project URL](https://priyapondi10-tech.github.io/praia-digital/), with HTTPS enforced and no custom domain. This evidence-only documentation commit does not change the HTML, CSS, routes, or sitemap tested in the improved revision.

## Crawl method and coverage

**Summary:** compare live navigation discovery with the six intended canonical routes, retaining full HTML so repeated menus do not masquerade as contextual content.

- Tool: Firecrawl v2 crawl; start URL is the project home page.
- Scope: `/praia-digital/` and service routes only. External links and subdomains were disabled. Sitemap discovery was skipped to test reachability through links.
- Discovery depth: 3. Page limit: 12, above the six expected pages.
- Formats: markdown, raw HTML, links. Full-page content was retained. Cache age was 0 and cache storage was disabled; verification also requested `Cache-Control: no-cache`.
- Initial crawl: `2026-11-15T11:06:10.460Z` to `2026-11-15T11:06:13.254Z`, completed 6/6, 6 credits reported.
- Verification crawl: `2026-11-15T11:11:27.628Z` to `2026-11-15T11:11:33.607Z`, completed 6/6, 6 credits reported.
- Total reported usage: **12 Firecrawl credits** on the connected account. No monetary price is inferred from credit usage.
- Neither response indicated another results page. Some page responses reported concurrency throttling, but all six pages completed successfully in each crawl.
- The tool returned completed results without a crawl-job identifier. Individual page scrape IDs are recorded below instead of inventing a job ID.

The expected pages are [Home](https://priyapondi10-tech.github.io/praia-digital/), the [service hub](https://priyapondi10-tech.github.io/praia-digital/services/), and all four guides listed in the [service catalogue](service-catalog.md).

## Before-and-after content and links

**Summary:** expand content to answer decision questions, not to satisfy an assumed search-engine word-count rule.

| Page | Initial main words | Verified main words | Initial contextual service links | Verified contextual service links | Final HTTP |
| --- | ---: | ---: | ---: | ---: | --- |
| Home | 212 | 346 | 4 | 4 | 200 |
| Service hub | 251 | 412 | 4 | 4 | 200 |
| Web Design & Development | 231 | 523 | 1 | 3 | 200 |
| SEO & Content | 236 | 525 | 1 | 3 | 200 |
| Digital Marketing | 228 | 522 | 1 | 3 | 200 |
| Website Care | 237 | 531 | 1 | 3 | 200 |

Counts use text inside `main`, excluding navigation inside it and repeated page headers/footers. Headings, lists, summary boxes, and FAQ answers are included. Contextual link counts are distinct destination service pages in main body content, excluding menus, breadcrumbs, and links to the current service. They are not raw counts of repeated anchors.

The initial service pages already explained broad scope, process, and preparation. Their 228–237-word length prompted an editorial completeness review, not an automatic 'thin content' or SEO penalty verdict. Useful information gaps were explicit review criteria, scannable section summaries, service-summary boxes, and answers to common scope questions. The home page and hub were assessed as directory pages rather than against service-page length expectations.

## Findings and changes

**Summary:** preserve the working baseline and improve missing explanations and service relationships without inventing defects or business claims.

| Area | Initial finding | Implemented and verified result |
| --- | --- | --- |
| Reachability | All six pages reachable; no orphan pages | All six remain reachable through live navigation |
| Link health | No broken in-scope content targets/fragments observed | None observed in the verification crawl |
| Navigation | Home, Services, and Documentation were consistent; switching between services relied on the hub or one body suggestion | Added How to choose and visible shortcuts to all four services on every content page; retained breadcrumbs and added section navigation |
| Content depth | Broad starter descriptions lacked explicit review criteria and common scope answers | Each guide now has fit, deliverables, process/review, preparation, questions, and related-service sections, each with a concise summary |
| Related services | One contextual complementary service per guide | Three contextual complementary services per guide, with reasons; 12 directed service-to-service relationships instead of 4 |
| Documentation | Initial source map and editing notes existed | Expanded catalogue summaries, relationship rationales, content rules, deployment instructions, and audit evidence |

The [home page](../index.html) and [service hub](../services/index.html) now include clearer section introductions and connected project routes. Every individual guide has a service-summary box, six section summaries, two FAQs, and contextual links to all three complementary services. These links describe real workflow relationships rather than unexplained lists added solely for search visibility.

## Validation results

**Summary:** source checks and fresh live checks passed for the improved content revision; manual browser and business fact reviews remain separate.

- `python3 scripts/check_site.py`: **7 HTML files, 6 canonical content pages, 5 Markdown files; 0 errors**.
- Structural checks covered local HTML targets/fragments, duplicate IDs, unique titles/descriptions, canonical URLs, sitemap equality, visible service-shortcut coverage, required service sections, summary/FAQ presence, contextual related-service coverage, and local Markdown file targets.
- Additional checks confirmed a summary directly inside each service section and verified that in-repository GitHub documentation links point to existing retrieved files.
- Fresh Firecrawl verification found HTTP 200 and `audited-v2` on **all six pages**.
- Live primary-menu labels and destinations were consistent across all six pages. All four service shortcuts were present on each page.
- Each of the four service guides contained six section summaries, one service-summary box, two FAQs, and three contextual related-service destinations.
- All observed in-scope page targets and section fragments resolved against the six crawled pages; no broken internal content links were found.

The [content guide](content-guide.md) describes how to repeat these checks after future edits. The validator protects structure and targets; it cannot decide whether a service claim is true or whether a paragraph is useful.

## Per-page scrape evidence

**Summary:** the identifiers below tie each observed live page to its initial and verification scrape result.

| Page | Initial Firecrawl scrape ID | Verification Firecrawl scrape ID |
| --- | --- | --- |
| Home | `01a1dee2-d80a-759e-b941-698916150cf0` | `01a1dee7-ae4c-7276-8430-08e5a4ba6a47` |
| Service hub | `01a1dee2-da3d-72de-ba0c-1781200e1c4b` | `01a1dee7-b185-719c-8adc-08cc92d2e6c9` |
| Web Design & Development | `01a1dee2-da4f-776e-b6bc-4888163e8d31` | `01a1dee7-b18c-7780-aa1e-e5fca7d8031c` |
| SEO & Content | `01a1dee2-da5c-75f9-8446-77c10bdb33a9` | `01a1dee7-b194-7138-be09-990c825ecc5b` |
| Digital Marketing | `01a1dee2-da67-7310-8ba9-fddd80ce853b` | `01a1dee7-b19a-7429-8e8c-014d2b05205c` |
| Website Care | `01a1dee2-da72-7287-96ed-c0decdbb5fb9` | `01a1dee7-b1a1-77f3-a580-28d071f50b07` |

## Limits and owner follow-up

**Summary:** the site is published and the requested navigation/editorial audit is complete, but starter service definitions still need real business details before commercial use.

No real-world capability, availability, pricing, clients, credentials, search rankings, conversion performance, legal compliance, or accessibility certification was independently verified. No fabricated claims were added. External destinations were not crawled as part of the site graph; repository documentation targets were checked against source files. Live asset performance, browser visual review, keyboard interaction, and assistive-technology testing were not part of the Firecrawl link/content verification and remain manual follow-up.

No contact channel, enquiry backend, advertising, analytics, consent collection, or monitoring service was activated. Confirm service facts, ownership, commercial terms, and an approved contact route before accepting enquiries. Follow the [content guide](content-guide.md) when adding them.

Return to the [documentation index](README.md), [service catalogue](service-catalog.md), [repository overview](../README.md), or [live service directory](https://priyapondi10-tech.github.io/praia-digital/services/).
