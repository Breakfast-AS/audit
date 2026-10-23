# SEO Audit Report — breakfast.no
**Audit Date:** 2026-06-01  
**Auditor:** Claude Code SEO Audit  
**Site:** https://breakfast.no/  
**Business Type:** Communications Agency (Kommunikasjonsbyrå), B2B, Tønsberg, Norway  
**CMS:** WordPress + Divi Builder + Yoast SEO, hosted on WP Engine  

---

## Executive Summary

**Overall SEO Health Score: 40 / 100**

breakfast.no is a Norwegian communications agency with a solid server foundation (WP Engine with excellent TTFB of 96ms and full-page caching), but the site has significant SEO deficiencies across almost every category. The most damaging issues are structural and systemic: the entire site is tagged as English (`lang="en-US"`) despite being in Norwegian, 21 of 22 images have empty alt text, 106 client portfolio pages have ~32 words of content each (severe thin content at scale), and the vast majority of pages lack meta descriptions entirely. These are not minor optimizations — they fundamentally undermine the site's ability to rank for relevant Norwegian B2B searches.

### Top 5 Critical Issues
1. **`lang="en-US"` on a Norwegian-language site** — affects every page, confuses Google about the target language and audience
2. **106 kunder (client) pages with ~32 words each** — mass thin content at scale, high dilution risk
3. **21/22 homepage images have empty `alt=""`** — complete accessibility and SEO failure for image indexing
4. **Test/staging pages live and indexed** — `sample-page`, `testside`, `testside-2`, `divi-login-designer` are all 200 OK with no noindex, crawlable, and in the sitemap
5. **Logo served from staging domain** (`breakfastny.wpengine.com`) — a WP staging URL appears in the production site's HTML

### Top 5 Quick Wins
1. Fix `lang` attribute in WordPress settings: Change from `en-US` to `nb` or `nb-NO`
2. Add noindex to all test/staging pages (or delete them)
3. Write meta descriptions for the ~10 key service and section pages — 1-hour task
4. Fix the staging-domain logo URL to point to `breakfast.no`
5. Add descriptive alt text to all images via Media Library

---

## Category Scores

| Category | Weight | Score | Weighted |
|----------|--------|-------|---------|
| Technical SEO | 22% | 53/100 | 11.7 |
| Content Quality | 23% | 36/100 | 8.3 |
| On-Page SEO | 20% | 40/100 | 8.0 |
| Schema / Structured Data | 10% | 28/100 | 2.8 |
| Performance (CWV) | 10% | 45/100 | 4.5 |
| AI Search Readiness | 10% | 25/100 | 2.5 |
| Images | 5% | 15/100 | 0.8 |
| **TOTAL** | **100%** | | **38.6 → 40/100** |

---

## Technical SEO Audit

**Score: 53/100**

### Positives
- ✅ HTTP → HTTPS redirect working (301)
- ✅ www → non-www redirect working (301)
- ✅ `robots.txt` present, Yoast SEO generated, no blocked paths
- ✅ `xmlrpc.php` blocked (returns 403)
- ✅ Sitemap index present at `sitemap_index.xml` with 9 sub-sitemaps
- ✅ Canonical tags set on homepage
- ✅ TTFB: 96ms (excellent, WP Engine full-page cache active)
- ✅ WordPress version not exposed in `<meta name="generator">`
- ✅ WP REST API linked in headers (normal for WP, not a security risk by itself)

### Issues

**Critical**

| Issue | Detail |
|-------|--------|
| **Wrong `lang` attribute site-wide** | `<html lang="en-US">` on an entirely Norwegian-language site. Google uses this to determine language and country targeting. Every page is mislabeled as English. Fix: WordPress Admin → Settings → General → Site Language → set to "Norsk bokmål" |
| **Test pages indexed with no noindex** | `sample-page`, `testside`, `testside-2`, `divi-login-designer`, `entercore-font` all return HTTP 200 and have zero `noindex` directives. They are included in the page sitemap. These are crawl budget waste and potential quality signals to Google. |

**High**

