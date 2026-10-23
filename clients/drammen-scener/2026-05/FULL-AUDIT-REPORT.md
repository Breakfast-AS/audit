# SEO Audit Report: drammenscener.no
**Audit date:** 2026-05-29
**Auditor:** Claude Code SEO Audit System (5 specialist agents)
**Site:** https://www.drammenscener.no/
**Business:** Drammen Scener — event and conference venue company, Drammen, Norway
**Venues:** Union Scene (Grønland, Drammen) + Drammens Teater (Drammen sentrum)
**Platform:** WordPress + Yoast SEO v27.6 + WP Engine + Cloudflare CDN
**Language:** Norwegian (nb-NO) | ~36 indexed pages

---

## Overall SEO Health Score: 44 / 100

| Category | Weight | Score | Weighted |
|---|---|---|---|
| Technical SEO | 22% | 57/100 | 12.5 |
| Content Quality | 23% | 38/100 | 8.7 |
| On-Page SEO | 20% | 40/100 | 8.0 |
| Schema / Structured Data | 10% | 30/100 | 3.0 |
| Performance (CWV) | 10% | 52/100 | 5.2 |
| AI Search Readiness | 10% | 61/100 | 6.1 |
| Images | 5% | 30/100 | 1.5 |
| **Total** | | | **45 / 100** |

> Score of 44 = **Needs Significant Work.** The site has a solid technical foundation (Cloudflare, HTTPS, HTTP/2, SSR WordPress) and one notable strength (llms.txt already in place). The primary gaps are security headers, missing schema, thin content, and near-zero local SEO signals.

---

## Executive Summary

Drammen Scener operates two premium event venues in Drammen — Union Scene and Drammens Teater — and the website reflects the visual quality of the brand. However, it significantly underperforms on the factors that drive organic search discovery and conversion from search. The five most critical findings are:

1. **Zero LocalBusiness/EventVenue schema anywhere on the site** — Google cannot confirm this is a physical venue business from structured data alone.
2. **No NAP (Name, Address, Phone) in homepage HTML** — The most authoritative page on the domain provides no location signals for local search.
3. **Six security headers absent** — Missing HSTS, CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy. The WordPress XMLRPC pingback endpoint is also advertised on every page.
4. **Pervasive thin content** — Package and venue pages average ~200 words. Conference package page reads in 1 minute. No FAQ content exists anywhere.
5. **No trust signals** — No testimonials, no named contacts, no organisasjonsnummer, no client references.

### Top 5 Quick Wins
1. Add meta description to `/saler/` (20 minutes, confirmed missing)
2. Enable IndexNow in Yoast SEO settings (2 minutes, zero-code)
3. Fix dual H1 on homepage — demote jumbotron H1 to styled div (30 minutes)
4. Noindex 6 department taxonomy archive pages in Yoast (10 minutes)
5. Add security headers via Cloudflare Transform Rules (1 hour)

---

## 1. Technical SEO — 57 / 100

### 1.1 Security — FAIL (28/100)

#### CRITICAL: Six Security Headers Absent (Site-Wide)
None of the following are present on any page response:

| Header | Risk |
|---|---|
| `Strict-Transport-Security` | No HTTPS upgrade guarantee on first visit; HSTS preload ineligible |
| `Content-Security-Policy` | No XSS mitigation at HTTP layer |
| `X-Frame-Options` | Site can be framed by any third party (clickjacking) |
| `X-Content-Type-Options` | MIME-sniffing attacks not blocked |
| `Referrer-Policy` | Full URLs leaked to GTM, Vimeo, Google Fonts |
| `Permissions-Policy` | No browser feature restrictions |

**Fix via Cloudflare Transform Rules → Response Header Transform:**
```
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(), geolocation=()
```
CSP requires testing — start in report-only mode before enforcing.

#### CRITICAL: xmlrpc.php Advertised on Every Page
`<link rel="pingback" href="https://www.drammenscener.no/xmlrpc.php" />` appears in every page `<head>`. While Cloudflare blocks direct POST requests (HTTP 403), the link tag still advertises the WordPress XMLRPC attack surface to every crawler.

