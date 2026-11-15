# Praia Digital

A responsive, dependency-free, English-language service website published with GitHub Pages. The four services are owner-approved starter topics, not independently verified business capabilities.

- [Live website](https://priyapondi10-tech.github.io/praia-digital/)
- [Service directory](https://priyapondi10-tech.github.io/praia-digital/services/)
- [Documentation index](docs/README.md)
- [Service catalogue and file map](docs/service-catalog.md)
- [Content maintenance guide](docs/content-guide.md)
- [Live audit record](docs/audit.md)

## Structure

`index.html` is the home page; `services/index.html` is the service hub. Each of the four service folders contains its own `index.html`. `assets/styles.css` is shared. `sitemap.xml` lists the six intended public content pages. `.nojekyll` makes Pages serve the static files directly. `404.html` provides a recovery route.

## Preview and validate

Clone into a directory named `praia-digital`. From its parent directory run `python3 -m http.server 8000`, then open `http://localhost:8000/praia-digital/`. The `/praia-digital/` base path is intentional for a GitHub Pages project site.

From the repository root run `python3 scripts/check_site.py` to check local HTML targets, fragments, canonical URLs, titles, descriptions, and sitemap coverage. This is a structural check, not a substitute for browser accessibility testing or a live crawl.

## Publishing

Publish `main` from `/` using GitHub Pages' branch-based build. No custom domain, build dependencies, analytics, cookies, advertising, or enquiry backend is configured. Deployment is asynchronous: inspect Settings → Pages and verify the public revision after each change. See the [content guide](docs/content-guide.md) before editing paths.

## Content and safety

No testimonials, client names, prices, credentials, contact details, or performance guarantees have been invented. Scope and availability require owner confirmation. Do not add credentials to this public repository. A licence has not been selected; public visibility does not itself grant a reuse licence.
