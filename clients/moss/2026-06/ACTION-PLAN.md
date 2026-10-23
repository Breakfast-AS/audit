# Action Plan — Moss Kulturhus SEO
**URL:** https://www.mosskulturhus.no/
**Generated:** 2026-06-03
**Overall Health Score:** 30/100

---

## CRITICAL — Fix Immediately

### C1. Fix duplicate brand name in all 164 page titles
**Category:** Technical / On-Page | **Effort:** 30 min | **Score impact:** High

All page titles currently end with "- Moss kulturhus - Moss kulturhus". Fix in:
**WordPress admin → Yoast SEO → Search Appearance → General → Title separator**

Change the title template from `%%title%% - %%sitename%% - %%sitename%%` to `%%title%% - %%sitename%%`

For the homepage specifically, set a custom title in Yoast:
> `Moss kulturhus - Kulturhuset midt i byen`

For venue archive pages, fix the "Arkiver" label:
**Yoast → Search Appearance → Content Types → Venues → Archive Title**

---

### C2. Add H1 to the homepage
**Category:** On-Page | **Effort:** 15 min | **Score impact:** High

The homepage has no H1 tag. Add in the WordPress page editor or theme template:

> `Moss Kulturhus — konsert- og kulturarena i Moss, Østfold`

---

### C3. Implement Event schema on all 59 event pages
**Category:** Schema | **Effort:** 4–8h (dev) | **Score impact:** Critical

First check: does The Events Calendar plugin (which powers `/event/` post type) have built-in schema? Check under **Events → Settings → General → Schema**.

If not available via plugin, add JSON-LD per event page (minimum viable):

```json
{
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "%%post_title%%",
  "startDate": "%%event_start_date%%",
  "eventStatus": "https://schema.org/EventScheduled",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "location": {
    "@type": "Place",
    "name": "%%venue_name%%",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Moss",
      "addressRegion": "Østfold",
      "addressCountry": "NO"
    }
  },
  "organizer": {
    "@type": "Organization",
    "name": "Moss Kulturhus",
    "url": "https://www.mosskulturhus.no"
  },
  "offers": {
    "@type": "Offer",
    "url": "%%ticket_url%%",
    "availability": "https://schema.org/InStock"
  }
}
```

See `schema-audit.md` for complete implementation with WordPress/Yoast integration code.

---

### C4. Add Organization + PerformingArtsTheater schema to homepage
**Category:** Schema / Local | **Effort:** 2h (dev) | **Score impact:** High

Add to `<head>` of all pages via `functions.php` or a custom Yoast filter:

```json
{
  "@context": "https://schema.org",
  "@type": ["Organization", "PerformingArtsTheater"],
  "name": "Moss Kulturhus",
  "url": "https://www.mosskulturhus.no",
  "logo": "https://www.mosskulturhus.no/[logo-path].png",
  "description": "Moss Kulturhus er en kulturarena i Moss, Østfold, bestående av Parkteatret og Samfunnshuset. Vi arrangerer konserter, teater, komedie og festivaler.",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[FILL IN]",
    "addressLocality": "Moss",
    "postalCode": "[FILL IN]",
    "addressRegion": "Østfold",
    "addressCountry": "NO"
  },
  "telephone": "404 09 924",
  "sameAs": [
    "https://www.facebook.com/mosskulturhus"
  ]
}
```

---

### C5. Enable HTTPS security headers via Cloudflare
**Category:** Technical / Security | **Effort:** 30 min | **Score impact:** Medium

In Cloudflare dashboard → **Security → Settings** or **Rules → Transform Rules → Modify Response Headers**:

| Header | Value |
|---|---|
| `Strict-Transport-Security` | `max-age=31536000; includeSubDomains` |
| `X-Content-Type-Options` | `nosniff` |
| `X-Frame-Options` | `SAMEORIGIN` |
| `Referrer-Policy` | `strict-origin-when-cross-origin` |
| `Permissions-Policy` | `camera=(), microphone=(), geolocation=()` |

---

## HIGH — Fix Within 1 Week

### H1. Fix 95% missing image alt text
**Category:** Images / Accessibility | **Effort:** 4–8h | **Score impact:** High

~285 images across the site are missing alt text. Priority pages:
1. Homepage event thumbnails: `[Artistnavn] – Moss Kulturhus`
2. /program/ event thumbnails: same pattern
3. Venue photos: `[Romnavn] i Moss Kulturhus, [kapasitet] sitteplasser`

Hero separator images (decorative): keep `alt=""` (empty, intentional).

In WordPress Media Library, alt text can be bulk-updated. For event thumbnails, configure the Events Calendar plugin to auto-populate alt text from event title.

---

### H2. Enable page caching
**Category:** Performance | **Effort:** 1h | **Score impact:** High

Currently **X-Cache-Enabled: False** and **cf-cache-status: DYNAMIC** — the site serves uncached HTML on every request.

