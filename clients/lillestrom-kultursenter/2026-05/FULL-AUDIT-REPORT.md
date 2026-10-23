# SEO Full Audit Report — Lillestrøm Kultursenter
**URL:** https://www.lillestrom-kultursenter.no/
**Audit date:** 2026-05-29
**Business type:** Brick-and-mortar performing arts venue (PerformingArtsTheater)
**Location:** Kirkegata 11, 2000 Lillestrøm, Norway
**Platform:** WordPress + Yoast SEO | WP Engine + Cloudflare CDN
**Language:** Norwegian (nb-NO)

---

## SEO Health Score: 46 / 100

| Category | Weight | Score | Weighted |
|---|---|---|---|
| Technical SEO | 22% | 52/100 | 11.4 |
| Content Quality | 23% | 48/100 | 11.0 |
| On-Page SEO | 20% | 35/100 | 7.0 |
| Schema / Structured Data | 10% | 30/100 | 3.0 |
| Performance (CWV) | 10% | 55/100 | 5.5 |
| AI Search Readiness | 10% | 44/100 | 4.4 |
| Images | 5% | 65/100 | 3.3 |
| **Overall** | **100%** | | **46 / 100** |

> **Interpretation:** The site has solid technical foundations (HTTPS, fast TTFB, Cloudflare CDN, Yoast SEO installed) but is held back by pervasive on-page gaps — missing meta descriptions across 356+ pages, no H1 on the homepage, broken Event schema, and a complete absence of Organization/LocalBusiness markup. Most critical issues are fixable without a developer in under a day.

---

## Executive Summary

### Business Context

Lillestrøm Kultursenter is a municipal cultural venue in Lillestrøm (Akershus), founded 1991, operating 338+ events per year across 12 halls. The site is built on WordPress with Yoast SEO and served via WP Engine + Cloudflare. The domain (`lillestrom-kultursenter.no`) contains the primary target keyword and the site has a strong structural base. Despite this, the site scores in the **"Poor"** range due to systemic on-page neglect, security exposures, and missing schema infrastructure.

### Top 5 Critical Issues

1. **Missing H1 on homepage** — the most visited page on the site has no primary heading, eliminating its targeting signal for the most important keyword cluster.
2. **Meta descriptions absent on 356+ pages** — every event page (338), hall page (12), and most static pages return no meta description. Google auto-generates low-quality snippets, depressing CTR site-wide.
3. **Internal board documents publicly indexed** — 8 `/internt/` and `/ansatt/` pages (including board meeting documents and quarterly financial reports) are indexed with `meta robots: index, follow`. One "protected" page (`/internt/beskyttet-underside/`) is fully public despite its name.
4. **Event schema has empty address fields** — `streetAddress`, `addressLocality`, and `postalCode` are blank strings in all 338 Event schema blocks. Google cannot display Event rich results without a valid location.
5. **No Organization/LocalBusiness schema** — the homepage has no structured entity data. Google has no schema signal for the venue's name, address, phone, or coordinates — critical for local pack eligibility and Knowledge Panel.

### Top 5 Quick Wins