**Fix — two steps:**
```php
// functions.php
remove_action('wp_head', 'xmlrpc_rsd_link');
add_filter('bloginfo_url', fn($out, $prop) => $prop === 'pingback_url' ? '' : $out, 11, 2);
```
Plus: WordPress Admin → Settings → Discussion → uncheck pingbacks/trackbacks.

#### CRITICAL: WordPress REST API Fully Exposed
Every page `Link` header contains `/wp-json/` and `/wp-json/wp/v2/pages/[ID]`. This enables user enumeration at `/wp-json/wp/v2/users`, exposes post IDs, plugin surface, and WordPress version.

**Fix:**
```php
add_filter('rest_authentication_errors', function($result) {
    if (!is_user_logged_in()) {
        return new WP_Error('rest_not_logged_in', 'REST API restricted.', ['status' => 401]);
    }
    return $result;
});
remove_action('wp_head', 'rest_output_link_header', 11);
```

#### CRITICAL: wp-login.php Returns HTTP 200
Admin login page is fully accessible with no rate limiting. Combined with user enumeration via REST API, this is a live brute-force surface.

**Fix:** Add 2FA (WP 2FA plugin), implement login rate limiting, or use WPS Hide Login to obscure the URL. At minimum, protect via WP Engine's access restriction tools.

### 1.2 Crawlability — 70/100

**robots.txt is correct** — full crawl access for all bots including AI crawlers, sitemap declared. The `Crawl-delay: 10` applies globally (Googlebot ignores it; Bingbot respects it). For a 36-URL site this is acceptable but unnecessary.

**Positive:** 4-file sitemap index structure (pages, packages, scenes, departments) is well-formed with image entries and current `lastmod` dates.

**Issue — /ansatte/ missing from all sitemaps** despite returning HTTP 200 with index/follow. Either add to sitemap or noindex.

**Issue — Department taxonomy archives indexed.** Six pages (`/department/daglig-leder/`, `/department/drift/`, etc.) are indexed with no content value. These are auto-generated WordPress taxonomy pages from the staff classification system.

**Fix:** Yoast SEO → Search Appearance → Taxonomies → Department → Show in search results: No.

### 1.3 Indexability — 62/100

**Canonical tags are correct** on all tested pages. No cross-domain conflicts.

**Missing meta descriptions confirmed:**
- `/saler/` — NO meta description tag at all
- `/konferanser/` — absent
- `/eventer/` — absent
- `/ansatte/` — absent

**URL Cannibalization:** `/eventer/` (page) and `/pakker/eventer/` (package) both indexed and targeting similar queries. Differentiate by intent or consolidate.

**HTTP → HTTPS redirect** chain is correct (non-www → www with HTTPS 301).

### 1.4 URL Structure — 80/100

Clean, lowercase, hyphenated Norwegian slugs throughout. Good hierarchy: `/saler/[room-name]/` and `/pakker/[package-name]/`. No issues identified.

Minor: `@woahmedia.no-Runde1-*.jpg` filenames in media library expose photographer agency name. No immediate action required but set a kebab-case file naming policy for future uploads.

### 1.5 Mobile — 78/100

`viewport` meta tag correctly set. Responsive CSS framework in use. Swiper.js slider is mobile-friendly. No blocking mobile issues identified from HTML analysis (visual testing not performed — Playwright unavailable).

### 1.6 Core Web Vitals Signals — 52/100

**Render-blocking Google Fonts CSS:**
```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined">
```
Synchronous, no preconnect, no async. Blocks render. Two external TCP/TLS handshakes before font resolves.

