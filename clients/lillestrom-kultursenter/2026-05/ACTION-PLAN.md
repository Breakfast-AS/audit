# SEO Action Plan — Lillestrøm Kultursenter
**Generated:** 2026-05-29 | **Overall score:** 46/100
**URL:** https://www.lillestrom-kultursenter.no/

---

## Priority Legend
- **CRITICAL** — Blocks indexing, causes penalties, or creates security/content exposure risks. Fix immediately.
- **HIGH** — Significantly impacts rankings, CTR, or rich results. Fix within 1 week.
- **MEDIUM** — Optimization opportunity. Fix within 1 month.
- **LOW** — Nice to have. Add to backlog.

---

## CRITICAL Actions (Fix today)

### C1 — Noindex all /internt/ and /ansatt/ pages
**Effort:** 10 min | **Tool:** Yoast SEO in WordPress admin | **No developer needed**

Set `noindex` via Yoast SEO > Edit each page > Advanced tab > "Allow search engines to show this page in search results" = No.

Pages to fix:
- /internt/styredokumenter/
- /internt/handlingsplan/
- /internt/arsberetninger/
- /internt/div-planverk/
- /internt/beskyttet-underside/ (also verify password protection is working)
- /ansatt/tilbud-fra-vare-samarbeidspartnere/
- /ansatt/handlingsplan/
- /ansatt/mal-og-strategi/

**Why:** Board documents, financial reports, and internal plans are publicly indexed. This is a governance failure and a direct E-E-A-T signal impairment. One "protected" page (`/internt/beskyttet-underside/`) shows full quarterly report content to all visitors.

---

### C2 — Noindex test pages
**Effort:** 5 min | **Tool:** Yoast SEO | **No developer needed**

Set noindex on:
- /nyhetsbrev-test/ (may be safe to delete entirely)
- /for-og-etter-test/ (still in active use as of November 2025 — ask team before deleting)

---

### C3 — Add H1 to homepage
**Effort:** 15 min | **Tool:** WordPress block editor | **No developer needed**

Add a visible H1 in the hero section above the first event listing:

> **Lillestrøm Kultursenter – konserter, teater og opplevelser i Lillestrøm**

The current tagline "Du kan bare begynne å glede deg!" should remain as a secondary text element (H2 or `<p>`), not as a substitute for a descriptive H1.

**Why:** The homepage has no H1 — the most important on-page ranking signal for the primary keyword cluster. Without it, the page cannot rank for "kultursenter Lillestrøm" or "konserter Lillestrøm" with any authority.

---

### C4 — Remove or redirect /smittevern/
**Effort:** 15 min | **Tool:** Yoast SEO + Yoast Redirects | **No developer needed**

Option A (recommended): Delete the page in WordPress and set a 301 redirect from `/smittevern/` to `/praktisk-informasjon/` via Yoast SEO Premium > Redirects.

Option B: Set `noindex` if the redirect is not possible immediately.

**Why:** A COVID pandemic page last modified February 2022 is still indexed in 2026. Stale health/safety content is a direct negative E-E-A-T signal per Google's Quality Rater Guidelines.

---

## HIGH Actions (Fix within 1 week)

### H1 — Add Organization + PerformingArtsTheater schema to homepage
**Effort:** 1–2 hours | **Tool:** WPCode plugin or functions.php | **Developer recommended**

