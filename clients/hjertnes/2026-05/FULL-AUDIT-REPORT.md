# SEO Audit Report — hjertnes.no
**Hjertnes Kulturhus, Sandefjord, Norway**
**Audit Date:** 2026-05-29
**Auditor:** Full-spectrum SEO audit (8 specialist agents)

---

## Overall SEO Health Score: 42 / 100

| Category | Weight | Score | Weighted |
|---|---|---|---|
| Technical SEO | 22% | 48/100 | 10.6 |
| Content Quality | 23% | 40/100 | 9.2 |
| On-Page SEO | 20% | 38/100 | 7.6 |
| Schema / Structured Data | 10% | 10/100 | 1.0 |
| Performance (CWV) | 10% | 68/100 | 6.8 |
| AI Search Readiness | 10% | 38/100 | 3.8 |
| Images | 5% | 62/100 | 3.1 |
| **TOTAL** | | | **42 / 100** |

**Local SEO Score (separate): 34 / 100**

### Interpretation
The site has a solid infrastructure foundation (Cloudflare CDN, WP Engine, HTTPS, working sitemaps) but scores critically low on content, schema, and local signals. The primary blockers are: (1) 895 event pages with zero Event schema, (2) homepage with no editorial text, (3) no LocalBusiness schema, (4) all security headers missing, and (5) no city name in any page title. These five issues alone suppress every major ranking category.

---

## Site Profile

| Property | Value |
|---|---|
| URL | https://hjertnes.no/ |
| Business type | Cultural center + cinema (brick-and-mortar) |
| Industry | PerformingArtsTheater / EntertainmentBusiness |
| Location | Sandefjordsveien 3, 3202 Sandefjord, Vestfold, Norway |
| Founded | 1975 (Sandefjord municipality-owned) |
| CMS | WordPress |
| Hosting | WP Engine + Cloudflare CDN (Oslo PoP) |
| SEO plugin | Yoast SEO v27.3 |
| Language | Norwegian Bokmål (nb-NO) |
| Total indexed URLs | ~1,454 (30 pages + 1,089 events + 335 taxonomy archives) |

---

## Executive Summary

### Top 5 Critical Issues
1. **895 event pages have zero Event schema** — no Google event rich results, no event carousels, no AI citations from event data
2. **Homepage contains zero editorial text** — AI systems and Google cannot answer "what is Hjertnes kulturhus?" from the homepage
3. **All 6 standard security headers missing** — no HSTS, no CSP, no X-Frame-Options, no X-Content-Type-Options
4. **Postal code inconsistency: 3202 vs 3208** — NAP mismatch across pages undermines local SEO entity matching
5. **No LocalBusiness/PerformingArtsTheater schema anywhere** — invisible to Google Knowledge Panel, Maps, and AI local queries

### Top 5 Quick Wins
1. Add a 150-word editorial intro paragraph to the homepage (1 hour)
2. Add `Sandefjord` to all page title tags via Yoast SEO templates (2 hours)
3. Fix postal code on contact page from 3208 → 3202 (10 minutes)
4. Create `/llms.txt` with structured site summary (2 hours)
5. Add security headers via Cloudflare Transform Rules (30 minutes)

---

## 1. Technical SEO

**Score: 48 / 100**

### Security Headers — CRITICAL (all absent)

The server returns zero security headers. Cloudflare can inject all of these at the edge:

| Header | Status | Risk |
|---|---|---|
| Strict-Transport-Security (HSTS) | MISSING | Browser can be downgraded to HTTP on first visit |
| X-Frame-Options | MISSING | Clickjacking risk |
| X-Content-Type-Options | MISSING | MIME-type sniffing |
| Content-Security-Policy | MISSING | XSS attack vector |
| Referrer-Policy | MISSING | Referrer leakage |
| Permissions-Policy | MISSING | Feature abuse |

**Fix:** Add via Cloudflare Transform Rules:
```
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
```

