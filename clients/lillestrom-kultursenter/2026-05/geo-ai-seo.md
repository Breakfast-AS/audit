# GEO / AI Search Readiness Audit — Lillestrøm Kultursenter

**Audit date:** 2026-05-29
**Site type:** Cultural venue / entertainment center, Lillestrøm, Norway
**CMS:** WordPress + Yoast SEO, served via Cloudflare CDN
**Language:** Norwegian (nb-NO)

---

## GEO Readiness Score: 44 / 100

| Dimension | Weight | Raw Score | Weighted |
|---|---|---|---|
| Citability | 25% | 28/100 | 7.0 |
| Structural Readability | 20% | 42/100 | 8.4 |
| Multi-Modal Content | 15% | 45/100 | 6.75 |
| Authority & Brand Signals | 20% | 40/100 | 8.0 |
| Technical Accessibility | 20% | 70/100 | 14.0 |
| **TOTAL** | | | **44 / 100** |

The site is technically accessible to AI crawlers but almost entirely lacks the content structures that drive AI citation.

---

## Platform-Specific Scores

| Platform | Score | Key Gap |
|---|---|---|
| Google AI Overviews | 35/100 | No FAQ schema, no Organization schema, thin Om oss |
| ChatGPT / GPT-4o browsing | 40/100 | No llms.txt, no self-contained answer passages |
| Perplexity AI | 48/100 | Event schema helps; no citation-ready prose |
| Bing Copilot | 42/100 | No structured entity data, weak author signals |

---

## 1. AI Crawler Access Status

**robots.txt summary:** All major AI crawlers are permitted via wildcard allow. However, `Crawl-delay: 10` applies universally — limiting any crawler to 6 pages/minute. With 585 sitemap URLs, full AI crawl coverage will be very slow.

| Crawler | Status | Notes |
|---|---|---|
| GPTBot (OpenAI) | ALLOWED | Wildcard allow; no explicit block |
| ClaudeBot (Anthropic) | ALLOWED | No explicit block |
| PerplexityBot | ALLOWED | No explicit block |
| Google-Extended (Gemini) | ALLOWED | No explicit block |
| CCBot (Common Crawl) | ALLOWED | No explicit block |

**Fix — add named entries before the wildcard to improve AI crawl speed:**

```
User-agent: GPTBot
Crawl-delay: 2

User-agent: OAI-SearchBot
Crawl-delay: 2

User-agent: ClaudeBot
Crawl-delay: 2

User-agent: PerplexityBot
Crawl-delay: 2

User-agent: Google-Extended
Crawl-delay: 2

User-agent: *
Crawl-delay: 10
Disallow: /wp-content/uploads/wpo/wpo-plugins-tables-list.json
```

---

## 2. llms.txt Status: NOT FOUND (HTTP 404)

No llms.txt file exists. This is the lowest-effort, highest-signal missing element.

**Recommended llms.txt template:**

```markdown
# Lillestrøm Kultursenter

> Lillestrøm Kultursenter er et kulturhus i Lillestrøm, Akershus, som siden 1991 har
> arrangert konserter, teater, musikaler, stand-up og konferanser.
> Kultursenteret eies av Stiftelsen Lillestrøm Kulturforum og holder
> til i Kirkegata 11, 2000 Lillestrøm – 150 meter fra Lillestrøm stasjon.

## Hva vi tilbyr

- [Program og billetter](/program/): Konserter, teaterstykker, musikaler og familieforestillinger
- [Saler til leie](/utleie/vare-saler/): 12 saler fra 6 til 600 personer
- [Konferanse](/utleie/moter-kurs-og-konferanse/): Møtepakker med mat og teknisk utstyr
- [Samfundet](/utleie/samfundet/): Festlokale for private arrangementer
- [Om oss og historikk](/om-oss/historikk/): Stiftet 1991, røtter tilbake til 1926

## Nøkkeldata

- Grunnlagt: 1991
- Adresse: Kirkegata 11, 2000 Lillestrøm
- Telefon: +47 64 84 55 50
- Åpent: Man–fre 09–20, lør 11–15
- Sertifisering: Miljøfyrtårn

## Kontakt

- E-post: billett@lillestrom-kultursenter.no
```

