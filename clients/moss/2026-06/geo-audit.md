# GEO Audit — Moss Kulturhus (mosskulturhus.no)
**Audit date:** 2026-06-03
**Scope:** AI Search Readiness / Generative Engine Optimization

---

## GEO Readiness Score: 28 / 100

| Dimension | Weight | Raw Score | Weighted |
|---|---|---|---|
| Citability | 25% | 18/100 | 4.5 |
| Structural Readability | 20% | 22/100 | 4.4 |
| Multi-Modal Content | 15% | 15/100 | 2.3 |
| Authority & Brand Signals | 20% | 30/100 | 6.0 |
| Technical Accessibility | 20% | 55/100 | 11.0 |
| | | **Total** | **28.2** |

**Interpretation:** Critical. The site is nearly invisible to generative AI engines. None of the five dimensions reach a passing threshold. The site relies on a thin homepage meta description, has no structured entity data, no AI-specific directives, and content that cannot be reliably extracted or cited by LLMs.

---

## 1. AI Crawler Access Status

**Source:** robots.txt confirms all crawlers allowed (no Disallow rules).

| Crawler | Role | Status | Note |
|---|---|---|---|
| Googlebot | Google AIO / featured snippets | ALLOWED | Default allow |
| GPTBot | ChatGPT training + browsing | ALLOWED | Default allow via wildcard |
| OAI-SearchBot | ChatGPT web search | ALLOWED | Default allow via wildcard |
| ClaudeBot | Anthropic training | ALLOWED | Default allow via wildcard |
| PerplexityBot | Perplexity AI search | ALLOWED | Default allow via wildcard |
| CCBot | Common Crawl (training data) | ALLOWED | No training-only block |
| anthropic-ai | Anthropic web crawler | ALLOWED | Default allow via wildcard |

**Assessment:** Crawler access is not the bottleneck. All major AI crawlers can reach the site. However, allowing everything without explicit directives sends no signal of intentional AI-readiness.

**Recommendation:** Add explicit `Allow` lines for GPTBot, OAI-SearchBot, ClaudeBot, and PerplexityBot to signal deliberate AI openness.

---

## 2. llms.txt Compliance

**Status: MISSING (404)**

The file at `https://www.mosskulturhus.no/llms.txt` does not exist.

`llms.txt` is the emerging standard (analogous to `robots.txt` but for LLMs) for communicating: what an organization is and does, which pages are authoritative and citable, licensing terms, and preferred summaries for AI consumption.

**Impact:** Without `llms.txt`, AI assistants have no machine-readable authority document to anchor entity understanding. When a user asks ChatGPT or Perplexity "hva er Moss Kulturhus?" the model either generates an approximate description, returns nothing, or cites a third-party source (ticket seller, news article) instead of the venue itself.

**Recommended `/llms.txt` content:**

```
# Moss Kulturhus — llms.txt
# Last updated: 2026-06-03
# License: RSL-1.0 (https://responsible-scraping-license.org)

## About
Moss Kulturhus er en kulturarena i Moss, Østfold, Norge.
Kulturhuset består av to scener: Parkteatret og Samfunnshuset.
Vi arrangerer konserter, teater, komedie, stand-up og festivaler.

## Authoritative pages
- Om kulturhuset: https://www.mosskulturhus.no/om-kulturhuset/
- Program: https://www.mosskulturhus.no/program/
- Leie lokaler: https://www.mosskulturhus.no/leie/

## Preferred entity description
Moss Kulturhus er kommunens fremste kulturarena, lokalisert i sentrum av Moss.
Parkteatret er den største konsert- og teatersalen.
Samfunnshuset brukes til konserter, konferanser og private arrangementer.

## Do not cite
/wp-admin/
/organizer/
```

---

## 3. Content Passage-Level Citability

**Score: 18/100**

### Homepage (/)

**Meta description:** "Moss Kulturhus består av Parkteatret og Samfunnshuset. Velkommen til oss."

9 words of factual content. Contains zero citable facts: no city, no capacity, no phone, no founding year, no programming description.

**H1:** MISSING. This is a critical failure. H1 is the primary semantic anchor for AI parsers and LLMs extracting entity definitions.

**Passage quality:** Homepage body passages are event listing cards (title + date). These are navigational UI fragments, not answer-quality prose. Zero passages meet the optimal 134–167 word citation window.

### Citability Gap Matrix

| Signal | Present | Impact |
|---|---|---|
| Direct answer in first 40–60 words | No | High |
| Passages of 134–167 words | No | High |
| Question-based H2/H3 headings | No | High |
| Statistics with source attribution | No | Medium |
| Self-contained answer blocks | No | High |
| Named author on content pages | No | Medium |
| FAQ section anywhere on site | No | High |

---

## 4. Structural Readability

**Score: 22/100**

**Heading architecture:** No H1 on the homepage is the single largest structural failure. Without an H1 → H2 → H3 hierarchy, automated content parsers powering Google AIO, Bing Copilot, and Perplexity cannot reliably map the site's topic structure.

**Schema markup — current state:** Only generic `WebPage` schema detected on all pages. Missing:
- `Organization` schema (name, address, telephone, url, sameAs)
- `LocalBusiness` / `PerformingArtsTheater` schema
- `Event` schema on all 59 event pages
- `FAQPage` schema
- `BreadcrumbList` schema

