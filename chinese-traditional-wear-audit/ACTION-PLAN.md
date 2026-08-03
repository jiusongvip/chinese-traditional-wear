# Chinese Traditional Wear — SEO Action Plan

## Phase 1: Critical Fixes (Week 1)

### Schema Implementation (0 → 60)
- [ ] Add `Organization` + `WebSite` JSON-LD to homepage
- [ ] Add `FAQPage` schema to homepage FAQ section (8 items)
- [ ] Add `FAQPage` schema to /faq/ page
- [ ] Add `BreadcrumbList` schema to all content pages
- [ ] Add `Article` schema to all content pages (hanfu, qipao-cheongsam, tang-suit, zhongshan, ethnic, accessories, dynasties, how-to-wear, plan-trip, all plan-trip subpages)

### Foundational SEO
- [ ] Create `robots.txt` with sitemap pointer, crawl-delay, and AI crawler directives
- [ ] Generate `sitemap.xml` listing all 23 pages with lastmod dates
- [ ] Add `<link rel="canonical">` to BaseLayout (dynamic per-page)
- [ ] Replace meta-refresh redirects on /qipao/ and /tang/ with proper 301 redirects

**Effort**: ~3-4 hours | **Impact**: Schema, crawlability, duplicate content prevention

---

## Phase 2: High-Impact Improvements (Weeks 2-3)

### Social & Sharing
- [ ] Add Open Graph tags (`og:title`, `og:description`, `og:image`, `og:url`, `og:type`) to BaseLayout
- [ ] Add Twitter Card tags (`twitter:card`, `twitter:title`, `twitter:description`, `twitter:image`) to BaseLayout
- [ ] Create default social share image (1200x630px)

### Thin Content Pages — Bulk Content Expansion

Priority order:
- [ ] Expand /faq/ from 158 to 800+ words (add 10+ FAQ items with detailed answers)
- [ ] Expand /dynasties/ from 243 to 600+ words (add per-dynasty details, migration paths, visual timeline)
- [ ] Expand /how-to-wear/ from 257 to 800+ words (step-by-step visual guides)
- [ ] Expand /tang-suit/ from 180 to 800+ words (history, styles, craftsmanship, where to buy)
- [ ] Expand /zhongshan/ from 161 to 600+ words (history, design elements, modern relevance)
- [ ] Expand /ethnic/ from 141 to 800+ words (Miao, Bai, Tibetan, Uyghur, Yao, Dong details)
- [ ] Expand /accessories/ from 169 to 600+ words (fan, hairpin, jade, shoes, jewelry categories)
- [ ] Expand plan-trip subpages to 500+ words each (6 subpages)

### E-E-A-T Signals
- [ ] Create /about/ page with site mission, author bio(s), credentials
- [ ] Add visible publication dates to all content pages
- [ ] Add author byline to article-type pages

### Fix Encoding Bugs
- [ ] Fix garbled UTF-8 characters in /dynasties/ and /accessories/ meta descriptions

**Effort**: ~15-20 hours | **Impact**: Content quality, social sharing, E-E-A-T, thin content elimination

---

## Phase 3: Content & Authority (Month 2)

### Blog Launch
- [ ] Write and publish 5 foundational blog posts:
  1. "Chinese Traditional Wear: A Complete Guide for First-Time Visitors" (2,000+ words)
  2. "Hanfu vs Qipao vs Tang Suit: Which Should You Wear in China?"
  3. "The History of Chinese Silk: From Ancient Trade to Modern Fashion"
  4. "10 Best Hanfu Photoshoot Locations in China (with Prices)"
  5. "Chinese Wedding Traditions: What to Wear and Why"

### Performance Optimization
- [ ] Self-host Google Fonts with `font-display: swap`
- [ ] Add `width` and `height` attributes to all `<img>` tags
- [ ] Add `<link rel="preload">` for hero image
- [ ] Implement responsive images with `srcset` and `sizes`

### Image Strategy
- [ ] Self-host hero and category card images
- [ ] Convert key images to WebP with JPEG fallback
- [ ] Add unique, descriptive alt text to all gallery images
- [ ] Add `ImageObject` schema to key images

**Effort**: ~20-30 hours | **Impact**: Content depth, long-tail keywords, performance, image SEO

---

## Phase 4: Monitoring & Iteration (Ongoing)

### Weekly
- [ ] Publish 1-2 blog posts targeting long-tail keywords
- [ ] Monitor Google Search Console for indexing and ranking changes
- [ ] Track Core Web Vitals via PageSpeed Insights

### Monthly
- [ ] Review and update existing content for freshness
- [ ] Identify new keyword opportunities from GSC data
- [ ] Check for broken links

### Quarterly
- [ ] Full site crawl and audit
- [ ] Backlink profile review
- [ ] Competitive analysis update

### Future Enhancements
- [ ] Create `/llms.txt` with structured content summary
- [ ] Add hreflang tags if multi-language pages are added
- [ ] Implement "Cite this page" feature on authoritative content
- [ ] Add interactive tools (quiz, comparison tool) with proper schema

---

## Effort Summary

| Phase | Timeframe | Effort | Critical Actions |
|-------|-----------|--------|------------------|
| Phase 1: Critical Fixes | Week 1 | 3-4 hrs | Schema, robots.txt, sitemap, canonical URLs |
| Phase 2: High-Impact | Weeks 2-3 | 15-20 hrs | OG tags, thin content expansion, E-E-A-T, encoding fixes |
| Phase 3: Content & Authority | Month 2 | 20-30 hrs | Blog launch, performance, image optimization |
| Phase 4: Monitoring | Ongoing | ~5 hrs/wk | Blog cadence, GSC monitoring, content freshness |

**Estimated total to production-ready SEO baseline**: ~40-55 hours over 8 weeks.