---

## 3. Citability Analysis — Score: 28/100

The optimal AI citation passage is 134–167 words, self-contained, with a direct answer in the first 40–60 words. The site has zero passages meeting this spec outside the historikk page.

**Existing citable facts (from historikk page — need surfacing on Om oss):**
- Founded April 17, 1991 by Stiftelsen Lillestrøm Kulturforum
- Original building: 1926 (Lillestrøm Kinoteater)
- 2006 expansion (two new buildings)
- 350,000 annual visitors (2019)
- INTRO and EKKO spaces opened August 29, 2022
- Miljøfyrtårn environmental certification
- Hosts Unge Viken Teater

---

## 4. Structural Readability — Score: 42/100

**Issues:**
- No H1 on homepage
- All H2s on homepage are event titles — none describe the venue
- No question-format headings anywhere
- No FAQ schema

**Schema gaps:**

| Schema Type | Present | Notes |
|---|---|---|
| Event | YES | Event pages — key strength |
| WebSite / WebPage / BreadcrumbList | YES | Sitewide — basic |
| Organization | NO | Critical gap |
| LocalBusiness | NO | Critical gap |
| PerformingArtsTheater | NO | Relevant subtype |
| FAQPage | NO | High-impact gap |
| Article | NO | Missing from /artikler/ posts |
| Person | NO | No staff profiles |

---

## 5. Authority and Brand Signals — Score: 40/100

| Platform | Status |
|---|---|
| Norwegian Wikipedia (no.wikipedia.org) | EXISTS |
| Facebook | EXISTS (linked in footer) |
| Instagram | EXISTS (linked in footer) |
| English Wikipedia | NOT FOUND |
| YouTube | UNKNOWN — not linked |
| TripAdvisor | NOT LISTED (returns 404) |

**No author bylines or publication dates visible on /artikler/ listing page.**

---

## 6. Top 5 Recommendations

### Priority 1 — Create /llms.txt (Low effort, High impact)
Upload as a static file at the domain root. No plugin required. 2–4 hours work.

### Priority 2 — Add Organization + PerformingArtsTheater JSON-LD (Medium effort, Critical impact)
Add to homepage `<head>`. Include `sameAs` pointing to no.wikipedia.org. Include founding date, address, coordinates, opening hours, telephone, and email.

### Priority 3 — Rewrite Om oss with Citation-Ready Prose (Medium effort, High impact)
Current page is a contact stub. Needs 200–400 words structured as self-contained sections answering implicit questions.

### Priority 4 — Add FAQPage Schema to key pages (Medium effort, High impact)
High-value FAQ clusters for /utleie/vare-saler/ and /praktisk-informasjon/:
- "Hvor mange saler har Lillestrøm Kultursenter?" → 12 saler fra 6 til 600 personer
- "Hva er kapasiteten i Teatersalen?" → 600 personer
- "Hvor ligger Lillestrøm Kultursenter?" → Kirkegata 11, 2000 Lillestrøm
- "Når åpnet kultursenteret?" → Stiftelsen etablert 17. april 1991

### Priority 5 — Fix Crawl-Delay and article metadata (Low effort, Medium impact)
- Add named AI bot entries to robots.txt with Crawl-delay: 2
- Enable author display and publication dates on article listing
- Restore or redirect /konferanse/ (returns 404)

---

## Summary Scorecard

| Finding | Status |
|---|---|
| All major AI crawlers allowed | PASS |
| Crawl-delay optimized per bot | FAIL |
| llms.txt present | FAIL |
| Organization schema | FAIL |
| Event schema on event pages | PASS |
| FAQPage schema | FAIL |
| Article schema on blog posts | FAIL |
| Citation-ready prose (Om oss) | FAIL |
| Norwegian Wikipedia entity | PASS |
| SSR rendering (not CSR) | PASS |
| Cloudflare CDN fast delivery | PASS |

**Passed: 5 / 11 | Failed: 6 / 11**