### www Redirect Chain — CRITICAL

`https://www.hjertnes.no/` → 301 → `http://hjertnes.no/` (unencrypted!) → 301 → `https://hjertnes.no/`

This 2-hop chain passes through an unencrypted HTTP intermediate step. Fix at Cloudflare: redirect `www.*` directly to `https://hjertnes.no/` in one 301.

### xmlrpc.php Exposed — CRITICAL

`https://hjertnes.no/xmlrpc.php` returns HTTP 200. This endpoint is a brute-force and DDoS amplification vector with no legitimate modern use. Block via Cloudflare WAF rule or WP Engine dashboard. Also disable the pingback link in `<head>`.

### Invalid datePublished in Schema — HIGH

All event pages output `"datePublished":"-0001-11-30T00:00:00+00:00"` — an invalid date from unset WordPress custom post type dates. Causes Google Rich Results Test validation failures.

### Thin Taxonomy Pages (263 URLs) — HIGH

All indexed with no `noindex`, no meta descriptions, no H1, and minimal content:
- `event_promoter` archives: 197 URLs
- `event_hall` archives: 87 URLs
- `event_genre` archives: 31 URLs
- `event_category` archives: 12 URLs
- `event_type` archives: 2 URLs

Many of these return "ingen treff" (no results). Apply conditional `noindex` when archive returns 0 events.

### user-scalable=no in Viewport Meta — MEDIUM

`<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">`

Violates WCAG 2.1 SC 1.4.4 (Resize Text) and is a Norwegian legal accessibility obligation under the Accessibility Act. Remove `user-scalable=no`.

### Render-Blocking Scripts — MEDIUM

Three scripts load synchronously in `<head>` without `defer`:
- `jquery.min.js` (3.7.1)
- `jquery-migrate.min.js` (3.4.1)
- `scripts.min.js` (theme)

Add `defer` where inline script dependencies allow.

### No Resource Hints — MEDIUM

Zero `<link rel="preload">`, `<link rel="preconnect">`, or `<link rel="dns-prefetch">` present. Preconnect to any third-party origins; preload the LCP hero image.

### Crawl-delay Malformed — MEDIUM

`Crawl-delay: 10` appears before any `User-agent:` block in robots.txt — syntactically invalid. Move inside `User-agent: *` block or remove entirely.

### No AI Crawler Policy — MEDIUM

No rules for GPTBot, ClaudeBot, Google-Extended, PerplexityBot, or other AI crawlers. All are currently allowed by the wildcard rule. Define an explicit policy.

### No IndexNow — LOW

With 1,089+ event URLs that change frequently, IndexNow would ensure faster indexing by Bing and other participating engines. Enable via free Yoast IndexNow plugin.

### WP REST API Exposed — LOW

`/wp-json/` returns full JSON. Consider restricting unauthenticated endpoints not required by the public theme.

---

## 2. Content Quality

**Score: 40 / 100**

### Homepage — Zero Editorial Text — CRITICAL

The homepage body contains exclusively a JavaScript-rendered event slider and film carousel. There is **no prose text** for Google or AI systems to read. No H1 in `<main>`. No value proposition. No location statement. Word count of unique editorial content: **0**.

A user asking "what is Hjertnes kulturhus?" cannot be answered from the homepage.

**Fix:** Add a 150–200 word editorial intro block:
> "Hjertnes Kulturhus er Sandefjords kulturhus og kino, åpnet i 1975. Vi tilbyr konserter, teater, film og kulturarrangementer for alle aldre, med saler fra intime rom til Harmonie arena med plass til 800 personer. Adresse: Sandefjordsveien 3, 3202 Sandefjord. Telefon: 33 41 67 60."

### /kino/ Cinema Page — Zero Editorial + No Meta Description — CRITICAL

The cinema landing page contains zero editorial text — only dynamically loaded film poster cards. No meta description exists. H1 is a single word: "Kino".

