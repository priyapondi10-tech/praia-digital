# Content maintenance guide

## Page purpose

Give each service page a distinct audience need. Explain the work, outline the process, and tell the reader what to prepare. Prefer useful detail over keyword repetition or a target word count. Never invent evidence, outcomes, prices, staff credentials, or contact information.

## Navigation and cross-links

All content pages share Home, Services, and Documentation links. Service pages include a breadcrumb and a route back to the service hub. Use descriptive link labels, not 'click here'. Keep links within the `/praia-digital/` base path and use trailing slashes for directory pages.

The [catalogue](service-catalog.md) maps live routes to HTML files. When changing a path, update the home page, hub, related service references, canonical URL, sitemap, and documentation together. Verify that the new route is live before removing an old route; GitHub Pages does not provide arbitrary server-side redirects.

## Editing checklist

1. Confirm the service facts and the page's intended purpose.
2. Use a single H1 and a logical sequence of headings.
3. Keep the title and description distinct from other pages.
4. Preserve the skip link, language attribute, and navigation labels.
5. Run `python3 scripts/check_site.py` from the repository root.
6. Review keyboard navigation, zoom, and narrow-screen layout in a browser.
7. Commit to `main`, wait for Pages, then verify the public pages and log the evidence.

## Hosting and boundaries

Pages serves the repository root on `main`; `.nojekyll` disables Jekyll processing. Assets use `/praia-digital/` paths, so preview the project from its parent directory as described in the [repository overview](../README.md). Do not add a project-level `robots.txt` and assume it controls the account domain: robots rules belong at the host root.

No analytics, advertisements, consent collection, working form, monitoring service, or external account integration is enabled. If those are later required, agree the data handling and implementation separately. Git history helps recover source changes, but it is not a backup of unrelated hosting services or databases.

## Audit log

Use [the audit record](audit.md) for crawl settings, coverage, findings, and verification limits. Report technical failures separately from editorial improvement opportunities. Return to the [documentation index](README.md).