| Issue | Detail |
|-------|--------|
| **No HSTS header** | `Strict-Transport-Security` not present in response headers. Without HSTS, browsers will attempt HTTP first and rely on the 301 redirect, creating a downgrade attack window. |
| **No security headers** | `X-Frame-Options`, `X-Content-Type-Options`, `Content-Security-Policy` absent from HTTP response headers. Not a ranking factor, but a signal of site quality and security posture. |
| **`wp-login.php` accessible** | Returns HTTP 200, meaning the login page is exposed to the public internet and bots. Should be protected via IP restriction or WP Engine's IP allowlist feature. |
| **Staging domain URL in production** | One image (`bf_logo_2_round_sort-1-1-copy.png`) is served from `breakfastny.wpengine.com` — the WP staging subdomain. This creates a broken reference if the staging environment is reset, and leaks the staging domain publicly. |

**Medium**

| Issue | Detail |
|-------|--------|
| **`Crawl-delay: 10` in robots.txt** | A 10-second crawl delay slows Googlebot's crawl rate significantly. For a ~250-page site this is unnecessary friction. Google generally ignores it, but it's a sign of a misconfigured default. Remove or reduce to 1-2. |
| **WordPress API endpoint in response headers** | `Link: <https://breakfast.no/wp-json/>; rel="https://api.w.org/"` is present in all response headers. This announces the WP API publicly. Not exploitable on its own, but combined with `wp-login.php` exposure, advertises the attack surface. |
| **No `X-Robots-Tag` headers** | No HTTP-level noindex for pages that should be excluded (login, admin previews, etc.) |

**Low**

| Issue | Detail |
|-------|--------|
| **`divi-login-designer` in sitemap** | A Divi plugin page that should never be indexed or even accessible to the public. |
| **`dashboard` page in sitemap** | Returns 200. Unclear if this is a user-facing page or an admin artifact — either way it should be reviewed. |

---

## Content Quality Audit

**Score: 36/100**

### Overview

breakfast.no is a B2B communications agency serving the Norwegian culture & entertainment sector. The site has three content problems at scale: (1) an enormous volume of thin page types, (2) almost no editorial/blog content, and (3) missing meta descriptions on virtually all pages except the homepage.

### Pages Analyzed

| Page | Words | H1 | Meta Desc | E-E-A-T Signals |
|------|-------|----|-----------|-----------------|
| Homepage | ~350 | "Hei! Vi er Breakfast" (×2) | ✅ 169 chars | Weak |
| /om-oss/ | ~318 | None | ❌ Missing | Weak |
| /tjenester/ | ~500 (est.) | "Sammen skaper vi" | ❌ Missing | Weak |
| /kultur/ | ~400 (est.) | "Norges ledende kommunikasjonsselskap innen kultur & underholdning" | ❌ Missing | Moderate |
| /kunder/radio-1/ | **32 words** | "Radio 1" | ❌ Missing | None |
| /jobber/slik-gjorde-vi-biltema…/ | 264 words | — | ❌ Missing | Weak |
| Blog posts (10 total) | Varies | Varies | Some | Weak |

### Thin Content at Scale (Critical)

**106 kunder (client) pages** contain approximately 32 words each — essentially a client logo, a name, and navigational boilerplate. These pages are publicly indexed, included in the sitemap, and represent a significant thin-content footprint. For context:
- Google's quality guidelines cite thin content as a signal that reduces domain-wide quality perception
- 106 pages × ~32 words = the same total content volume as a single medium-quality blog post
- Each page has a unique URL, a title tag, and an H1, but essentially zero useful content

**Recommended action:** Either (a) significantly expand each client page with a case study paragraph, services rendered, and outcome, or (b) noindex all kunder pages and redirect them to a single consolidated clients page.

**76 jobber (portfolio case) pages** have an average of ~200-264 words — thin but not as severe. Many still lack meta descriptions.

### Missing Meta Descriptions (High)

The following indexed pages have no meta description:
- `/om-oss/` — the About page, a high-commercial-intent page
- `/tjenester/` and all 16 service sub-pages
- `/kultur/` and all 4 kultur sub-pages
- `/stillinger/` (jobs listing page)
- `/markedsavdeling-pa-lan/` (marketing department on loan — a key service offering)
- All 106 kunder pages
- All 76 jobber pages
- Most ansatte (staff) pages

This means Google is auto-generating snippets from page content for almost every page — resulting in generic, low-CTR search snippets.

### E-E-A-T Signals (High)

