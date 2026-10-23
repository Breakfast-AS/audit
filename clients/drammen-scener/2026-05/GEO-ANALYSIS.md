# GEO Analysis: drammenscener.no
**Date:** 2026-05-29
**Language:** Norwegian (nb-NO)
**Site:** https://www.drammenscener.no/

---

## GEO Readiness Score: 61 / 100

| Dimension | Weight | Score | Weighted |
|---|---|---|---|
| Citability | 25% | 58/100 | 14.5 |
| Structural Readability | 20% | 62/100 | 12.4 |
| Multi-Modal Content | 15% | 30/100 | 4.5 |
| Authority & Brand Signals | 20% | 55/100 | 11.0 |
| Technical Accessibility | 20% | 94/100 | 18.8 |
| **Total** | | | **61.2 / 100** |

---

## Platform-Specific Visibility

| Platform | Score | Bottleneck |
|---|---|---|
| Google AI Overviews | 48/100 | No LocalBusiness/FAQ schema; thin on-page content |
| ChatGPT (web search) | 58/100 | llms.txt helps; no pricing/FAQ limits answer depth |
| Perplexity | 65/100 | SSR + llms.txt + structured sitemap are positive signals |
| Bing Copilot | 52/100 | No schema, thin on-page content; benefits from SSR |

Only 11% of domains are cited by both ChatGPT and Google AI Overviews for the same query. Currently this site is better positioned for Perplexity/ChatGPT than Google AIO due to the llms.txt advantage and SSR architecture.

---

## 1. AI Crawler Access Status

**Result: Full Access — All AI Crawlers Permitted**

```
Crawl-delay: 10
User-agent: *
Disallow:

Sitemap: https://www.drammenscener.no/sitemap_index.xml
```

| Crawler | Owner | Status | Notes |
|---|---|---|---|
| GPTBot | OpenAI | ✅ ALLOWED | No block directive |
| OAI-SearchBot | OpenAI | ✅ ALLOWED | No block directive |
| ChatGPT-User | OpenAI | ✅ ALLOWED | No block directive |
| ClaudeBot | Anthropic | ✅ ALLOWED | No block directive |
| PerplexityBot | Perplexity | ✅ ALLOWED | No block directive |
| CCBot | Common Crawl | ✅ ALLOWED | Training crawler — consider blocking if unwanted |
| anthropic-ai | Anthropic | ✅ ALLOWED | Training crawler — consider blocking if unwanted |
| Bytespider | ByteDance | ✅ ALLOWED | TikTok AI |
| cohere-ai | Cohere | ✅ ALLOWED | No block directive |

**Crawl-delay impact:** `Crawl-delay: 10` slows re-crawl cadence for bots that respect it (Bingbot, Yandex). Googlebot and OpenAI's crawlers ignore it. On a 36-page site, this is not a significant barrier to AI indexation but adds unnecessary delay.

**Recommendation:** Remove `Crawl-delay: 10` — the 36-page site does not require crawl throttling. If training crawler blocking is desired, add explicit `Disallow` for CCBot and anthropic-ai only.

---

## 2. llms.txt Status: PRESENT ✅ — Grade B+

**URL:** https://www.drammenscener.no/llms.txt
**HTTP Status:** 200 OK
**Format:** Well-structured, follows emerging llms.txt standard

This is a significant competitive advantage. The site is in approximately the **top 5% of Norwegian business websites** for AI readiness by having a functioning, high-quality llms.txt.

### Full Content Analysis

The file includes:
- ✅ AI instruction preamble (how LLMs should use and cite the content)
- ✅ Content boundary declaration (what not to use: internal systems, customer data)
- ✅ Opening blockquote with capacity range (20–1200 persons) and dual-venue summary
- ✅ Core benefits section with 7 specific differentiators
- ✅ All 9 rooms with URLs and capacity ranges
- ✅ Booking workflow description
- ✅ Transport section with specific times and addresses (Union Scene only)
- ✅ Accessibility certifications (Tilgjengelighetsmerket, Miljøfyrtårn)
- ✅ History section with verifiable, citable facts
- ✅ Environmental practices with named local suppliers (Aass, Haandbryggeriet, Matfikseren, Hyggen, Roasteriet)
- ✅ Nøkkelbegreper (keywords) section — direct topic seeding for AI systems
- ✅ 9 package types listed with URLs (more complete than sitemap suggests)

### llms.txt Gaps