Google must write its own snippet from a movie title for searches like "kino Sandefjord". Add 300–400 words describing the cinema's features, halls, technology, and ticket options.

### FAQ Page — No FAQPage Schema, Broken Heading Hierarchy — CRITICAL

The FAQ page has 14+ question/answer accordion pairs with strong, detailed content. However:
- No `FAQPage` JSON-LD schema applied
- Questions use `<strong>` inside `<p class="toggle">` rather than `<h3>` or `<h4>` headings
- Google AI Overviews heavily reward FAQ schema for local business questions

Add `FAQPage` schema and convert question toggles to proper heading elements.

### /utleie/ Venue Rental — Thin Content — HIGH

Only ~280 words of editorial text on the primary venue rental page. No capacity figures for any hall. No pricing. No booking process. Minimum 800 words for a primary service page. Expand to include: individual hall capacities (Harmonie arena: 800, Sal 1: X, Sal 2: X, Sal 3: X), AV specifications, catering options, pricing range, booking process.

### Homepage Title Tag — HIGH

"Velkommen til Hjertnes Kulturhus" — "Velkommen til" wastes the first 15 characters on a greeting.

**Recommended:** "Hjertnes Kulturhus – Konserter, Kino og Kulturarrangementer i Sandefjord" (73 chars)

### /kinokortet/ Meta Description — HIGH

Current: "Kinokortet – Den perfekte bedriftsgaven!" (40 chars — critically short, no keywords).

**Recommended:** "Kjøp Kinokortet fra Hjertnes kulturhus – kr 130 per kort, 20% rabatt på snacks. Perfekt bedriftsgave i Sandefjord. Bestill på e-post." (133 chars)

### E-E-A-T Assessment — MEDIUM

| Signal | Status |
|---|---|
| Author bylines | None on any page |
| Staff profiles | Contact for venue rental only (Jonas Myklebust Lima) |
| Founding date stated | About page only |
| Municipality ownership stated | Contact page only |
| Press citations | None visible on-page |
| External authority links | lovdata.no, barnevakten.no in FAQ (positive) |

### Sitewide og:type Error — MEDIUM

All pages use `og:type: article`. Permanent service/landing pages should use `og:type: website`.

### No Breadcrumbs on Service Pages — MEDIUM

`<!-- No breadcrumbs -->` comment suppresses breadcrumbs on /kino/, /utleie/, /kinokortet/, and others. Re-enable breadcrumbs sitewide — they are a direct Google SERP signal.

### Accordion Content Visibility — MEDIUM

FAQ accordion answers exist in the HTML DOM but are toggled via JavaScript. While Googlebot renders JS, accordion content is weighted lower than visible-on-load text. Ensure answers are present in rendered HTML.

---

## 3. On-Page SEO

**Score: 38 / 100**

### No City Name in Any Title Tag — CRITICAL for Local

Not a single page title contains "Sandefjord". Yoast SEO is installed but not configured for geo-targeting.

| Current | Recommended |
|---|---|
| "Kino - Hjertnes kulturhus" | "Kino i Sandefjord \| Hjertnes Kulturhus" |
| "Utleie - Hjertnes kulturhus" | "Lei saler i Sandefjord \| Hjertnes Kulturhus" |
| "Om Hjertnes kulturhus" | "Om Hjertnes Kulturhus – Kulturhus i Sandefjord siden 1975" |
| "Kontakt - Hjertnes kulturhus" | "Kontakt Hjertnes Kulturhus Sandefjord – Tlf 33 41 67 60" |

### No Meta Descriptions on Most Pages — HIGH

Only the homepage has a meta description. All event pages, all taxonomy archives, and most service pages lack meta descriptions entirely. Yoast SEO can generate these via templates:

For event pages: `%%post_title%% – %%excerpt%% – Billetter og info på Hjertnes Kulturhus Sandefjord.`

### H1 Missing on Homepage — HIGH

No H1 in `<main>` content. The SVG logo has no text fallback accessible as H1. Add one clear H1 to the homepage body.

