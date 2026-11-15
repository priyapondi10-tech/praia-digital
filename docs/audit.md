# Live website audit

## Audit summary

**Summary:** the initial live site was fully reachable and had no observed broken internal content links; the main opportunities were deeper decision-support content and more contextual service relationships.

The initial Firecrawl crawl ran on **2026-11-15, 11:06:10–11:06:13 UTC** against [the live site](https://priyapondi10-tech.github.io/praia-digital/). It returned all six expected content pages with HTTP 200 and revision marker `starter-v1`. No missing pages, orphan pages, or broken in-scope anchor targets/fragments were found.

## Source and crawl method

**Summary:** compare actual live navigation coverage with the six intended canonical routes, not just the repository file list.

- Initial source: [commit 7eb448e](https://github.com/priyapondi10-tech/praia-digital/commit/7eb448ed202a41cb106e23e58631deac06fdac44).
- Initial Pages build: `1371600331`, status `built`, completed at `2026-11-15T11:05:54Z`.
- Tool: Firecrawl v2 crawl; start URL is the project home page; sitemap discovery skipped to test link-based reachability.
- Scope: `/praia-digital/` and its service routes only; external links and subdomains disabled; discovery depth 3; limit 12, above the six expected pages.
- Formats: markdown, raw HTML, links; full-page content retained; cache age 0 and cache storage disabled.
- Completion: 6 completed / 6 total, no pagination indicated; 6 Firecrawl credits reported. Some pages reported concurrency throttling, but all completed successfully.
- The tool returned completed page results without a crawl-job identifier. Individual scrape identifiers are recorded below rather than inventing one.

Main-content word counts exclude navigation inside `main` and exclude repeated page headers and footers. They include headings, lists, and FAQ text where present. The counts are editorial review signals, not SEO ranking factors.

## Initial observations

**Summary:** preserve the working baseline and address real information gaps rather than labelling all short pages as defective.

| Page | HTTP | Main words | Contextual links to other services |
| --- | --- | ---: | ---: |
| Home | 200 | 212 | 4 |
| Service hub | 200 | 251 | 4 |
| Web Design & Development | 200 | 231 | 1 |
| SEO & Content | 200 | 236 | 1 |
| Digital Marketing | 200 | 228 | 1 |
| Website Care | 200 | 237 | 1 |

The four service pages explained broad scope, process, and preparation, but did not yet provide a service-summary box, consistent section summaries, FAQs, or explicit review criteria. Each linked one related service in body content, leaving useful complementary journeys unexplained. The primary menu consistently offered Home, Services, and Documentation; service-to-service switching relied on the hub or the single body recommendation.

## Changes implemented

**Summary:** expand decision-useful detail and connect related services in both visible navigation and contextual content.

All six pages now use revision marker `audited-v2`. Changes add a How to choose menu entry, visible shortcuts to all four services, more informative home/hub summaries, and connected project routes. Each service guide now has a service-summary box, six clearly summarised sections, concrete deliverables, process review criteria, boundaries, preparation guidance, two FAQs, and three contextual related-service recommendations with a reason for each link.

The [service catalogue](service-catalog.md), [content guide](content-guide.md), [documentation index](README.md), and [repository overview](../README.md) were updated together. The structural validator now protects section coverage, menu coverage, contextual cross-links, and documentation file targets as well as HTML targets, metadata, and sitemap consistency.

## Follow-up verification state

**Summary:** expanded content is being committed; a fresh live verification must follow the successful Pages build.

At the time of this content-improvement commit, the follow-up live crawl is pending. Do not interpret the implementation list as proof that `audited-v2` has already deployed. This section will be replaced with actual build and Firecrawl verification results.

## Initial scrape evidence

| Page | Firecrawl scrape ID |
| --- | --- |
| Home | `01a1dee2-d80a-759e-b941-698916150cf0` |
| Service hub | `01a1dee2-da3d-72de-ba0c-1781200e1c4b` |
| Web Design & Development | `01a1dee2-da4f-776e-b6bc-4888163e8d31` |
| SEO & Content | `01a1dee2-da5c-75f9-8446-77c10bdb33a9` |
| Digital Marketing | `01a1dee2-da67-7310-8ba9-fddd80ce853b` |
| Website Care | `01a1dee2-da72-7287-96ed-c0decdbb5fb9` |

## Limits and owner follow-up

**Summary:** this is a navigation and editorial audit of a newly created starter website, not evidence about a pre-existing Praia Digital business or site.

No real-world service capability, commercial availability, pricing, clients, credentials, rankings, conversion performance, legal compliance, or accessibility certification was independently verified. External destinations were not crawled as part of the site graph. Browser-based visual, keyboard, and assistive-technology testing remains a manual follow-up. No contact channel, form backend, advertising, analytics, or monitoring service was activated.

Return to the [documentation index](README.md), [service catalogue](service-catalog.md), or [live service directory](https://priyapondi10-tech.github.io/praia-digital/services/).