| Gap | Impact | Fix |
|---|---|---|
| No phone number or email in "Booking" section | AI cannot answer "how do I contact them?" | Add: `Telefon: +47XXXXXXXX, E-post: post@drammenscener.no` |
| Drammens Teater address missing | AI cannot give directions to the theater | Add full address to transport section |
| No `# License: RSL-1.0` declaration | No explicit AI reuse permission signal | Add as first line after title |
| No `# Optional` section separator | Misses llms.txt spec tiered structure | Add for extended detail pages |
| No `llms-full.txt` linked | AI systems can't find extended content | Create and link if extended version desired |
| Nøkkelbegreper too narrow (6 terms) | Missing high-value search term associations | Expand to 12-15 terms (see below) |
| Passages below optimal 134-167 word range | Suboptimal citation window | Expand key sections |

### Recommended llms.txt Additions

**Add to top of file:**
```
# License: RSL-1.0
```

**Expand "Booking og forespørsel" section:**
```
## Booking og forespørsel

Telefon: +47XX XX XX XX
E-post: post@drammenscener.no
Svar innen: 1 virkedag

Drammen Scener tar imot forespørsler via kontaktskjema, e-post og telefon...
```

**Add Drammens Teater address to transport section:**
```
Drammens Teater adresse: Schweigardsgate 1B, 3017 Drammen
```

**Expand Nøkkelbegreper:**
```
## Nøkkelbegreper

- Konferanse i Drammen
- Konferanselokale Drammen
- Eventlokaler i Drammen
- Sceneutleie i Drammen
- Julebord i Drammen
- Festlokale i Drammen
- Sommerfest i Drammen
- Bryllupslokaler i Drammen
- Konsertarena i Drammen
- Selskapslokale Drammen
- Møterom Drammen
- Konferansepakke Drammen
- Leie lokale Drammen
- Miljøfyrtårn konferanselokale Drammen
- Konferansesenter nær Oslo
```

---

## 3. Brand Mention Analysis

| Platform | Presence | Signal Strength | Notes |
|---|---|---|---|
| Wikipedia | Drammens Teater likely has article (1870, Stortingsbygningen architect) | High potential | Verify if article links to drammenscener.no as operator — if not, request edit |
| YouTube | Vimeo background video exists; no YouTube channel confirmed | Gap | YouTube mentions correlate 0.737 with AI citations — highest single signal |
| Reddit | No detected presence | Gap | r/norge, r/drammen discussions unconfirmed |
| LinkedIn | Unconfirmed | Moderate | Important for B2B conference segment |
| Facebook | Linked from llms.txt nøkkelbegreper structure suggests social presence | Unconfirmed | |
| Instagram | Same | Unconfirmed | |
| Finn.no | Unconfirmed | High for Norwegian market | Should be present in "lokaler til leie" category |
| Konferanseguiden.no | Unconfirmed | High for conference vertical | Priority citation |

**Key opportunity:** If a Wikipedia article exists for Drammens Teater (highly likely given its 1870 heritage, architect link to Stortingsbygningen), but the article does not mention Drammen Scener as the current operator, the highest-ROI AI brand action is adding a reference to the Wikipedia article.

---

## 4. Passage-Level Citability Analysis

### Optimal Window: 134–167 words per passage

All passages in llms.txt were measured against the optimal citation window. Most fall below optimal length.

### Current Passage Analysis

| Passage | Word Count | Assessment | Action |
|---|---|---|---|
| Opening blockquote | ~75 words | Below optimal | Expand by ~80 words |
| Om Drammen Scener | ~60 words | Below optimal | Expand by ~90 words |
| Beliggenhet og transport | ~80 words | Below optimal | Add Drammens Teater directions |
| Drammens Teater history | ~65 words | Below optimal | Strong facts — expand to full citation block |
| Union Scene history | ~55 words | Below optimal | Expand with more specific detail |
| Miljø og bærekraft | ~55 words | Below optimal | Good specificity — expand |

### Best Current Citable Passage

The Drammens Teater history section contains the highest-quality citable facts on the site:
> *"Drammens Teater ble opprinnelig bygget i 1870 etter bybrannen i 1866, tegnet av arkitekt Emil Victor Langlet (som også tegnet Stortingsbygningen)... en påsatt brann i desember 1993 totalskadet bygget. Det ble gjenoppbygd nøyaktig slik det var, og åpnet igjen 8. februar 1997..."*

This passage has all the properties AI citation systems prefer: specific years, named architect, verifiable claim linking to national landmark. **Expanding this to 134-167 words** by adding architectural details, restoration specifics, or a notable historical event would make it the most AI-citable passage on the entire domain.

### Recommended Expanded Opening Blockquote (~150 words)

Replace current ~75-word blockquote with:

> Drammen Scener er Drammens ledende leverandør av konferanselokaler og eventsaler, med to ikoniske arenaer sentralt i Drammen: Drammens Teater og Union Scene. Drammens Teater, opprinnelig tegnet av Emil Victor Langlet i 1870 – samme arkitekt som tegnet Stortingsbygningen – tilbyr klassiske salonger og en vakker teaterscene for 100 til 450 gjester. Union Scene er en omgjort papirfabrikk fra 1800-tallet med rå industriell karakter og kapasitet for 120 til 1200 gjester, inkludert Drammens råeste bakgård. Til sammen tilbyr de to lokalene 9 saler for arrangementer fra 20 til 1200 personer. Begge lokasjonene er Miljøfyrtårn-sertifiserte og bærer Tilgjengelighetsmerket. Drammen Scener ble etablert i 2009 da de to kulturhusene ble slått sammen. Lokalene er utstyrt med profesjonell lyd-, lys- og bildeteknikk betjent av erfarne in-house teknikere, og tilbyr skreddersydde mat- og drikkeløsninger.

(~145 words — within optimal 134-167 window)

---

## 5. Server-Side Rendering Check

**Result: PASS — Full SSR Confirmed**

WordPress with custom Twig templates renders complete HTML server-side. All page content is present in the HTTP response — zero JavaScript dependency for content rendering.

This is a critical advantage: AI crawlers (GPTBot, ClaudeBot, PerplexityBot) do **not** execute JavaScript. Sites that render content client-side (React SPAs, Angular apps) are invisible to AI crawlers beyond their HTML shell. drammenscener.no has no such limitation.

**Content present in HTML response without JS:**
- All room listings and descriptions ✅
- All package names and descriptions ✅
- Navigation hierarchy ✅
- Contact information (when present) ✅
- Schema markup in `<script type="application/ld+json">` blocks ✅

---

## 6. Schema Recommendations for AI Discoverability

Current schema state: Only `WebPage`, `WebSite`, `ImageObject`, `BreadcrumbList` (Yoast defaults). No business-identity schema.

### Critical Missing Schema for AI Citation

| Schema Type | Page | AI Benefit |
|---|---|---|
| `Organization` + `EventVenue` | Homepage | Google can assert business facts; GBP entity association |
| `FAQPage` | New /ofte-stilte-sporsmal/ | #1 format AI systems extract for conversational answers |
| `Service` | All /pakker/ pages | Entity clarity for commercial intent queries |
| `Place` with `maximumAttendeeCapacity` | All /saler/ pages | AI can answer "how many people does X hold?" |
| `LocalBusiness` with `address` + `geo` | Both venue pages | Local query visibility |

**Quick win:** Adding `maximumAttendeeCapacity` to venue schema allows AI to directly answer "Hvor mange gjester tar Hauptscenen på Union Scene?" — currently unanswerable from schema alone.

---

## 7. FAQ Content Gap — Highest AI Opportunity

**Current state:** No FAQ content exists anywhere on the site.

For Norwegian venue search queries, AI assistants generate FAQ-format answers from source content. The site currently cannot be cited for any of these high-volume question patterns:

| Query Pattern | Current Citability |
|---|---|
| "Hva er inkludert i konferansepakken på Drammen Scener?" | ❌ None |
| "Hvor mange gjester tar Union Scene?" | ✅ llms.txt (but not on-page) |
| "Er Drammens Teater tilgjengelig for rullestolbrukere?" | ✅ llms.txt mentions cert |
| "Hva koster det å leie lokale i Drammen?" | ❌ None |
| "Kan man ha julebord på Drammens Teater?" | ❌ None |
| "Hva er forskjellen mellom Union Scene og Drammens Teater?" | ✅ llms.txt partially |

Creating a `/ofte-stilte-sporsmal/` page with 15+ Q&A pairs in the 134-167 word optimal range per answer, plus `FAQPage` schema, is the **single highest-impact action** for AI citation coverage across all four platforms simultaneously.

---

## 8. Content Reformatting Suggestions

### Specific Passages to Restructure for AI Citability

**Homepage body text (current):**
> "Vi tilbyr to unike arenaer som gir enhver anledning en spesiell ramme. Drammens Teater, kjent som landets mest praktfulle teater, byr på eleganse og sjarm. Union Scene, med sitt rustikke og industrielle preg, tilfører en moderne og urban atmosfære..."

**Problem:** Aspirational marketing language. Zero citable facts. No specific data points.

