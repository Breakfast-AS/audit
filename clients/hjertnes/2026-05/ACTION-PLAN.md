# SEO Action Plan — hjertnes.no
**Priority order: Critical → High → Medium → Low**
**Generated:** 2026-05-29

---

## CRITICAL — Fix Immediately

These issues block rankings, violate legal requirements, or cause active harm.

---

### C1. Fix Postal Code Inconsistency on Contact Page
**Effort: 10 min | Impact: NAP consistency, local entity matching**

The contact page shows postal code **3208**. Every other page (footer, About page) shows **3202**. The correct code for Sandefjordsveien is 3202.

- Edit `/praktisk-informasjon/kontakt/` in WordPress
- Change visiting address from "3208 Sandefjord" to "3202 Sandefjord"
- Verify all instances of the address across the site use 3202 consistently

---

### C2. Add Security Headers via Cloudflare
**Effort: 30 min | Impact: Security, trust signals**

Add via Cloudflare Dashboard → Rules → Transform Rules → Response Headers:

```
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(), geolocation=()
```

---

### C3. Remove user-scalable=no from Viewport Meta
**Effort: 10 min | Impact: WCAG compliance, Norwegian accessibility law, mobile ranking**

In the WordPress theme's `header.php` or via functions.php, change:
```html
<!-- Before -->
<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">

<!-- After -->
<meta name="viewport" content="width=device-width, initial-scale=1">
```

This is a legal requirement under the Norwegian Accessibility Act (likestillings- og diskrimineringsloven § 17).

---

### C4. Block xmlrpc.php via Cloudflare WAF
**Effort: 15 min | Impact: Security**

In Cloudflare: Security → WAF → Custom Rules → Create rule:
- Expression: `(http.request.uri.path eq "/xmlrpc.php")`
- Action: Block

Also remove the pingback link tag from WordPress (add to `functions.php`):
```php
remove_action('wp_head', 'xmlrpc_rsd_link');
remove_action('wp_head', 'wp_generator');
```

---

### C5. Fix www → HTTPS Redirect (1 hop, not 2)
**Effort: 15 min | Impact: Crawl efficiency, security**

In Cloudflare: Rules → Redirect Rules → Create rule:
- Match: `Hostname equals www.hjertnes.no`
- Action: Dynamic redirect to `https://hjertnes.no${http.request.uri.path}` (301)

This bypasses the intermediate HTTP step.

---

### C6. Add Editorial Intro Text to Homepage
**Effort: 1–2 hours | Impact: Content quality, AI citations, local SEO, E-E-A-T**

In WordPress homepage editor, add a text block above or alongside the event slider:

```
Hjertnes Kulturhus er Sandefjords kulturhus og kino, åpnet i 1975 og
eid av Sandefjord Kommune. Vi tilbyr konserter, teater, film og
kulturarrangementer for alle aldre — fra intime forestillinger til
Harmonie arena med plass til 800 gjester.

Adresse: Sandefjordsveien 3, 3202 Sandefjord
Telefon: 33 41 67 60
E-post: hjertnes@hjertnes.no

[Kulturprogram] [Kinoprogram] [Lei en sal] [Gavekort]
```

Also add a semantic `<h1>` tag if not present in the template.

---

### C7. Add Event Schema to All Event Pages
**Effort: 4–8 hours (developer) | Impact: Rich results, event carousels, AI citation**

This is the highest-volume schema opportunity on the site (895 pages). Implement via WordPress `wp_head` action hook that fires on single event post types:

