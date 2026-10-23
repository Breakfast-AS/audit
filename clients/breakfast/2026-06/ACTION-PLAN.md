# SEO Action Plan — breakfast.no
**Generated:** 2026-06-01  
**Overall Score:** 40/100  
**Target Score (3 months):** 65/100  

---

## Priority Framework

- 🔴 **Critical** — Fix immediately. Blocks rankings or causes quality penalties.
- 🟠 **High** — Fix within 1 week. Significant ranking impact.
- 🟡 **Medium** — Fix within 1 month. Optimization opportunity.
- 🟢 **Low** — Backlog. Nice to have.

---

## 🔴 CRITICAL — Fix This Week

### C1 — Fix Language Attribute (1 hour)
**Impact:** All pages | **Effort:** 5 minutes

The entire site is tagged as English (`lang="en-US"`) but is written in Norwegian. This affects Google's language detection and targeting.

**Steps:**
1. WordPress Admin → Settings → General
2. Change "Site Language" to "Norsk bokmål (nb_NO)"
3. Save. WordPress will update the `<html lang="">` attribute automatically.
4. Yoast SEO will automatically update `inLanguage` in schema markup.
5. Verify by checking source: should show `<html lang="nb-NO">`

---

### C2 — Noindex or Delete Test/Staging Pages (30 minutes)
**Impact:** Crawl budget, quality signals | **Effort:** Low

These pages are indexed and in the sitemap but should not be:

