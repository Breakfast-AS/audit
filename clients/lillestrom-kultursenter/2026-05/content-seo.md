# Content Quality SEO Audit — Lillestrøm Kultursenter

**URL:** https://www.lillestrom-kultursenter.no/
**Audit date:** 2026-05-29
**Language scope:** Norwegian (nb-NO)

---

## Overall Content Quality Score: 48 / 100

| Dimension | Score | Weight | Weighted |
|---|---|---|---|
| E-E-A-T | 42/100 | 35% | 14.7 |
| Technical content hygiene | 35/100 | 25% | 8.75 |
| Keyword optimisation | 55/100 | 15% | 8.25 |
| AI citation readiness | 40/100 | 15% | 6.0 |
| Content freshness | 50/100 | 10% | 5.0 |
| **Total** | | | **48** |

---

## 1. E-E-A-T Assessment

### 1.1 Experience — 30 / 100

**Present:** Event listings imply a live, operating venue. Hall rental pages (12 venues) confirm physical facilities. NAP data (Kirkegata 11, 2000 Lillestrøm / 64 84 55 50) is crawlable.

**Missing:**
- No first-hand editorial voice on the homepage or about pages.
- No visitor testimonials, audience quotes, or post-event write-ups.
- No behind-the-scenes or operational knowledge signals.
- 17 blog posts for a venue with 338 active events represents severe under-documentation of lived experience.

**Recommendation:** Rewrite /om-oss/ to include founding year, milestones, named staff voices, and visitor volume figures.

---

### 1.2 Expertise — 45 / 100

**Present:** Topical breadth across events and hall types. Hall pages reach 1,000–5,000 words.

**Missing:**
- /om-oss/ansatte/ lacks structured author bios.
- No author attribution on 17 blog posts.
- Hall pages likely lack technical specs (acoustic ratings, stage dimensions, AV specs).
- Event descriptions appear templated from promoter feeds without editorial augmentation.

**Recommendation:** Add structured author bios with photos and roles. Add 2–3 sentences of local editorial voice to each event page. Include hall technical riders as summary tables.

---

### 1.3 Authoritativeness — 40 / 100

**Present:** Generalsponsorer section signals commercial legitimacy.

**Missing:**
- No press coverage citations or links to external media mentions.
- No awards, certifications, or industry body memberships.
- No links to/from Lillestrøm kommune, Akershus cultural bodies, or Kulturrådet.
- Site does not reference a Wikipedia/Wikidata entity.
- No "Presse og omtale" section.

**Recommendation:** Create a dedicated "Presse og omtale" page. Add outbound links to authoritative Norwegian cultural institutions. Submit/verify a Wikidata entity.

---

### 1.4 Trustworthiness — 52 / 100

**Present:** Physical address and phone are crawlable.

**Missing — critical:**
- **Indexed internal pages:** /internt/styredokumenter/, /internt/handlingsplan/, /internt/arsberetninger/ are publicly indexed. This signals poor content governance.
- **Indexed test page:** /nyhetsbrev-test/ and /for-og-etter-test/ are indexed.
- **Outdated COVID content:** /smittevern/ contains stale pandemic health/safety content. Per QRG, stale health/safety content is a direct negative E-E-A-T signal.