### Phone Numbers Not `tel:` Links — HIGH

`33 41 67 60` appears on all pages as plain text. Wrap in `<a href="tel:+4733416760">33 41 67 60</a>` for mobile click-to-call and local signal.

### No Google Maps Embed on Contact Page — HIGH

The contact page lists the address but has no interactive map. Add a Google Maps iframe pinned to the verified GBP listing.

### OG Image Missing on Homepage — HIGH

`twitter:card: summary_large_image` declared but no `og:image` or `twitter:image` set. Every social share renders with no image. Add a branded 1200×630px image via Yoast SEO Social settings.

### Internal Links — MEDIUM

Service sub-pages (/kinoprogram/, /kino/kinobursdag/, etc.) are navigation-only links with no editorial contextual linking. Add contextual links from related pages.

### H1 "Kino" on Cinema Page — MEDIUM

One-word H1 provides no topical signal. Use: "Kino på Hjertnes Kulturhus – Se de nyeste filmene i Sandefjord."

---

## 4. Schema / Structured Data

**Score: 10 / 100**

This is the lowest-scoring category and the highest-leverage improvement area.

### No Event Schema on 895+ Event Pages — CRITICAL

Every event page (`/program/`, `/kinoprogram/`) has only Yoast's default `WebPage` schema. Zero `Event` structured data. Google supports rich results for events — date chips, venue, ticket price, event carousels — that would appear directly in SERPs for searches like "konserter Sandefjord", "kino Sandefjord".

**Minimum required properties:** `name`, `startDate`, `location` (with `Place`/`PostalAddress`), `offers` (with ticket URL), `eventStatus`.

For cinema screenings, use `ScreeningEvent` subtype with `workPresented` Movie entity.

**Implementation:** WordPress `wp_head` action hook, fires only on single event post templates. Template variables from the event's custom fields/ACF data.

### No LocalBusiness Schema — CRITICAL

No `LocalBusiness`, `PerformingArtsTheater`, or any venue-type schema anywhere on the site. The Yoast `Organization` block has no `address`, `telephone`, `email`, `openingHours`, `geo`, or `sameAs`.

**Fix:** Add `["LocalBusiness", "PerformingArtsTheater"]` block to homepage with full address (postal code **3202**), phone, geo coordinates, opening hours, and `sameAs` links.

### No FAQPage Schema — MEDIUM

FAQ page has 14+ Q&A pairs but no `FAQPage` JSON-LD. Google no longer shows FAQ rich results for commercial sites, but FAQPage schema is actively used by LLMs (ChatGPT, Perplexity, Claude) for direct answer extraction.

### Organization Schema Empty Fields — HIGH

Yoast's auto-generated Organization block has:
- `"description": ""` (empty string)
- No `telephone`
- No `address`
- No `sameAs`
- Logo at 800×200px (4:1 ratio — valid but suboptimal for Knowledge Panel)

### Invalid datePublished (-0001) — HIGH

All event pages output a corrupt datePublished of `-0001-11-30T00:00:00+00:00`. This fails Google's Rich Results Test validation. Fix by mapping Yoast's `datePublished` field to the actual event date.

---

## 5. Performance (Core Web Vitals)

**Score: 68 / 100**

### Lab Measurements

| Metric | Value | Assessment |
|---|---|---|
| TTFB (Cloudflare cache HIT) | 38–46ms | Excellent |
| Page HTML size (homepage) | 73.8 KB | Good |
| Page HTML size (event page) | 61.5 KB | Good |
| HTTP/2 | Yes | Pass |
| Gzip/Brotli compression | Yes (Cloudflare) | Pass |
| CDN (Cloudflare, Oslo PoP) | Yes | Pass |
| Cache-Control | max-age=600 | Pass |

### Core Web Vitals Estimates (lab-based — no CrUX field data available)

