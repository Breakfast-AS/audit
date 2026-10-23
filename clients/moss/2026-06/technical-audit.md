# Technical SEO Audit — Moss Kulturhus
**URL:** https://www.mosskulturhus.no/
**Audit date:** 2026-06-03
**Platform:** WordPress + Yoast SEO v27.0 / WP Engine / Cloudflare CDN
**Language:** Norwegian (nb-NO)

---

## Technical SEO Score: 47 / 100

| Category | Score | Status |
|---|---|---|
| Crawlability & robots.txt | 7/10 | Needs improvement |
| Indexability | 6/15 | Critical issues |
| Security & HTTPS | 5/20 | Critical issues |
| URL Structure | 8/10 | Good |
| Site Architecture | 6/15 | High issues |
| Structured Data | 3/10 | Critical issues |
| Core Web Vitals signals | 7/10 | Needs improvement |
| JavaScript rendering | 5/10 | Needs improvement |

---

## 1. Crawlability & robots.txt

**Status: PASS with warnings**

### Findings

**robots.txt is accessible and syntactically valid.** The file is correctly referenced at `https://www.mosskulturhus.no/robots.txt` and points to the sitemap index.

```
Crawl-delay: 10
User-agent: *
Disallow:
Sitemap: https://www.mosskulturhus.no/sitemap_index.xml
```

**Issues:**

- **Crawl-delay: 10 is unnecessarily aggressive.** Google ignores `Crawl-delay` entirely; Bing and others honour it. A 10-second delay will significantly throttle Bing and other crawlers on a 164-page site. For a site this size, 1–2 seconds is more appropriate, or the directive can be removed entirely.
- **`Disallow:` with no path** is syntactically ambiguous. The intent appears to be "allow everything," which is correct, but the empty `Disallow:` line is redundant when there is no path — it does not disallow anything, but it can confuse older or non-standard crawlers. Remove it or replace with explicit `Allow: /`.
- **AI crawler tokens are absent.** There are no directives for known AI training crawlers (GPTBot, Google-Extended, ClaudeBot, CCBot, Bytespider, etc.). Without explicit rules, these crawlers are permitted to crawl and train on all content. This is a policy decision the site owner should make consciously.
- **Only one Sitemap directive.** The sitemap index is correctly listed; no redundant individual sitemap paths are declared. This is correct practice.

### Recommendations

1. Remove `Crawl-delay: 10` or reduce to `Crawl-delay: 1`.
2. Remove the bare `Disallow:` line to avoid ambiguity.
3. Add explicit `User-agent` blocks for AI crawlers with `Disallow: /` if the organisation does not consent to AI training use.

---

## 2. Indexability

**Status: FAIL — Multiple critical issues**

### 2a. Sitemap quality

The sitemap index (`sitemap_index.xml`) is present and Yoast-generated. Six child sitemaps cover 164 URLs.

| Sitemap | URLs | Notes |
|---|---|---|
| page-sitemap.xml | 38 | Static pages |
| event-sitemap.xml | 59 | Event custom post type |
| category-sitemap.xml | 24 | Taxonomy archive pages |
| post_tag-sitemap.xml | 14 | Tag archive pages |
| venue-sitemap.xml | 5 | Venue CPT |
| organizer-sitemap.xml | 24 | Organiser taxonomy |

**Sitemap issues:**

- **Tag archives in sitemap (14 URLs).** `post_tag-sitemap.xml` is included. Tag archives on an events/cultural venue site are almost universally thin content with low indexing value. Unless tags are editorially maintained with unique, substantive content, these pages should be set to `noindex` in Yoast and excluded from the sitemap. Indexing thin tag archives dilutes crawl budget and can trigger Google's thin content signals.
- **Category archives (24 URLs) need review.** Depending on content depth, many category archive pages may be thin. These should be audited individually.
- **Organiser taxonomy (24 URLs).** Organiser pages can be valuable if they contain rich content. If they are auto-generated stubs, they should be noindexed.
- **`lastmod` accuracy is unknown without direct inspection.** Yoast sets `lastmod` to the post modified date, which is generally reliable for pages and posts, but taxonomy archives often show inflated `lastmod` dates (updated whenever any post in the taxonomy is modified). This can cause unnecessary recrawl overhead.
- **`priority` values** in Yoast-generated sitemaps are typically uniform (0.6 default). Google has stated it largely ignores `priority`, so this is a low concern.
- **Past events in event-sitemap.xml.** With 59 event URLs in the sitemap, it is very likely that past/expired events are included. Expired event pages with no updated content become thin pages over time. A strategy for past events is needed (see Site Architecture section).

