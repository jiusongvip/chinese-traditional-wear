## AI Search Readiness Findings

### AI Crawler Access

| Signal | Status |
|--------|--------|
| robots.txt | Missing — no directives for AI crawlers |
| llms.txt | Missing — no machine-readable content summary |
| /llms.txt endpoint | Not present |
| AI bot directives | No GPTBot, Claude-Web, PerplexityBot directives |

### Citability Factors

| Factor | Status | Impact |
|--------|--------|--------|
| Author attribution | None | AI models prioritize content with clear authorship |
| Publication dates | None visible | AI models prefer dated, current content |
| Citations to sources | None | AI models cite content that itself cites authorities |
| Structured data | None | Schema helps AI understand content structure |
| Clear headings | Good | H1-H3 hierarchy helps AI parse content |
| FAQ content | Present on homepage and /faq/ | FAQ content is favored for featured snippets and AI responses |

### Structural Readiness

| Factor | Status |
|--------|--------|
| Semantic HTML | Good — uses `<header>`, `<nav>`, `<main>`, `<footer>`, `<section>`, `<article>` (inferred) |
| Table of contents | Not present — would help AI navigation |
| Content chunking | Adequate — sections with clear H2 headings |
| Definition lists | Not used — `<dl>` would help for glossary-style content |

### Brand Mention Signals

| Signal | Status |
|--------|--------|
| Consistent brand name | "ChinaStyle" — but target keyword is "Chinese Traditional Wear" |
| Knowledge panel signals | None (no schema, no about page, no Wikipedia presence) |
| Social proof | None on-site (no testimonials, reviews, social embeds) |

### Recommendations

1. Add `/robots.txt` with explicit AI crawler directives
2. Create `/llms.txt` with a structured summary of site content and key pages
3. Add author attribution and publication dates to all content pages
4. Implement FAQPage schema on FAQ content
5. Add cited references/sources to historical claims
6. Create an About page with organizational and author credentials
7. Consider a "Cite this page" feature for authoritative content

### Summary
- Zero AI crawler readiness — no robots.txt, no llms.txt, no author signals
- Content is well-structured for AI parsing (good heading hierarchy)
- FAQ content exists but lacks schema markup for AI discoverability
- Missing author/date signals significantly reduce AI citation likelihood