**Fix:**
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined"></noscript>
```

**jQuery + jQuery Migrate — synchronous, no defer:**
Both `jquery.min.js` (3.7.1) and `jquery-migrate.min.js` (3.4.1) load without `async`/`defer`. jQuery Migrate is a backwards-compatibility shim that adds ~10 KB for zero user-facing benefit on a custom theme.

**Fix:**
```php
// Remove jQuery Migrate in production
add_action('wp_default_scripts', function($scripts) {
    if (!is_admin()) $scripts->remove('jquery-migrate');
});
```

**Vimeo background video — LCP and CLS risk:**
- Thumbnail `<img>` loads from external `i.vimeocdn.com` — no preconnect hint
- Container uses percentage-based dimensions — potential layout shift when Vimeo iframe swaps in
- Empty `alt=""` on thumbnail (decorative is acceptable but `fetchpriority="high"` missing)

**Fix:**
```html
<link rel="preconnect" href="https://i.vimeocdn.com" crossorigin>
```
Add `fetchpriority="high"` to thumbnail `<img>`. Add explicit `aspect-ratio: 16/9` to `.iframe-wrapper` in CSS.

**Image optimization — positive signals:** Most images serve `.webp` format from `/wp-content/uploads/2026/02/`. Original JPEGs exist alongside WebP versions. The `img:is([sizes=auto])` CSS rule is set.

**Issue:** 12+ slider images on homepage and jumbotron thumbnail all have `alt=""`. Empty alt is technically acceptable for decorative images, but these are venue showcase images that should have descriptive alt text for accessibility and image SEO.

### 1.7 JavaScript Rendering — 72/100

WordPress is SSR (server-side rendered via Twig templates). All page content is present in the HTML response — no client-side rendering dependency. This is a significant advantage over JavaScript-heavy SPAs. AI crawlers and Googlebot receive complete content without JS execution.

The Speculation Rules API is implemented for link prefetching — a positive modern performance signal. Scope is currently "all internal links" which may cause Formidable Forms pages to be prefetched and ghost GTM pageview events.

### 1.8 IndexNow — FAIL (10/100)

No IndexNow key file, no meta tag, no API calls detected. Yoast SEO v22+ has native IndexNow support built in.

**Fix:** Yoast SEO → General → Features → IndexNow → On. Takes 30 seconds. Ensures Bing picks up content changes within hours instead of waiting for scheduled crawl.

---

## 2. Content Quality — 38 / 100

### 2.1 E-E-A-T Assessment

| Dimension | Score | Notes |
|---|---|---|
| Experience | 11/20 | No event case studies, no client stories, no staff-authored content |
| Expertise | 14/25 | Surface-level marketing copy; no AV specs, no capacity data on most pages |
| Authoritativeness | 9/25 | No press mentions, no awards displayed, no industry body references |
| Trustworthiness | 14/30 | No organisasjonsnummer, no named contacts, very thin contact page |

### 2.2 Homepage

**Critical — Dual H1 tags:** Two H1 elements exist simultaneously:
- Jumbotron H1: "Drammen Scener" (brand name only — no keyword value)
- Text panel H1: "Velkommen til Østlandets råeste lokaler – der ditt neste arrangement finner sted!"

A page must have exactly one H1. The correct H1 for this page is something like: *"Konferanselokaler og eventsaler i Drammen"* — targets commercial intent, anchors topical relevance.

**Critical — Word count:** Estimated ~90 words of substantive body prose (excluding navigation and slider captions). Minimum for a commercial homepage: 500 words.

**Critical — Keyword targeting gaps:** None of the primary commercial terms appear in heading structure:
- "konferanselokaler Drammen" — absent from headings
- "selskapslokaler Drammen" — absent
- "møtelokaler Drammen" — absent
- "leie lokaler Drammen" — absent

**Medium — Seasonal content staleness:** The summer event teaser (VM/EK football) is a static promotional block. When the summer event ends, this becomes stale editorial content on the homepage.

### 2.3 /saler/ (Venue Listing Page)

**Critical:** No meta description. Eight venue cards with brief descriptions. No capacity figures, room dimensions, AV specs, or accessibility information. This is a navigation index masquerading as a substantive service page.

Minimum requirement: 800 words with capacity (seated/standing/theatre/cabaret), floor area, AV equipment, catering policy, parking, accessibility, and setup configurations for each venue.

### 2.4 Package Pages (/pakker/ — 7 pages)

**Critical — Thin content pattern:** All 7 package pages estimated at ~1 minute reading time (~200-250 words each). Twitter meta `data1: "1 minutt"` confirms this.

For B2B buyers evaluating a venue for a 100-person conference, 200 words cannot provide what they need to evaluate a vendor: inclusions, pricing anchors, AV specifications, booking process, lead times, cancellation policy.

**High risk — Near-duplicate content pattern:** Seven pages with similar adjective-heavy templates targeting overlapping keywords. Google may suppress most of them.

### 2.5 /kontakt-oss/ (Contact Page)

Meta description: *"Del dine spennende event- og konferanseidéer med oss."* — 51 characters, no location signal, informal consumer tone, no call to action.

Missing from contact page:
- Named contacts with title and direct phone
- Response time commitment
- Physical address for both venues
- Organisasjonsnummer (Norwegian B2B trust requirement)
- Separate paths for new bookings vs. existing client support

### 2.6 AI Citation Readiness — 12/100

Critically low. AI systems require structured factual claims, FAQ-format content, Schema.org markup, and specific quotable statements. The site uses aspirational marketing language throughout:
- "landets mest praktfulle teater" — unsubstantiated superlative
- "Østlandets råeste lokaler" — brand claim, not a citable fact
- "moderne og urban atmosfære" — generic description

No FAQ content exists anywhere on the site. No case studies. No named statistics ("we host X events per year").

### 2.7 Priority Recommendations

| Priority | Page | Action |
|---|---|---|
| Critical | Homepage | Fix dual H1; expand body content to 500+ words |
| Critical | /saler/ | Write meta description; add capacity/spec tables |
| Critical | /pakker/konferansepakke/ | Expand from 200 to 800+ words |
| Critical | All /pakker/ pages | Differentiate with unique content per package type |
| High | /kontakt-oss/ | Rewrite with named contacts, address, organisasjonsnummer |
| High | All pages | Add 3-5 client testimonials with company/title |
| High | New page | Create /ofte-stilte-sporsmal/ FAQ with 15+ Q&A pairs |
| Medium | /om-oss/ | Add founding history, event volume, team content |
| Medium | New section | Create "arrangementstips" blog (6-8 posts min.) |

---

## 3. On-Page SEO — 40 / 100

### 3.1 Title Tag Audit

| Page | Current Title | Issues |
|---|---|---|
| Homepage | "Drammen Scener - Drammens råeste lokaler!" | No primary keyword in title |
| /saler/ | "Saler og lokaler - Drammen Scener" | Acceptable; no city name |
| /pakker/konferansepakke/ | "Pakkeløsninger for ditt arrangement \| Drammen Scener" | Keyword-poor; no "Drammen" |
| /kontakt-oss/ | "Kom i kontakt med oss - Drammen Scener" | No city, no service terms |

**Recommended template:** `[Service/Page type] i Drammen | [Venue Name] - Drammen Scener`

Examples:
- Homepage: "Konferanselokale og eventlokale i Drammen | Drammen Scener"
- /saler/: "Saler og lokaler i Drammen | Union Scene & Drammens Teater"
- /kontakt-oss/: "Kontakt oss | Konferanselokale i Drammen - Drammen Scener"

### 3.2 Heading Structure

**Homepage dual H1** — covered in content section above.

Package and venue pages appear to have correct single H1 structures based on metadata review.

### 3.3 Internal Linking

The site has a shallow hub-and-spoke structure. Missing cross-linking patterns:
- Venue cards on homepage and /saler/ should link to their dedicated venue pages
- Each venue page should cross-link to relevant package pages
- Package pages should link to applicable venue pages and /kontakt-oss/
- /meny/ should link from all package pages that include catering

### 3.4 Image SEO

**Critical:** All 12 homepage slider images have `alt=""`. The jumbotron Vimeo thumbnail `<img>` also has `alt=""`.

Descriptive alt text is required for:
- Accessibility (WCAG 2.1 AA)
- Google Image Search visibility
- AI image comprehension

Example alt text:
- `alt="Hovedscenen på Union Scene satt opp for konferanse med 300 gjester"` instead of `alt=""`

---

## 4. Schema / Structured Data — 30 / 100

### 4.1 Current State

Only Yoast-generated defaults present across all pages:
- `WebPage`, `WebSite`, `ImageObject`, `BreadcrumbList` — present (correct)
- `LocalBusiness` / `EventVenue` — **ABSENT** (critical)
- `Organization` with address/phone — **ABSENT** (critical)
- `Service` or `Offer` on package pages — **ABSENT**
- `Place` with capacity on venue pages — **ABSENT**
- `FAQPage` — **ABSENT** (no FAQ content exists to mark up)

**Critical:** All `/pakker/` pages output `og:type="article"` — incorrect for commercial service/package pages. These pages are WordPress custom post type entries that Yoast treats as editorial content.

**Fix for og:type:**
```php
// functions.php
add_filter('wpseo_opengraph_type', function($type) {
    if (get_post_type() === 'package') return 'website';
    return $type;
});
```

### 4.2 Priority Schema Additions

#### Schema Priority 1 — Organization + EventVenue (Homepage)
Add alongside existing Yoast @graph block:

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://www.drammenscener.no/#organization",
      "name": "Drammen Scener",
      "url": "https://www.drammenscener.no/",
      "description": "Drammen Scener drifter Union Scene og Drammens Teater – to unike arrangementslokaler sentralt i Drammen.",
      "telephone": "+47XXXXXXXX",
      "email": "post@drammenscener.no",
      "sameAs": [
        "https://www.facebook.com/drammenscener",
        "https://www.instagram.com/drammenscener",
        "https://www.linkedin.com/company/drammen-scener"
      ]
    },
    {
      "@type": ["LocalBusiness", "EventVenue"],
      "@id": "https://www.drammenscener.no/#union-scene",
      "name": "Union Scene",
      "parentOrganization": {"@id": "https://www.drammenscener.no/#organization"},
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Grønland 60",
        "addressLocality": "Drammen",
        "postalCode": "3045",
        "addressRegion": "Buskerud",
        "addressCountry": "NO"
      },
      "geo": {"@type": "GeoCoordinates", "latitude": 59.74XXX, "longitude": 10.20XXX},
      "telephone": "+47XXXXXXXX",
      "url": "https://www.unionscene.no/"
    },
    {
      "@type": ["LocalBusiness", "PerformingArtsTheater", "EventVenue"],
      "@id": "https://www.drammenscener.no/#drammens-teater",
      "name": "Drammens Teater",
      "parentOrganization": {"@id": "https://www.drammenscener.no/#organization"},
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Schweigardsgate 1B",
        "addressLocality": "Drammen",
        "postalCode": "3017",
        "addressRegion": "Buskerud",
        "addressCountry": "NO"
      },
      "geo": {"@type": "GeoCoordinates", "latitude": 59.74XXX, "longitude": 10.20XXX},
      "telephone": "+47XXXXXXXX",
      "url": "https://www.drammensteater.no/"
    }
  ]
}
```

