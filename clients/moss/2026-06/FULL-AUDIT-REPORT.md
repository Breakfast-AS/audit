# SEO Full Audit Report — Moss Kulturhus
**URL:** https://www.mosskulturhus.no/
**Audit date:** 2026-06-03
**Platform:** WordPress + Yoast SEO v27.0 + WP Engine + Cloudflare
**Language:** Norwegian (nb-NO)
**Business type:** Brick-and-mortar performing arts venue (Moss, Østfold)

---

## Overall SEO Health Score: 30 / 100

| Category | Weight | Score | Weighted |
|---|---|---|---|
| Technical SEO | 22% | 47 | 10.3 |
| Content Quality | 23% | 28 | 6.4 |
| On-Page SEO | 20% | 22 | 4.4 |
| Schema / Structured Data | 10% | 8 | 0.8 |
| Performance (CWV) | 10% | 38 | 3.8 |
| AI Search Readiness | 10% | 28 | 2.8 |
| Images | 5% | 8 | 0.4 |
| **Total** | **100%** | | **28.9 → 30** |

> **Supplemental score — Local SEO:** 31/100 (not in main weighting; included as separate audit track)

---

## Executive Summary

Moss Kulturhus is a legitimate, publicly significant cultural venue that is underperforming in search due to a cluster of high-impact, fixable issues rather than fundamental architectural problems. The site's infrastructure (WordPress, Yoast, Cloudflare, WP Engine) is sound. The problems are configuration and content issues that a focused 4–6 week sprint can largely resolve.

### Top 5 Critical Issues

1. **Duplicate brand name in all 164 page titles** — Every title ends with "- Moss kulturhus - Moss kulturhus". One Yoast template fix resolves all pages simultaneously.
2. **Zero Event schema on 59 event pages** — The entire event catalog is invisible to Google's event rich results. For a venue that sells tickets, this is direct revenue loss.
3. **95% of images missing alt text** — 61 of 64 images on the homepage alone have no alt attribute. This affects image search, accessibility, and AI crawler understanding.
4. **No H1 on the homepage** — The most fundamental on-page signal is absent on the most important page.
5. **No Organization or LocalBusiness schema** — Google cannot build a reliable knowledge panel or entity graph for Moss Kulturhus.

### Top 5 Quick Wins (< 2 hours each)

1. Fix Yoast title template to remove brand duplication (30 min)
2. Add H1 to the homepage: "Moss Kulturhus — konsert- og kulturarena i Moss, Østfold" (15 min)
3. Enable HSTS in Cloudflare SSL settings (5 min)
4. Set tag archive pages to noindex in Yoast (15 min)
5. Add `X-Content-Type-Options`, `Referrer-Policy`, and `X-Frame-Options` headers via Cloudflare Transform Rules (30 min)

---

## Section 1: Technical SEO — Score: 47/100

*Full details: technical-audit.md*

### Crawlability
- **robots.txt:** Valid, allows all crawlers ✓
- **Crawl-delay: 10** — unnecessarily throttles Bing and other crawlers. Remove or reduce to 1.
- Empty `Disallow:` line is syntactically ambiguous — remove it.
- No explicit AI crawler directives (GPTBot, ClaudeBot, etc.)

### Indexability
- Canonical tags correct and self-referencing on all sampled pages ✓
- Sitemap index present and referenced in robots.txt ✓
- **CRITICAL: All 164 page titles contain duplicate brand name** — Yoast title separator misconfiguration
- **Tag archive pages (14)** indexed — almost certainly thin content, should be noindexed
- **Organizer archive pages (24)** — external promoter pages, likely thin, review for noindex
- **Past events** accumulating in event-sitemap with no lifecycle management
- `lastmod` on page-sitemap is unreliable — /program/ shows 2018, /homepage/ shows 2024 despite showing 2026 events

### Security
- HTTPS enforced ✓
- Cloudflare CDN active ✓
- **MISSING: Strict-Transport-Security (HSTS)** — enable in Cloudflare SSL panel
- **MISSING: X-Frame-Options** — add via Cloudflare Transform Rules
- **MISSING: X-Content-Type-Options** — add via Cloudflare Transform Rules
- **MISSING: Content-Security-Policy** — complex, medium priority
- **MISSING: Referrer-Policy** — add via Cloudflare Transform Rules
- `X-Powered-By: WP Engine` exposes platform — minor info disclosure
- `wp-json` API link in headers exposes REST API endpoint

### Caching
- **cf-cache-status: DYNAMIC** — Cloudflare is not caching HTML pages
- **X-Cache-Enabled: False** — WP Engine object cache disabled
- This directly increases TTFB and hurts LCP scores. Enable page caching in WP Engine dashboard.

### URL Structure
- Clean, readable URLs ✓
- No trailing slash inconsistencies detected ✓
- Year-specific slugs: `/christian-frederik-dagene-2024/`, `/kryssover-jazzfest-moss-2026/` — will become stale

---

## Section 2: Content Quality — Score: 28/100

