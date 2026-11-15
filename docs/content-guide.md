# Content maintenance guide

## Purpose and factual ownership

**Summary:** give each page one distinct visitor need and verify service facts before publication.

Explain who the service fits, what it delivers, what is excluded, and how to take a useful next step. Never invent clients, evidence, outcomes, pricing, staff credentials, or contact details. Starter service definitions need owner confirmation before they become commercial commitments. Refer to the [catalogue](service-catalog.md) for the intended boundaries.

## Required service-page sections

**Summary:** make pages easy to scan while answering the questions needed to choose and scope the work.

Each individual guide has one H1, a short service-summary box, a linked on-page contents list, and six sections: `fit`, `deliverables`, `process`, `prepare`, `questions`, and `related`. Start each section with a concise `p.section-intro` summary. Include concrete deliverables, review criteria, exclusions, preparation requirements, and at least two useful FAQs. Do not pad text to meet a word count. A short page can trigger review, but completeness and distinct purpose decide whether expansion is needed.

## Navigation and contextual links

**Summary:** provide both predictable menus and explanations for moving between related services.

The primary menu contains Home, Services, How to choose, and Documentation. A separate visible Service shortcuts navigation links all four guides without requiring a hover action or JavaScript. Each guide has a breadcrumb back to the hub and a current-page marker in the shortcuts. Preserve navigation labels and keyboard focus styles.

Every service guide should include at least two distinct contextual links to related service pages; the current four-service catalogue links all three complementary guides. Explain why each destination helps. Do not count repeated header, breadcrumb, footer, or on-page menu links as contextual recommendations. Use descriptive service names, not 'click here'.

Use `/praia-digital/` base paths and trailing slashes for public directories. When renaming a route, update home cards, hub cards, both menus, breadcrumbs, related-service lists, canonical URLs, the sitemap, and documentation together. GitHub Pages does not provide arbitrary server-side redirects; plan a static redirect page if an old address must remain usable.

## Validation and publication

**Summary:** validate source structure, wait for deployment, and check the public result separately.

1. Confirm the page purpose, service facts, exclusions, and approvers.
2. Run `python3 scripts/check_site.py` from the repository root. It checks local HTML targets/fragments, metadata, sitemap coverage, required service sections and summaries, menu coverage, related-service targets, and local Markdown file links.
3. Review keyboard navigation, zoom, narrow-screen layout, and FAQ controls in a browser. Automated HTML checks do not certify accessibility.
4. Commit approved changes to `main`. Pages publishes `/` with `.nojekyll`; no build dependencies or custom domain are configured.
5. Wait for the latest Pages build to report `built` for the intended revision. Verify the live `site-revision` marker instead of assuming the source is already public.
6. Crawl all six expected content pages with Firecrawl after meaningful navigation or content changes. Keep the crawl inside `/praia-digital/`, disable cached content, and retain full HTML to inspect navigation.
7. Compare expected and observed URLs, HTTP status, internal targets/fragments, main-content explanations, and contextual service links. Record evidence and limits in the [audit log](audit.md).

For local preview, follow the [repository overview](../README.md). Project-level `robots.txt` files do not control the account host root, so this repository does not pretend to configure host-wide crawler rules.

## Data handling and operational boundaries

**Summary:** publishing static service guides does not activate external systems or authorise data collection.

No enquiry backend, analytics, advertising, monitoring service, or external integration is enabled. Agree access, consent, data handling, and implementation separately if those are added later. Never place secrets or customer data in public content or issues. Git history recovers source changes, not unrelated databases or external services.

Return to the [documentation index](README.md), [service catalogue](service-catalog.md), or [live service hub](https://priyapondi10-tech.github.io/praia-digital/services/).