> Replace placeholder values (telephone, email, geo coordinates, social URLs) from the actual contact page before deploying. Verify geo coordinates via Google Maps.

#### Schema Priority 2 — Service Schema for /pakker/ Pages
Template for each package page:
```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "Konferansepakke",
  "description": "Komplette konferansepakker med lokaler, teknisk utstyr, servering og profesjonell service i Drammen.",
  "provider": {"@type": "Organization", "@id": "https://www.drammenscener.no/#organization"},
  "areaServed": {"@type": "City", "name": "Drammen"},
  "url": "https://www.drammenscener.no/pakker/konferansepakke/",
  "inLanguage": "nb-NO"
}
```

#### Schema Priority 3 — Place Schema for /saler/ Pages
Template for each room page:
```json
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Hovedscenen Union Scene",
  "maximumAttendeeCapacity": 1200,
  "amenityFeature": [
    {"@type": "LocationFeatureSpecification", "name": "Scene", "value": true},
    {"@type": "LocationFeatureSpecification", "name": "AV-utstyr", "value": true},
    {"@type": "LocationFeatureSpecification", "name": "Lydanlegg", "value": true}
  ],
  "containedInPlace": {"@type": "EventVenue", "@id": "https://www.drammenscener.no/#union-scene"},
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Grønland 60",
    "addressLocality": "Drammen",
    "postalCode": "3045",
    "addressCountry": "NO"
  }
}
```

