# Praia Digital

A responsive, dependency-free, English-language website with home, a service hub, and four connected service guides. The topics are owner-approved starter definitions, not independently verified business capabilities.

## Explore

Use the [live home page](https://priyapondi10-tech.github.io/praia-digital/) and [service selection guide](https://priyapondi10-tech.github.io/praia-digital/services/#choose) to find a starting point.

- [Web Design & Development](https://priyapondi10-tech.github.io/praia-digital/services/web-design-development/): page planning, responsive implementation, and handover.
- [SEO & Content](https://priyapondi10-tech.github.io/praia-digital/services/seo-content/): page purpose, useful explanations, and internal links.
- [Digital Marketing](https://priyapondi10-tech.github.io/praia-digital/services/digital-marketing/): focused campaign planning and measurement boundaries.
- [Website Care](https://priyapondi10-tech.github.io/praia-digital/services/website-care/): approved changes, recurring checks, and escalation.

## Documentation

The [documentation index](docs/README.md) connects the [service catalogue](docs/service-catalog.md), [content maintenance guide](docs/content-guide.md), and [live audit record](docs/audit.md). The catalogue maps each public page to its source and explains the related-service links.

## Structure and preview

`index.html` is the home page; `services/index.html` is the hub. Each service folder contains `index.html`. `assets/styles.css` is shared, and `sitemap.xml` lists the six canonical content pages. `.nojekyll` enables direct static serving. `404.html` provides recovery links.

Clone into a directory named `praia-digital`. From its parent run `python3 -m http.server 8000`, then open `http://localhost:8000/praia-digital/`. The base path is intentional for a GitHub Pages project site.

## Validate and publish

From the repository root run `python3 scripts/check_site.py`. It checks HTML targets and fragments, unique metadata, sitemap coverage, service shortcuts, editorial section structure, contextual service links, and local Markdown file targets. It does not replace browser accessibility testing, live HTTP checks, or editorial fact review.

GitHub Pages publishes `main` from `/` over HTTPS without a custom domain. Deployment is asynchronous. After a change, check Pages build status and the public `site-revision` marker. `starter-v1` identifies the initial live audit; `audited-v2` identifies the expanded guides. See the [audit record](docs/audit.md) for evidence and limits.

## Scope and safety

No enquiry backend, analytics, advertising, monitoring service, external integration, or contact details are configured. No testimonials, client claims, prices, credentials, or outcome guarantees have been invented. Confirm actual service availability and commercial terms before accepting enquiries. Never commit secrets or personal data. A reuse licence has not been selected; public visibility alone is not a licence.