```php
add_action('wp_head', function() {
    if (!is_singular('event')) return;
    $event = get_queried_object();
    // Fetch ACF/custom fields: start_date, end_date, ticket_url, price, performer
    $schema = [
        '@context' => 'https://schema.org',
        '@type' => 'Event',
        'name' => get_the_title(),
        'description' => wp_strip_all_tags(get_the_excerpt()),
        'startDate' => get_field('start_date'), // ISO 8601 with TZ: 2026-06-14T19:30:00+02:00
        'endDate' => get_field('end_date'),
        'eventStatus' => 'https://schema.org/EventScheduled',
        'eventAttendanceMode' => 'https://schema.org/OfflineEventAttendanceMode',
        'image' => [get_the_post_thumbnail_url(null, 'large')],
        'location' => [
            '@type' => 'Place',
            'name' => 'Hjertnes Kulturhus',
            'address' => [
                '@type' => 'PostalAddress',
                'streetAddress' => 'Sandefjordsveien 3',
                'addressLocality' => 'Sandefjord',
                'postalCode' => '3202',
                'addressCountry' => 'NO'
            ]
        ],
        'organizer' => ['@type' => 'Organization', 'name' => 'Hjertnes Kulturhus', 'url' => 'https://hjertnes.no'],
        'offers' => [
            '@type' => 'Offer',
            'url' => get_field('ticket_url'),
            'priceCurrency' => 'NOK',
            'availability' => 'https://schema.org/InStock'
        ]
    ];
    echo '<script type="application/ld+json">' . json_encode($schema) . '</script>';
});
```

Validate one event URL at https://search.google.com/test/rich-results before rolling out sitewide.

---

### C8. Add LocalBusiness/PerformingArtsTheater Schema to Homepage
**Effort: 2–3 hours | Impact: Knowledge Panel, Maps, local pack, AI entity recognition**

Add via Yoast SEO `wpseo_schema_graph` filter or as a custom `wp_head` block on the homepage template:

```json
{
  "@context": "https://schema.org",
  "@type": ["LocalBusiness", "PerformingArtsTheater"],
  "@id": "https://hjertnes.no/#business",
  "name": "Hjertnes Kulturhus",
  "alternateName": "Hjertnes",
  "url": "https://hjertnes.no",
  "telephone": "+4733416760",
  "email": "hjertnes@hjertnes.no",
  "description": "Kulturhus og kino i Sandefjord med konserter, teater, film og arrangementer for alle aldre. Åpnet i 1975, eid av Sandefjord Kommune.",
  "foundingDate": "1975",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Sandefjordsveien 3",
    "addressLocality": "Sandefjord",
    "postalCode": "3202",
    "addressRegion": "Vestfold",
    "addressCountry": "NO"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 59.1315,
    "longitude": 10.2167
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
      "opens": "08:00",
      "closes": "15:30"
    }
  ],
  "sameAs": [
    "https://www.facebook.com/hjertneskulturhus",
    "https://www.instagram.com/hjertnes.kulturhus/"
  ],
  "logo": {
    "@type": "ImageObject",
    "url": "https://hjertnes.no/wp-content/uploads/2024/07/hjertnes-kulturhus-logo.png",
    "width": 800,
    "height": 200
  }
}
```

*Verify latitude/longitude against the actual Google Maps pin before deploying.*

---

### C9. Add FAQPage Schema to FAQ Page
**Effort: 2–3 hours | Impact: AI/LLM citations, Google AI Overviews**

