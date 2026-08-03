## Schema & Structured Data Findings

### Current Implementation

**Result**: No schema markup found on ANY of the 23 pages. Zero JSON-LD blocks. Zero microdata. Zero RDFa.

### Missing Schema Opportunities

| Page | Recommended Schema | Priority |
|------|-------------------|----------|
| Homepage | `Organization`, `WebSite` (with SearchAction), `BreadcrumbList` | Critical |
| /hanfu/ | `Article`, `FAQ`, `BreadcrumbList`, `ImageObject` | High |
| /qipao-cheongsam/ | `Article`, `FAQ`, `BreadcrumbList`, `ImageObject` | High |
| /tang-suit/ | `Article`, `BreadcrumbList` | High |
| /zhongshan/ | `Article`, `BreadcrumbList` | High |
| /ethnic/ | `Article`, `BreadcrumbList` | High |
| /accessories/ | `Article`, `BreadcrumbList` | High |
| /dynasties/ | `CollectionPage`, `BreadcrumbList` | High |
| /faq/ | `FAQPage` (critical — this page exists solely for FAQ schema) | Critical |
| /plan-trip/ | `Article`, `BreadcrumbList` | High |
| /plan-trip/budget/ | `Article`, `BreadcrumbList` | Medium |
| /plan-trip/itineraries/ | `Article`, `BreadcrumbList` | Medium |
| /plan-trip/packing/ | `Article`, `BreadcrumbList` | Medium |
| /plan-trip/seasons/ | `Article`, `BreadcrumbList` | Medium |
| /plan-trip/transport/ | `Article`, `BreadcrumbList` | Medium |
| /plan-trip/visa/ | `Article`, `BreadcrumbList` | Medium |
| /compare/ | `Article` | Medium |
| /blog/ | `Blog` (CollectionPage + BlogPosting items) | High |
| /gallery/ | `ImageGallery`, `ImageObject` (multiple) | Medium |
| /quiz/ | `WebApplication` | Low |

### FAQ Schema Opportunity

The homepage contains 8 FAQ items in a `<details>` block. These should be marked up with `FAQPage` schema. Google frequently shows FAQ rich results for informational queries — this is a high-ROI, low-effort win.

### BreadcrumbList

Every page deeper than the homepage should have `BreadcrumbList` schema. Example for /hanfu/:
```json
{
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "/" },
    { "@type": "ListItem", "position": 2, "name": "Hanfu Experiences", "item": "/hanfu/" }
  ]
}
```

### Summary
- 0/23 pages have schema — this is the single largest SEO gap
- `FAQPage` on /faq/ and homepage FAQ section would yield immediate rich-result potential
- Organization schema on homepage is table-stakes for brand authority
