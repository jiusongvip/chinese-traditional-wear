## Images Findings

### Image Sources

All 20 images on the homepage are served from `images.unsplash.com`. Category pages use the same Unsplash source. No locally hosted images exist.

### Alt Text Analysis

| Finding | Detail |
|---------|--------|
| Homepage hero | "Traveler in traditional Chinese Hanfu standing before ancient pagoda" — descriptive and keyword-rich |
| Category cards | "Hanfu traditional clothing experience in Xi'an & Luoyang", "Tang Suit traditional clothing experience in Beijing", etc. — good |
| Gallery section | All 6 gallery images use the same src and alt text — repetitive, lost opportunity |
| Dynasty cards | "Han Dynasty traditional clothing", "Tang Dynasty traditional clothing", etc. — acceptable |

**Issue**: The gallery section images all have the same alt text ("Hanfu photoshoot at Xi'an ancient city wall") despite showing different locations. This is a clear content quality signal issue.

### Image Format

| Format | Status |
|--------|--------|
| WebP/AVIF | Not explicitly used. Unsplash `auto=format` may serve WebP but isn't guaranteed |
| JPEG | Default from Unsplash |
| Responsive sizes | No `srcset` or `sizes` attributes |

### Image Dimensions

| Finding | Detail |
|---------|--------|
| Explicit width/height | Not set on most images — CLS risk |
| aspect-ratio CSS | Used on hero container (aspect-[4/5]), but not on all image containers |

### Missing Image Opportunities

| Page | Issue |
|------|-------|
| /hanfu/ | 0 images on what should be a visually rich page |
| /qipao-cheongsam/ | 0 images on a fashion/style page |
| /dynasties/ | 0 images on a dynasty overview page |
| All category pages | parse_html detected 0 images — images may be loaded via JavaScript or are missing |

### Recommendations

1. Self-host key images (hero, category cards) for consistent CDN performance
2. Use `<picture>` with WebP/AVIF sources + JPEG fallback
3. Add `srcset` with 2-3 breakpoints for responsive loading
4. Add explicit `width`/`height` to all `<img>` elements
5. Fix gallery alt text — each image should have a unique, descriptive alt
6. Add images to category pages (hanfu, qipao-cheongsam, dynasties, etc.)
7. Add ImageObject schema for hero and key images

### Summary
- Alt text quality is good where present
- Gallery section has repetitive alt text
- All images are externally hotlinked with no format optimization
- No `srcset`, no responsive images, no explicit dimensions
- Category pages appear to have 0 images in their static HTML output