| Metric | Estimate | Risk Factors |
|---|---|---|
| LCP | Likely GOOD (<2.5s) | Hero images loaded via JS `data-source` attr; no `<link rel="preload">` for LCP image |
| INP | Likely GOOD (<200ms) | jQuery + theme JS only; no heavy SPA framework |
| CLS | Unknown — risk present | `user-scalable=no` + no explicit image dimensions on event thumbnails |

*Field data requires Google Search Console CrUX access. Run https://pagespeed.web.dev/?url=https://hjertnes.no/ for real Lighthouse scores.*

### Render-Blocking Resources — MEDIUM

3 scripts load synchronously without `defer`:
- `jquery.min.js` (3.7.1) — in `<head>`
- `jquery-migrate.min.js` (3.4.1) — in `<head>`
- `scripts.min.js` (theme) — in `<head>`

### No Resource Hints — MEDIUM

Zero `<link rel="preconnect">` or `<link rel="preload">` tags. Add preconnect for any third-party origins; preload LCP hero image.

### Event Images External CDN — INFO

Event images are served from `storage.googleapis.com/pim-ambio.appspot.com` (external ticketing platform CDN). These are loaded via `data-source` attributes and rendered by JavaScript — meaning they are not in the initial HTML `<img>` elements and cannot be preloaded. No direct fix available (controlled by the ticketing platform Ambio), but ensure above-fold event images have explicit width/height attributes to prevent CLS.

---

## 6. AI Search Readiness (GEO)

**Score: 38 / 100**

### Platform Scores

| Platform | Score | Primary Blocker |
|---|---|---|
| Google AI Overviews | 25/100 | No FAQPage schema, no LocalBusiness schema, empty homepage |
| ChatGPT / OpenAI | 35/100 | No llms.txt, thin entity definition, no Wikipedia |
| Perplexity | 40/100 | Content crawlable, FAQ answers good prose, no structured data |
| Bing Copilot | 30/100 | NAP inconsistency, no rich schema, no author signals |

### No llms.txt — CRITICAL

`https://hjertnes.no/llms.txt` returns 404. This is the fastest way to give AI systems a structured, authoritative entry point. Create at site root:

```
# Hjertnes Kulturhus
> Hjertnes Kulturhus er et kulturhus og kino i Sandefjord, Vestfold, Norge.
> Adresse: Sandefjordsveien 3, 3202 Sandefjord. Telefon: 33 41 67 60.
> Kulturhuset åpnet i 1975 og eies av Sandefjord Kommune.

## Viktige sider
- Om oss: https://hjertnes.no/om-hjertnes-kulturhus/
- Kulturprogram: https://hjertnes.no/program/
- Kino: https://hjertnes.no/kino/
- Spørsmål og svar: https://hjertnes.no/praktisk-informasjon/ofte-stilte-sporsmal/
- Kontakt: https://hjertnes.no/praktisk-informasjon/kontakt/
- Utleie: https://hjertnes.no/utleie/
```

### AI Crawler Access — PASS

All major AI crawlers (GPTBot, ClaudeBot, PerplexityBot) are allowed via the wildcard `User-agent: *` rule. No explicit policy defined.

### About Page — Only 90 Words — HIGH

The most important page for AI entity recognition contains only 3 short paragraphs (~90 words). Missing: municipality ownership, hall capacities, full service descriptions, structured facts section. Minimum 300 words needed.

### NAP Inconsistency — HIGH

Contact page uses postal code 3208; all other pages use 3202. This directly confuses AI systems building entity graphs. Fix immediately.

### Opening Hours Buried in FAQ — MEDIUM

Hours exist in the FAQ page ("Generelt" section) but not in a dedicated, addressable location. AI asked "hva er åpningstidene for Hjertnes kulturhus?" cannot extract a clean answer. Create a dedicated hours section on the contact page with `OpeningHoursSpecification` schema.

### No Wikipedia Presence — MEDIUM

