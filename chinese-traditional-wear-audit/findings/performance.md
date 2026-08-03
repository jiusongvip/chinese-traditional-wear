## Performance Findings (Estimated)

### Resource Summary

| Resource | Size | Impact |
|----------|------|--------|
| CSS bundle 1 (index.D_HPQqOj.css) | 21.4 KB | Good — main styles |
| CSS bundle 2 (index.DmfNAlA2.css) | 21.3 KB | Good — component styles |
| Google Fonts (Outfit + Noto Serif SC) | External CDN | Render-blocking, no font-display: swap |
| Unsplash images | External CDN | ~20 images on homepage, mixed loading strategies |
| Inline JavaScript | ~8 KB | Acceptable — interactive map + FAQ toggles |
| Total CSS | ~43 KB | Acceptable |

### Render-Blocking Resources

| Resource | Issue | Fix |
|----------|-------|-----|
| Google Fonts CSS | Blocks text rendering until fonts load | Add `&display=swap` to font URL; self-host fonts for production |
| No preload hints | Critical CSS not prioritized | Add `<link rel="preload">` for hero image |
| No async/defer on scripts | Inline scripts block parsing | Move scripts to end of body (already done for most) |

### Image Optimization

| Issue | Detail |
|-------|--------|
| External hotlinking | All images served from images.unsplash.com — no control over CDN performance, caching, or format |
| No srcset | Images have single `src` — no responsive image sizes |
| No WebP/AVIF | Unsplash URLs use `auto=format` parameter which may serve modern formats, but not guaranteed |
| Mixed loading strategies | Hero image uses `loading="eager"`, others use `loading="lazy"` — this is correct |
| No explicit dimensions | Missing `width`/`height` attributes on many images — CLS risk |

### Core Web Vitals Estimates

| Metric | Estimate | Risk |
|--------|----------|------|
| LCP | 2.5-4.0s | Moderate-High — external Unsplash hero image + Google Fonts |
| INP | <50ms | Low — minimal JavaScript |
| CLS | 0.05-0.15 | Moderate — font swap, missing image dimensions |

### Recommendations

1. Self-host fonts with `font-display: swap` to eliminate render-blocking and CLS
2. Self-host optimized images or use a proxied image CDN
3. Add explicit `width` and `height` to all `<img>` tags
4. Add `<link rel="preload">` for the hero image
5. Minify CSS further (Tailwind purging is already in place)

### Summary
- Lightweight site overall (no heavy JS frameworks)
- Main performance bottlenecks: Google Fonts render-blocking and external Unsplash images
- CSS bloat from unused Tailwind utilities is likely minimal (Astro purges at build)