### 2b. Canonical tags

All sampled pages have correct self-referencing canonical tags. No canonical chain or cross-domain canonical issues detected.

### 2c. Title tag duplication — CRITICAL

Every sampled page title repeats the brand name twice:

| Page | Title |
|---|---|
| Homepage | "Moss kulturhus - Kulturhuset midt i byen - Moss kulturhus" |
| /program/ | "PROGRAM - Moss kulturhus - Moss kulturhus" |
| /venue/parkteatret/ | "Parkteatret Arkiver - Moss kulturhus - Moss kulturhus" |
| /venue/samfunnshuset/ | "Samfunnshuset Arkiver - Moss kulturhus - Moss kulturhus" |
| Event page | "Around the world in 80 toys - Nonstop - Moss kulturhus - Moss kulturhus" |

This is caused by a misconfigured Yoast SEO title template. The separator + brand append is firing twice, likely because both the page title field and the global template append the site name. This affects all 164 pages.

**Impact:** Wasted title real estate, potential keyword dilution, poor appearance in SERPs, and a risk of Google rewriting titles.

**Fix:** In Yoast SEO > Search Appearance > General, verify the title separator template. The correct template for most pages should be `%%title%% %%sep%% %%sitename%%`. Check that individual page titles in the Yoast meta box do not also manually append the brand name.

Additionally, the "Arkiver" suffix on venue archive titles (`Parkteatret Arkiver`) is a Yoast default for archive/taxonomy pages in Norwegian. This looks unprofessional in SERPs. Change the archive title template to remove "Arkiver."

### 2d. H1 tag missing on homepage — CRITICAL

The homepage has no H1 element. This is a significant on-page SEO issue. The H1 is the primary heading signal for search engines and should contain the primary keyword target for the page (e.g., "Moss Kulturhus — Parkteatret og Samfunnshuset").

### 2e. Missing meta descriptions

The sampled event page (`around-the-world-in-80-toys-nonstop`) has no meta description. If this is representative of the event post type, then most or all 59 event pages lack meta descriptions. Google will auto-generate snippets, but these are often suboptimal. Event pages should either have individually authored descriptions or a Yoast dynamic template using event-specific fields.

### Recommendations

1. Fix Yoast title template to eliminate double brand name across all 164 pages.
2. Remove "Arkiver" from taxonomy/archive title templates.
3. Add an H1 to the homepage immediately.
4. Set `post_tag` archives to `noindex` in Yoast (Search Appearance > Taxonomies > Tags > Show in search results: No).
5. Audit category and organiser archives for thin content; noindex those without substantive content.
6. Create a meta description template for event post types in Yoast.
7. Define a strategy for past events: either update with archival content, redirect to programme page, or set to noindex after expiry.

---

## 3. Security & HTTPS

**Status: FAIL — Critical security header gaps**

### 3a. HTTPS and redirect behaviour

HTTPS is active via Cloudflare. Cloudflare's Universal SSL is almost certainly handling the certificate. HTTP-to-HTTPS redirect should be in place via Cloudflare's "Always Use HTTPS" rule; however, this could not be directly verified due to tool restrictions in this environment.

**Critical finding: No HSTS (Strict-Transport-Security) header.**

The absence of HSTS means browsers will not pin the HTTPS connection on repeat visits. Users who type the domain without a scheme, or follow an HTTP link, rely on a redirect rather than the browser enforcing HTTPS natively. HSTS eliminates this attack window (SSL stripping). For a public cultural venue site handling ticket data or user accounts, HSTS should be considered mandatory.