Add JSON-LD to `/praktisk-informasjon/ofte-stilte-sporsmal/`. Map each accordion item to a Question/Answer pair. Also fix heading hierarchy: convert `<p class="toggle"><strong>Question</strong></p>` to `<h3>Question</h3>`.

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Kan man ha bursdag på kino?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja! Vi tilbyr kinobursdag for barn og unge. Du velger en film, kjøper billetter og bestiller snackspakke. Ta kontakt for mer informasjon."
      }
    }
    // ... map all 14+ FAQ items
  ]
}
```

*Note: Google will NOT show FAQ rich results for commercial sites (August 2023 restriction), but ChatGPT, Perplexity, and Claude use FAQPage schema for direct answer extraction.*

---

### C10. Add "Sandefjord" to All Page Title Tags
**Effort: 1–2 hours | Impact: Local rankings for all city+service queries**

In Yoast SEO → Search Appearance → set title templates:

| Page | New Title |
|---|---|
| Homepage | Hjertnes Kulturhus – Konserter, Kino og Kultur i Sandefjord |
| /kino/ | Kino i Sandefjord \| Hjertnes Kulturhus |
| /program/ | Kulturprogram Sandefjord \| Hjertnes Kulturhus |
| /utleie/ | Lei saler i Sandefjord \| Hjertnes Kulturhus |
| /om-hjertnes-kulturhus/ | Om Hjertnes Kulturhus – Kulturhus i Sandefjord siden 1975 |
| /praktisk-informasjon/kontakt/ | Kontakt Hjertnes Kulturhus Sandefjord – Tlf 33 41 67 60 |

---

### C11. Create /llms.txt
**Effort: 1 hour | Impact: AI search visibility (ChatGPT, Perplexity, Claude)**

Create the file at `https://hjertnes.no/llms.txt` (place in WordPress root or serve via WP Engine rewrite):

```
# Hjertnes Kulturhus
> Hjertnes Kulturhus er et kulturhus og kino i Sandefjord, Vestfold, Norge.
> Adresse: Sandefjordsveien 3, 3202 Sandefjord. Telefon: 33 41 67 60. E-post: hjertnes@hjertnes.no.
> Kulturhuset åpnet i 1975 og eies av Sandefjord Kommune.
> Vi tilbyr kulturarrangementer, konserter, teater, kino, saleie og gavekort.

## Viktige sider
- Om oss: https://hjertnes.no/om-hjertnes-kulturhus/
- Kulturprogram: https://hjertnes.no/program/
- Kino: https://hjertnes.no/kino/
- FAQ: https://hjertnes.no/praktisk-informasjon/ofte-stilte-sporsmal/
- Kontakt: https://hjertnes.no/praktisk-informasjon/kontakt/
- Utleie: https://hjertnes.no/utleie/
- Gavekort: https://hjertnes.no/gavekort/
```

---

## HIGH — Fix Within 1 Week

---

### H1. Add Meta Descriptions to All Key Pages
**Effort: 2 hours | Impact: CTR in all search engines**

In Yoast SEO, set meta description templates. All descriptions must include "Sandefjord":

| Page | Meta Description |
|---|---|
| /kino/ | Se de nyeste filmene på Hjertnes kino i Sandefjord. Kinoprogram, billetter og informasjon om kinobursdag, familiedag og kinokortet. |
| /program/ | Kulturprogram på Hjertnes Kulturhus i Sandefjord – konserter, teater og forestillinger for alle aldre. Kjøp billetter online. |
| /utleie/ | Lei saler og scener på Hjertnes Kulturhus i Sandefjord. Fra intime rom til Harmonie arena med plass til 800 personer. Kontakt oss. |
| Event pages | `%%post_title%% – %%excerpt%% Hjertnes Kulturhus, Sandefjord. Kjøp billetter online.` |

---

### H2. Noindex Internal Playlist Pages + Remove from Sitemap
**Effort: 1 hour | Impact: Crawl budget, prevents test content appearing in Google**

6 URLs in `playlist-sitemap.xml` are internal info-screen display tools. The `testliste` and `tom-tester` entries are clearly test content.

Add to the `ambio-info-screen` WordPress template:
```php
add_filter('wpseo_robots', function($robots) {
    if (is_singular('playlist')) return 'noindex, nofollow';
    return $robots;
});
```

Remove the entire `playlist-sitemap.xml` from the sitemap index via Yoast SEO settings.

---

### H3. Conditionally Noindex Empty Taxonomy Archives
**Effort: 2–3 hours (developer) | Impact: Index quality, crawl budget**

Many genre, category, promoter, and venue archives return 0 results. Add conditional noindex:

