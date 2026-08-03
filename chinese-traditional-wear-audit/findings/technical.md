## Technical SEO Findings

### Crawlability

| Finding | Severity | Detail |
|---------|----------|--------|
| No robots.txt | Critical | No `/robots.txt` file in dist/ or public/. Search engines have no crawling directives. All pages crawlable by default but no sitemap pointer, crawl-delay, or disallow rules. |
| No sitemap.xml | Critical | No XML sitemap found. 23 pages exist but search engines must discover them organically via internal links. |
| No HTML sitemap | Low | No human-readable sitemap page for users or crawlers. |

### Indexability

| Finding | Severity | Detail |
|---------|----------|--------|
| No canonical URLs | Critical | 0 of 23 pages have a canonical link tag. Multi-version URL risk (www vs non-www, HTTP vs HTTPS, trailing slash variants) will cause duplicate content when deployed. |
| No self-referencing canonicals | Critical | Even the 2 redirect pages (/qipao/, /tang/) only redirect via `<meta http-equiv="refresh">` without a proper `<link rel="canonical">`. |
| No noindex tags | Info | Appropriate for this stage — all pages are indexable. |
| /qipao/ and /tang/ use meta refresh redirect | High | These pages use `<meta http-equiv="refresh" content="0;url=/qipao-cheongsam/">` instead of proper 301 redirects. Search engines handle meta refresh poorly for SEO value transfer. |

### URL Structure

| Finding | Severity | Detail |
|---------|----------|--------|
| Clean URLs | Good | All pages use clean `/directory/` URLs without `.html` extensions. |
| Consistent trailing slash | Good | Astro generates `/page/index.html` consistently. |

### Security & Headers

| Finding | Severity | Detail |
|---------|----------|--------|
| No HTTPS enforcement | Medium | No HSTS headers. When deployed, ensure HTTPS redirect. |
| Viewport meta present | Good | All pages include `<meta name="viewport" content="width=device-width, initial-scale=1.0">`. |
| No CSP headers | Low | No Content Security Policy defined. |
| No security headers | Medium | Missing X-Content-Type-Options, X-Frame-Options, Referrer-Policy headers (server-level config needed on deployment). |

### Core Web Vitals (Estimated)

| Metric | Status | Notes |
|--------|--------|-------|
| LCP | Moderate risk | Hero image is external Unsplash URL. Google Fonts block render. |
| INP | Low risk | Minimal JavaScript; main interaction is the interactive map which loads inline. |
| CLS | Risk | Google Fonts swap can cause layout shift. No explicit font-display: swap control. No explicit image dimensions on all images. |

### Redirects

| Source | Target | Method | SEO Value |
|--------|--------|--------|-----------|
| /qipao/ | /qipao-cheongsam/ | meta refresh (0s) | Poor — should be 301 |
| /tang/ | /tang-suit/ | meta refresh (0s) | Poor — should be 301 |

### Summary
- **Critical gaps**: robots.txt, sitemap.xml, canonical URLs (all pages)
- **High priority**: Replace meta refresh redirects with proper 301s
- CSS size: ~44KB across two files — acceptable
- No heavy JavaScript bundles visible
