# Content Quality & E-E-A-T Analysis
## Chinese Traditional Wear (ChinaStyle)

**Audit Date**: 2026-08-03
**Pages Analyzed**: 15 content pages
**Analysis Method**: content_quality.py (QRG-aligned) + manual E-E-A-T assessment

---

## Content Quality Score: 96 / 100

### Per-Page Quality Scores

| Page | Quality | Tokens | Unique | Repetition | Filler | AI Pattern |
|------|---------|--------|--------|------------|--------|------------|
| /faq/ | **97** | 1,839 | 610 | 18 | 0 | 0 |
| /how-to-wear/ | **97** | 1,629 | 505 | 23 | 0 | 0 |
| /about/ | **97** | 1,212 | 384 | 23 | 0 | 0 |
| /hanfu/ | 96 | 2,793 | 636 | 24 | 0 | 0 |
| /qipao-cheongsam/ | 96 | 2,230 | 549 | 24 | 0 | 0 |
| /tang-suit/ | 96 | 1,329 | 423 | 27 | 0 | 0 |
| /zhongshan/ | 96 | 1,358 | 434 | 27 | 0 | 0 |
| /ethnic/ | 96 | 1,437 | 461 | 25 | 0 | 0 |
| /compare/ | 96 | 1,746 | 431 | 28 | 0 | 0 |
| /dynasties/ | 96 | 1,122 | 357 | 24 | 0 | 0 |
| /accessories/ | 96 | 1,016 | 310 | 24 | 0 | 0 |
| /blog/ | 96 | 966 | 281 | 26 | 0 | 0 |
| / (homepage) | 96 | 8,616 | 929 | 30 | 0 | 0 |
| /gallery/ | 95 | 1,329 | 294 | 35 | 0 | 0 |
| /quiz/ | 95 | 921 | 255 | 29 | 0 | 0 |

**Key findings**:
- Zero filler content detected on all pages
- Zero AI-pattern matches on all pages
- Information density at 1.0 (maximum) across all pages
- Repetition scores are low (18-35 range), with /faq/ being the least repetitive and /gallery/ the most
- All pages pass QRG scaled-content-abuse detection

---

## E-E-A-T Assessment: 42 / 100

| Factor | Score (Max 25) | Key Signals |
|--------|---------------|-------------|
| Experience | **10** | No original photos, no first-person accounts, no case studies. Content is well-researched but generic. |
| Expertise | **12** | Specific prices, city names, and procedural details show domain knowledge. /about/ page exists but no individual author bios with credentials. |
| Authoritativeness | **8** | No external citations, no backlinks (not yet deployed), no brand recognition, no cited-by-expert signals. |
| Trustworthiness | **12** | Date stamps present on articles. /about/ page with mission statement. Missing: contact info, privacy policy, terms, HTTPS. |

### Detailed E-E-A-T Breakdown

#### Experience (10/25) — Weak

**What's missing**:
- Original photography: All images are stock (Unsplash). No "real traveler" photos despite gallery page claiming "real travelers."
- First-person narrative: Content reads like a well-researched guide but never uses "we tried" or "our experience." No specific anecdotes.
- Original data: Prices and procedures are listed but there's no indication they were gathered firsthand.
- Case studies: No specific trip diaries or named travelers.

**What works**:
- The /about/ page claims "firsthand research" — this is a start
- Specific procedural details (e.g., qipao fitting steps, Tang suit tailoring process) suggest domain familiarity
- City-specific recommendations are detailed and actionable

**Recommendation**: Add 2-3 first-person trip diaries. Replace some Unsplash images with real traveler photos. Add "how we researched this" notes to key guides.

#### Expertise (12/25) — Moderate

**What's missing**:
- No individual author names on any article
- No author bio page with credentials
- No mention of years of experience or specific qualifications
- No distinction between different writers/topics

**What works**:
- Content demonstrates genuine knowledge: specific fabric types, historical periods, tailoring procedures
- Prices are realistic and specific (not vague ranges)
- Cultural context is accurate and nuanced
- The /about/ page states the mission and research methodology

**Recommendation**: Add author bylines to each article. Create an authors page or add author bios with relevant credentials. Even "Written by the ChinaStyle editorial team, based on on-the-ground research" would help.

#### Authoritativeness (8/25) — Weak

**What's missing**:
- Zero external citations: No links to museum websites, academic sources, or authoritative references
- No backlinks (site not yet deployed)
- No brand mentions or industry recognition
- Not cited by other experts in the field

**What works**:
- Content is consistent and thorough
- The /about/ page establishes organizational identity

**Recommendation**: Cite authoritative sources for historical claims (Palace Museum, China National Silk Museum, academic papers). Get listed in travel directories. Build guest posts and collaborations for backlinks.

#### Trustworthiness (12/25) — Moderate