Recommended HSTS header:
```
Strict-Transport-Security: max-age=31536000; includeSubDomains
```
Once stable, consider adding `preload` and submitting to the HSTS preload list.

### 3b. Missing security headers — HIGH

The following headers are absent, all of which are detectable by security scanners and can affect user trust signals:

| Header | Risk | Recommended Value |
|---|---|---|
| `X-Frame-Options` | Clickjacking vulnerability | `DENY` or `SAMEORIGIN` |
| `X-Content-Type-Options` | MIME-sniffing attacks | `nosniff` |
| `Content-Security-Policy` | XSS, injection attacks | Site-specific policy needed |
| `Referrer-Policy` | Data leakage via referrer | `strict-origin-when-cross-origin` |

All four of these can be added as Cloudflare Transform Rules (HTTP Response Headers), requiring no server-side changes.

### 3c. Information disclosure — MEDIUM

The `X-Powered-By: WP Engine` header and the `Link` header exposing `wp-json` API endpoint and internal page ID (46750) disclose the hosting provider and CMS internals. This is low-severity on its own but reduces the attack surface cost for targeted probing.

- Remove `X-Powered-By` via Cloudflare Transform Rule.
- Disable or restrict the REST API link header exposure via a WordPress filter (`remove_action('template_redirect', 'rest_output_link_header', 11)`), or use a security plugin.

### 3d. Caching configuration — MEDIUM

`cf-cache-status: DYNAMIC` and `X-Cache-Enabled: False` indicate the homepage is not being served from Cloudflare's edge cache. With `Cache-Control: max-age=600`, the page is cacheable for 10 minutes but is bypassed at the CDN level. This reduces the benefit of Cloudflare and increases origin server load.

WP Engine has its own caching layer, and Cloudflare's default behaviour is to not cache HTML unless Page Rules or Cache Rules explicitly enable it. Enabling Cloudflare HTML caching for the homepage and other static or semi-static pages would improve TTFB and LCP.

### Recommendations

1. Enable HSTS via Cloudflare SSL/TLS > Edge Certificates > HSTS. Start with `max-age=86400` (1 day), then extend to 1 year after verification.
2. Add `X-Content-Type-Options: nosniff`, `X-Frame-Options: SAMEORIGIN`, and `Referrer-Policy: strict-origin-when-cross-origin` as Cloudflare Transform Rules.
3. Develop a Content-Security-Policy — start in report-only mode to avoid breaking changes.
4. Remove or suppress `X-Powered-By` header.
5. Disable REST API link header in WordPress for non-authenticated users.
6. Create a Cloudflare Cache Rule to cache HTML responses for static pages (homepage, /program/, venue pages) with a short TTL (e.g., 5–10 minutes).

---

## 4. URL Structure

**Status: PASS with minor issues**

### Findings

URL structure is generally clean and follows WordPress conventions:

- Homepage: `https://www.mosskulturhus.no/` — correct
- Programme page: `https://www.mosskulturhus.no/program/` — clean
- Event: `https://www.mosskulturhus.no/event/around-the-world-in-80-toys-nonstop/` — clean
- Venue: `https://www.mosskulturhus.no/venue/parkteatret/` — clean

**Issues:**

- **"Arkiver" in URL slug is not present** (only in title tags), which is correct — WordPress archive URLs do not append "arkiver" to slugs. This is a title-only issue already captured in section 2c.
- **URL language.** URLs are in a mix of Norwegian and English (`/venue/`, `/event/`, `/organizer/` are English slugs from the The Events Calendar plugin, while page slugs are Norwegian). This is a minor inconsistency. Changing CPT base slugs (`/arrangement/`, `/sted/`) would require 301 redirects and carries risk of breaking external links — evaluate the trade-off carefully before acting.
- **www vs. non-www canonicalisation** should be enforced at both the DNS/Cloudflare level and in WordPress settings (Settings > General). The canonical tags use `https://www.mosskulturhus.no/`, which is correct. Cloudflare should be configured to redirect `mosskulturhus.no` to `www.mosskulturhus.no` via a redirect rule if not already in place.
- **Trailing slash consistency.** All sampled URLs use trailing slashes, which is consistent with WordPress defaults. This is correct.