A venue founded in 1975, primary cultural institution of a city of ~62,000 people — no Norwegian Wikipedia article exists. A Wikipedia entity is one of the strongest AI citation signals. Commission or draft a Wikipedia article for Hjertnes Kulturhus.

### AI Citation Readiness by Query

| Query | Answerable? | Gap |
|---|---|---|
| "Hva er Hjertnes kulturhus?" | No — homepage empty | Add editorial text to homepage |
| "Hvor er Hjertnes kulturhus?" | Partial | Postal code inconsistency |
| "Åpningstider Hjertnes kulturhus?" | Buried | Add dedicated hours section + schema |
| "Hva vises på kino i Sandefjord?" | Partial | No Event schema on film listings |
| "Kan man leie lokale på Hjertnes?" | Partial | Thin utleie content |
| "Har Hjertnes kino barnebursdag?" | Yes | Good FAQ content — add FAQ schema |

---

## 7. Images

**Score: 62 / 100**

### Missing OG Image — HIGH

No `og:image` on the homepage. All social shares render with no image thumbnail. Event pages do have images (from the Ambio ticketing CDN). Set a branded 1200×630px image in Yoast SEO social settings.

### Alt Text Coverage — PASS (mostly)

Sampled pages show good alt text coverage:
- Om Hjertnes: 7/7 images have non-empty alt text
- Kontakt: 2/2 images
- Harmonie arena: 4/4 images

One confirmed empty alt issue: the eBillett screenshot on the FAQ page has a debugging overlay suggesting an issue (though the alt attribute itself appears descriptive — investigate and remove the overlay).

### Hero Images via data-source — MEDIUM

Hero/slider images are loaded via `data-source` JavaScript attributes rather than standard `<img src>` elements. These images are not visible to crawlers without JavaScript execution and cannot benefit from `<link rel="preload">` optimization. No direct fix (controlled by Ambio ticketing platform), but verify Google renders them correctly via Google's URL Inspection tool in Search Console.

### SVG Logo No Alt Text — HIGH

The inline SVG logo has no `role="img"`, `<title>` element, or `aria-label`. Screen readers either skip it or read garbled path data.

**Fix:**
```html
<a href="/" aria-label="Hjertnes Kulturhus — gå til forsiden">
  <svg aria-hidden="true" focusable="false">...</svg>
</a>
```

### External CDN Images — INFO

Event images served from `storage.googleapis.com/pim-ambio.appspot.com`. No control over these image formats/sizes — managed by the Ambio ticketing platform.

---

## 8. Local SEO

**Score: 34 / 100**

### NAP Audit

| Source | Street | Postal Code | Phone |
|---|---|---|---|
| Homepage footer | Sandefjordsveien 3 | **3202** | 33 41 67 60 |
| Contact page (visiting) | Sandefjordsveien 3 | **3208** ❌ | 33 41 67 60 |
| About page | Sandefjordsveien 3 | 3202 | — |
| Any schema | — | — | — |

**CRITICAL INCONSISTENCY: Contact page postal code is 3208; all others are 3202. The correct postal code for Sandefjordsveien is 3202. Fix the contact page immediately.**

### Google Business Profile — Unknown

No GBP embed, no place ID reference, no review widget, no Maps iframe on any page. GBP status cannot be confirmed from the website alone. If unclaimed or inconsistently configured, this is a critical gap for local pack rankings.

### Local Schema — Missing Entirely — CRITICAL

No `LocalBusiness`, `PerformingArtsTheater`, or any local business schema. No `address`, `telephone`, `openingHours`, or `geo` coordinates in any JSON-LD anywhere on the site.

### No Reviews Surfaced — HIGH

No Google review count, star rating, or `aggregateRating` schema displayed anywhere. For a venue open since 1975, review volume should be significant. Add a review widget or at minimum `aggregateRating` schema.

### Local Keyword Targeting — HIGH

Zero pages have "Sandefjord" in their title tag. Local SEO fundamentally requires city+service keyword combinations in titles and H1s.