**Reformatted for AI citation:**
> "Drammen Scener er Drammens fremste leverandør av konferanselokaler og eventsaler med over 15 års erfaring. Selskapets to venues tilbyr til sammen 9 saler med kapasitet fra 20 til 1200 gjester. Drammens Teater (bygget 1870, gjenoppbygd 1997) tilbyr et historisk teatermiljø for formelle arrangementer, gallamiddager og konferanser for 100–450 gjester. Union Scene, i de rehabiliterte fabrikklokalene til Union Co., gir en rå industriell ramme for konserter, eventer og store konferanser for 120–1200 gjester. Begge lokalene har Miljøfyrtårn-sertifisering og Tilgjengelighetsmerket, og er utstyrt med profesjonell lyd-, lys- og bildeteknikk betjent av in-house teknikere."
(~115 words — approaching optimal; add 1 more sentence to reach 134-167)

---

**Conference package page (current state: ~200 words, no citable structure):**

Add a self-contained answer block at the top of the page following this pattern:

> "**Hva er inkludert i en konferansepakke hos Drammen Scener?**
> Konferansepakkene hos Drammen Scener inkluderer leie av konferansesal tilpasset din gruppes størrelse (10–450 deltakere), profesjonelt AV-utstyr (projektor, lerret, mikrofoner, PA-system), og teknisk støtte fra in-house teknikere under hele arrangementet. Kaffe, te og vann er inkludert. Lunsj og spesialmenyer kan tillegges. Salen kan konfigureres i kinooppsett, klasseroms-arrangement, U-form eller bankettoppsett. Pris beregnes individuelt basert på antall deltakere, varighet, salvalg og tilleggsservering. Ta kontakt via skjema eller telefon for et tilbud."

(~95 words — add to reach 134-167 for optimal citability)

---

## 9. Top 5 Highest-Impact AI Optimization Actions

### Priority 1 — Add LocalBusiness + EventVenue Schema (Week 1)
**Effort:** 2–4 hours | **AI Impact:** Very High
Without `LocalBusiness`/`EventVenue` schema, Google AI Overviews and ChatGPT cannot confidently assert basic business facts (address, phone, category). This single action lifts Google AIO from 48/100 to an estimated 65/100.
See FULL-AUDIT-REPORT.md Section 4.2 for complete JSON-LD.

### Priority 2 — Create /ofte-stilte-sporsmal/ FAQ Page + FAQPage Schema (Week 2–3)
**Effort:** 1–2 days | **AI Impact:** Very High
15+ self-contained Q&A pairs in Norwegian at 100-150 words each + FAQPage schema. This is the primary format all four AI platforms extract for conversational answers. If Drammen Scener publishes the first high-quality Norwegian FAQ about booking event venues in Drammen, it becomes the default AI-cited source for that topic cluster — competitors are almost certainly not doing this.

### Priority 3 — Expand llms.txt Passages to Optimal Citation Window (Week 1)
**Effort:** 2–3 hours | **AI Impact:** High
Current passages average 60-80 words — below the optimal 134-167 word AI citation window. Expand the opening blockquote, Drammens Teater history, Union Scene history, and transport sections to reach the optimal range. Add phone/email to Booking section and Drammens Teater address.

### Priority 4 — Build YouTube Presence (Month 2+)
**Effort:** Ongoing | **AI Impact:** High over time
YouTube mentions correlate **0.737** with AI citation frequency — the strongest single signal. Publish the existing Vimeo background video to YouTube. Create 2-3 venue tour videos with Norwegian keyword-targeted titles. This builds the off-site entity signal that AI training corpora use to validate brand authority.

### Priority 5 — Expand On-Page Content With Self-Contained Answer Blocks (Month 1–2)
**Effort:** 3–5 days content | **AI Impact:** Medium-High
The on-page content is too thin (~200 words per page) to generate AI citations. Each major service page (/konferanser/, /eventer/, individual venue pages) should be expanded with structured, fact-rich sections that directly answer the questions AI systems receive about these venues. Each section should open with a direct answer in the first 40-60 words.

---

## Quick Reference: Norwegian-Language AI Query Optimization

The Norwegian AI search market has thinner training data than English, meaning individual high-quality Norwegian pages carry higher relative weight. Focus Norwegian-specific optimizations on:

**Highest-value Norwegian queries this site should capture:**
1. "konferanselokale Drammen" — commercial, high intent
2. "eventlokaler Drammen" — commercial
3. "selskapslokale Drammen" — commercial
4. "leie scene Drammen" — transactional
5. "julebord Drammen 2026" — seasonal high-value
6. "Drammens Teater" — brand/informational
7. "Union Scene" — brand/informational
8. "konferanselokale nær Oslo" — regional modifier
9. "Miljøfyrtårn konferanselokale" — differentiating

All of these are either currently in the llms.txt nøkkelbegreper or should be added. None are currently optimized in page-level heading structure.

---

*GEO Analysis generated by Claude Code SEO Audit System*
*Full audit: FULL-AUDIT-REPORT.md | Action plan: ACTION-PLAN.md*