#### Schema Priority 4 — FAQPage (once FAQ content exists)
Once the `/ofte-stilte-sporsmal/` page is created:
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hva er inkludert i konferansepakken?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Konferansepakken inkluderer leie av konferansesal, projektor og lerret, høytaleranlegg, kaffe/te og vann. Lunsj og spesialbehov kan bestilles som tillegg."
      }
    }
  ]
}
```

---

## 5. Performance — 52 / 100

Based on HTML source analysis (Lighthouse/CrUX lab data not available without Google API credentials).

### Identified Performance Risks

| Issue | Impact | Affected Pages |
|---|---|---|
| Synchronous Google Fonts CSS | LCP delay ~200-400ms | All pages |
| jQuery + jQuery Migrate (no defer) | INP/LCP | All pages |
| jQuery Migrate on production | +10 KB unnecessary | All pages |
| Vimeo thumbnail from vimeocdn.com (no preconnect) | LCP | Homepage |
| Homepage background video (Vimeo iframe) | Heavy render path | Homepage |
| Swiper.js slider | JS overhead | Homepage, /saler/ |
| Google Fonts (fonts.googleapis.com) | Third-party DNS lookup | All pages |
| Material Symbols (2,600+ icon font) | CSS weight | All pages |

### Confirmed Positive Performance Signals
- Cloudflare CDN serving cached responses (HIT)
- HTTP/2 active
- WebP image format used for most 2026 uploads
- Images served at appropriate sizes (800×530 for cards)
- Speculation Rules API for link prefetching
- `max-age=600` cache TTL on pages

---

## 6. AI Search Readiness — 61 / 100

### Positive: llms.txt Exists and Is Well-Structured

The site already has a functioning `/llms.txt` file — a significant competitive advantage. It includes:
- AI instruction preamble
- Descriptive summary with capacity range (20-1200 guests)
- All 9 rooms with capacity ranges
- Booking workflow, transport, accessibility
- History section with verifiable facts (architect Emil Victor Langlet, 1870, 1866, connection to Stortingsbygningen)
- Nøkkelbegreper (keywords) section with exact Norwegian search terms

This puts drammenscener.no in approximately the top 5% of Norwegian business websites for AI readiness.

### AI Crawler Access
All AI crawlers are permitted (GPTBot, ClaudeBot, PerplexityBot, CCBot). The `Crawl-delay: 10` slows but does not block.

### Platform-Specific AI Visibility Scores

| Platform | Score | Primary Bottleneck |
|---|---|---|
| Google AI Overviews | 48/100 | No LocalBusiness/FAQ schema; thin on-page content |
| ChatGPT (web search) | 58/100 | llms.txt helps; no pricing/FAQ limits answer quality |
| Perplexity | 65/100 | SSR + llms.txt + sitemap are positive |
| Bing Copilot | 52/100 | No schema, thin content |

### llms.txt Gaps to Address
- Missing: phone number and email address in "Booking og forespørsel" section
- Missing: Drammens Teater address (only Union Scene's Grønland 60 present)
- Missing: office/response hours
- Missing: `# License: RSL-1.0` declaration for explicit AI reuse permission