Install the free WPCode plugin and add the following as a "Header & Footer" script block:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": ["Organization", "PerformingArtsTheater"],
  "@id": "https://www.lillestrom-kultursenter.no/#organization",
  "name": "Lillestrøm Kultursenter",
  "url": "https://www.lillestrom-kultursenter.no/",
  "description": "Lillestrøm Kultursenter er et kulturhus i hjertet av Lillestrøm med konserter, teater, musikaler, stand-up og konferanser.",
  "logo": {
    "@type": "ImageObject",
    "url": "https://www.lillestrom-kultursenter.no/wp-content/uploads/2025/10/Nettstedsikon-gronn-300x300.png"
  },
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Kirkegata 11",
    "addressLocality": "Lillestrøm",
    "postalCode": "2000",
    "addressCountry": "NO"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 59.9557,
    "longitude": 11.0518
  },
  "telephone": "+4764845550",
  "email": "post@lillestrom-kultursenter.no",
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
      "opens": "09:00",
      "closes": "20:00"
    },
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Saturday"],
      "opens": "11:00",
      "closes": "15:00"
    }
  ],
  "sameAs": [
    "https://no.wikipedia.org/wiki/Lillestr%C3%B8m_Kultursenter",
    "https://www.facebook.com/lillestromkultursenter",
    "https://www.instagram.com/lillestromkultursenter"
  ]
}
</script>
```

**Validate with:** https://search.google.com/test/rich-results

**Why:** Without this, Google has no structured entity data for the venue. This blocks Knowledge Panel eligibility, local pack entry, and AI entity recognition. The `sameAs` to Norwegian Wikipedia connects the schema entity to the existing knowledge graph node.

---

### H2 — Set Yoast meta description templates
**Effort:** 20 min | **Tool:** Yoast SEO Settings | **No developer needed**

Go to Yoast SEO > Search Appearance > Content Types and set description templates:

| Post type | Template |
|---|---|
| Events | `%%title%% – %%excerpt%% Kjøp billetter på Lillestrøm Kultursenter.` |
| Halls | `%%title%% – %%excerpt%% Lei lokaler på Lillestrøm Kultursenter, Kirkegata 11.` |
| Posts | `%%title%% – %%excerpt%%` |
| Pages | `%%title%% – %%excerpt%%` |

Then manually write descriptions for these 6 pages (event templates will cover the rest):
1. /program/ — "Se hele programmet på Lillestrøm Kultursenter – konserter, teater, musikaler, stand-up og familieforestillinger i Lillestrøm."
2. /utleie/ — "Lei sal eller lokale på Lillestrøm Kultursenter. Vi tilbyr 12 unike saler for konferanser, selskaper og events i hjertet av Lillestrøm."
3. /om-oss/ — "Lillestrøm Kultursenter er Lillestrøms ledende kulturhus. Les om vår historie, ansatte og visjon for kulturlivet i Lillestrøm og Akershus."
4. /kontakt-oss/ — "Kontakt Lillestrøm Kultursenter – Kirkegata 11, 2000 Lillestrøm. Tlf: 64 84 55 50. Åpent man–fre 09–20, lør 11–15."
5. /praktisk-informasjon/ — "Alt du trenger å vite om besøk til Lillestrøm Kultursenter: parkering, tilgjengelighet, garderobe, billettskranke og mer."
6. /gavekort/ — "Gi en uforglemmelig opplevelse! Gavekort til Lillestrøm Kultursenter gjelder på alle forestillinger og arrangementer."

---

### H3 — Fix robots.txt
**Effort:** 20 min | **Tool:** Yoast SEO > Tools > File Editor | **No developer needed**

1. Go to Yoast SEO > Tools > File Editor
2. Replace the entire robots.txt content with:

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
Disallow: /internt/
Disallow: /ansatt/
Disallow: /wp-admin/
Disallow: /wp-json/

Sitemap: https://www.lillestrom-kultursenter.no/sitemap_index.xml
```

3. Turn off Yoast's automatic robots.txt management to prevent it regenerating the duplicate block.

---

### H4 — Add security headers via Cloudflare
**Effort:** 30 min | **Tool:** Cloudflare Dashboard > Transform Rules | **No developer needed**

In Cloudflare: Rules > Transform Rules > Modify Response Headers > Create Rule: "Add SEO Security Headers" — apply to all requests.

Add these headers:
```
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(), geolocation=()
```

Also: add a rule to remove the `x-powered-by` response header.

---

### H5 — Disable low-value sitemaps and author archives
**Effort:** 15 min | **Tool:** Yoast SEO > Search Appearance | **No developer needed**

Go to Yoast SEO > Search Appearance > Taxonomies and set to "No" (noindex + remove from sitemap):
- Author archives (stops exposing WordPress login usernames)
- event_type
- event_venue
- event_promoter (review first — 127 URLs of thin promoter archive pages)
- sponsor
- sponsor_category

