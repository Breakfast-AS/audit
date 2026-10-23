# Sitemap Audit — Lillestrøm Kultursenter

**Audit date:** 2026-05-29 | **Generator:** Yoast SEO (WordPress)
**Total URLs:** 585 across 14 sitemaps

---

## Validation Checks

| Check | Result | Detail |
|---|---|---|
| Valid XML format | PASS | All 14 sitemaps parse correctly |
| Sitemap index format | PASS | Well-formed |
| 50,000 URL limit | PASS | Largest file: event-sitemap.xml at 338 URLs |
| Total URL count | PASS | 585 total — well within limits |
| HTTPS on all URLs | PASS | |
| `priority` / `changefreq` tags | INFO | Not present — correct, Google ignores both |
| `lastmod` accuracy | WARN | 19 entries in event_promoter-sitemap.xml have `lastmod: -0001-11-30` (PHP epoch zero) |
| Noindex on sitemap URLs | FAIL | 10 pages are `index, follow` but should be excluded |
| Password-protected page | FAIL | `/internt/beskyttet-underside/` returns HTTP 200 — not actually protected |
| Test pages in sitemap | FAIL | 2 test pages publicly indexed |
| Author sitemap exposes usernames | FAIL | 3 WordPress login usernames exposed |
| Stale content | WARN | `/smittevern/` last modified 2022-02-12 |

---

## Sitemap Inventory

| Sitemap | URLs | Assessment |
|---|---|---|
| post-sitemap.xml | 17 | OK |
| page-sitemap.xml | 36 | ISSUES — internal/test pages present |
| event-sitemap.xml | 338 | OK — core value sitemap |
| hall-sitemap.xml | 12 | OK — unique venue pages with images |
| sponsor-sitemap.xml | 1 | Low value — single entry |
| category-sitemap.xml | 1 | Remove — "Uncategorized" only |
| post_tag-sitemap.xml | 2 | Low value |
| event_promoter-sitemap.xml | 127 | Review — 19 invalid dates, thin content risk |
| event_category-sitemap.xml | 21 | Marginal |
| event_hall-sitemap.xml | 22 | Review — partial overlap with hall-sitemap.xml |
| event_venue-sitemap.xml | 2 | Low value |
| event_type-sitemap.xml | 1 | Remove — `/event_type/event/` has no SEO purpose |
| sponsor_category-sitemap.xml | 2 | Low value |
| author-sitemap.xml | 3 | Security issue — disable |

---

## Critical Issues

### 1. Internal and staff pages are publicly indexed (HIGH)

All pages below return HTTP 200 and have `meta robots: index, follow`:

| URL | Description | Last modified |
|---|---|---|
| `/internt/styredokumenter/` | Board documents | 2023-08-28 |
| `/internt/handlingsplan/` | Internal action plan | 2024-01-16 |
| `/internt/arsberetninger/` | Annual reports | 2024-07-03 |
| `/internt/div-planverk/` | Internal plans | 2024-07-03 |
| `/internt/beskyttet-underside/` | Quarterly reports ("Tertialrapporter") — NOT actually password protected | 2025-06-27 |
| `/ansatt/tilbud-fra-vare-samarbeidspartnere/` | Staff partner offers | 2023-09-29 |
| `/ansatt/handlingsplan/` | Staff action plan | 2024-01-16 |
| `/ansatt/mal-og-strategi/` | Staff goals & strategy | 2024-06-27 |

**Fix:** Set each to `noindex` in Yoast SEO > Advanced tab. Yoast auto-removes them from the sitemap on next regeneration.

---

### 2. Test pages are indexed (HIGH)

| URL | Title | Last modified |
|---|---|---|
| `/nyhetsbrev-test/` | nyhetsbrev-test | 2022-09-26 |
| `/for-og-etter-test/` | Før og etter – test | 2025-11-25 |

Both return HTTP 200 with `index, follow`. Set noindex immediately; delete if no longer needed.

---

### 3. Author sitemap exposes WordPress login usernames (MEDIUM)

`author-sitemap.xml` lists author archive URLs revealing exact login usernames: `breakfast`, `annemerete`, `camilla`. This removes the username-discovery step from a brute-force attack.

**Fix:** Yoast SEO > Search Appearance > Archives > Author archives > set to No.

---

## Warnings

### 4. COVID/smittevern page is outdated (MEDIUM)

`/smittevern/` — last modified 2022-02-12. Content references the February 2022 removal of COVID restrictions. Entirely irrelevant in 2026.

**Fix:** Delete the page and 301 redirect to `/praktisk-informasjon/`.

---

### 5. Invalid lastmod dates in event_promoter-sitemap.xml (LOW)

19 of 127 promoter pages have `lastmod: -0001-11-30T00:00:00+00:00` — a PHP/MySQL epoch-zero value. These are empty archive pages for taxonomy terms with no published events.

**Fix:** Evaluate whether event_promoter taxonomy warrants indexing. If not, set to noindex in Yoast > Search Appearance > Taxonomies.

---

### 6. Low-value single-entry sitemaps consuming crawl budget (LOW)

| Sitemap | URLs | Issue |
|---|---|---|
| event_type-sitemap.xml | 1 | Duplicates /program/ |
| category-sitemap.xml | 1 | WordPress "Uncategorized" default |
| post_tag-sitemap.xml | 2 | No content value |
| event_venue-sitemap.xml | 2 | Thin taxonomy archives |
| sponsor_category-sitemap.xml | 2 | Low value |
| sponsor-sitemap.xml | 1 | Single sponsor entry |

**Fix:** Disable all in Yoast > Search Appearance > Taxonomies.

---

## Structural Note: Duplicate Venue Taxonomy

`hall-sitemap.xml` (12 URLs at `/hall/`) and `event_hall-sitemap.xml` (22 URLs at `/scene/`) both map to physical rooms. Several names appear in both. Architecturally acceptable if canonical tags are set correctly — verify there is no competing duplicate issue.

---

## Priority Action List

1. **Immediate** — Noindex all 8 `/internt/` and `/ansatt/` pages in Yoast.
2. **Immediate** — Fix `/internt/beskyttet-underside/`: restore password protection or noindex properly.
3. **Immediate** — Noindex and delete `/nyhetsbrev-test/` and `/for-og-etter-test/`.
4. **Short-term** — Disable author archives in Yoast (stops username exposure).
5. **Short-term** — Delete `/smittevern/` and 301 redirect to `/praktisk-informasjon/`.
6. **Short-term** — Evaluate event_promoter taxonomy; if thin content, noindex the entire taxonomy.
7. **Cleanup** — Disable in Yoast > Taxonomies: `event_type`, `sponsor`, `sponsor_category`, `category`, `post_tag`, `event_venue`.

---

## Correctly Configured Sitemaps (no action needed)

- **event-sitemap.xml** — 338 unique event pages. Primary organic discovery asset.
- **hall-sitemap.xml** — 12 venue pages with rich image data. Strong rental query landing pages.
- **post-sitemap.xml** — 17 posts, actively maintained.
- **page-sitemap.xml** — Once internal/test pages are removed, remaining pages are correctly included.