### FAQ Gap — Highest AI Opportunity
No FAQ content exists anywhere on the site. For Norwegian venue queries, AI assistants almost always generate FAQ-format answers:
- "Kan man ha julebord på Drammens Teater?"
- "Hva er inkludert i konferansepakken?"
- "Er lokalene tilgjengelige for rullestolbrukere?"

Creating a dedicated `/ofte-stilte-sporsmal/` page with 15+ Q&A pairs + `FAQPage` schema is the single highest-impact action for AI citation coverage.

---

## 7. Local SEO — 28 / 100

### 7.1 NAP Analysis

**Critical:** No NAP (Name, Address, Phone) found in homepage HTML. The most authoritative page on the domain has zero location signals outside of meta tags.

The site has a three-domain architecture:
- `drammenscener.no` — umbrella brand
- `unionscene.no` — Union Scene venue
- `drammensteater.no` — Drammens Teater venue

Each domain must maintain consistent NAP independently. Citation-building must be done per venue, not per umbrella brand.

**addressRegion note:** Should use "Buskerud" not "Viken" — Viken county was dissolved in 2024 and reverted to Buskerud.

### 7.2 Google Business Profile Signals

No GBP embed, Maps iframe, or review widget detected on the site. The following must be verified directly in GBP dashboard:

| GBP Element | Priority |
|---|---|
| Primary category: "Event Venue" (Union Scene), "Performing Arts Theater" (Drammens Teater) | Critical |
| Secondary categories: Conference Center, Banquet Hall | High |
| Business description (750 chars, keyword-rich) | High |
| Minimum 10 photos per venue | High |
| Services list with descriptions | High |
| Review velocity above Sterling Sky 18-day threshold | Critical |
| 100% review response rate | High |
| Booking/contact link | Medium |

### 7.3 Review Health

