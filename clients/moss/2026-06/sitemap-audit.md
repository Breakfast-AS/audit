# Sitemap Audit — mosskulturhus.no

**URL:** https://www.mosskulturhus.no/
**Date:** 2026-06-03
**Auditor:** Claude Code / seo-sitemap

---

## Sitemap Health Score: 38 / 100

| Category | Score | Max |
|---|---|---|
| Structure & format | 8 | 15 |
| lastmod accuracy | 3 | 20 |
| Duplicate / canonical hygiene | 6 | 25 |
| Crawl signal quality | 10 | 20 |
| URL naming & taxonomy | 11 | 20 |
| **Total** | **38** | **100** |

**Summary:** The sitemap setup has a solid foundation (split by content type, sitemap index, HTTPS throughout) but is undermined by pervasive stale `lastmod` dates, a meaningful number of duplicate and near-duplicate URLs, thin-content archive pages being indexed, and taxonomy inconsistencies that confuse both crawlers and users. Fixing the high-priority items below would realistically lift the score to 70+.

---

## Sitemap Inventory

| File | URLs | Notes |
|---|---|---|
| page-sitemap.xml | 38 | Core site pages |
| event-sitemap.xml | 59 | Event detail pages |
| category-sitemap.xml | 24 | Taxonomy archive pages |
| post_tag-sitemap.xml | 14 | Tag archive pages |
| venue-sitemap.xml | 5 | Venue pages |
| organizer-sitemap.xml | 24 | Organizer archive pages |
| **Total** | **164** | Well under 50k limit |

---

## Issues by Severity

### CRITICAL

None found (no broken URLs confirmed, no HTTP redirect loops, no non-HTTPS URLs, under 50k URL limit).

---

### HIGH

#### H1 — Wholesale stale `lastmod` dates across page-sitemap.xml

`lastmod` is the primary signal Google uses to decide whether to re-crawl a page. When these dates are wrong, Googlebot may deprioritize crawls of pages that have actually changed, and may waste crawl budget re-crawling pages that haven't.

**Affected URLs and staleness:**

| URL | lastmod in sitemap | Reality |
|---|---|---|
| / | 2024-03-01 | Homepage actively shows 2026 events — at least 2 years stale |
| /program/ | 2018-04-27 | ~8 years stale |
| /publikum/ | 2018-08-29 | ~8 years stale |
| /nyhetsbrev/ | 2019-07-29 | ~7 years stale |
| /stand-up/ | 2020-10-15 | ~6 years stale |
| /barneprogram/ | 2021-09-10 | ~5 years stale |
| /leie/ | 2023-10-02 | Likely updated since — rental pages change frequently |

**Root cause:** The CMS (likely WordPress with an SEO plugin) is not updating `lastmod` on re-save or when dynamic content (events, embedded programs) changes. The plugin may be caching the first-publish date.

**Fix:** Configure the SEO plugin (Yoast / Rank Math / The SEO Framework) to use the `post_modified` date for `lastmod`, not `post_date`. For dynamically driven pages (homepage, /program/), set up a hook that touches the page's modified date whenever the underlying event data changes.

---

#### H2 — All event lastmod dates are identical (auto-generated, not real)

Every one of the 59 event URLs in event-sitemap.xml shows `lastmod=2026-06-03` — today's date. This is a telltale sign that the plugin is outputting the current date at generation time rather than the actual modification date.

**Why this matters:** Google has stated they ignore `lastmod` they consider unreliable. Showing the same date across 59 URLs, changing every time the sitemap is regenerated, will cause Google to distrust all `lastmod` signals from this domain — including in the page sitemap where dates would otherwise be meaningful.

**Fix:** Use a plugin that stores and outputs actual `post_modified` timestamps for events. If using The Events Calendar + Yoast, verify that the Yoast sitemap module is reading `post_modified` correctly. Avoid any sitemap configuration that regenerates dates at request time.

---

#### H3 — Duplicate event slugs (typo variant both indexed)

`/event/riksteateret-ubesvart-anrop/` and `/event/riksteatret-ubesvart-anrop/` are both present in the sitemap.

"Riksteateret" (with an extra 'e') is the typo; the correct name is "Riksteatret". Both pages are apparently live and both are being submitted for indexing. This splits any backlink equity and can cause Google to index the wrong version.

**Fix:**
1. Identify which slug has the canonical content.
2. Set up a 301 redirect from the typo slug to the correct one.
3. Remove the typo URL from the sitemap.
4. Add a `rel="canonical"` on the typo page pointing to the correct URL (belt and suspenders).

---

#### H4 — Duplicate content pages: flat pages vs. venue post type

Both of the following pairs represent the same physical venue with the same content, but live at different URL paths:

| Flat page | Venue post type |
|---|---|
| /parkteatret/ | /venue/parkteatret/ |
| /samfunnshuset/ | /venue/samfunnshuset/ |

Both URLs in each pair appear in the sitemap. This means Google is crawling two copies of what is likely near-identical content. Without a canonical tag chain, PageRank and relevance signals are split.