Go to Yoast SEO > Search Appearance > Archives and disable:
- Author archives

---

### H6 — Disable REST API user enumeration
**Effort:** 20 min | **Tool:** child theme functions.php or WPCode plugin | **Developer or WPCode**

Add via WPCode (Code Snippets > Add New > PHP snippet):

```php
// Block user enumeration via REST API
add_filter( 'rest_endpoints', function( $endpoints ) {
    unset( $endpoints['/wp/v2/users'] );
    unset( $endpoints['/wp/v2/users/(?P<id>[\d]+)'] );
    return $endpoints;
} );

// Remove WordPress head disclosure links
remove_action( 'wp_head', 'rest_output_link_wp_head' );
remove_action( 'wp_head', 'wp_oembed_add_discovery_links' );
remove_action( 'wp_head', 'rsd_link' );
```

---

### H7 — Enable IndexNow in Yoast
**Effort:** 5 min | **Tool:** Yoast SEO > Integrations | **No developer needed**

Go to Yoast SEO > Integrations > IndexNow > Toggle to enabled.

Yoast will automatically generate the verification key file and ping the IndexNow endpoint every time a page is published or updated. This ensures Bing, Yandex, and other participating search engines are notified instantly of all 338 event page updates.

---

## MEDIUM Actions (Fix within 1 month)

### M1 — Fix Event schema address fields
**Effort:** 2–4 hours | **Tool:** Ambio PIM integration or custom plugin | **Developer needed**

The PIM (Ambio) integration is outputting empty strings for `streetAddress`, `addressLocality`, and `postalCode` in all Event schema blocks. This prevents Google from displaying Event rich results.

Investigation steps:
1. Check the dx-calendar / Ambio plugin settings for a "venue address" mapping field
2. If the plugin supports a default venue, set Lillestrøm Kultursenter as the default venue with full address
3. If not, add a filter via `functions.php` to inject the address:

```php
add_filter('lks_event_schema', function($schema) {
    if (empty($schema['location']['address']['streetAddress'])) {
        $schema['location']['address']['streetAddress'] = 'Kirkegata 11';
        $schema['location']['address']['addressLocality'] = 'Lillestrøm';
        $schema['location']['address']['postalCode'] = '2000';
    }
    return $schema;
});
```

Also add `offers`, `organizer`, and `performer` fields — see full templates in `schema-seo.md`.

Fix invalid `datePublished: "-0001-11-30"` by setting explicit Published dates in WordPress for all affected events.

---

### M2 — Add deferred loading to all JavaScript
**Effort:** 2–4 hours | **Tool:** functions.php or WPCode | **Developer needed**

All 11 JavaScript files on the site are render-blocking (no `async` or `defer`). This is the primary driver of poor LCP and INP scores.

```php
add_filter('script_loader_tag', function($tag, $handle, $src) {
    // Do not defer jQuery core (required synchronously by theme)
    $no_defer = ['jquery'];
    if (in_array($handle, $no_defer)) return $tag;
    return str_replace(' src=', ' defer="defer" src=', $tag);
}, 10, 3);
```

Test carefully after applying — some plugins may break if jQuery loads asynchronously.

---

### M3 — Add lazy loading and image dimensions
**Effort:** 2–3 hours | **Tool:** theme templates | **Developer needed**

For all `<img>` tags in theme templates:
1. Add `loading="lazy"` to all below-fold images
2. Add `loading="eager" fetchpriority="high"` to the first hero/event image
3. Add explicit `width` and `height` attributes to all images to prevent CLS

WordPress built-in: verify `add_filter('wp_lazy_loading_enabled', '__return_true')` is not disabled.

---

### M4 — Rewrite title tags for all 36 static pages
**Effort:** 2–3 hours | **Tool:** Yoast SEO per-page editor | **No developer needed**