### Positive Signals
- Physical address in footer on all pages (good)
- Facebook + Instagram linked from footer
- Long establishment history (1975)
- Multiple venue sub-pages exist (individual pages for Sal 1, Sal 2, Sal 3, Harmonie arena, etc.)
- Municipality ownership signals authority

---

## 9. Sitemap Analysis

**Total URLs in all sitemaps: 1,454**

| Sitemap | Post Type | URL Count | Issues |
|---|---|---|---|
| page-sitemap.xml | Static pages | 30 | Legal pages (minor) |
| event-sitemap.xml | Events | 1,089 | None critical |
| playlist-sitemap.xml | Info-screen playlists | 6 | HIGH: Should be noindex + excluded |
| event_promoter-sitemap.xml | Organiser archives | 197 | HIGH: Invalid lastmod, thin content |
| event_genre-sitemap.xml | Genre archives | 31 | HIGH: Empty archives, invalid lastmod |
| event_category-sitemap.xml | Category archives | 12 | HIGH: Some empty archives |
| event_hall-sitemap.xml | Venue archives | 87 | HIGH: Duplicate slugs, invalid lastmod |
| event_type-sitemap.xml | Event type | 2 | Pass |

### Key Sitemap Issues

**Internal playlist pages in sitemap (HIGH):** 6 URLs including `testliste` and `tom-tester` are internal display-screen tools with no SEO value. Add `noindex,nofollow` to the `ambio-info-screen` template and remove from sitemap.

**Invalid lastmod dates (HIGH):** ~10+ entries with `lastmod: -0001-11-30` across 3 sitemaps. Fix WordPress date fields for custom post types.

**Empty taxonomy archives (HIGH):** Multiple genre/category archives return "ingen treff" but are indexed and in sitemap. Implement conditional `noindex` when archive has 0 events.

**Duplicate venue slugs (MEDIUM):** `harmonie-arena` and `harmonie-arena-kom`, `harmonie-arena-back` and `harmonie-arena-backstage` — truncated slug artifacts. Add canonicals or merge and redirect.

---

## Full Issue List by Severity

### CRITICAL (fix immediately)

| # | Issue | Category |
|---|---|---|
| C1 | All 6 security headers missing | Technical |
| C2 | xmlrpc.php exposed (HTTP 200) | Technical |
| C3 | www redirect chain passes through HTTP (3 hops) | Technical |
| C4 | 895+ event pages have zero Event schema | Schema |
| C5 | Invalid datePublished (-0001) in all event page schema | Schema |
| C6 | Homepage contains zero editorial text | Content |
| C7 | /kino/ has zero editorial text + no meta description | Content |
| C8 | No FAQPage schema on FAQ page | Schema |
| C9 | No llms.txt — AI systems have no guided entry point | GEO |
| C10 | Postal code inconsistency: 3208 vs 3202 on contact page | Local |
| C11 | No LocalBusiness/PerformingArtsTheater schema | Schema/Local |
| C12 | user-scalable=no violates WCAG 2.1 + Norwegian accessibility law | Technical/Accessibility |
| C13 | No "Sandefjord" in any page title (zero local geo-targeting) | On-Page |

### HIGH (fix within 1 week)

| # | Issue | Category |
|---|---|---|
| H1 | 263 thin taxonomy archive pages indexed (many empty) | Technical |
| H2 | No meta descriptions on event pages or most service pages | On-Page |
| H3 | Playlist pages in sitemap with no noindex | Sitemap |
| H4 | OG image missing on homepage + twitter:image absent | On-Page |
| H5 | Organization schema has no address, telephone, or sameAs | Schema |
| H6 | About page only 90 words — too thin for AI entity recognition | Content/GEO |
| H7 | SVG logo has no aria-label or accessible text | Visual/Accessibility |
| H8 | Header amber background likely fails contrast (WCAG AA) | Visual/Accessibility |
| H9 | Phone numbers are plain text, not tel: links | On-Page/Local |
| H10 | No Google Maps embed on contact page | Local |
| H11 | Invalid lastmod dates (-0001) in multiple sitemaps | Sitemap |
| H12 | Empty taxonomy archive pages indexed and in sitemap | Sitemap |
| H13 | /utleie/ thin content (~280 words, no capacity data) | Content |
| H14 | FAQ heading hierarchy broken (H1 → H3 with no H2) | Content |
| H15 | Breadcrumbs suppressed on service pages | On-Page |