**Fix (choose one per venue):**
- **Option A (preferred):** Decide the `/venue/` URL is canonical. 301 redirect the flat page to it. Update all internal links. Remove the flat page from the sitemap.
- **Option B:** If the flat page must exist (e.g., it's in the main nav and you don't want to change the URL), add `rel="canonical"` on the flat page pointing to the `/venue/` version, and remove the flat page from the sitemap.

Do not maintain both as equals.

---

### MEDIUM

#### M1 — Year-hardcoded URLs for recurring events

Two festival pages have the year baked into the slug:

- `/christian-frederik-dagene-2024/` (lastmod 2024-08-07)
- `/kryssover-jazzfest-moss-2026/` (lastmod 2026-01-23)

Year-in-URL creates a new page every year, splitting SEO equity and leaving the previous year's page as a zombie URL. This is a common pattern on event/venue sites but it has meaningful cost: a page called `/christian-frederik-dagene-2024/` will never rank for someone searching for the 2025 or 2026 edition.

**Near-duplicate pair:** `/kryssover-jazzfest-moss-2026/` and `/kryssover-jazzfest-moss/` are both in the sitemap. These almost certainly cover the same festival — one is the evergreen URL, one is the year-specific edition. Without canonical tags, they compete.

**Fix:**
- Establish one evergreen URL per recurring festival: `/christian-frederik-dagene/`, `/kryssover-jazzfest-moss/`.
- Update the evergreen page each year with the new edition's content.
- 301 redirect the year-specific URL to the evergreen one.
- Remove year-specific URLs from the sitemap once redirected.
- Ensure `/kryssover-jazzfest-moss/` is the canonical and `/kryssover-jazzfest-moss-2026/` redirects to it.

---

#### M2 — Duplicate event pages created by "-2", "-3" suffix pattern

WordPress Event plugins sometimes create duplicate posts when an event is re-published or cloned. The following groups appear in event-sitemap.xml:

| Event | Duplicates |
|---|---|
| Viken Tattoorama | /event/viken-tattoorama/, /event/viken-tattoorama-2/, /event/viken-tattoorama-3/, /event/viken-tattoorama-2026-tattooramapass/ |
| B16 In Motion | /event/b16-in-motion/, /event/b16-in-motion-2/ |
| Fiin Argang Pa Gyngende Grunn | /event/fiin-argang-pa-gyngende-grunn/, /event/fiin-argang-pa-gyngende-grunn-2/ |
| Musikalen Ingvar | /event/musikalen-ingvar-en-mobelsaga/, /event/musikalen-ingvar-en-mobelsaga-2/ |

If the `-2` / `-3` variants are separate showings (different dates, same event), they should have distinct enough content (different dates, ticket links, performers) and a canonical tag pointing to the main event. If they are accidental duplicates from cloning, they should be deleted and 301 redirected.

**Fix:**
1. Audit each pair in the CMS admin.
2. If duplicate: delete the `-2` post, set up 301 redirect.
3. If distinct showing: ensure each has unique content (dates, cast, description) and add `rel="canonical"` pointing to the primary event.
4. Remove all non-canonical duplicates from the sitemap.

---

#### M3 — Duplicate jobs pages

Both `/ledig-stilling/` (singular, lastmod 2022-02-16) and `/ledige-stillinger/` (plural, lastmod 2022-07-07) are in the sitemap. These are almost certainly the same concept (job openings) with one being a legacy URL.

**Fix:** 301 redirect `/ledig-stilling/` to `/ledige-stillinger/`. Remove the singular form from the sitemap.

---

#### M4 — 24 organizer archive pages likely contain thin content

The organizer-sitemap.xml contains 24 URLs for external promoter archive pages. These are auto-generated WordPress taxonomy pages listing events by a given organizer. In most cases, these pages:

- Have no unique editorial content (just a list of events)
- Are not pages users would navigate to directly
- Provide no differentiated value over the events themselves
- May have very few or zero upcoming events listed (especially for one-off promoters)

If the content is thin (fewer than ~300 words of unique text, only listing events), these pages dilute crawl budget and index quality.

**Fix:**
- Audit the 24 organizer pages: count how many have 3+ events and meaningful organizer descriptions.
- For pages with thin content: add `noindex, follow` meta tag and remove from sitemap.
- For the most prominent recurring organizers (e.g., Riksteatret which has its own /riksteatret/ page): ensure content is substantial and unique, or consolidate with the existing page.

---

#### M5 — 14 tag archive pages of uncertain quality

post_tag-sitemap.xml contains 14 tag pages. Tag archives are a frequent source of thin/duplicate content on WordPress sites. Unless each tag page has:
- A curated editorial description
- 5+ pieces of content tagged
- A distinct search intent

...these pages burn crawl budget and can dilute the domain's index quality.

**Specific conflict:** `/tag/riksteatret/` overlaps with the content page `/riksteatret/`. A user (and Googlebot) may be confused about which page should rank for "Riksteatret."