### Recommendations

1. Verify that `mosskulturhus.no` (non-www) issues a 301 redirect to `https://www.mosskulturhus.no/`. Configure this in Cloudflare if not confirmed.
2. Verify HTTP redirects to HTTPS with a 301 (permanent), not 302.
3. Consider localising CPT base slugs (`/venue/` → `/sted/`, `/organizer/` → `/arrangorer/`) in a planned migration with proper 301 redirects, if URL consistency is prioritised.

---

## 5. Site Architecture

**Status: FAIL — High-priority structural issues**

### 5a. Event lifecycle management — HIGH

With 59 event URLs in the sitemap, expired events inevitably accumulate. The Events Calendar plugin (indicated by `/venue/`, `/organizer/`, `/event/` URL patterns) does not remove past events from sitemaps by default. Past event pages that receive no updates become:

- Thin content signals (no upcoming date, no ticket CTA, stale information)
- Crawl budget waste
- Potential negative user experience signals (bounce rate from search)

**Recommended strategy for past events:**

Option A (preferred): After event date passes, update the page with a short archival note ("Dette arrangementet er avsluttet. Se kommende arrangementer →") and add an internal link to /program/. Keep the URL live for potential backlink equity.

Option B: 301-redirect expired events to `/program/` or the relevant category/venue. Simpler but loses any link equity built to specific event URLs.

Option C: Set past events to `noindex` via Yoast after the event date. Keeps URLs live for backlink purposes but removes them from Google's index.

A hybrid approach — noindex after 30 days post-event, then evaluate 301 vs. archive based on link equity — is defensible for a site this size.

### 5b. Thin taxonomy archives — HIGH

24 category archives and 14 tag archives represent 38 URLs that are likely thin or auto-generated. If these pages do not have unique editorial descriptions, they are low-value index candidates. This is particularly risky for tag archives, which are typically the weakest taxonomy content.

### 5c. Event schema absent — CRITICAL

Event pages lack `Event` structured data. The Events Calendar plugin supports schema, but it either is not activated or is not generating valid `Event` markup. Event rich results in Google Search (date, venue, ticket availability, cancellation status) are a high-visibility SERP feature for cultural venues. Missing this schema means Moss Kulturhus is not eligible for these features.

**Minimum required Event schema fields:**
```json
{
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "Event title",
  "startDate": "2026-06-15T19:00+02:00",
  "endDate": "2026-06-15T21:00+02:00",
  "location": {
    "@type": "Place",
    "name": "Parkteatret",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "...",
      "addressLocality": "Moss",
      "addressCountry": "NO"
    }
  },
  "eventStatus": "https://schema.org/EventScheduled",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "organizer": { "@type": "Organization", "name": "Moss Kulturhus" }
}
```

The Events Calendar Pro has built-in JSON-LD output. Check if the "Schema" module is enabled under Events > Settings > Additional Fields. Alternatively, implement via Yoast SEO's schema graph or a custom `wp_head` action.

### 5d. Only WebPage schema on homepage — MEDIUM

The homepage outputs only a `WebPage` schema type. A cultural venue homepage should include `Organization`, `LocalBusiness` (with `openingHours`, `address`, `telephone`, `geo` coordinates), and potentially `PerformingArtsTheater` as the most specific applicable type.

### 5e. Internal linking to programme — MEDIUM

The `/program/` page and event pages should be the primary conversion targets. Without seeing the full DOM structure, the presence of 10 external scripts suggests significant third-party load (ticket system, analytics, social widgets). Internal linking architecture from category/venue/organiser pages to events, and from events to related events, should be audited to ensure crawl depth is minimised and PageRank flows to high-value pages.