Priority pages and suggested titles:
| Page | Current title | Recommended title |
|---|---|---|
| Homepage | Lillestrøm Kultursenter - Du kan bare begynne å glede deg! | Lillestrøm Kultursenter – Konserter, teater og kultur i Lillestrøm |
| /program/ | Program - Lillestrøm Kultursenter | Konsertprogram og billetter – Lillestrøm Kultursenter |
| /utleie/ | Utleie - Lillestrøm Kultursenter | Lei saler og konferanselokaler i Lillestrøm – Lillestrøm Kultursenter |
| /utleie/vare-saler/ | Våre saler - Lillestrøm Kultursenter | 12 saler til leie i Lillestrøm – Kapasitet og priser |
| /kontakt-oss/ | Kontakt oss - Lillestrøm Kultursenter | Kontakt Lillestrøm Kultursenter – Kirkegata 11, 2000 Lillestrøm |
| /om-oss/ | Om oss - Lillestrøm Kultursenter | Om Lillestrøm Kultursenter – Historikk, eierskap og ansatte |
| /gavekort/ | Gavekort - Lillestrøm Kultursenter | Gavekort til Lillestrøm Kultursenter – Perfekt kulturgave |

---

### M5 — Create /llms.txt
**Effort:** 2 hours | **Tool:** WP Engine file manager or FTP | **No developer needed**

Upload a static text file to the domain root. Content template is in `geo-ai-seo.md` section 2.

This is the lowest-effort AI search optimization available and surfaces key entity facts (address, founding date, hall count, visitor figures) to all major LLMs.

---

### M6 — Rewrite /om-oss/ with entity-rich content
**Effort:** 4–8 hours | **Tool:** WordPress block editor | **No developer needed**

Current /om-oss/ is a stub showing only contact info. Rewrite to include:
- Lead paragraph (50–70 words): What the venue is, where it is, how long it has operated
- Founding story: April 17, 1991, Stiftelsen Lillestrøm Kulturforum
- Milestones: Original 1926 building, 2006 expansion, 2022 INTRO/EKKO addition
- Scale: 350,000+ annual visitors, 22+ halls (actual current count), 25 annual positions
- Programming: Types of events, genres, community role
- Certifications: Miljøfyrtårn
- Hosted organizations: Unge Viken Teater

Target: 600–800 words. Add "Sist oppdatert: [date]" at the bottom.

---

### M7 — Fix viewport user-scalable=no
**Effort:** 5 min | **Tool:** theme header.php | **Developer needed**