*Full details: content-audit.md*

### E-E-A-T Assessment

| Signal | Status | Score |
|---|---|---|
| Experience (reviews, testimonials) | Missing | 4/25 |
| Expertise (staff profiles, artistic director) | Missing | 3/25 |
| Authoritativeness (third-party mentions, press) | Partial | 9/25 |
| Trustworthiness (privacy policy, HTTPS, contact info) | Partial | 12/25 |

No staff profiles, no named artistic director, no audience testimonials, no visible phone/address on most pages.

### Thin Content Pages

| Page | Word count | Status |
|---|---|---|
| /venue/parkteatret/ | ~127 words | CRITICAL |
| /venue/samfunnshuset/ | ~131 words | CRITICAL |
| /stand-up/ | ~174 words | HIGH |
| /om-kulturhuset/ | ~273 words | HIGH |

Venue pages contain only opening hours and phone number. No venue description, history, capacity, facilities, or accessibility info.

### Meta Description Coverage

| Page | Meta Description |
|---|---|
| / (homepage) | "Moss Kulturhus består av Parkteatret og Samfunnshuset. Velkommen til oss." (thin) |
| /om-kulturhuset/ | Has one ✓ |
| All 59 event pages | MISSING |
| /program/, /stand-up/, /teater/, venue pages | MISSING |

~90% of pages lack meta descriptions.

### AI Citation Readiness: 12/100

- No FAQ sections anywhere on the site
- No structured answer blocks
- No question-format headings (H2/H3)
- Event pages contain date and venue info in body text but zero schema support
- No named authorship on any pages

---

## Section 3: On-Page SEO — Score: 22/100

### Title Tags

All 164 pages use broken title template: `[Page Name] - Moss kulturhus - Moss kulturhus`

**Fix in Yoast SEO → Search Appearance → Title separator:**
- Current (likely): `%%title%% - %%sitename%% - %%sitename%%`
- Correct: `%%title%% - %%sitename%%`
- Homepage specific: `Moss kulturhus - Kulturhuset midt i byen`

Venue pages show "Arkiver" (WordPress archive label) in titles — these need custom titles via Yoast taxonomy settings.

### Meta Descriptions

Write for all event pages (template approach):
> `[Artistnavn] opptrer på Moss Kulturhus [dato]. Kjøp billetter og les mer om forestillingen her.`

### Heading Structure

| Page | H1 | H2 | Notes |
|---|---|---|---|
| / (homepage) | MISSING | Event names only | Critical |
| /program/ | "PROGRAM" | None | OK but not keyword-rich |
| /venue/parkteatret/ | MISSING | None | Critical |
| /venue/samfunnshuset/ | MISSING | None | Critical |
| Event pages | Event name ✓ | "Praktisk info" only | Good H1 |

### Internal Linking
- 90 internal links on homepage ✓ (good distribution)
- Navigation structure logical ✓
- Venue pages are navigation dead-ends (no links to related events)

---

## Section 4: Schema / Structured Data — Score: 8/100

*Full details: schema-audit.md*

### Current Implementation

Every page on the site uses Yoast's auto-generated `WebPage` schema only. This is the absolute minimum Yoast outputs and delivers zero rich result value.

### Missing Schema (Priority Order)

| Priority | Schema Type | Pages | Impact |
|---|---|---|---|
| 1 | `Event` | 59 event pages | Google Events tab, event rich results, AI summaries |
| 2 | `Organization` + `PerformingArtsTheater` | Homepage | Knowledge panel, entity graph, AI citations |
| 3 | `EventVenue` + `LocalBusiness` | Venue pages | Local pack, venue rich results |
| 4 | `BreadcrumbList` | All pages | SERP breadcrumb display |
| 5 | `FAQPage` | /om-kulturhuset/ | Featured snippets, AI overviews |

### Implementation Note

The Events Calendar plugin (which appears to power the `/event/` post type) likely has built-in Event schema support. Check the plugin settings before building custom schema — it may require only a configuration toggle.

Complete JSON-LD templates for all 5 schema types are in `schema-audit.md`.

---

## Section 5: Sitemap — Score: 38/100

*Full details: sitemap-audit.md*

### Structure Issues

| Issue | Impact |
|---|---|
| Homepage lastmod = 2024-03-01 despite showing 2026 events | Misleads crawler freshness signals |
| /program/ lastmod = 2018-04-27 (8 years stale) | Same |
| All 59 events show lastmod = today (auto-generated) | Google learns to distrust lastmod for entire domain |
| /event/riksteateret-ubesvart-anrop/ + /event/riksteatret-ubesvart-anrop/ | Duplicate event (typo in slug) |
| /parkteatret/ + /venue/parkteatret/ both exist | Potential duplicate pages for same venue |
| /kryssover-jazzfest-moss/ + /kryssover-jazzfest-moss-2026/ | Near-duplicate festival pages |
| /category/concert/ (English slug on Norwegian site) | Inconsistency |
| /category/festival/ + /category/festivaler/ | Near-duplicate categories |
| /category/julekonsert/ + /category/julekonserter/ | Near-duplicate categories |
| /category/ukategorisert/ (uncategorized) in sitemap | Should be noindexed |
| 24 organizer archive pages | Likely thin, review for noindex |