```php
add_filter('wpseo_robots', function($robots) {
    if (is_tax(['event_genre', 'event_category', 'event_promoter', 'event_hall', 'event_type'])) {
        $query = new WP_Query(['post_type' => 'event', 'tax_query' => [/* current term */], 'posts_per_page' => 1]);
        if (!$query->have_posts()) return 'noindex, follow';
    }
    return $robots;
});
```

Also remove noindexed URLs from their respective sitemaps.

---

### H4. Add OG Image to Homepage (and twitter:image)
**Effort: 30 min | Impact: All social sharing (Facebook, LinkedIn, WhatsApp)**

Create a branded 1200×630px image showing the Hjertnes logo on venue photography. Upload to WordPress, then in Yoast SEO → Social → Facebook → Default image.

Also add explicitly in page template or Yoast:
```html
<meta name="twitter:image" content="https://hjertnes.no/path/to/og-image.jpg">
```

---

### H5. Enrich Yoast Organization Schema
**Effort: 30 min | Impact: Knowledge Panel, AI entity signals**

In Yoast SEO → General → Organization:
- Set Telephone: +47 33 41 67 60
- Set Email: hjertnes@hjertnes.no
- Add social profiles: Facebook and Instagram URLs
- This auto-populates `sameAs` and `telephone` in the Organization JSON-LD block

---

### H6. Add Google Maps Embed to Contact Page
**Effort: 30 min | Impact: Local rankings, user experience, GBP signal**

Add a lazy-loaded Google Maps iframe to `/praktisk-informasjon/kontakt/` pinned to the GBP listing:
```html
<iframe
  src="https://www.google.com/maps/embed?pb=..."
  loading="lazy"
  width="100%"
  height="400"
  style="border:0;"
  allowfullscreen=""
  title="Kart til Hjertnes Kulturhus">
</iframe>
```

---

### H7. Wrap Phone Numbers in tel: Links
**Effort: 1 hour | Impact: Mobile conversions, local signal**

Find all instances of phone numbers across templates and pages. Wrap in:
```html
<a href="tel:+4733416760">33 41 67 60</a>
```

---

### H8. Add Accessible Label to SVG Logo
**Effort: 15 min | Impact: Accessibility, screen reader users**

In the theme header template, wrap the SVG in a labeled anchor:
```html
<a id="branding" href="https://hjertnes.no" aria-label="Hjertnes Kulturhus — tilbake til forsiden">
  <svg aria-hidden="true" focusable="false" viewBox="0 0 112 28" ...>
    ...
  </svg>
</a>
```

---

### H9. Expand /om-hjertnes-kulturhus/ to 300+ Words
**Effort: 1–2 hours | Impact: AI entity recognition, E-E-A-T**

Current: ~90 words. Target: 300–400 words with structured facts:
- Founding year (1975)
- Owner (Sandefjord Kommune)
- Address
- Hall inventory: Sal 1, Sal 2, Sal 3, Harmonie arena (800 capacity), Hjertnes Amfi, Foajéscenen
- Services: cinema, concerts, theatre, venue hire, gift cards
- Accessibility features (hearing loops, wheelchair access)
- Scandic Park Hotel co-location

---

### H10. Expand /utleie/ to 800+ Words
**Effort: 3–4 hours | Impact: Content quality, local commercial rankings**

Add to the venue rental page:
- Capacity table for all 6 halls
- AV/technical specifications summary
- Catering/partnership details
- Booking process (step-by-step)
- Pricing range (or "contact for quote")
- Accessibility features per room

---

### H11. Fix Invalid datePublished in Event Schema
**Effort: 2 hours (developer) | Impact: Schema validation, Google Rich Results**

The `-0001-11-30` date value comes from WordPress event post types with no publication date. In the Yoast SEO `wpseo_schema_graph` filter, override the `datePublished` for event post types to use the event start date or `post_date` field instead.

---