1. **WP Engine:** Dashboard → Performance → Caching → Enable
2. **Cloudflare:** Create a Cache Rule for `hostname: www.mosskulturhus.no` and `URI Path: /*` → Cache Eligibility: Eligible for cache (exclude `/wp-admin/*`, `/wp-login.php`)

Expected improvement: TTFB reduction from ~600ms to ~80ms.

---

### H3. Add meta descriptions to all event pages
**Category:** On-Page | **Effort:** 2h (template config) | **Score impact:** High

In Yoast → Search Appearance → Content Types → Events → Meta description:

```
%%excerpt%% Kjøp billetter til Moss Kulturhus.
```

For individual event pages, add specific descriptions. Template:
> `[Artistnavn] opptrer på Moss Kulturhus [dato]. [1-setnings beskrivelse av showet]. Kjøp billetter her.`

---

### H4. Set tag and organizer archive pages to noindex
**Category:** Technical / Indexability | **Effort:** 30 min | **Score impact:** Medium

In Yoast SEO → Search Appearance → Taxonomies:
- **Post Tags:** Toggle "Show in search results" → OFF
- **Organizers:** Toggle "Show in search results" → OFF
- **Uncategorized category:** Add `noindex` via Yoast category settings

This removes 38 thin pages from Google's index and consolidates crawl budget.

---

### H5. Claim/optimize Google Business Profile
**Category:** Local SEO | **Effort:** 2–4h | **Score impact:** High (local pack)

1. Search Google for "Moss Kulturhus" and click "Claim this business" (or create new listing)
2. Primary category: **Performing arts theater**
3. Secondary categories: Concert hall, Event venue
4. Ensure NAP matches exactly what will be added to site footer
5. Add all venue photos, hours (by venue), description, and services
6. Enable messaging and Q&A features
7. Consider: one umbrella GBP listing with Parkteatret and Samfunnshuset as departments

---

### H6. Add NAP block to site footer
**Category:** Local SEO | **Effort:** 1h (dev) | **Score impact:** High

Add crawlable plain text (not image) to footer:

```html
<address>
  <strong>Moss Kulturhus</strong><br>
  [Gateadresse], [Postnummer] Moss<br>
  Telefon: <a href="tel:+4740409924">404 09 924</a><br>
  E-post: [kontaktepost]
</address>
```

This must exactly match the GBP listing for citation consistency.

---

## MEDIUM — Fix Within 1 Month

### M1. Rebuild venue pages as location pages
**Category:** Content / Local | **Effort:** 4–6h per venue | **Score impact:** High (local)

Both `/venue/parkteatret/` and `/venue/samfunnshuset/` currently have ~130 words and no H1/H2.

Each page needs:
- Custom H1: "Parkteatret — konsertsal i Moss sentrum"
- 400+ words of unique venue description
- Capacity, facilities, accessibility info
- Opening hours (structured with schema)
- Google Maps embed tied to GBP place_id
- Phone and address block
- Booking/inquiry CTA
- Link to upcoming events at this venue
- `EventVenue` + `LocalBusiness` schema with geo coordinates

---

### M2. Rewrite /om-kulturhuset/ with E-E-A-T signals + FAQ
**Category:** Content / AI | **Effort:** 4h | **Score impact:** High

Current page: 273 words, no H2, no FAQ, no staff info.

Expand to:
- 600+ words with organization history (founding year, renovations 2018–2019)
- Named leadership/artistic director
- Annual statistics (visitor numbers, events per year)
- FAQ section with FAQPage schema (6 questions — see geo-audit.md for Norwegian copy examples)
- Press/media contact info

---

### M3. Fix sitemap lastmod accuracy
**Category:** Technical | **Effort:** 2h (plugin config or custom code) | **Score impact:** Medium

Options:
1. Yoast premium has better lastmod management — configure in Yoast settings
2. For the program/event sitemaps: ensure event modification dates are updated when event details change (not just when events are published today)
3. Resolve the homepage lastmod (2024) by saving the homepage post in WordPress

---

### M4. Resolve duplicate/near-duplicate pages
**Category:** Technical | **Effort:** 2–4h | **Score impact:** Medium

| Issue | Resolution |
|---|---|
| `/event/riksteateret-ubesvart-anrop/` vs `/event/riksteatret-ubesvart-anrop/` | 301 redirect one to the other + fix canonical |
| `/parkteatret/` vs `/venue/parkteatret/` | Audit both; 301 redirect the thinner one or canonicalize |
| `/kryssover-jazzfest-moss/` vs `/kryssover-jazzfest-moss-2026/` | Make the year-specific one the canonical; 301 the evergreen URL to it or vice-versa |
| `/category/festival/` vs `/category/festivaler/` | Merge categories; 301 one to the other |
| `/category/julekonsert/` vs `/category/julekonserter/` | Same — merge and redirect |
| `/ledig-stilling/` vs `/ledige-stillinger/` | Audit both; redirect or merge |

---