1. **Add H1 to homepage** (30 minutes, no developer needed) — `Lillestrøm Kultursenter – konserter, teater og opplevelser i Lillestrøm`
2. **Noindex /internt/* pages** (10 minutes in Yoast) — stop indexing board documents and internal planning files
3. **Set Yoast meta description templates** (20 minutes) — fix all 338 event pages at once with a dynamic template
4. **Enable IndexNow in Yoast** (5 minutes) — Yoast Integrations > IndexNow — instant re-indexation signals for all future edits
5. **Delete /smittevern/ + 301 redirect** (15 minutes) — remove the 2022 COVID page still indexed in 2026

---

## Detailed Findings

### 1. Technical SEO — 52/100

**Full report:** `technical-seo.md`

#### Crawlability

| Signal | Status |
|---|---|
| HTTPS deployed | PASS |
| HTTP → HTTPS redirect | PASS (301) |
| non-www → www redirect | PASS (301) |
| Canonical tags | PASS — self-referencing on all checked pages |
| robots.txt accessible | PASS |
| Sitemap index accessible | PASS |
| xmlrpc.php blocked | PASS (405) |

#### Crawlability Issues

- **robots.txt has two conflicting `User-agent: *` blocks** — the first has `Crawl-delay: 10` and a Disallow; the second (Yoast-generated) has an empty Disallow. Undefined crawler behavior. Fix by merging to a single block.
- **Crawl-delay: 10 applied to all bots** — limits AI crawlers to 6 pages/minute; add named entries with `Crawl-delay: 2` for GPTBot, ClaudeBot, PerplexityBot, Google-Extended.

#### Indexability Issues

- **8 internal/staff pages indexed** — `/internt/styredokumenter/`, `/internt/handlingsplan/`, `/internt/arsberetninger/`, `/internt/div-planverk/`, `/internt/beskyttet-underside/`, `/ansatt/tilbud-fra-vare-samarbeidspartnere/`, `/ansatt/handlingsplan/`, `/ansatt/mal-og-strategi/`
- **2 test pages indexed** — `/nyhetsbrev-test/` (2022), `/for-og-etter-test/` (2025)
- **Outdated COVID page indexed** — `/smittevern/` last modified 2022-02-12

#### Security

- **No security headers** — HSTS, X-Frame-Options, X-Content-Type-Options, CSP, Permissions-Policy all absent
- **WP Engine stack exposed** — `x-powered-by: WP Engine` header
- **WordPress REST API exposes staff usernames** — `/wp-json/wp/v2/users` returns full account list including login slugs (`breakfast`, `annemerete`, `camilla`)
- **Page IDs exposed in every `<head>`** via `<link rel="alternate" href="/wp-json/wp/v2/pages/1069">`

#### Infrastructure Positives

- Server response time: 75–120ms (excellent)
- HTML sizes: 52–142 KB (reasonable)
- Cloudflare CDN active with cache hits confirmed
- HTML `lang="nb-NO"` and `og:locale="nb_NO"` correctly set
- `<meta name="viewport">` present (though `user-scalable=no` needs removing)

---

### 2. Content Quality — 48/100

**Full report:** `content-seo.md`

#### E-E-A-T Assessment

| Signal | Score | Issue |
|---|---|---|
| Experience | 30/100 | No visitor testimonials, no editorial voice, 17 blog posts for 338 active events |
| Expertise | 45/100 | No author bios, no bylines on blog posts, templated event copy |
| Authoritativeness | 40/100 | No press section, no links to/from Kulturrådet or Lillestrøm kommune |
| Trustworthiness | 52/100 | Indexed internal pages, test pages, stale COVID content |

#### Content Gaps

- **Homepage body text under 400 words** — mostly event titles and navigation labels
- **No testimonials or audience quotes** anywhere on the site
- **No visible "Sist oppdatert" timestamps** on static pages
- **Blog publishing rate: 17 posts total** — severely under-invested for an active venue
- **No seasonal programme landing pages** — e.g., `/program/host-2026/`

---

### 3. On-Page SEO — 35/100

#### Meta Descriptions

| Page type | Count | Has Meta Description |
|---|---|---|
| Homepage | 1 | YES |
| Core static pages (program, utleie, om-oss, kontakt, etc.) | ~15 | NO |
| Event pages | 338 | NO |
| Hall pages | 12 | NO |
| **Total missing** | **365+** | |

#### Title Tags

- Pattern: `[Page Name] - Lillestrøm Kultursenter`
- Issue: Page names contain no keywords (e.g., "Om oss", "Utleie", "Kontakt oss")
- Homepage title is a slogan, not keyword-driven: "Du kan bare begynne å glede deg!"

#### Heading Structure

| Page | H1 | H2 Count | Issue |
|---|---|---|---|
| Homepage | MISSING | 9 | H2s are all event titles — no venue description |
| /om-oss/ | "Om oss" | — | Generic — no keywords |
| /program/ | "Program" | — | Generic |
| /utleie/ | "Utleie" | — | Generic |
| Event pages | Event name | Multiple | Good |
| Hall pages | Hall name | Multiple | Good |

#### Internal Linking

- No deliberate hub-and-spoke architecture
- No category landing pages linking to related events/halls
- Navigation-driven linking only

---

### 4. Schema / Structured Data — 30/100

**Full report:** `schema-seo.md`

#### Current Schema Inventory

| Page type | Schema types present |
|---|---|
| Homepage | WebPage, BreadcrumbList, WebSite (Yoast @graph) |
| Event pages | WebPage, BreadcrumbList, WebSite + standalone Event |
| Hall pages | WebPage, ImageObject, BreadcrumbList, WebSite |

#### Critical Schema Failures

| Issue | Impact |
|---|---|
| No Organization/PerformingArtsTheater on homepage | Blocks Knowledge Panel, local pack eligibility |
| Event schema `streetAddress`, `addressLocality`, `postalCode` are empty strings | Google will not display Event rich results |
| Event schema missing `offers` | Ticket CTAs cannot appear in Event SERP features |
| Event schema missing `organizer` | Required for Google Events experience |
| Some events have `datePublished: "-0001-11-30T00:00:00+00:00"` | Invalid date suppresses rich results |
| WebSite schema `description` is empty string `""` | Broken schema output |

#### Recommended Action

Add a standalone `<script type="application/ld+json">` block to the homepage (via WPCode or `wp_head` hook) with `@type: ["Organization", "PerformingArtsTheater"]` — see `schema-seo.md` for complete JSON-LD. Fix Event schema address fields in the PIM/Ambio integration plugin settings.

---

### 5. Performance / Core Web Vitals — 55/100

**Full report:** `performance-seo.md`

#### Measured Signals

| Metric | Homepage | /program/ | /utleie/ |
|---|---|---|---|
| TTFB | 110ms (Excellent) | 75ms (Excellent) | 120ms (Excellent) |
| HTML size | 72.9 KB | 141.6 KB | 51.7 KB |
| Render-blocking JS | 11 scripts | 11 scripts | 11 scripts |
| Async/defer JS | 0 | 0 | 0 |
| Images with lazy loading | 0 of 6 | 0 of 3 | 0 of 3 |
| Preload hints | 0 | 0 | 0 |

#### Estimated CWV Impact

| Metric | Estimated | Target | Primary Fix |
|---|---|---|---|
| LCP | ~3.0–4.5s (Poor) | < 2.5s | Add `fetchpriority="high"` to hero image + defer all JS |
| INP | ~200–350ms (Needs Improvement) | < 200ms | Reduce JS parse/execute time |
| CLS | ~0.1–0.2 (Needs Improvement) | < 0.1 | Add explicit `width`/`height` to all `<img>` tags |

#### Issues

1. **All 11 JS files render-blocking** — none use `async` or `defer`
2. **No lazy loading on any images** — all images load on initialization
3. **No `fetchpriority="high"` on LCP candidate**
4. **No preload hints** for critical CSS or images
5. **No explicit image dimensions** — CLS risk on every page
6. **/program/ page is 141.6 KB HTML** — needs pagination
7. **Event images from third-party storage.googleapis.com** — extra DNS/TCP overhead
8. **Moment.js loaded twice** — duplicate ~72 KB library
9. **Cache TTL only 10 minutes** — unnecessarily low for static pages
10. **`user-scalable=no` in viewport** — WCAG violation + Google mobile usability flag

