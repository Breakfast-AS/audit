# Technical SEO Audit — Lillestrøm Kultursenter

**Audit date:** 2026-05-29
**URL:** https://www.lillestrom-kultursenter.no/
**Platform:** WordPress + Yoast SEO | Hosting: WP Engine + Cloudflare CDN
**Language:** nb-NO

---

## Overall Technical Score: 52 / 100

| Category | Status | Score |
|---|---|---|
| Crawlability | PARTIAL PASS | 65/100 |
| Indexability | FAIL | 40/100 |
| Security | FAIL | 35/100 |
| URL Structure | PASS | 80/100 |
| Mobile | PASS | 75/100 |
| Core Web Vitals (signals) | PARTIAL PASS | 60/100 |
| Structured Data | FAIL | 30/100 |
| JavaScript Rendering | PASS | 85/100 |
| IndexNow Protocol | FAIL | 0/100 |

---

## CRITICAL Issues

### C1 — robots.txt has conflicting User-agent: * blocks

A bare `Crawl-delay: 10` appears before any `User-agent` declaration (invalid per RFC 9309). The file then has two separate `User-agent: *` blocks that conflict:

- Block 1: Disallows `/wp-content/uploads/wpo/wpo-plugins-tables-list.json`
- Block 2 (Yoast): Empty `Disallow:` (allows everything)

**Fix:** Merge into a single block:

```
User-agent: *
Crawl-delay: 10
Disallow: /wp-content/uploads/wpo/wpo-plugins-tables-list.json

Sitemap: https://www.lillestrom-kultursenter.no/sitemap_index.xml
```

Edit via Yoast SEO > Tools > File editor, then disable Yoast's robots.txt management to prevent regeneration of the duplicate block.

---

### C2 — Internal board documents indexed and crawlable

Five `/internt/` pages return HTTP 200, carry `meta name="robots" content="index, follow"`, and appear in the page sitemap:

- `/internt/styredokumenter/`
- `/internt/handlingsplan/`
- `/internt/arsberetninger/`
- `/internt/div-planverk/`
- `/internt/beskyttet-underside/` — name implies password-protection that is NOT enforced; content loads fully for all visitors

**Fix:** Set each to `noindex` in Yoast SEO > Advanced tab. If pages must remain accessible only to logged-in users, enforce that at the server or WordPress plugin level.

---

### C3 — No HTTP security headers present

None of these are set:

| Header | Status |
|---|---|
| Strict-Transport-Security (HSTS) | MISSING |
| X-Frame-Options | MISSING |
| X-Content-Type-Options | MISSING |
| Content-Security-Policy | MISSING |
| Permissions-Policy | MISSING |
| Referrer-Policy | MISSING |

Additionally `x-powered-by: WP Engine` is exposed, confirming the full hosting stack.

**Fix via Cloudflare Transform Rules > Modify Response Headers:**

```
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(), geolocation=()
```

Request WP Engine support to suppress `x-powered-by`, or remove via Cloudflare transform rule.

---

### C4 — WordPress REST API exposes staff usernames

`/wp-json/wp/v2/users` returns a public JSON list of staff accounts including real names and login slugs. Every page `<head>` also leaks page IDs via `<link rel="alternate" href="/wp-json/wp/v2/pages/1069">`.

**Fix — add to child theme `functions.php`:**

```php
add_filter( 'rest_endpoints', function( $endpoints ) {
    unset( $endpoints['/wp/v2/users'] );
    unset( $endpoints['/wp/v2/users/(?P<id>[\d]+)'] );
    return $endpoints;
} );

remove_action( 'wp_head', 'rest_output_link_wp_head' );
remove_action( 'wp_head', 'wp_oembed_add_discovery_links' );
remove_action( 'wp_head', 'rsd_link' );
```

---

## HIGH Issues

### H1 — Meta descriptions missing on all pages except homepage

Confirmed missing on: `/program/`, `/utleie/`, all 338 event pages, all 12 hall pages, all core static pages.

**Fix in Yoast SEO > Search Appearance, set templates per post type:**
- Events: `%%title%% — %%excerpt%% Billetter og informasjon på Lillestrøm Kultursenter.`
- Pages: `%%title%% — %%excerpt%%`

Write individual descriptions manually for highest-traffic events and core pages.

---

### H2 — Event schema location address empty on all 338 event pages

`streetAddress`, `addressLocality`, and `postalCode` are all empty strings in the Event schema. Google will not display Event rich results without a valid location. Additionally, some events have `datePublished: "-0001-11-30T00:00:00+00:00"` — an invalid null timestamp that can suppress rich results.

**Fix required fields for Google Event rich results:**
- `name`, `startDate` (ISO 8601), `location.name`, `location.address` (full), `eventStatus`, `eventAttendanceMode`
- Fix null datePublished by ensuring `post_date` is populated at PIM import time

---

### H3 — No Organization or LocalBusiness schema on the site

Homepage schema graph contains only `WebPage`, `BreadcrumbList`, and `WebSite`. No `Organization` or `PerformingArtsTheater` entity. Google has no structured signal for venue name, address, phone, or coordinates.

**Fix:** Add to Yoast SEO > Search Appearance > Knowledge Graph, or inject via `wp_head`:

```json
{
  "@context": "https://schema.org",
  "@type": ["Organization", "PerformingArtsTheater"],
  "@id": "https://www.lillestrom-kultursenter.no/#organization",
  "name": "Lillestrøm Kultursenter",
  "url": "https://www.lillestrom-kultursenter.no/",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Kirkegata 11",
    "addressLocality": "Lillestrøm",
    "postalCode": "2000",
    "addressCountry": "NO"
  },
  "telephone": "+4764845550"
}
```

---

### H4 — Test page and outdated COVID page publicly indexed

- `/nyhetsbrev-test/` — live at HTTP 200, no content value
- `/for-og-etter-test/` — last modified November 2025, still in use as test
- `/smittevern/` — last modified 2022-02-12, references lifted COVID restrictions

**Fix:** Set all three to `noindex` in Yoast. Create 301 redirect from `/smittevern/` to `/praktisk-informasjon/`.

---

### H5 — Low-value taxonomy sitemaps waste crawl budget

Disable these in Yoast SEO > Search Appearance > Taxonomies and Archives:
- event_promoter (127 URLs, many with invalid dates)
- author archives (exposes usernames)
- event_venue, event_type, sponsor, sponsor_category, category (Uncategorized), post_tag

---

## MEDIUM Issues

### M1 — LCP candidate images missing fetchpriority and explicit dimensions

Above-the-fold images have no `fetchpriority="high"`, no `loading="eager"`, and no explicit `width`/`height` attributes. Event card images are served from third-party Google Cloud Storage, adding DNS resolution overhead.

**Fix:**
- Add `fetchpriority="high"` and `loading="eager"` to first visible event image.
- Add explicit `width` and `height` to all `<img>` tags.
- Consider proxying event images through Cloudflare Image Optimization.

---

### M2 — user-scalable=no in viewport meta tag

`<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">`

This prevents zoom on mobile — a WCAG 1.4.4 Level AA violation and a Google mobile usability flag.

**Fix:** Change to: `<meta name="viewport" content="width=device-width, initial-scale=1">`

---

### M3 — WebSite schema has empty description

All pages have `"description": ""` in the `WebSite` schema node.

**Fix:** Go to WordPress > Settings > General and add a meaningful tagline, e.g. "Konsertscene og kulturhus i Lillestrøm". Yoast automatically uses this value.

---

### M4 — Cache TTL is only 10 minutes

`Cache-Control: max-age=600, must-revalidate` applied site-wide.

**Fix:** Use Cloudflare Cache Rules:
- Static pages (homepage, /utleie/, /om-oss/): `max-age=86400`
- Event pages: `max-age=3600`

---

### M5 — Moment.js loaded twice

Two Moment.js bundles enqueued: `moment.min.js` (~17KB) and `moment-with-locales.min.js` (~72KB). The second is a complete superset.

**Fix:** Dequeue the redundant core script via `wp_dequeue_script()` in `functions.php`.

---

### M6 — No IndexNow implementation

No IndexNow key file at root. No `IndexNow-Key` response header.

**Fix:** Yoast SEO > Integrations > enable IndexNow. Yoast automatically generates the verification key and pings the endpoint on every publish/update.

---

## LOW Issues

### L1 — Numeric PIM IDs in event URL slugs
Event URLs use `/program/15231-event-name/`. Not harmful but reduces URL cleanliness. Changing existing URLs requires 301 redirects for all 338 events — not recommended unless a full migration is planned.

### L2 — RSS discovery links on every page
Add to `functions.php` if desired:
```php
remove_action( 'wp_head', 'feed_links', 2 );
remove_action( 'wp_head', 'feed_links_extra', 3 );
```

### L3 — No hreflang (no action needed)
`lang="nb-NO"` correctly set on `<html>`. No multilingual version exists. Add hreflang only if an English version is created.

---

## What Is Working Well

- HTTP to HTTPS redirect: 301 configured correctly
- non-www to www redirect: working
- xmlrpc.php: blocked at server level (returns 405)
- Canonical tags: present and self-referencing on all checked pages
- HTML lang attribute: correctly set to `nb-NO`
- og:locale: correctly set to `nb_NO`
- Server response times: excellent at 80–120ms
- Page weights: 52–142KB
- Sitemap index: accessible, 14 child sitemaps
- Complianz GDPR premium: active
- H1 tags: present on event pages
- BreadcrumbList schema: present on all checked pages
- HTTPS fully deployed via Cloudflare

---

## Recommended Action Order

| Step | Action | Time Estimate |
|---|---|---|
| 1 | Fix robots.txt — merge into single User-agent block | 15 min |
| 2 | Noindex all /internt/ and /ansatt/ pages | 10 min |
| 3 | Add security headers via Cloudflare Transform Rules | 30 min |
| 4 | Disable REST API user enumeration + remove head disclosure links | 20 min |
| 5 | Add Organization/PerformingArtsTheater schema via Yoast Knowledge Graph | 20 min |
| 6 | Set meta description templates in Yoast Search Appearance | 20 min |
| 7 | Noindex /nyhetsbrev-test/, /for-og-etter-test/, /smittevern/ | 10 min |
| 8 | Disable low-value taxonomy sitemaps in Yoast | 15 min |
| 9 | Enable IndexNow in Yoast Integrations | 5 min |
| 10 | Remove user-scalable=no from viewport tag | 5 min |
| 11 | Fix Event schema address fields — developer work | Developer |
| 12 | Fix LCP image fetchpriority and dimensions | Developer |
| 13 | Resolve Moment.js double-load | Developer |