| URL | Action |
|-----|--------|
| /sample-page/ | Delete (it's WordPress default) |
| /testside/ | Delete or noindex |
| /testside-2/ | Delete or noindex |
| /divi-login-designer/ | Add noindex via Yoast SEO on the page |
| /entercore-font/ | Review — if internal tool, noindex |
| /dashboard/ | Review — if admin tool, noindex |

**To noindex via Yoast:** Edit page → Yoast SEO → Advanced → "Allow search engines to show this post in search results" → No

**After deleting:** Submit updated sitemap to Google Search Console.

---

### C3 — Fix Staging Domain Logo URL (15 minutes)
**Impact:** Production reliability | **Effort:** Low

One image is served from `breakfastny.wpengine.com` (WP staging domain):
- `breakfastny.wpengine.com/wp-content/uploads/2023/01/bf_logo_2_round_sort-1-1-copy.png`

**Steps:**
1. Find the element in WordPress → Appearance → Customize, or in the Divi header module
2. Replace the image with the same file uploaded to the production media library
3. Confirm the new src uses `breakfast.no`

---

### C4 — Add Alt Text to All Images (2–3 hours)
**Impact:** Image SEO, accessibility, Core Web Vitals signals | **Effort:** Medium

21 of 22 homepage images have `alt=""` (empty). This is true across the site.

**Steps:**
1. WordPress Admin → Media → Library
2. Click each image → Add alt text that describes what the image shows
3. Be specific: "Breakfast-teamet jobber med strategi i Tønsberg" not "Team"
4. For portfolio/client images: "[Client name] – [what the image shows]"
5. Divi modules override Media Library alt text — verify in Divi module settings under Image Alt Text field

**Priority images to fix first:**
- Logo (currently from staging domain — also C3)
- Hero/homepage slider images
- Client work showcase images
- Team photos on om-oss page

---

## 🟠 HIGH — Fix Within 1 Week

### H1 — Write Meta Descriptions for Key Pages (2 hours)
**Impact:** CTR in search results | **Effort:** Low

Add 150–160 character meta descriptions to these pages via Yoast SEO:

| Page | Suggested Meta Description |
|------|---------------------------|
| /om-oss/ | "Breakfast er et kommunikasjonsbyrå i Tønsberg med 15 år i bransjen. Vi hjelper merkevarer innen kultur, media og næringsliv med å nå sine mål." |
| /tjenester/ | "Vi tilbyr design, strategi, teknologi og kommunikasjonstjenester – skreddersydd for merkevarer som vil vokse. Se våre tjenester." |
| /kultur/ | "Breakfast er Norges ledende kommunikasjonspartner for kultursektor. Vi jobber med kulturhus, museer, festivaler og podkaster." |
| /markedsavdeling-pa-lan/ | "Trenger du en erfaren markedsavdeling uten fast ansettelse? Breakfast tilbyr markedsavdeling på lån – strategisk og operativt." |
| /stillinger/ | "Se ledige stillinger hos Breakfast – et kreativt kommunikasjonsbyrå i Tønsberg. Vi ser alltid etter dyktige folk." |
| /tjenester/design/ | "Breakfast leverer logo, visuell identitet, grafisk design, webdesign, animasjon og mer. Se designtjenester." |
| /tjenester/strategi/ | "Vi utvikler kommunikasjonsstrategier basert på innsikt og analyse. Les om vår tilnærming til strategi." |
| /tjenester/teknologi/ | "Fra nettsider til digitale løsninger – Breakfast hjelper deg med teknologi som understøtter merkevaren din." |

---

### H2 — Expand or Noindex All Kunder Pages (1–2 days)
**Impact:** Thin content at scale (106 pages) | **Effort:** High

This is the most significant content quality issue. Two paths:

**Option A (Recommended): Noindex all kunder pages + create a showcase page**
1. In Yoast SEO: bulk-noindex all 106 kunder posts (or use a plugin like Bulk Edit Pro)
2. Create a single `/kunder/` page with logo grid, 2–3 sentence description per client
3. Point `/kunder/[client]/` URLs to redirect (301) to the main `/kunder/` page

**Option B: Expand each kunder page (significant effort)**
1. Add 150–300 words per page: what was the brief, what Breakfast delivered, what the outcome was
2. Add a representative image with alt text
3. Link to related services

Option A delivers faster results with less effort.

---

### H3 — Add Organization Schema (30 minutes)
**Impact:** Rich results, AI citation, local search | **Effort:** Low

Add this to Yoast SEO → Search Appearance → Knowledge Graph:
- Organization type: Company
- Organization name: Breakfast
- Logo: Upload to Yoast
- Social profiles: Instagram, Facebook

Then add LocalBusiness details:
- Address: Møllegaten 6, 3111 Tønsberg
- Contact: hei@breakfast.no

Or add JSON-LD directly in the site header (see schema recommendation in full report).

---

### H4 — Fix Duplicate H1 on Homepage (30 minutes)
**Impact:** On-page SEO clarity | **Effort:** Low

The H1 "Hei! Vi er Breakfast" appears twice on the homepage. Find the duplicate in Divi Builder and either:
- Delete the duplicate module
- Change the second H1 to an H2 or H3

---

### H5 — Enable Divi Performance Optimizations (1–2 hours)
**Impact:** Core Web Vitals, mobile PageSpeed score | **Effort:** Medium

**In Divi → Theme Options → General → Performance:**
- ✅ Enable "Static CSS File Generation"
- ✅ Enable "Dynamic CSS" (generates per-page CSS instead of full stylesheet)
- ✅ Enable "Defer jQuery and Theme Scripts" (test thoroughly after enabling)
- ✅ Enable "Lazy Loading" for images

**In WP Engine Portal (WP Engine → Performance):**
- ✅ Enable JS Defer
- ✅ Enable CSS Minification
- ✅ Enable HTML Minification

**Expected improvement:** Mobile PageSpeed score from ~40 to ~55–65.

---

### H6 — Add Image Lazy Loading (30 minutes)
**Impact:** LCP, bandwidth, CWV | **Effort:** Low

If Divi's lazy loading toggle (above) doesn't work, add to `functions.php`:

```php
add_filter('wp_lazy_loading_enabled', '__return_true');
```

And verify in Divi Builder that image modules have "Loading: Lazy" set.

---

### H7 — Restrict wp-login.php (30 minutes)
**Impact:** Security | **Effort:** Low

In WP Engine Portal → Security → IP Restrictions:
- Restrict `/wp-login.php` to your office IP addresses only
- Or enable WP Engine's built-in login protection

---

## 🟡 MEDIUM — Fix Within 1 Month

### M1 — Improve Title Tags on Inner Pages (2 hours)
Replace formulaic titles with descriptive, keyword-rich ones:

| Current | Recommended |
|---------|------------|
| "Om oss - Breakfast" | "Om Breakfast – Kommunikasjonsbyrå i Tønsberg siden 2011" |
| "Tjenester - Breakfast" | "Tjenester – Design, Strategi, Teknologi og Kommunikasjon" |
| "Stillinger - Breakfast" | "Ledige stillinger hos Breakfast – Kommunikasjonsbyrå" |
| "KulturApp - Breakfast" | "KulturApp – Digital billettløsning for kulturhus og festivaler" |

---

### M2 — Create llms.txt File (1 hour)
**Impact:** AI search visibility | **Effort:** Low

Create at `https://breakfast.no/llms.txt`:

```
# Breakfast – Kommunikasjonsbyrå i Tønsberg, Norge
# https://breakfast.no/

## About
Breakfast er et kommunikasjonsbyrå grunnlagt i Tønsberg, Norge.
Vi spesialiserer oss på merkevarebygging og kommunikasjon for kultur- og underholdningssektoren.
Vi tilbyr design, strategi, teknologi og kommunikasjonstjenester.

## Key Pages
- https://breakfast.no/om-oss/
- https://breakfast.no/tjenester/
- https://breakfast.no/kultur/
- https://breakfast.no/jobber/

## Services
- Kommunikasjonsstrategi
- Visuell identitet og design
- Nettsider og digitale løsninger
- Sosiale medier og innhold
- Markedsavdeling på lån
- KulturApp

## Target Industries
- Kulturhus og konserthus
- Museer og gallerier
- Festivaler og arrangementer
- Radio og podkast
```

---

### M3 — Add FAQ Sections to Service Pages (4–6 hours)
**Impact:** AI Overviews, featured snippets, user experience | **Effort:** Medium

Add 3–5 FAQ items to each of these pages using `<details>/<summary>` or an accordion, then add `FAQPage` schema:
- /tjenester/design/
- /tjenester/strategi/
- /markedsavdeling-pa-lan/
- /kultur/

Example questions for /markedsavdeling-pa-lan/:
- "Hva er en markedsavdeling på lån?"
- "Passer dette for små bedrifter?"
- "Hva koster det å leie en markedsavdeling?"

---

### M4 — Add Preconnect for Google Fonts (15 minutes)
**Impact:** FCP, LCP | **Effort:** Very Low

In WordPress header (via theme functions or WP Engine header injection):

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
```

---

### M5 — Fix Tjenester Sitemap Lastmod (15 minutes)
**Impact:** Crawl prioritization | **Effort:** Low

The tjenester sitemap shows `lastmod: 2023-10-24` — over 2.5 years ago. Touch and re-save each service page in WordPress to trigger Yoast to update the lastmod date.

---

### M6 — Expand Om Oss Page (3–4 hours)
**Impact:** E-E-A-T, brand authority | **Effort:** Medium

Currently ~318 words with no H1 and missing meta description. Add:
- H1: "Vi er Breakfast – 15 år med kommunikasjon som virker"
- Agency founding story and mission (200 words)
- Named team overview with photos (link to ansatte pages)
- Notable clients or sectors served
- Awards, press mentions, or certifications
- Address and contact confirmation

Target: 600–800 words with proper heading structure.

---

### M7 — Add Security Headers via WP Engine (30 minutes)
**Impact:** Security posture | **Effort:** Low

In WP Engine → Security, or via `nginx.conf` / `.htaccess`:

```
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
```

---

### M8 — Install Image Optimization Plugin (1 hour)
**Impact:** Page weight, LCP, image quality | **Effort:** Low**

Install **ShortPixel** or **Imagify**:
1. Install plugin
2. Configure to auto-optimize on upload
3. Enable WebP conversion
4. Run bulk optimization on existing 100+ images

Expected: 40–60% reduction in image file sizes.

---

## 🟢 LOW — Backlog

### L1 — Content Strategy: Publish 6 Articles per Year
The site has 10 blog posts total — extremely sparse for an agency. Publish quarterly thought leadership content:
- "Slik jobber vi med merkevarebygging for kulturhus" (case study format)
- "Hva kjennetegner god markedsføring av festivaler?"
- Industry trend pieces for the cultural sector

### L2 — Remove `Crawl-delay: 10` from robots.txt
Reduces unnecessary crawl throttling. Edit via Yoast SEO → Tools → File Editor → robots.txt.

### L3 — Add Author Bylines to Blog Posts
Assign each post to a named author with an author archive page and bio. This supports E-E-A-T signals.

### L4 — Add `fetchpriority="high"` to Hero Image
Add `fetchpriority="high"` to the LCP hero image. Can be done via Divi module custom attributes or a filter in `functions.php`.

### L5 — Rename Uploaded Images to Descriptive Filenames
Future uploads should use descriptive names: `breakfast-team-tonsberg-2024.jpg` not `IMG_2317.jpg`.

### L6 — Add Service Schema to Tjenester Pages
Add `Service` schema markup to each of the 16 service pages via Yoast SEO or custom JSON-LD.

### L7 — Add Person Schema to Ansatte Pages
Each staff member profile should have `Person` schema with name, role, and `worksFor` linking to the Organization schema.

---

## Projected Impact

| Action Group | Effort | Score Impact |
|-------------|--------|-------------|
| C1–C4 (Critical fixes) | 4–5 hours | +6–8 points |
| H1–H7 (High priority) | 2–3 days | +10–14 points |
| M1–M8 (Medium priority) | 1–2 weeks | +8–10 points |
| **Combined 3-month projection** | | **~65/100** |

---

*Action Plan generated by Claude Code SEO Audit · breakfast.no · 2026-06-01*