---

### 6. AI Search Readiness — 44/100

**Full report:** `geo-ai-seo.md`

| Finding | Status |
|---|---|
| All major AI crawlers allowed | PASS |
| llms.txt present | FAIL |
| Crawl-delay optimized for AI bots | FAIL |
| Organization schema (entity recognition) | FAIL |
| Event schema present | PASS |
| FAQPage schema | FAIL |
| Citation-ready prose on Om oss | FAIL |
| Norwegian Wikipedia entity exists | PASS |
| Question-format headings | FAIL |
| Author bylines on blog posts | FAIL |

**Norwegian Wikipedia article exists** for Lillestrøm Kultursenter — this is the strongest existing AI authority signal. Adding `sameAs: "https://no.wikipedia.org/wiki/Lillestrøm_Kultursenter"` to the Organization schema connects the site entity to this knowledge graph node.

---

### 7. Images — 65/100

| Finding | Status |
|---|---|
| Homepage images — alt text | PASS (6/6) |
| Hall pages — alt text | PARTIAL (some missing) |
| Event images — alt text | PASS (served with alt from PIM) |
| WebP format on homepage | PARTIAL (3/6 images) |
| WebP on event/hall pages | FAIL (JPG/PNG only) |
| Explicit dimensions | FAIL — none observed |
| Lazy loading | FAIL — none observed |
| Oversized images | Unknown (third-party PIM) |