Change:
```html
<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
```
To:
```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

This fixes a WCAG 1.4.4 Level AA accessibility violation and a Google mobile usability warning.

---

### M8 — Add Google Maps embed to contact page
**Effort:** 30 min | **Tool:** WordPress block editor | **No developer needed**

Embed a Google Maps iframe showing Kirkegata 11, 2000 Lillestrøm on the /kontakt-oss/ page. This creates an on-page link between the website and the Google Business Profile.

---

### M9 — Write meta descriptions for 12 hall pages
**Effort:** 1 hour | **Tool:** Yoast SEO per-page editor | **No developer needed**

Each hall page needs a conversion-focused meta description with capacity and use-case:
- Pattern: `[Hall name] – [capacity] plasser. [Key feature]. Lei til [use case] på Lillestrøm Kultursenter i Lillestrøm.`
- Example: `Teatersalen – Plass til 600 gjester, profesjonell scene og lyd. Lei til konserter, teaterstykker, galas og konferanser. Lillestrøm Kultursenter.`

---

### M10 — Increase Cloudflare cache TTL
**Effort:** 30 min | **Tool:** Cloudflare Cache Rules | **No developer needed**

Create cache rules:
- `/om-oss/*`, `/utleie/*`, `/kontakt-oss/*`, `/om-oss/*`, `/hall/*` → `max-age=86400`
- `/program/[0-9]*` (event pages) → `max-age=3600`
- `/` (homepage) → `max-age=1800`

---

## LOW Actions (Backlog)

### L1 — Write 2 blog posts per month
Covering: artist spotlights, behind-the-scenes, local culture angles, staff profiles. Target: 50 total posts within 12 months. This builds E-E-A-T and creates topical authority.

### L2 — Create seasonal programme landing pages
Examples: `/program/host-2026/`, `/program/jul-2026/`, `/program/var-2027/`. These create predictable fresh-content cycles and rank for seasonal intent queries.

### L3 — Add structured author bios to /om-oss/ansatte/
Named staff with photos, roles, and 2–3 sentence professional backgrounds. Directly improves E-E-A-T expertise signals.

### L4 — Add FAQ schema to /praktisk-informasjon/ and /utleie/
Cover: parkering, tilgjengelighet, billettpriser, avbestillingsregler, cateringmuligheter. Benefits AI Overview eligibility for common venue queries.

### L5 — Create TripAdvisor listing
TripAdvisor returns 404 for the venue — it appears to be unlisted. A verified TripAdvisor listing is a major local citation source and review platform for entertainment venues.

### L6 — Dequeue Moment.js duplicate
Remove `moment.min.js` (core bundle) and keep only `moment-with-locales.min.js`. Saves ~17 KB per page load.

### L7 — Conditionally load dx-calendar.css
Only enqueue on /program/ and event pages, not on all pages site-wide.

### L8 — Verify and expand GBP (Google Business Profile)
Claim/verify the GBP listing if not already done. Set primary category to "Performing Arts Theater". Upload 20+ high-quality photos. Add all services. Ensure NAP matches the website exactly. Set up review response protocol.

### L9 — Submit Wikidata entity
If a Wikidata entity does not exist for Lillestrøm Kultursenter, create one. Add `sameAs` to the homepage Organization schema pointing to the Wikidata entity. This strengthens AI/LLM entity recognition.

### L10 — Add preconnect hint for event image CDN
```html
<link rel="preconnect" href="https://storage.googleapis.com" crossorigin>
```
Reduces DNS + TCP setup time for the first event image loaded from the Ambio PIM.

---

## Implementation Roadmap

### Week 1 — No developer required (~3 hours total)
- [ ] C1: Noindex /internt/ and /ansatt/ pages (10 min)
- [ ] C2: Noindex test pages (5 min)
- [ ] C3: Add H1 to homepage (15 min)
- [ ] C4: Remove /smittevern/ + 301 redirect (15 min)
- [ ] H2: Set Yoast meta description templates (20 min)
- [ ] H3: Fix robots.txt (20 min)
- [ ] H4: Add security headers via Cloudflare (30 min)
- [ ] H5: Disable low-value sitemaps (15 min)
- [ ] H7: Enable IndexNow (5 min)

### Week 2 — Light developer work (~4 hours)
- [ ] H1: Add Organization/PerformingArtsTheater schema via WPCode (2 hours)
- [ ] H6: Disable REST API user enumeration via WPCode (20 min)
- [ ] M5: Create /llms.txt (2 hours)
- [ ] M7: Fix viewport user-scalable=no (5 min)

### Week 3–4 — Developer sprints (~8 hours)
- [ ] M1: Fix Event schema address fields + add offers/organizer
- [ ] M2: Add defer to JavaScript files
- [ ] M3: Add lazy loading and image dimensions

### Month 2 — Content & optimization (~12 hours)
- [ ] M4: Rewrite title tags for 36 static pages (3 hours)
- [ ] M6: Rewrite /om-oss/ with entity-rich content (4–8 hours)
- [ ] M8: Add Google Maps embed to contact page (30 min)
- [ ] M9: Write meta descriptions for 12 hall pages (1 hour)
- [ ] M10: Increase Cloudflare cache TTL (30 min)

### Month 3+ — Ongoing
- [ ] L1–L10: Backlog items in priority order

---

## Expected Score Improvements

| Action group | Current | Expected |
|---|---|---|
| Noindex internal pages + remove outdated content | 46/100 | +3 pts |
| Add H1 + meta descriptions + title rewrites | +8 pts | +8 pts |
| Add Organization/Event schema fixes | +6 pts | +6 pts |
| Performance fixes (defer JS + lazy load) | +4 pts | +4 pts |
| Content improvements (om-oss, blog) | +5 pts | +5 pts |
| **Projected score after full implementation** | | **~72/100** |