**Fix:**
- Audit all 14 tag pages for content depth.
- Noindex tags with fewer than 3–5 events or no editorial description.
- Ensure `/tag/riksteatret/` either has unique content vs. `/riksteatret/` or is noindexed and that page removed from the sitemap.

---

### LOW / INFO

#### L1 — English category slug on a Norwegian site

`/category/concert/` is present in category-sitemap.xml. The site is Norwegian; all other category slugs are Norwegian. This slug is either a default WordPress category that was never renamed, or an import artifact.

**Fix:** Rename the category slug to `/category/konsert/` in WordPress (Settings > Permalinks will update automatically). Update any internal links. The old URL should 301 redirect automatically if configured correctly, but verify.

---

#### L2 — Near-duplicate category pairs

| Pair | Issue |
|---|---|
| /category/festival/ + /category/festivaler/ | Singular vs. plural — same concept |
| /category/julekonsert/ + /category/julekonserter/ | Singular vs. plural — same concept |

Both members of each pair appear in the sitemap. Googlebot will see two archive pages with very similar (potentially identical) event listings and may treat one or both as thin/duplicate.

**Fix:**
- Pick one form (prefer plural for category archives: `/category/festivaler/`, `/category/julekonserter/`).
- Merge the content: move all posts tagged with the singular to the plural category.
- 301 redirect the deprecated category URL.
- Remove the deprecated URL from the sitemap.

---

#### L3 — Uncategorized category indexed

`/category/ukategorisert/` is present in category-sitemap.xml. This is WordPress's default "Uncategorized" category, translated to Norwegian. It should never be indexed — posts land here when a category is forgotten, meaning the archive has no coherent topic.

**Fix:**
- In WordPress, set the default post category to a real category (not Ukategorisert).
- Add `noindex, follow` to the Ukategorisert category template (Yoast: SEO > Search Appearance > Taxonomies > Categories > "Ukategorisert" > No Index).
- Remove `/category/ukategorisert/` from the sitemap.

---

#### L4 — `priority` and `changefreq` tags

Note: The audit data does not show `priority` values being set, and the user prompt mentions "no priority values on any URLs." This is actually fine — Google has explicitly stated that `<priority>` and `<changefreq>` are ignored. Not setting them is the correct behavior. No action needed.

---

#### L5 — /tag/riksteatret/ conflicts with /riksteatret/ page

The tag archive `/tag/riksteatret/` and the editorial page `/riksteatret/` likely target overlapping search intent. Both being indexed can cause keyword cannibalization for queries like "Riksteatret Moss."

**Fix:** If `/riksteatret/` is the intentional ranking page, noindex the tag archive. If the tag archive has unique editorial content, differentiate them clearly.

---

## Summary Action Plan

### Immediate (this sprint)

| # | Action | Impact |
|---|---|---|
| 1 | Fix lastmod generation — use `post_modified`, not generation time | High — restores crawl signal reliability |
| 2 | Delete or 301 redirect typo event `/event/riksteateret-ubesvart-anrop/` | High — eliminates confirmed duplicate |
| 3 | Resolve /parkteatret/ vs /venue/parkteatret/ — pick one, redirect the other | High — eliminates content duplication |
| 4 | Resolve /samfunnshuset/ vs /venue/samfunnshuset/ — same as above | High |
| 5 | Noindex + remove from sitemap: /category/ukategorisert/ | Medium |
| 6 | 301 redirect /ledig-stilling/ → /ledige-stillinger/ | Medium |

### Next sprint

| # | Action | Impact |
|---|---|---|
| 7 | Audit -2/-3 event duplicates; delete or add canonicals | Medium |
| 8 | Resolve kryssover-jazzfest-moss-2026 vs kryssover-jazzfest-moss | Medium |
| 9 | Rename /category/concert/ → /category/konsert/ | Low-Medium |
| 10 | Merge festival/festivaler and julekonsert/julekonserter category pairs | Low-Medium |
| 11 | Audit 24 organizer pages; noindex thin ones | Medium |
| 12 | Audit 14 tag pages; noindex thin ones | Low-Medium |

### Ongoing

| # | Action | Impact |
|---|---|---|
| 13 | Establish evergreen URL policy for recurring festivals | Medium (long-term equity) |
| 14 | Set up year-specific URLs to 301 → evergreen after event ends | Medium |
| 15 | Monitor sitemap coverage in Google Search Console monthly | Medium |

---

## What Is Working Well

- Sitemap is split by content type (pages, events, categories, tags, venues, organizers) — this is best practice.
- All URLs use HTTPS — no mixed-content issues.
- Total URL count (164) is well within the 50,000-per-file limit.
- A sitemap index structure appears to be in use.
- No 404 URLs were flagged in the provided data.
- No `<priority>` or `<changefreq>` clutter (Google ignores these).

---

*Audit based on sitemap data as of 2026-06-03. HTTP status codes and canonical tag configurations were not individually verified via live crawl in this report — a full crawl with Screaming Frog or Sitebulb would confirm redirect chains and canonical implementations.*