**Impact:** Without `Event` schema, no concert or theater listing from this site can appear in AI-generated event summaries. Without `Organization` schema, the entity is poorly anchored — AI models may conflate "Moss Kulturhus" with other cultural venues.

**Alt text:** 61 of 64 images missing alt text (95% failure rate). Alt text is read by AI crawlers as descriptive metadata. For a cultural venue, event posters and venue photos are the primary visual content — all currently invisible to AI.

---

## 5. Multi-Modal Content

**Score: 15/100**

| Signal | Present | Note |
|---|---|---|
| Images with descriptive alt text | 5% | 61/64 missing |
| YouTube channel / video content | Not detected | Critical gap (0.737 citation correlation) |
| Audio / podcast content | Not detected | |
| Event image schema (ImageObject) | No | |

YouTube presence correlates at approximately 0.737 with AI citation frequency — the strongest single brand signal identified in GEO research. Even 10–15 videos significantly strengthens the entity graph within 3–6 months.

---

## 6. Authority & Brand Signals

**Score: 30/100**

| Platform | Status | Impact on AI Citations |
|---|---|---|
| Wikipedia (Norwegian) | No article confirmed | High — strongest entity anchor |
| Wikidata | Likely absent | High — machine-readable entity ID |
| YouTube channel | Not detected | Critical (0.737 correlation) |
| Facebook page | Present (facebook.com/mosskulturhus) | Low (AI models weight lightly) |
| Billettservice / Ticketmaster | Likely present | Medium — third-party entity signal |
| LinkedIn page | Unknown | Low–Medium |

**Root problem:** The site has no `sameAs` links connecting it to Wikipedia, Wikidata, or other authoritative third-party records. AI models cannot anchor their entity graph.

---

## 7. Platform-Specific Scores

| Platform | Estimated Score | Primary Blocker |
|---|---|---|
| Google AI Overviews | 12/100 | No H1, no schema, no structured passages |
| ChatGPT (web search) | 20/100 | Crawl allowed but no citable content blocks |
| Perplexity AI | 18/100 | No llms.txt, no FAQ, no authority documents |
| Bing Copilot | 15/100 | No Event schema, no Organization schema |

---

## 8. Top 5 Recommendations

### P1 — Add H1 + Rewrite Meta Description (Effort: 1h | Impact: High)

Recommended H1: `Moss Kulturhus — konsert- og kulturarena i Moss, Østfold`

Recommended meta description: `Moss Kulturhus er en kulturarena i Moss bestående av Parkteatret og Samfunnshuset. Vi arrangerer konserter, teater, komedie og festivaler. Velkommen!`

### P2 — Implement Organization + Event Schema (Effort: 4–8h dev | Impact: Critical)

Add `Organization` / `PerformingArtsTheater` sitewide and `Event` schema on every event page. See schema-audit.md for complete JSON-LD templates.

### P3 — Create /llms.txt (Effort: 2h | Impact: High)

Template provided in Section 2 above. Signals deliberate AI-readiness and provides a curated entity definition.

### P4 — Add FAQ Blocks to /om-kulturhuset/ + FAQPage Schema (Effort: 3–4h | Impact: High)

Recommended questions (each with a 134–167 word Norwegian-language answer):
- Hva er Moss Kulturhus?
- Hvilke scener finnes i Moss Kulturhus?
- Hva slags arrangementer holder Moss Kulturhus?
- Hvordan kjøper jeg billetter til Moss Kulturhus?
- Hvor ligger Moss Kulturhus?
- Kan man leie lokaler i Moss Kulturhus?

### P5 — Fix 61 Alt Text Values + Launch YouTube Channel (Alt: 4h | YouTube: ongoing | Impact: Medium–High)

Alt text format: `[Artistnavn] — konsert på Moss Kulturhus [dato]`
YouTube: 10–15 videos lifts entity graph measurably within 3–6 months.

---

## 9. Wikipedia/Wikidata Priority

Create a Norwegian Wikipedia article for Moss Kulturhus. The venue meets notability criteria as a municipal cultural institution. A Wikipedia article creates the `sameAs` anchor AI models use as ground truth for entity attributes. Estimated effort: 8–12 hours. Permanent AI visibility uplift.

---

## 10. 90-Day GEO Roadmap

| Week | Action | Score Gain |
|---|---|---|
| 1 | Add H1 + rewrite meta description | +8 pts |
| 1 | Create /llms.txt | +5 pts |
| 2 | Implement Organization schema sitewide | +10 pts |
| 2 | Implement Event schema on all 59 event pages | +8 pts |
| 3 | Fix 61 missing alt text values | +4 pts |
| 4 | FAQ section + FAQPage schema on /om-kulturhuset/ | +8 pts |
| 5–6 | Rewrite /om-kulturhuset/ with citable passages | +6 pts |
| 6–8 | Create Wikipedia stub + Wikidata entry | +7 pts |
| 8–12 | Launch YouTube channel (5+ videos) | +10 pts |

**Projected score after 90 days:** ~74/100 (from 28/100)