**Recommendation:** Immediately noindex all /internt/* pages and test pages. Either update /smittevern/ or 301 redirect to /praktisk-informasjon/.

---

## 2. Technical Content Hygiene

**Score: 35 / 100**

### 2.1 Missing H1 on Homepage — CRITICAL

The homepage has no H1. This is the single most damaging individual content signal on the site.

**Fix:** Add one H1 immediately in the hero section:
`Lillestrøm Kultursenter – konserter, teater og opplevelser i Lillestrøm`

The current title tag slogan "Du kan bare begynne å glede deg!" belongs as a brand tagline (H2 or `<p>`).

---

### 2.2 Meta Descriptions Missing at Scale

| Scope | Count |
|---|---|
| Core static pages | 6 |
| Hall pages | 12 |
| Event pages | 338 |
| **Total affected** | **356+** |

Google is auto-generating SERP snippets from body text — likely pulling dates or generic phrases.

**Fix priority:**
1. 6 core static pages: rewrite manually with target keywords.
2. 12 hall pages: commercial intent — each needs a unique, conversion-focused description.
3. 338 event pages: implement a Yoast dynamic template:
   `%%title%% – %%event_date%% | Kjøp billetter – Lillestrøm Kultursenter`

---

### 2.3 Title Tag Patterns — Weak Keyword Signal

**Current pattern:** `[Page Name] - Lillestrøm Kultursenter`

| Current | Recommended |
|---|---|
| Om oss - Lillestrøm Kultursenter | Om Lillestrøm Kultursenter – Historikk og ansatte |
| Utleie - Lillestrøm Kultursenter | Lei saler og lokaler i Lillestrøm – Konferanser og selskaper |
| Kontakt oss - Lillestrøm Kultursenter | Kontakt Lillestrøm Kultursenter – Kirkegata 11, 2000 Lillestrøm |

**Fix:** Rewrite title tags for all 36 static pages. Event pages template:
`%%title%% – Billett og info | Lillestrøm Kultursenter`

---

### 2.4 Word Count Assessment

| Page type | Min required | Observed | Status |
|---|---|---|---|
| Homepage | 500 | ~400 body text | BELOW MINIMUM |
| Hall pages | 800 | 1,000–5,000 | PASS |
| Event pages | 300+ (event) | 1,400–1,700 | PASS |
| Core info pages | 800 | Unknown | NEEDS AUDIT |

---

### 2.5 Image Alt Text

Hall pages have images with missing alt text — both an accessibility failure and an image search gap.

**Fix pattern:** `[Hall name] – [key feature], Lillestrøm Kultursenter`
Example: `Stjernesalen – 800-seters konsertsal med profesjonell lyd og lys, Lillestrøm Kultursenter`

---

## 3. Keyword Optimisation

**Score: 55 / 100**

**Strengths:**
- Event pages have H1s with event names — effective long-tail targeting.
- Homepage meta description covers core service terms.

**Gaps:**
- No H1 containing "Lillestrøm" on homepage.
- Rental/utleie pages are underoptimised for "lei konferansesal Lillestrøm", "selskapslokale Lillestrøm".
- No topical cluster architecture: no hub-and-spoke linking from homepage → category pages → individual pages.

---

## 4. AI Citation Readiness

**Score: 40 / 100**

**What works:**
- Event schema on 338 pages is the strongest AI citation signal.
- NAP data is crawlable.

**What fails:**
- No Organization schema on homepage (foundational for AI entity recognition).
- No FAQ schema on /praktisk-informasjon/ or /utleie/.
- No quotable factual statements (e.g., founding year, visitor volumes).
- Indexed internal pages damage entity coherence for AI crawlers.

---

## 5. Content Freshness

**Score: 50 / 100**

**Positive:** 338 event pages with 2026 dates signal active maintenance.

**Negative:**
- /smittevern/ is a 2022 COVID page still indexed in 2026.
- No "Sist oppdatert" timestamps on static pages.
- 17 blog posts total — severe under-investment for an active venue.
- No seasonal programme landing pages.

---

## 6. Prioritised Recommendations

### Priority 1 — Immediate (within 1 week)

1. **Add H1 to homepage:** `Lillestrøm Kultursenter – konserter, teater og opplevelser i Lillestrøm`
2. **Noindex /internt/* and test pages.** Governance failure with active exposure risk.
3. **Remove or redirect /smittevern/.** 301 to /praktisk-informasjon/.
4. **Add Organization + PerformingArtsTheater schema to homepage.** Most impactful AI fix.

### Priority 2 — Short term (within 1 month)

5. Write meta descriptions for 6 core static pages manually.
6. Implement Yoast dynamic meta description template for 338 event pages.
7. Rewrite title tags for all 36 static pages.
8. Expand homepage body content to 200+ words of genuine venue description.
9. Audit and fix all 12 hall page image alt texts.

### Priority 3 — Medium term (1–3 months)

10. Rewrite /om-oss/ with founding story, visitor figures, staff quotes, last-updated date.
11. Add structured author bios to /om-oss/ansatte/.
12. Write individual meta descriptions for all 12 hall pages.
13. Add FAQ schema to /praktisk-informasjon/ and /utleie/.
14. Build topical cluster architecture with deliberate internal linking.
15. Add editorial paragraphs to top 20 events to differentiate from promoter copy.

### Priority 4 — Ongoing

16. Publish 2 editorial blog posts per month.
17. Add visible "Sist oppdatert" timestamps to all static pages.
18. Create seasonal programme landing pages (e.g., /program/host-2026/).
19. Submit/verify Wikidata entity for AI knowledge graph association.

---

## Quick-Reference Metrics

| Metric | Current | Target |
|---|---|---|
| Content quality score | 48/100 | 70+ |
| E-E-A-T composite | 42/100 | 65+ |
| AI citation readiness | 40/100 | 60+ |
| Pages missing meta description | 356+ | 0 |
| H1 issues | 1 (homepage — critical) | 0 |
| Indexed internal/test pages | 7+ | 0 |
| Blog posts published | 17 | 50+ |