### H12. Enable Breadcrumbs on All Pages
**Effort: 30 min | Impact: SERP sitelinks breadcrumb, navigation signals**

In the WordPress theme, locate where `<!-- No breadcrumbs -->` is conditionally output and remove the condition that suppresses it on /kino/, /utleie/, /kinokortet/, and other service pages. Breadcrumbs should display on all pages except the homepage.

---

## MEDIUM — Fix Within 1 Month

---

### M1. Add H1 to Homepage
Add a visually styled H1 (can be visually hidden if design requires) to the `<main>` element:
```html
<h1 class="sr-only">Hjertnes Kulturhus – Konserter, kino og kulturarrangementer i Sandefjord</h1>
```

### M2. Add defer to Render-Blocking Scripts
In the theme's `functions.php`, use `wp_script_add_data()` to defer jQuery and the theme script:
```php
wp_script_add_data('jquery-core', 'defer', true);
wp_script_add_data('hjertnes-kulturhus', 'defer', true);
```
Test thoroughly — inline scripts that use jQuery synchronously will break if jQuery is deferred without them also being deferred.

### M3. Add Resource Hints
In the theme `<head>`, add preconnect for any third-party origins:
```html
<link rel="preconnect" href="https://storage.googleapis.com">
<link rel="dns-prefetch" href="https://www.googletagmanager.com">
```
Preload the above-the-fold hero image (identify the LCP element first via PageSpeed Insights).

### M4. Fix og:type on Service Pages
In Yoast SEO, ensure permanent service/landing pages use `og:type: website`, not `article`. This is set in Yoast SEO → Search Appearance → Content Types.

### M5. Add Opening Hours to Contact Page + Schema
Add visible opening hours to `/praktisk-informasjon/kontakt/` with `OpeningHoursSpecification` schema:
- Administration: Mon–Fri 08:00–15:30
- Phone: 10:00–21:00
- Ticket window: opens 30 min before first show, max 16:00 weekdays / 14:00 weekends

### M6. Add Place Schema to Venue Pages
For each rental venue sub-page (Harmonie arena, Sal 1, Sal 2, Sal 3, etc.), add a `Place` schema block with `maximumAttendeeCapacity` and `containedInPlace` referencing the main kulturhus.

### M7. Define AI Crawler Policy in robots.txt
Decide whether to allow or restrict AI training crawlers (GPTBot, Google-Extended, Bytespider, CCBot). Add explicit directives. Note: blocking GPTBot only affects training, not ChatGPT browsing.

### M8. Implement IndexNow
Enable via the free Yoast SEO IndexNow plugin. 10-minute setup. Ensures near-instant Bing indexation for new/updated events.

### M9. Fix Duplicate Venue Slugs in event_hall Taxonomy
Audit `harmonie-arena` vs `harmonie-arena-kom`, `harmonie-arena-back` vs `harmonie-arena-backstage`, etc. Merge duplicate terms in WordPress admin, set 301 redirects from truncated slugs, remove duplicates from sitemap.

### M10. Fix Crawl-delay Placement in robots.txt
Move `Crawl-delay: 10` inside the `User-agent: *` block (or remove it entirely):
```
User-agent: *
Crawl-delay: 1
Disallow:

Sitemap: https://hjertnes.no/sitemap_index.xml
```

### M11. Claim Bing Places + Apple Business Connect
- Bing Places: https://bingplaces.com (powers ChatGPT local results)
- Apple Business Connect: https://register.apple.com/maps

Ensure NAP matches website exactly (3202 postal code, +47 33 41 67 60).

### M12. Fix /kinokortet/ Meta Description
Change from "Kinokortet – Den perfekte bedriftsgaven!" (40 chars) to:
"Kjøp Kinokortet fra Hjertnes Kulturhus – kr 130 per kort med 20% rabatt på snacks. Perfekt bedriftsgave i Sandefjord. Bestill på e-post."