### MEDIUM (fix within 1 month)

| # | Issue | Category |
|---|---|---|
| M1 | No H1 on homepage | On-Page |
| M2 | og:type "article" on all permanent service pages | On-Page |
| M3 | Render-blocking jQuery + theme JS (no defer) | Performance |
| M4 | No resource hints (preconnect, preload) | Performance |
| M5 | No AI crawler policy in robots.txt | Technical |
| M6 | No IndexNow implementation | Technical |
| M7 | Duplicate venue slug entries in event_hall sitemap | Sitemap |
| M8 | Hero images loaded via data-source JS attr (not preloadable) | Performance |
| M9 | No opening hours on homepage or contact page | Local/GEO |
| M10 | No Wikipedia article for the venue | GEO |
| M11 | /kinokortet/ meta description 40 chars (critically short) | Content |
| M12 | FAQ accordion answers may be weighted lower (JS toggle) | Content |
| M13 | No YouTube channel linked | GEO |
| M14 | No Bing Places / Apple Business Connect claimed | Local |
| M15 | Unsubstantiated sustainability/tax claims on /kinokortet/ | Content/E-E-A-T |
| M16 | Place schema missing on individual venue pages | Schema |
| M17 | CTA buttons likely below fold on mobile (no verified screenshot) | Visual |

### LOW (backlog)

| # | Issue | Category |
|---|---|---|
| L1 | No IndexNow key file | Technical |
| L2 | Pingback link in <head> advertises xmlrpc.php | Technical |
| L3 | Crawl-delay: 10 placed outside User-agent block (malformed) | Technical |
| L4 | WebSite schema has empty description field | Schema |
| L5 | Cookie/GDPR pages in sitemap (minor crawl budget) | Sitemap |
| L6 | og:type "article" on service pages | On-Page |
| L7 | Archive page titles include "Arkiver" suffix | On-Page |
| L8 | No "last updated" date visible on editorial pages | Content |
| L9 | WP REST API fully exposed | Technical |
| L10 | `http://gmpg.org/xfn/11` link (non-HTTPS reference) | Technical |
| L11 | No author attribution on any content | Content/E-E-A-T |
| L12 | Favicon setup complete — no action needed | — |

---

## Appendix: Positive Signals

These are working correctly and should be preserved:

- ✅ HTTPS enforced via Cloudflare (valid certificate)
- ✅ HTTP → HTTPS redirects working
- ✅ Sitemap index referenced in robots.txt
- ✅ Language attribute correct: `lang="nb-NO"` on all pages
- ✅ GTM installed (GTM-KTGD43NX)
- ✅ Canonical tags present on all pages (self-referencing)
- ✅ Yoast SEO BreadcrumbList schema on subpages
- ✅ Excellent server response time (TTFB ~40ms via Cloudflare)
- ✅ HTTP/2 enabled
- ✅ Gzip/Brotli compression active
- ✅ Favicon setup complete (32×32, 192×192, 180×180 apple-touch-icon)
- ✅ Skip link present for keyboard navigation
- ✅ OG tags present on most pages (except og:image)
- ✅ Event pages have robots: index, follow
- ✅ All static pages return HTTP 200
- ✅ Facebook and Instagram linked from footer
- ✅ Complianz GDPR Premium installed (cookie consent)
- ✅ Image alt text present on most sampled pages
- ✅ FAQ content is detailed, accurate, and citable
- ✅ Individual venue sub-pages exist for each rental space