### 5f. JavaScript rendering load — MEDIUM

10 external scripts on the homepage is high. If the primary content (event listings, navigation) is rendered client-side via JavaScript, Googlebot's two-wave indexing process means content may be indexed with a delay and may not be weighted equally. Server-side or hybrid rendering for key content blocks (event listings, navigation) is preferable. Inspect the page source to confirm whether event listings are in the initial HTML response or injected via JavaScript.

### Recommendations

1. Implement Event schema on all event post types immediately — this is the highest-impact structured data action available.
2. Add `Organization` + `LocalBusiness` (`PerformingArtsTheater`) schema to the homepage.
3. Establish an event lifecycle policy: noindex or 301-redirect events more than 30 days past their end date.
4. Noindex all post_tag archives in Yoast and remove from sitemap.
5. Audit category and organiser archives; noindex stubs without unique content.
6. Audit JavaScript rendering: use "View Source" (not DevTools) to verify event listing HTML is present in the initial server response.
7. Reduce external script count where possible; defer or lazy-load non-critical third-party scripts.

---

## Priority Action List

### Critical (fix within 1–2 weeks)

| # | Issue | Impact | Effort |
|---|---|---|---|
| C1 | Double brand name in all 164 title tags | High — affects all SERP listings | Low — 1 Yoast template fix |
| C2 | Missing H1 on homepage | High — primary on-page signal | Low |
| C3 | No Event schema on event pages | High — misses Event rich results | Medium |
| C4 | No HSTS header | Security — SSL stripping risk | Low — Cloudflare setting |

### High (fix within 1 month)

| # | Issue | Impact | Effort |
|---|---|---|---|
| H1 | Missing security headers (X-Frame, X-Content-Type, Referrer-Policy) | Security posture, user trust | Low — Cloudflare Transform Rules |
| H2 | Tag archives indexed (14 thin URLs) | Crawl budget, thin content risk | Low — Yoast toggle |
| H3 | No meta descriptions on event pages | SERP CTR | Medium — template or manual |
| H4 | Past events accumulating in sitemap/index | Crawl budget, thin content | Medium — policy + automation |
| H5 | Homepage not cached at Cloudflare edge | TTFB / LCP | Medium — Cache Rule config |

### Medium (plan within quarter)

| # | Issue | Impact | Effort |
|---|---|---|---|
| M1 | "Arkiver" in taxonomy archive titles | SERP appearance | Low |
| M2 | Organization/LocalBusiness schema missing | Rich results eligibility | Medium |
| M3 | Information disclosure headers (X-Powered-By, Link/wp-json) | Security hardening | Low |
| M4 | Cloudflare HTML caching not enabled | Performance | Medium |
| M5 | Audit JS rendering for event listings | Indexability assurance | Medium |

### Low (backlog)

| # | Issue | Impact | Effort |
|---|---|---|---|
| L1 | Crawl-delay: 10 throttling non-Google crawlers | Bing crawl rate | Low |
| L2 | AI crawler policy absent from robots.txt | Content rights | Low |
| L3 | English CPT base slugs (/venue/, /organizer/) | URL consistency | High effort — defer |
| L4 | www/non-www redirect verification | Canonicalisation | Low |

---

## Audit Notes

- Direct HTTP response verification (curl) was not available in this environment. Redirect behaviour (HTTP→HTTPS, non-www→www) is inferred from platform configuration (Cloudflare Universal SSL, WordPress Settings > General canonical URL). These should be independently verified with `curl -sIL http://mosskulturhus.no/`.
- Sitemap `lastmod` accuracy, individual page `noindex` status, and JS rendering behaviour require direct browser/tool inspection to fully validate.
- Core Web Vitals field data (CrUX) was not available. LCP risk is flagged based on 10 external scripts and uncached HTML responses. INP risk is flagged based on external script count. CLS risk is unknown without visual inspection.
- This audit covers the technical layer only. Content quality, backlink profile, and hreflang (Norwegian/multilingual considerations) are outside scope.