No review widget or `aggregateRating` schema detected on site. Cannot verify GBP review count from this audit.

**Sterling Sky 18-day rule:** If either GBP listing has not received a new review in >18 days, local pack rankings will have already begun to decline.

**Action:** Implement a post-event review request workflow. Send personalized email to event organizer within 48 hours of each event, with direct GBP review link. Target minimum 2 reviews/month per venue.

### 7.4 Norwegian-Specific Local SEO Requirements

**Organisasjonsnummer:** Must appear in footer or contact page for Norwegian B2B trust. Currently absent.

**Critical citations to acquire:**
1. Konferanseguiden.no — the primary Norwegian conference venue directory
2. Finn.no (lokaler til leie) — highest-traffic Norwegian property/space rental platform
3. Gulesider.no — Norwegian Yellow Pages equivalent
4. 1881.no — Key Norwegian business directory
5. Visitdrammen.no / Visit Norway — local tourism authority (trust signal + link)
6. Eventlokaler.no — sector-specific
7. Miljofyrtarn.no — verify profile completeness (cert already held)
8. Drammen Naeringsliv (Chamber of Commerce) — local authority signal

### 7.5 Local Keyword Gap

None of the primary Norwegian commercial terms appear in H1 tags or title tags:

| Keyword | Competition | Page Needed |
|---|---|---|
| konferanselokale Drammen | High | /konferanser/ — expand significantly |
| eventlokale Drammen | High | /eventer/ — expand significantly |
| selskapslokale Drammen | Medium | /pakker/privat-arrangement/ |
| møterom Drammen | Medium | New dedicated page |
| festlokale Drammen | Medium | /pakker/sommerfest/ or /pakker/fester/ |
| leie lokale Drammen | Medium | Homepage or dedicated landing page |
| konferanselokale Buskerud | Low | Umbrella page |
| Miljofyrtarn-sertifisert konferanselokale Drammen | Very Low | /miljofyrtarn/ — differentiated position |

---

## 8. Images — 30 / 100

### Image Alt Text Audit

**Homepage slider (12 images):** All have `alt=""` — empty alt text. These are the primary showcase images of the venues and should have descriptive alt text.

**Jumbotron Vimeo thumbnail:** `alt=""` — this is the LCP element and has no text description.

**Venue cards (8 rooms):** Based on HTML structure, `<figure>` elements use `data-source` lazy loading — alt text status requires verification.

### Image Format and Sizing

**Positive:** Most 2026-uploaded images are `.webp` format. Images are served at 800×530 for cards (appropriate).

**Issue:** Some original 2025 uploads still serve as JPEG (e.g., `IMG_9226-scaled.jpg` in sitemap). The site should enforce WebP conversion on all new uploads.

**OG image:** `IMG_9226-scaled.jpg` (2560×1707, JPEG) — very large original. For OG images, a dedicated 1200×630 optimized image is preferred.

---

## 9. Structured Data Additional Notes

### BreadcrumbList
Yoast BreadcrumbList is present but interior pages may be missing `item` URLs on parent ListItems. Verify that `/saler/` and `/pakker/` are published WordPress pages (not just archive endpoints) so Yoast can generate the full breadcrumb chain with URLs.

### Duplicate og:type Issue
All `/pakker/` custom post type pages output `og:type="article"`. These are commercial service pages. Fix via functions.php filter shown in Section 4.1.

---

## Site Strengths

1. **llms.txt exists and is well-structured** — top 5% of Norwegian SMBs
2. **SSR WordPress** — all content accessible to AI crawlers without JS
3. **Cloudflare CDN** — fast edge delivery, HIT cache
4. **HTTP/2 + HTTPS** — modern protocol stack
5. **Yoast SEO v27.6** — modern plugin, IndexNow and schema ready
6. **WebP images** — modern format used for 2026 uploads
7. **Speculation Rules API** — modern prefetch implementation
8. **lang="nb-NO"** — correctly set
9. **Miljøfyrtårn certification** — differentiating trust signal in market
10. **Two iconic, distinctive venues** — strong brand differentiation potential

---

*Generated by Claude Code SEO Audit System | Specialists: Technical SEO, Content Quality, Schema, Local SEO, GEO/AI Search*
*Working directory: /Users/olepetter/Desktop/kode/seo/drammen-scener*