---

### 8. Local SEO — 38/100

**Full report:** `local-seo.md`

| Dimension | Score |
|---|---|
| GBP Signals | 20/100 |
| Reviews & Reputation | 25/100 |
| Local On-Page SEO | 55/100 |
| NAP Consistency & Citations | 50/100 |
| Local Schema Markup | 5/100 |
| Local Link & Authority Signals | 90/100 |

**NAP found on site:** Kirkegata 11, 2000 Lillestrøm / Tlf: 64 84 55 50 (consistent across all pages)

**Key local issues:**
- No Google Maps embed on contact/praktisk-informasjon pages
- No LocalBusiness/PerformingArtsTheater schema anywhere
- Phone number lacks E.164 format (`+47 64 84 55 50`)
- TripAdvisor listing not found (404 — venue appears unlisted)
- No review acquisition strategy evident
- GBP optimization status unknown (unauthenticated)

---

### 9. Sitemap — Score: Issues Found

**Full report:** `sitemap-seo.md`

- Total URLs: 585 across 14 sitemaps
- Format: Valid XML, well within 50,000 URL limit
- **8 internal pages in sitemap** (indexed with `index, follow`)
- **2 test pages in sitemap** (`/nyhetsbrev-test/`, `/for-og-etter-test/`)
- **Author sitemap exposes 3 WordPress login usernames**
- **19 event_promoter entries have invalid `lastmod: -0001-11-30`**
- **7 low-value taxonomy sitemaps** wasting crawl budget (single entries, catch-all archives)

---

## Site Structure Summary

```
www.lillestrom-kultursenter.no
├── / (Homepage)                   H1: MISSING | Meta: YES | Schema: WebPage only
├── /program/                      H1: YES | Meta: NO | Events: 338
│   └── /program/[id]-[slug]/      H1: YES | Meta: NO | Schema: Event (broken addr)
├── /hall/                         12 venue pages
│   └── /hall/[hall-name]/         H1: YES | Meta: NO | Schema: WebPage only
├── /utleie/                       H1: YES | Meta: NO
├── /om-oss/                       H1: YES | Meta: NO
├── /kontakt-oss/                  H1: YES | Meta: NO | NAP: YES
├── /artikler/                     17 posts | No authors | No dates shown
├── /internt/                      INDEXED — should be noindex (8 pages)
└── /ansatt/                       INDEXED — should be noindex (3 pages)
```

---

## Technology Stack

| Component | Technology | Notes |
|---|---|---|
| CMS | WordPress | Standard install |
| SEO Plugin | Yoast SEO | Premium features in use |
| Hosting | WP Engine | x-powered-by header exposed |
| CDN | Cloudflare | Cache HIT confirmed |
| Event System | Ambio PIM | External events management system |
| Calendar Plugin | dx-calendar | Loaded globally |
| GDPR | Complianz GDPR Premium | Active |
| Analytics | Google Tag Manager | `googletagmanager` confirmed in HTML |
| Images CDN | None (third-party GCS) | Event images from storage.googleapis.com |
| Caching | WP Engine (max-age=600) | Only 10 min TTL |

---

## Appendix: Page Index by Type

| Type | Count | Key Issues |
|---|---|---|
| Events (/program/) | 338 | No meta desc, Event schema broken |
| Static pages | 36 | No meta desc on most, internal pages indexed |
| Hall pages | 12 | No meta desc, some alt text missing |
| Blog posts | 17 | No author display, no pub dates shown |
| Promoter archives | 127 | Thin content, invalid lastmod on 19 |
| Hall taxonomy | 22 | Overlaps with /hall/ pages |
| Author archives | 3 | Exposes login usernames |
| Event categories | 21 | Marginal value |

**Total indexed URLs: ~585+**