### M5. Create /llms.txt
**Category:** AI / GEO | **Effort:** 2h | **Score impact:** Medium (growing)

Create at `https://www.mosskulturhus.no/llms.txt` — see `geo-audit.md` for complete template. This signals deliberate AI-readiness and provides a curated entity definition for Perplexity, ChatGPT, and future LLM crawlers.

---

### M6. Add BreadcrumbList schema sitewide
**Category:** Schema | **Effort:** 1h | **Score impact:** Medium

Yoast already generates BreadcrumbList schema in some configurations. Verify it's enabled:
**Yoast SEO → Search Appearance → General → Breadcrumbs → Enable**

Also ensure breadcrumbs are enabled in WordPress theme template files.

---

### M7. Submit citations to Norwegian directories
**Category:** Local SEO | **Effort:** 3–4h | **Score impact:** Medium

Submit NAP (must exactly match GBP listing) to:
1. **1881.no** — Norway's primary business directory
2. **gulesider.no** — Schibsted-owned, major Norwegian citation
3. **visitostfold.com** — Regional tourism authority
4. **kulturnett.no** — National arts council database
5. **Moss kommune kulturkalender** — Municipal cultural calendar
6. **finn.no** — Norway's dominant classifieds (activity/event listings)

---

### M8. Defer non-critical JavaScript
**Category:** Performance | **Effort:** 2h | **Score impact:** Medium

10 external scripts load on the homepage. Audit each:
- Google Analytics / Tag Manager: use `async` attribute
- Facebook Pixel: defer until after user interaction
- Booking/ticketing widgets: load on demand
- Chat widgets: defer 3+ seconds

Use Query Monitor plugin to identify render-blocking scripts.

---

## LOW — Backlog

### L1. Create Wikipedia/Wikidata entry
**Category:** AI / Authority | **Effort:** 8–12h | **Score impact:** Long-term high

Create a Norwegian Wikipedia article for Moss Kulturhus. Meets notability criteria as a municipal cultural institution. This creates the `sameAs` anchor that AI models use as ground truth. Add `sameAs` link to Organization schema once live.

---

### L2. Launch YouTube channel
**Category:** AI / Brand | **Effort:** Ongoing | **Score impact:** Medium–High (3–6 month horizon)

YouTube presence correlates at ~0.737 with AI citation frequency. Start with:
- Venue walkthrough video
- Season preview / "coming up at Moss Kulturhus" video
- Short artist interview clips
- Best-of clips from past events (with artist permission)

---

### L3. Implement WebP/AVIF image serving
**Category:** Performance | **Effort:** 2h | **Score impact:** Medium

WP Engine supports WebP via their CDN. Enable in WP Engine dashboard → CDN → Image Optimization. This can reduce image weight by 25–40%, directly improving LCP on event listing pages.

---

### L4. Add artist/event review integration
**Category:** Content / E-E-A-T | **Effort:** 4–6h | **Score impact:** Medium

Add post-event review emails via existing newsletter infrastructure. Display aggregate ratings with `aggregateRating` schema on venue pages and selected event pages.

---

### L5. Fix /category/concert/ slug
**Category:** On-Page | **Effort:** 30 min | **Score impact:** Low

The English slug `/category/concert/` on a Norwegian site is inconsistent. Rename to `/category/konsert/` with 301 redirect from old slug.

---

### L6. Reduce Crawl-delay in robots.txt
**Category:** Technical | **Effort:** 5 min | **Score impact:** Low

Change `Crawl-delay: 10` to `Crawl-delay: 1` or remove entirely. Google ignores it; other crawlers (Bing, DuckDuckGo) are currently throttled unnecessarily.

---

## Estimated Score After Full Implementation

| Category | Current | After Critical+High | After All |
|---|---|---|---|
| Technical SEO | 47 | 72 | 82 |
| Content Quality | 28 | 42 | 68 |
| On-Page SEO | 22 | 65 | 78 |
| Schema | 8 | 62 | 80 |
| Performance | 38 | 68 | 75 |
| AI Search Readiness | 28 | 55 | 74 |
| Images | 8 | 72 | 80 |
| **Overall** | **30** | **62** | **77** |

---

## Implementation Roadmap

| Week | Focus | Key Actions |
|---|---|---|
| 1 | Quick wins | C1 (title fix), C2 (H1), C5 (security headers), H2 (caching), H4 (noindex tags) |
| 2 | Schema sprint | C3 (Event schema), C4 (Organization schema), M6 (BreadcrumbList) |
| 3 | Content + Local | H1 (alt text), H5 (GBP), H6 (NAP footer), H3 (meta descriptions) |
| 4 | On-page depth | M1 (venue pages), M2 (about page + FAQ), M3 (sitemap lastmod) |
| 5–6 | Cleanup | M4 (duplicate URLs), M5 (llms.txt), M7 (citations), M8 (JS defer) |
| 7–12 | Authority | L1 (Wikipedia), L2 (YouTube), L3 (WebP), L4 (reviews) |