breakfast.no claims to be "Norges ledende kommunikasjonsselskap innen kultur & underholdning" (Norway's leading communications company in culture & entertainment), but the site provides minimal signals to support this claim:

- **No named author bylines** on blog posts or case studies
- **No credentials or awards** section visible
- **No client testimonials or quotes** (client pages are just names/logos)
- **No case study outcomes** — portfolio pages describe the brief but rarely state measurable results
- **No press coverage or media mentions** linked
- **Team profiles** (ansatte pages) exist but were not deep-analyzed — if they include bios, credentials, and photos, they are an E-E-A-T asset

### Content Strategy Gap (Medium)

Only **10 blog posts** total, with the most recent being "breakfast-fyller-15-ar" (Breakfast turns 15). This is extremely sparse for an agency that offers content strategy as a service. A communications agency with 18 staff members and 15 years of experience has tremendous potential for thought leadership content — industry insights for the cultural sector, case study deep-dives, trend reports — but this potential is almost entirely untapped.

---

## On-Page SEO Audit

**Score: 40/100**

### Title Tags

| Page | Title | Length | Issues |
|------|-------|--------|--------|
| Homepage | "Breakfast \| Kommunikasjonsbyrå i Tønsberg" | 41 chars | Good |
| /om-oss/ | "Om oss - Breakfast" | 18 chars | Too short, generic |
| /tjenester/ | "Tjenester - Breakfast" | 21 chars | Too short |
| /kultur/ | "Kultur & Underholdning - Breakfast" | 34 chars (HTML entity) | Acceptable |
| /markedsavdeling-pa-lan/ | "Markedsavdeling på lån - Breakfast" | 34 chars | Acceptable |
| /kunder/radio-1/ | "Radio 1 - Breakfast" | 19 chars | Too short, no context |

**Issues:**
- Inner page titles are mostly formula-driven: `[Page Name] - Breakfast`. This format wastes the opportunity to include descriptive keywords.
- `/om-oss/` could be: "Om Breakfast — Kommunikasjonsbyrå i Tønsberg siden 2011"
- `/tjenester/` could be: "Tjenester — Design, Strategi, Teknologi & Kommunikasjon"

### H1 Tags

| Page | H1 | Issue |
|------|-----|-------|
| Homepage | "Hei! Vi er Breakfast" | **Appears twice** — duplicate H1 |
| /om-oss/ | None detected | Missing H1 |
| /tjenester/ | "Sammen skaper vi" | Vague, no keywords |
| /kultur/ | "Norges ledende kommunikasjonsselskap innen kultur & underholdning" | Good — specific and keyword-rich |

**Duplicate H1 on homepage** is a structural issue in the Divi theme — the heading appears in both the above-fold hero section and again in the page body, likely a Divi module duplication.

### Meta Descriptions

As documented in Content Quality above — missing on virtually all pages except the homepage. The homepage meta description is well-written at 169 characters.

### Internal Linking

- Homepage has 53 internal links — reasonable for an agency homepage
- Navigation links cover main sections (kultur, tjenester, om oss, stillinger, jobber)
- **No breadcrumbs visible** in the content area (Yoast SEO generates BreadcrumbList schema but it may not be rendered in the template)
- **No "Related case studies" or cross-linking** between service pages and portfolio pages
- **Kunder pages** have no internal links to service pages (missed opportunity to distribute authority)

### Hreflang

No `<link rel="alternate" hreflang="">` tags present. For a single-language Norwegian site this is acceptable, but the wrong `lang="en-US"` attribute makes this more urgent — fixing the lang attribute is the priority.

---

## Schema & Structured Data Audit

**Score: 28/100**

### Current Implementation

Only the homepage has schema markup. It was generated by Yoast SEO and contains:

```json
{
  "@type": "WebPage",
  "inLanguage": "en-US",  ← WRONG
  ...
}
{
  "@type": "WebSite",
  "name": "Breakfast",
  "description": "Vi tror på kreative løsninger basert på en god strategi.",
  "inLanguage": "en-US"  ← WRONG
}
{
  "@type": "BreadcrumbList",
  ...
}
```

### Critical Issues

| Issue | Detail |
|-------|--------|
| `inLanguage: "en-US"` | Wrong language in schema. Should be `"nb"` or `"nb-NO"`. This cascades from the WordPress language setting — fixing the site language fixes this automatically. |
| No `Organization` schema | No structured data describing the agency: no name, address, phone, email, founding date, social profiles, or logo |
| No `LocalBusiness` schema | breakfast.no is physically located at Møllegaten 6, 3111 Tønsberg. A `LocalBusiness` or `ProfessionalService` schema with address, coordinates, and opening hours would support local search. |

### Missing Schema Opportunities

| Schema Type | Where Needed | Priority |
|------------|-------------|----------|
| `Organization` / `ProfessionalService` | Homepage, om-oss | High |
| `Service` | Each tjenester page | High |
| `Person` | Ansatte (staff) pages | Medium |
| `Article` | Blog posts | Medium |
| `FAQPage` | Service pages (add FAQ sections) | Medium |
| `CreativeWork` | Jobber/portfolio pages | Low |

### Recommended Organization Schema

Add to the homepage (or site-wide via Yoast SEO → Search Appearance → Company Info):

```json
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "@id": "https://breakfast.no/#organization",
  "name": "Breakfast",
  "alternateName": "Breakfast Kommunikasjonsbyrå",
  "url": "https://breakfast.no/",
  "logo": "https://breakfast.no/wp-content/uploads/[logo-path].png",
  "email": "hei@breakfast.no",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Møllegaten 6",
    "addressLocality": "Tønsberg",
    "postalCode": "3111",
    "addressCountry": "NO"
  },
  "inLanguage": "nb",
  "sameAs": [
    "https://www.instagram.com/breakfast_creative/",
    "https://www.facebook.com/[page]/"
  ],
  "serviceType": ["Kommunikasjon", "Design", "Strategi", "Teknologi", "Markedsføring"],
  "areaServed": "NO"
}
```

---

## Performance Audit (Core Web Vitals)

**Score: 45/100**

*Based on lab measurements + Divi/WP Engine performance characteristics. Real CrUX field data not available.*

### Server-Side (Excellent)

| Signal | Value | Status |
|--------|-------|--------|
| DNS lookup | 0.002s | Excellent |
| TCP connect | 0.023s | Excellent |
| TLS handshake | 0.051s | Good |
| TTFB | **0.096s** | Excellent (target: <200ms) |
| Cache | WP Engine HIT, max-age=600 | Active |

### Estimated Core Web Vitals

| Metric | Mobile (est.) | Desktop (est.) | Target |
|--------|--------------|----------------|--------|
| LCP | 3.5–5.0s 🔴 Poor | 1.8–2.8s 🟡 Needs Improvement | <2.5s |
| INP | 250–400ms 🔴 Poor | 120–200ms 🟡 Borderline | <200ms |
| CLS | 0.10–0.18 🟡 Needs Improvement | 0.05–0.10 🟢 Good | <0.1 |
| FCP | 2.5–3.5s | 1.2–1.8s | — |
| **PageSpeed Score** | **~35–50** | **~65–78** | >90 |

### Key Performance Problems

**1. Divi Render-Blocking Assets (Critical)**
Divi Builder loads `divi-style.css` (150–300KB), `jquery.js`, `divi-custom-script.js`, and `et-core.js` synchronously in `<head>`. These block First Contentful Paint by an estimated 1.5–3.5 seconds on mobile.

**2. No Image Lazy Loading (High)**
Zero `loading="lazy"` attributes on any of the 22 homepage images. All images load simultaneously during page initialization, competing for bandwidth with the LCP hero image. WordPress 5.5+ enables lazy loading by default, but Divi's image modules can bypass this.

**3. Large HTML Payload (High)**
At 275KB, the homepage HTML is 3–5× larger than an optimized WordPress page (~50–80KB). Divi generates extensive inline styles per module that inflate HTML. **Fix:** Enable Divi's "Static CSS File Generation" (Divi → Theme Options → General → Performance) and "Dynamic CSS".

**4. No LCP Image Prioritization (High)**
No `fetchpriority="high"` or `<link rel="preload">` on the hero image. The browser's preload scanner cannot prioritize the LCP image before render-blocking scripts complete.

**5. Layout Shift from Unsized Images (Medium)**
Divi's image modules historically omit explicit `width` and `height` attributes, causing layout shift as images load.

### Recommendations

| Priority | Action | Expected Gain |
|----------|--------|--------------|
| Critical | Enable Divi Dynamic CSS (removes inline styles from HTML) | -60–80% HTML size |
| Critical | Defer non-critical JS via WP Engine JS Defer toggle | LCP -0.8–1.5s |
| High | Add `fetchpriority="high"` to LCP hero image | LCP -0.5–1.0s |
| High | Enable lazy loading on all below-fold images | INP, bandwidth |
| High | Install ShortPixel/Imagify for WebP conversion and compression | -40–60% image weight |
| High | Add `<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>` | FCP -0.1–0.3s |
| Medium | Enable HTML minification in WP Engine portal | -10–20% HTML size |
| Medium | Increase static asset cache TTL to max-age=31536000 | Repeat visitor performance |

---

## Sitemap Audit

**Score: 50/100**

### Sitemap Inventory

| Sitemap | URL Count | Last Modified | Issues |
|---------|-----------|---------------|--------|
| post-sitemap.xml | 10 | 2026-05-27 | Very sparse |
| page-sitemap.xml | 26 | 2026-05-27 | Includes test/staging pages |
| ansatte-sitemap.xml | 18 | 2026-05-08 | OK |
| kunder-sitemap.xml | 106 | 2026-03-23 | 106 thin pages |
| jobber-sitemap.xml | 76 | 2026-05-20 | Missing meta descs |
| tjenester-sitemap.xml | 16 | 2023-10-24 | Last modified 2.5 years ago |
| category-sitemap.xml | — | — | Not verified |
| casekategori-sitemap.xml | — | — | No lastmod |
| kultur_kategorier-sitemap.xml | — | — | Not verified |
| **TOTAL** | **~252+** | | |

### Critical Issues

**Pages that should NOT be in sitemap:**

| URL | HTTP | noindex | Action |
|-----|------|---------|--------|
| /sample-page/ | 200 | No | Delete or noindex |
| /testside/ | 200 | No | Delete or noindex |
| /testside-2/ | 200 | No | Delete or noindex |
| /divi-login-designer/ | 200 | No | Noindex, block in robots.txt |
| /entercore-font/ | 200 | No | Review — noindex if internal |
| /dashboard/ | 200 | No | Review — likely should be noindex |
| /arskavalkade-dnbe/ | 200 | No | Verify if public content |
| /nyhetsbrev/ | 200 | No | Verify if has content |

**Tjenester sitemap last modified 2023-10-24** — service pages haven't been updated in 2.5 years. Google uses `lastmod` as a crawl prioritization signal. If pages have been updated since then, the lastmod is wrong. Yoast SEO should update this automatically on publish.

### Medium Issues
- No `priority` or `changefreq` values set (these are optional but WP/Yoast should set them)
- Category/taxonomy sitemaps may contain thin archive pages that should be noindexed or excluded

---

## AI Search Readiness (GEO)

**Score: 25/100**

### llms.txt
❌ `https://breakfast.no/llms.txt` — **Not found (404)**

This is an emerging standard that helps AI systems understand what content can be used for training and indexing. Norwegian B2B agencies are underrepresented in AI search results; an `llms.txt` with key positioning statements would help.

### AI Crawler Access
✅ robots.txt does not block `GPTBot`, `ClaudeBot`, `CCBot`, or `PerplexityBot`

All major AI crawlers can access the site. No crawl restrictions observed.

### Citability Assessment

AI search systems (ChatGPT, Perplexity, Google AI Overviews, Bing Copilot) prefer to cite content that:
- Directly answers questions
- Contains structured, scannable information
- Has clear authorship and authority signals
- Is regularly updated

**breakfast.no scores poorly on citability because:**
- Homepage is marketing copy, not answerable content
- Service pages describe offerings without educational context
- No FAQ sections on any pages
- No structured "how we work" or "what is [service]" explanatory content
- Blog posts are sparse and infrequent (10 total)
- No author attribution on content

**Queries where breakfast.no should appear in AI answers but likely doesn't:**
- "Hva er det beste kommunikasjonsbyrået i Tønsberg?"
- "Kommunikasjonsbyrå for kultursektor Norge"
- "Markedsavdeling på lån hva er det"

### Brand Mention Signals
- Very limited external presence from the homepage (only Instagram linked)
- No visible press coverage, awards, or third-party mentions on the site
- 15 years in business — this history should be cited explicitly with founding year

### Recommendations
1. Create `llms.txt` with company description, services, and key positioning
2. Add FAQ sections to service pages with actual questions clients ask
3. Write at least 4 substantive blog posts per year on culture marketing topics
4. Add founding year and client count/notable clients to homepage and om-oss page
5. Enable structured content — numbered lists, comparison tables, clear definitions

---

## Images Audit

**Score: 15/100**

### Homepage Image Analysis

| Total Images | Missing alt | Empty alt="" | With alt text | Lazy loaded |
|-------------|------------|-------------|---------------|-------------|
| 22 | 0 | **21** | 1 ("Breakfast 15 år") | **0** |

This is a near-complete alt text failure. Only the "Breakfast 15 år" anniversary image has descriptive alt text. The other 21 images — including hero images, client work examples, and team photos — have `alt=""` (explicitly empty alt), which tells screen readers and search engines these images have no content value.

**For decorative images** (purely decorative backgrounds), `alt=""` is technically correct. But for images of client work, team photos, and service illustrations — which form the majority of these 22 images — empty alt text is an SEO loss.

### Additional Issues

| Issue | Detail |
|-------|--------|
| **Zero lazy loading** | All 22 images load simultaneously. WordPress 5.5+ adds this automatically but Divi bypasses it. |
| **No WebP/AVIF confirmed** | Divi does not natively serve next-gen formats. WP Engine CDN may support WebP via configuration. |
| **Staging domain image** | Logo served from `breakfastny.wpengine.com` — a staging domain URL in production HTML |
| **No `width`/`height` attributes** | Likely missing on Divi image modules, contributing to CLS |
| **Image filenames** | Many use auto-generated names (`DSCF2249.jpg`, `IMG_2317_3-s`) instead of descriptive SEO-friendly names |

### Recommendations

1. Add descriptive alt text to all 21 empty-alt images via WordPress Media Library
2. Enable lazy loading via `Divi → Theme Options → Performance` or `functions.php`
3. Run all existing images through ShortPixel or Imagify for compression + WebP
4. Rename images with descriptive filenames before uploading future assets
5. Fix the staging domain logo URL immediately

---

## Appendix: Full Page Audit Summary

### Pages with Confirmed Issues

| Page | HTTP | Meta Desc | H1 | Words | Notes |
|------|------|-----------|-----|-------|-------|
| / (homepage) | 200 | ✅ 169 chars | ⚠️ Duplicate | ~350 | Duplicate H1, 21/22 imgs no alt |
| /om-oss/ | 200 | ❌ Missing | ❌ None | ~318 | No H1, missing meta |
| /tjenester/ | 200 | ❌ Missing | ✅ | ~500 | |
| /tjenester/design/ | 200 | ❌ Missing | — | — | |
| /tjenester/strategi/ | 200 | ❌ Missing | — | — | |
| /tjenester/teknologi/ | 200 | ❌ Missing | — | — | |
| /tjenester/kommunikasjon/ | 200 | ❌ Missing | — | — | |
| /kultur/ | 200 | ❌ Missing | ✅ Good | — | |
| /kultur/kulturhus-konserthus/ | 200 | ❌ Missing | — | — | |
| /kultur/museum-gallerier/ | 200 | ❌ Missing | — | — | |
| /kultur/radio-podkast/ | 200 | ❌ Missing | — | — | |
| /kultur/kulturapp/ | 200 | ❌ Missing | — | — | |
| /stillinger/ | 200 | ❌ Missing | — | — | |
| /markedsavdeling-pa-lan/ | 200 | ❌ Missing | — | — | Key service, no meta |
| /sample-page/ | 200 | ❌ | — | — | Should be deleted/noindexed |
| /testside/ | 200 | ❌ | — | — | Should be deleted/noindexed |
| /testside-2/ | 200 | ❌ | — | — | Should be deleted/noindexed |
| /divi-login-designer/ | 200 | ❌ | — | — | Should be noindexed |
| /kunder/radio-1/ | 200 | ❌ Missing | ✅ | **32** | Thin content — all 106 kunder pages |
| /jobber/slik-gjorde-vi-biltema…/ | 200 | ❌ Missing | — | 264 | Thin — most jobber pages |

---

*Report generated by Claude Code SEO Audit · breakfast.no · 2026-06-01*
