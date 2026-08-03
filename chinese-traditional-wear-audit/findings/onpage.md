## On-Page SEO Findings

### Title Tags

| Page | Title | Length | Keyword "Chinese Traditional Wear" |
|------|-------|--------|-----------------------------------|
| Homepage | Chinese Traditional Wear: Where to Experience Hanfu, Qipao & More in China | 89 chars | At start |
| /hanfu/ | Hanfu Guide: Best Cities, Costs & Travel Tips \| ChinaStyle | 56 chars | No |
| /qipao-cheongsam/ | Qipao & Cheongsam: Shanghai Tailoring, Suzhou Silk \| ChinaStyle Travel Guide | 85 chars | No |
| /tang-suit/ | Tang Suit Guide: Beijing Tailors & Festive Wear \| ChinaStyle | 59 chars | No |
| /zhongshan/ | Zhongshan Suit Guide: Mao Suit History & Tailors \| ChinaStyle | 65 chars | No |
| /ethnic/ | Ethnic Minority Clothing in China: Miao, Bai & More \| ChinaStyle | 68 chars | No |
| /accessories/ | Chinese Traditional Accessories: Where to Buy \| ChinaStyle | 61 chars | No |
| /dynasties/ | Chinese Clothing by Dynasty: Travel Guide \| ChinaStyle | 53 chars | No |
| /how-to-wear/ | How to Wear Traditional Chinese Clothing: Travel Guide \| ChinaStyle | 69 chars | No |
| /faq/ | Chinese Traditional Wear FAQ: Travel Questions Answered \| ChinaStyle | 69 chars | Yes |
| /plan-trip/ | Plan Your Trip: Chinese Traditional Wear Travel Guide \| ChinaStyle | 67 chars | Yes |
| /compare/ | Hanfu vs Qipao vs Kimono: Chinese Traditional Wear Comparisons \| ChinaStyle | 79 chars | Yes |
| /gallery/ | Chinese Traditional Wear Gallery: Travel Photos \| ChinaStyle | 63 chars | Yes |
| /quiz/ | Which Chinese Traditional Wear Suits You? Quiz \| ChinaStyle | 63 chars | Yes |
| /blog/ | Chinese Traditional Wear Blog: Travel Stories & Tips \| ChinaStyle | 67 chars | Yes |

**Issues**:
- 11 of 15 titles exceed the 60-character truncation limit
- Most category pages lack the primary keyword "Chinese Traditional Wear"
- Title format is inconsistent: some end with "\| ChinaStyle", others with "\| ChinaStyle Travel Guide"
- The homepage title (89 chars) will be truncated in SERPs

### Meta Descriptions

| Finding | Detail |
|---------|--------|
| Present on | 15 of 23 pages (redirect pages have none) |
| Encoding bug | /dynasties/ and /accessories/ descriptions contain garbled UTF-8 characters ("бк") — likely an encoding issue from the source Astro components |
| Travel focus | All descriptions are travel-oriented, even on pages that should be informational |
| No CTA | Descriptions lack a clear call-to-action |

### Heading Structure

| Page | H1 | H2 Count | Issue |
|------|----|----------|-------|
| Homepage | "Wear China's History on Your Journey" | 8 | H1 missing primary keyword |
| /hanfu/ | 1 | 5 | Good |
| /qipao-cheongsam/ | 1 | 5 | Good |
| /plan-trip/ | 1 | 6 | Good |
| /dynasties/ | 1 | 5 | Good |
| /faq/ | 1 | 1 | Too few H2s for FAQ structure |
| /blog/ | 1 | 0 | No H2s at all |
| /compare/ | 1 | 0 | No H2s |
| /gallery/ | 1 | 0 | No H2s |
| /quiz/ | 1 | 0 | No H2s |

### Open Graph & Social

| Tag | Status |
|-----|--------|
| og:title | Missing on all pages |
| og:description | Missing on all pages |
| og:image | Missing on all pages |
| og:url | Missing on all pages |
| og:type | Missing on all pages |
| twitter:card | Missing on all pages |
| twitter:title | Missing on all pages |
| twitter:description | Missing on all pages |
| twitter:image | Missing on all pages |

### Internal Linking

| Finding | Detail |
|---------|--------|
| Navigation links | Present in header and footer (consistent across all pages) |
| In-content links | Limited. Homepage links to category pages via card grids. Category pages have minimal cross-linking. |
| Orphan pages | /blog/ is linked from footer but contains no content. /quiz/, /compare/, /gallery/ linked from footer only. |
| Anchor text | Generally descriptive ("Hanfu Photoshoots", "Qipao Tailoring", etc.) |

### Summary
- Title tags are keyword-aware but too long (73% exceed 60 chars)
- Meta descriptions have encoding bugs on 2 pages
- Zero social meta tags (Open Graph / Twitter Cards)
- Homepage H1 lacks primary keyword
- Internal linking exists via nav/footer but in-content cross-linking is sparse