**What's missing**:
- No contact page or email address
- No privacy policy or terms of service
- No physical address or business registration
- No HTTPS (not yet deployed)
- Gallery page claims "real travelers" but uses identical Unsplash images

**What works**:
- Publication dates on all content pages (2026-08-03)
- /about/ page with mission statement and editorial approach
- Content includes practical disclaimers (e.g., "Prices are 20-30% lower")
- No affiliate marketing pressure or aggressive sales tactics

**Recommendation**: Add contact page with email. Add privacy policy and terms pages. Switch gallery images to actual user submissions or clearly label as "inspiration." Enable HTTPS on deployment.

---

## AI Citation Readiness: 45 / 100

| Factor | Score | Detail |
|--------|-------|--------|
| Structured data | **5/20** | Have Organization + WebSite + BreadcrumbList. Missing: Article schema on content pages, FAQPage schema on FAQ content, Person schema for authors. |
| Heading hierarchy | **18/20** | Excellent H1-H2 structure across all pages. FAQ page uses H3 for individual questions. |
| Answer-first formatting | **15/20** | FAQ page has clear Q&A format. How-to-wear has step-by-step structure. Compare page has side-by-side format. |
| Quotable statements | **5/15** | Content has useful facts but few citation-ready statistics. No original research data. |
| Citations & attribution | **0/15** | Zero external source citations. No "according to" statements with linked references. |
| Freshness signals | **10/10** | All pages dated 2026-08-03. Consistent across site. |

### Key AI Citation Gaps

1. **Article schema**: Not implemented on content pages. Without it, AI systems cannot reliably parse author, date, and content structure.
2. **FAQPage schema**: The /faq/ page and homepage FAQ section lack this schema despite being the #1 most-cited schema type in AI Overviews.
3. **Zero source citations**: AI models preferentially cite content that itself cites authorities. Adding even 2-3 citations per page dramatically increases citability.
4. **No original data**: AI models heavily favor content with proprietary statistics, survey results, or unique datasets. The site has none.

---

## Content Structure Review

| Page | H1 | H2 Count | Lists | Internal Links | External Links | Images |
|------|----|----------|-------|---------------|---------------|--------|
| Homepage | ✅ | 8 | Cards + list | Category links | 0 | 20 (Unsplash) |
| /hanfu/ | ✅ | 5 | No | 0 | 0 | 0 |
| /qipao-cheongsam/ | ✅ | 5 | No | 0 | 0 | 0 |
| /tang-suit/ | ✅ | 3 | No | 0 | 0 | Placeholders |
| /zhongshan/ | ✅ | 3 | No | 0 | 0 | Placeholders |
| /ethnic/ | ✅ | 5 | No | 0 | 0 | Placeholders |
| /faq/ | ✅ | 3 | No | 0 | 0 | 0 |
| /how-to-wear/ | ✅ | 6 | No | 0 | 0 | Placeholders |
| /compare/ | ✅ | 5 | No | 1 (to quiz) | 0 | Placeholders |
| /about/ | ✅ | 4 | No | 0 | 0 | 0 |

**Issues**:
- Zero internal links in content body on most pages (nav/footer links only)
- Zero external citations across entire site
- No bullet lists or numbered steps where they would help scanability
- No tables for comparative data (e.g., /compare/ page has comparison text but no comparison table)

---

## Recommendations

### Immediate (Week 1)
1. Add `Article` schema to BaseLayout for article-type pages (headline, datePublished, author)
2. Add `FAQPage` schema to /faq/ and homepage FAQ section
3. Add 2-3 external citations per content page (link to museum sites, academic sources)
4. Add author bylines to key pages
5. Add Contact page with email

### Short-term (Weeks 2-3)
1. Create author bio page with credentials
2. Add privacy policy and terms pages
3. Add bullet lists and comparison tables to /compare/ and /how-to-wear/
4. Add 3-5 internal cross-links per content page
5. Replace gallery placeholder text with "Traveler-submitted photos" language

### Medium-term (Month 2+)
1. Publish 2-3 first-person trip diaries with original photos
2. Conduct and publish original survey/pricing research
3. Build external citations and backlinks through guest posting
4. Implement Person schema for authors
5. Add "Cite this page" feature with citation-ready summaries

---

## FLOW Framework Status

| Stage | Status | Action |
|-------|--------|--------|
| **Find** | ✅ Done | Keyword identified: "chinese traditional wear" |
| **Leverage** | ✅ Done | Site structure and content built around target keywords |
| **Optimize** | 🔄 In Progress | Content quality is high (96/100). E-E-A-T needs work. AI citation readiness at 45/100. |
| **Win** | ⬜ Pending | Needs deployment, backlinks, and ongoing content cadence |

---

*Analysis generated by SEO Content Quality v2.2.0. Scores based on QRG-aligned detection, E-E-A-T framework evaluation, and AI citation readiness assessment.*