---

## Section 6: Performance (CWV) — Score: 38/100 mobile / 62/100 desktop

*Full details: performance-audit.md*

### Key Issues

- **Cloudflare not caching HTML** (cf-cache-status: DYNAMIC) — primary cause of poor TTFB
- **WP Engine page caching disabled** (X-Cache-Enabled: False)
- 10 external scripts loaded on homepage (render-blocking risk)
- 64 images on homepage without lazy loading confirmation
- Custom fonts (Monterio) preloaded ✓ but may cause FOUT
- No evidence of WebP/AVIF image serving
- HTTP/3 support present (alt-svc: h3=":443") ✓
- Brotli compression active ✓

### Priority Performance Fixes

1. Enable WP Engine page caching (dashboard toggle)
2. Configure Cloudflare caching rules for HTML pages
3. Audit 10 external scripts — defer/async non-critical ones
4. Implement WebP/AVIF serving for event thumbnails
5. Verify lazy loading on images below the fold

---

## Section 7: AI Search Readiness (GEO) — Score: 28/100

*Full details: geo-audit.md*

| Platform | Score | Primary Blocker |
|---|---|---|
| Google AI Overviews | 12/100 | No H1, no schema, no structured passages |
| ChatGPT web search | 20/100 | No citable content blocks |
| Perplexity AI | 18/100 | No llms.txt, no FAQ, no authority docs |
| Bing Copilot | 15/100 | No Event/Organization schema |

**Top AI fixes:**
1. Create `/llms.txt` with entity definition (2h effort, high impact)
2. Add H1 + rewrite meta description
3. Implement Organization + Event schema
4. Add FAQ section to /om-kulturhuset/ with FAQPage schema
5. Create Wikipedia/Wikidata entry (permanent entity anchor)
6. Launch YouTube channel (0.737 correlation with AI citation frequency)

---

## Section 8: Images — Score: 8/100

### Alt Text Coverage

| Page | Total images | Missing alt | Rate |
|---|---|---|---|
| / (homepage) | 64 | 61 | 95% |
| /program/ | 58 | 55 | 95% |
| /venue/parkteatret/ | 13 | 10 | 77% |
| Event page (Dybdahl) | 10 | 7 | 70% |
| **Site total (estimated)** | **~300+** | **~285** | **~95%** |

Note: Hero separator images (decorative) should use `alt=""` (empty, not missing) — this is correct. Event poster images and venue photos must have descriptive alt text.

**Recommended alt text format:**
- Event posters: `[Artistnavn] – konsert på Moss Kulturhus, [dato]`
- Venue photos: `[Romnavn] i Moss Kulturhus med [kapasitet] sitteplasser`

---

## Section 9: Local SEO — Score: 31/100

*Full details: local-audit.md*

### Critical Gaps

| Issue | Impact |
|---|---|
| No Google Business Profile confirmed | Missing #1 local ranking factor |
| No LocalBusiness / PerformingArtsTheater schema | Google cannot geolocate entity |
| No machine-readable NAP anywhere on site | Cannot verify address in search |
| No venue location pages with substantive content | Core local ranking asset absent |
| No review integration or aggregateRating schema | Trust signal missing |
| Subdomain fragmentation (billetter., nyhetsbrev.) | Splits authority signals |

### NAP Found on Site (Parkteatret page)
- Phone: 404 09 924
- Hours: "En time før alle forestillinger" (opening time) / "Mandag–fredag: kl. 12.00–15.00" (phone hours)
- Address: Not confirmed in machine-readable form

### Top Local SEO Actions
1. Claim/optimize Google Business Profile with primary category "Performing Arts Theater"
2. Add `PerformingArtsTheater` + `LocalBusiness` schema with geo coordinates
3. Add crawlable NAP block to site-wide footer
4. Rebuild venue pages as genuine location pages (400+ words each)
5. Submit consistent citations to 1881.no, gulesider.no, visitostfold.com
6. Embed Google Maps on homepage and venue pages

---

## Technical Details

**Platform:** WordPress, custom theme `mosskulturhus-redesign`
**SEO Plugin:** Yoast SEO v27.0
**Hosting:** WP Engine (X-Powered-By header)
**CDN:** Cloudflare (Oslo PoP confirmed: CF-RAY ends in -OSL)
**HTTP version:** HTTP/3 support (h3=":443") ✓
**Compression:** Brotli ✓
**HTTPS:** Enforced ✓
**Facebook verification:** Present ✓
**Google site verification:** Present ✓
**OG tags:** Present ✓
**Twitter card:** summary_large_image ✓
**hreflang:** Not detected (single language site — OK)
**XML sitemap:** 6-part sitemap index ✓
**robots.txt:** Valid ✓