### M13. Rewrite /kino/ H1
Change from "Kino" to "Kino på Hjertnes Kulturhus – Sandefjords kinosenter."

### M14. Audit Header Color Contrast
Test amber header background `rgb(226, 153, 83)` against text colors using WebAIM Contrast Checker. White on this background gives ~2.6:1 (fails WCAG AA 4.5:1). Darken to at least `rgb(180, 110, 40)` for WCAG AA compliance, or switch to dark text.

### M15. Address Tax/Sustainability Claims on /kinokortet/
Add a link to Skatteetaten for the tax benefit claim. Add specifics or remove the "skaper minner, ikke avfall" sustainability claim if unverifiable.

---

## LOW — Backlog

| # | Action | Effort |
|---|---|---|
| L1 | Enable IndexNow key file | 10 min |
| L2 | Remove pingback `<link>` from `<head>` | 15 min |
| L3 | Remove xfn profile link (HTTP ref) | 5 min |
| L4 | Populate WebSite schema description field in Yoast | 5 min |
| L5 | Exclude cookie/privacy pages from sitemap | 10 min |
| L6 | Remove "Arkiver" suffix from taxonomy archive titles | 30 min |
| L7 | Add visible "Sist oppdatert" date to editorial pages | 30 min |
| L8 | Restrict WP REST API unauthenticated access | 1 hour |
| L9 | Add author attribution to content ("Hjertnes Kulturhus") | 1 hour |
| L10 | Commission Norwegian Wikipedia article | 4+ hours |
| L11 | Verify skip link visibility on keyboard focus | 30 min |
| L12 | Set up AggregateRating schema (when reviews available) | 1 hour |

---

## Implementation Timeline

### Week 1 (Critical fixes — no developer needed for most)
- Fix postal code on contact page (10 min)
- Add security headers via Cloudflare (30 min)
- Remove user-scalable=no (10 min)
- Block xmlrpc.php via Cloudflare (15 min)
- Fix www redirect chain (15 min)
- Add editorial intro text to homepage (1–2 hours)
- Create /llms.txt (1 hour)
- Add "Sandefjord" to all title tags via Yoast (1–2 hours)
- Add OG image (30 min)
- Enrich Yoast Organization with telephone and social profiles (30 min)

### Week 2 (Schema and content — developer required)
- Implement Event schema on all event pages
- Implement LocalBusiness/PerformingArtsTheater schema
- Add FAQPage schema to FAQ page
- Fix invalid datePublished values
- Enable breadcrumbs sitewide
- Add `aria-label` to SVG logo

### Week 3 (Content expansion)
- Expand /om-hjertnes-kulturhus/ to 300+ words
- Expand /utleie/ to 800+ words
- Add meta descriptions to all pages
- Add H1 to homepage
- Add tel: links to all phone numbers
- Add Google Maps embed to contact page
- Add opening hours to contact page + schema

### Week 4 (Technical optimisation)
- Noindex empty taxonomy archives
- Noindex playlist pages + remove from sitemap
- Fix duplicate venue slugs
- Defer render-blocking scripts
- Add resource hints
- Claim Bing Places and Apple Business Connect

### Month 2 (Medium priority)
- All remaining MEDIUM items
- Commission Wikipedia article
- Set up review collection and AggregateRating schema
- Consider YouTube channel for event previews

---

## Expected Score Improvement

If all Critical and High items are implemented:

| Category | Current | Projected |
|---|---|---|
| Technical SEO | 48/100 | 75/100 |
| Content Quality | 40/100 | 65/100 |
| On-Page SEO | 38/100 | 70/100 |
| Schema / Structured Data | 10/100 | 72/100 |
| Performance (CWV) | 68/100 | 78/100 |
| AI Search Readiness | 38/100 | 68/100 |
| Images | 62/100 | 80/100 |
| **Overall** | **42/100** | **~73/100** |

Local SEO: 34/100 → projected 62/100 after schema + NAP + geo-targeting fixes.
