# SEO Action Plan: drammenscener.no
**Generated:** 2026-05-29 | **Overall Score:** 44/100
**Target Score:** 72/100 (achievable within 90 days)

---

## Priority Legend
- 🔴 **CRITICAL** — Fix immediately. Blocks indexing, creates security risk, or directly suppresses rankings.
- 🟠 **HIGH** — Fix within 1 week. Significant ranking or conversion impact.
- 🟡 **MEDIUM** — Fix within 1 month. Optimization opportunity with measurable upside.
- 🟢 **LOW** — Backlog. Technical hygiene or minor improvements.

---

## Week 1 — Security & Foundation (Critical)

### 🔴 1. Add Six Missing Security Headers
**Effort:** 1 hour | **Impact:** Security + trust signal
**How:** Cloudflare dashboard → Security → Custom Rules → Response Header Transform

Add all six headers:
```
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(), geolocation=()
```
Add Content-Security-Policy in report-only mode first, then enforce after testing 2 weeks.
After HSTS is stable: submit domain to https://hstspreload.org

---

### 🔴 2. Remove xmlrpc.php Pingback Link
**Effort:** 30 minutes | **Impact:** Security attack surface reduction
**How:** Add to functions.php:
```php
remove_action('wp_head', 'xmlrpc_rsd_link');
add_filter('bloginfo_url', fn($out, $prop) => $prop === 'pingback_url' ? '' : $out, 11, 2);
```
Also: WordPress Admin → Settings → Discussion → uncheck "Allow link notifications from other blogs"

---

### 🔴 3. Restrict WordPress REST API
**Effort:** 30 minutes | **Impact:** Prevents user enumeration and version disclosure
**How:** Add to functions.php:
```php
add_filter('rest_authentication_errors', function($result) {
    if (!is_user_logged_in()) {
        return new WP_Error('rest_not_logged_in', 'REST API restricted.', ['status' => 401]);
    }
    return $result;
});
remove_action('wp_head', 'rest_output_link_header', 11);
remove_action('template_redirect', 'rest_output_link_header', 11);
```

---

### 🔴 4. Protect wp-login.php
**Effort:** 1 hour | **Impact:** Prevents brute-force attacks
**How:** 
- Install WP 2FA plugin, enable for all admin users
- Via WP Engine dashboard: add IP restriction to wp-login.php for known admin IPs, OR install WPS Hide Login plugin to change the login URL

---

### 🔴 5. Fix Dual H1 on Homepage
**Effort:** 30 minutes | **Impact:** Critical on-page signal
**How:** In WordPress editor, change the jumbotron "Drammen Scener" H1 to a non-heading element (styled div/span). The remaining H1 should be rewritten to target the primary keyword:
> *"Konferanselokaler og eventsaler i Drammen"* — or similar incorporating primary service terms + city

---

### 🔴 6. Write Meta Description for /saler/
**Effort:** 20 minutes | **Impact:** Immediate SERP CTR improvement on high-value page
**How:** Yoast SEO → edit /saler/ archive settings → Meta description field

Suggested (156 chars):
> "Utforsk 8 unike saler på Union Scene og Drammens Teater i Drammen. Fra intime rom til storstilte scener for opptil 1200 gjester. Be om tilbud i dag."

---

### 🔴 7. Add Organization + EventVenue Schema to Homepage
**Effort:** 2 hours | **Impact:** Enables Google local pack, GBP entity association, AI citations

Add as standalone `<script type="application/ld+json">` block in homepage (via Yoast custom schema or child theme header):
- Organization entity with name, URL, phone, email, sameAs (social profiles)
- Two EventVenue entities (Union Scene + Drammens Teater) with full PostalAddress, geo coordinates (5 decimal places), telephone, URL

**Before deploying:** Verify exact addresses, phone numbers, geo coordinates from contact page. Use "Buskerud" for addressRegion (Viken was dissolved 2024).

See full JSON-LD in FULL-AUDIT-REPORT.md Section 4.2.

---

## Week 1–2 — Indexability & Quick Wins

### 🔴 8. Noindex Department Taxonomy Pages
**Effort:** 10 minutes | **Impact:** Removes 6 thin/worthless pages from index
**How:** Yoast SEO → Search Appearance → Taxonomies → Department → Show in search results: **No**

This automatically removes `/department/daglig-leder/` and 5 similar pages from sitemaps and adds noindex.

---

### 🟠 9. Write Meta Descriptions for All Missing Pages
**Effort:** 1 hour | **Impact:** SERP CTR on commercial pages
Pages confirmed missing descriptions:
- `/konferanser/` — target: "konferanselokale Drammen"
- `/eventer/` — target: "eventlokale Drammen"
- `/ansatte/` — add description or noindex

Suggested for /konferanser/ (158 chars):
> "Profesjonelle konferanselokaler i Drammen. Union Scene og Drammens Teater tilbyr fleksible konferansepakker med teknisk utstyr og catering for 10–400 deltagere."

---

### 🟠 10. Enable IndexNow in Yoast SEO
**Effort:** 2 minutes | **Impact:** Bing indexes content changes within hours
**How:** Yoast SEO → General → Features → IndexNow → **On**

---

### 🟠 11. Fix Google Fonts to Async Loading
**Effort:** 1 hour | **Impact:** Removes render-blocking CSS, improves LCP
**How:** Replace in header.php or via WordPress hook:
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined"></noscript>
```

---

### 🟠 12. Remove jQuery Migrate from Frontend
**Effort:** 30 minutes | **Impact:** Removes ~10 KB, improves INP
**How:** Add to functions.php:
```php
add_action('wp_default_scripts', function($scripts) {
    if (!is_admin()) $scripts->remove('jquery-migrate');
});
```
Test site thoroughly after removing — if any frontend functionality breaks, identify which plugin requires it and update that plugin instead.

---

### 🟠 13. Fix Vimeo LCP Performance
**Effort:** 1 hour | **Impact:** Improves homepage LCP score
**How:**
1. Add `<link rel="preconnect" href="https://i.vimeocdn.com" crossorigin>` to `<head>`
2. Add `fetchpriority="high"` to the jumbotron thumbnail `<img>` tag
3. Add `aspect-ratio: 16/9` to `.panel-jumbotron .iframe-wrapper` in CSS to prevent CLS

---

### 🟠 14. Add NAP to Footer (All Three Domains)
**Effort:** 1–2 hours | **Impact:** Critical local SEO signal
**How:** Add full Name + Address + Phone to footer of drammenscener.no (both venues), unionscene.no (Union Scene only), drammensteater.no (Drammens Teater only).

Format: Plain HTML text (not image). Ensure address matches GBP exactly, character for character.

---

## Week 2–4 — Content Expansion (High Priority)

### 🟠 15. Expand /pakker/konferansepakke/ to 800+ Words
**Effort:** 1 day | **Impact:** Highest commercial-intent page on site
**Add:**
- Package inclusions list (what's included at each tier)
- Capacity ranges for each included room
- AV equipment specifications
- Catering options and restrictions
- Booking process and lead time requirements
- Cancellation/change policy outline
- FAQ block (min. 5 questions): inline Q&A answering objections
- CTA with direct link to /kontakt-oss/ and phone number

---

### 🟠 16. Add Capacity + Spec Tables to All 8 Venue Pages
**Effort:** 2 days | **Impact:** Converts brochure pages into decision-making tools
**Add per room page:**
- Seated capacity / standing capacity / theatre layout / cabaret layout
- Floor area (m²) and ceiling height if relevant
- AV equipment list (projector, screen, PA system, mic types)
- Natural light / blackout capability
- Accessibility (wheelchair, hearing loop)
- Catering: in-house, approved caterers, open policy
- Nearest parking
- Setup/breakdown time policy

---

### 🟠 17. Rewrite /kontakt-oss/ Page
**Effort:** 2 hours | **Impact:** B2B trust + conversion
**Replace current thin page with:**
- Named contact(s) with title and direct phone/email for event inquiries
- "Vi svarer innen 1 virkedag" response time commitment
- Full address for both venues with embedded Google Maps (via GBP place embed)
- Organisasjonsnummer in footer or contact page
- Separate contact paths: new bookings vs. existing client support

---

### 🟠 18. Create /ofte-stilte-sporsmal/ FAQ Page
**Effort:** 1–2 days | **Impact:** Highest AI citation opportunity; enables FAQPage schema
**Write 15+ Q&A pairs covering:**
- What is included in the conference package?
- What is the difference between Union Scene and Drammens Teater?
- Can I bring my own catering?
- Is there parking at Union Scene / Drammens Teater?
- What AV equipment is available?
- How far in advance should I book?
- Are the venues accessible for wheelchair users?
- Can I have a private arrangement on weekends?
- What is the maximum capacity for a standing event?
- How do I get to Drammen from Oslo?

After creating: implement `FAQPage` JSON-LD schema on the page.

---

### 🟠 19. Add Trust Signals to Homepage
**Effort:** 1 day | **Impact:** Directly addresses lowest E-E-A-T dimension
**Add minimum viable trust block:**
- 3–5 named client testimonials (company + title + short quote)
- Event volume claim: "Over X arrangementer siden 2009" (use actual figure)
- Miljøfyrtårn certification badge with link to /miljofyrtarn/
- Logos of notable corporate clients (with permission)

---

### 🟠 20. Fix og:type on Package Pages
**Effort:** 30 minutes | **Impact:** Correct social sharing signals
Add to functions.php:
```php
add_filter('wpseo_opengraph_type', function($type) {
    if (get_post_type() === 'package') return 'website';
    return $type;
});
```

---

### 🟠 21. Update Title Tags with Drammen Keywords
**Effort:** 1 hour | **Impact:** Local keyword targeting in highest-weight on-page signal
**Template:** `[Service] i Drammen | [Venue] - Drammen Scener`

Key title rewrites:
- Homepage: "Konferanselokale og eventlokale i Drammen | Drammen Scener"
- /pakker/konferansepakke/: "Konferansepakke i Drammen | Union Scene & Drammens Teater"
- /saler/: "Saler og lokaler i Drammen | Union Scene & Drammens Teater"
- /kontakt-oss/: "Kontakt oss | Konferanselokale i Drammen - Drammen Scener"

---

## Month 2 — Structured Data & Local Citations

### 🟡 22. Add Service Schema to All 7 Package Pages
**Effort:** 2 hours | **Impact:** Entity clarity for commercial pages
Add `Service` JSON-LD to each `/pakker/` page. See FULL-AUDIT-REPORT.md Section 4.2 for template. Adapt `name`, `serviceType`, and `description` per package type.

---

### 🟡 23. Add Place Schema to All 8 Venue Pages
**Effort:** 3 hours | **Impact:** Rich entity signals for room pages
Add `Place` JSON-LD with `maximumAttendeeCapacity`, `amenityFeature`, and `containedInPlace` linking to parent EventVenue entity. See FULL-AUDIT-REPORT.md Section 4.2 for template.

---

### 🟡 24. Claim and Complete Norwegian Citation Profiles
**Effort:** 4 hours (one-time) | **Impact:** Local pack rankings + AI entity verification

Priority order:
1. **Konferanseguiden.no** — highest conversion value for conference vertical
2. **Finn.no** (lokaler til leie) — highest-traffic Norwegian space rental platform
3. **Gulesider.no** — Norwegian Yellow Pages equivalent
4. **1881.no** — key business directory
5. **Visitdrammen.no** — local authority + trust signal
6. **Eventlokaler.no** — sector-specific
7. **Miljofyrtarn.no** — verify certification profile is complete and linked

**Critical:** Each citation must use venue-specific NAP (not umbrella brand), matching GBP exactly.

---

### 🟡 25. Update llms.txt With Missing Information
**Effort:** 30 minutes | **Impact:** Better AI answer quality for contact queries
Add to existing `/llms.txt`:
- Phone number and email address in "Booking og forespørsel" section
- Full address for Drammens Teater (currently only Union Scene present)
- Office hours / response time for enquiries
- Add `# License: RSL-1.0` at top of file

---

### 🟡 26. Add Descriptive Alt Text to All Slider + Venue Images
**Effort:** 2 hours | **Impact:** Accessibility + image SEO
Replace all `alt=""` on showcase images with descriptive Norwegian alt text.

Examples:
- `alt="Hovedscenen på Union Scene satt opp for konferanse med rundt 300 gjester"`
- `alt="Bakgården på Union Scene under sommerfest med dekor og scenebelysning"`
- `alt="Glassfoajéen på Drammens Teater pyntet for gallamiddag"`

---

### 🟡 27. Verify GBP Categories and Optimize Both Listings
**Effort:** 2 hours | **Impact:** #1 local pack ranking factor
**In GBP dashboard:**
- Union Scene primary category: "Event Venue"
- Drammens Teater primary category: "Performing Arts Theater"
- Add secondary categories: Conference Center, Banquet Hall
- Write keyword-rich Norwegian description (750 chars max)
- Upload minimum 10 high-quality interior photos per venue
- Populate Services list for each venue
- Add accessibility attributes, parking, Wi-Fi, AV equipment attributes
- Verify correct domain URL per venue (unionscene.no, drammensteater.no)

---

### 🟡 28. Implement Post-Event Review Request Workflow
**Effort:** 2 hours setup, ongoing | **Impact:** Review velocity (Sterling Sky 18-day threshold)
**Create:**
- Email template for event organizers (send within 48 hours post-event)
- Direct GBP review link for each venue
- Calendar reminder protocol for events team
- Response templates for GBP reviews (in Norwegian, mentioning venue name naturally)

**Target:** Minimum 2 new reviews/month per venue to maintain local pack positions.

---

## Month 2–3 — Content Authority Building

### 🟡 29. Create Dedicated Service Landing Pages with Drammen Keyword
**Effort:** 3–4 days content | **Impact:** #1 local organic ranking factor (Whitespark 2026)

Create or significantly expand one page per major service type with "Drammen" in H1 and throughout copy (minimum 600 words each):
- "Konferanselokaler i Drammen" — expand /konferanser/ significantly
- "Møterom i Drammen" — new dedicated page
- "Eventlokaler i Drammen" — expand /eventer/
- "Festlokaler og selskapslokaler i Drammen" — new or expand /pakker/privat-arrangement/
- "Julebord i Drammen" — seasonal but high-traffic, expand /pakker/julebord/

---

### 🟡 30. Remove x-powered-by Header and Theme Version from Assets
**Effort:** 1 hour | **Impact:** Reduces attack surface fingerprinting
**Via Cloudflare:** Add "Remove Response Header" Transform Rule for `x-powered-by`
**In functions.php:** Remove `wp_generator` and change asset enqueue to use file hash instead of version number

---

### 🟡 31. Differentiate /eventer/ vs /pakker/eventer/ Pages
**Effort:** 2 hours | **Impact:** Eliminates topical cannibalization
Make `/eventer/` the informational hub page (event types, inspiration, what makes a good event) that links to `/pakker/eventer/` as the sales-focused page. Ensure no content duplication between the two.

---

### 🟡 32. Add YouTube Presence (Venue Videos)
**Effort:** Ongoing | **Impact:** YouTube mentions correlate 0.737 with AI citation frequency
**Priority content:**
1. Publish existing Vimeo background video to YouTube
2. Venue tour: Union Scene walk-through (5–7 min)
3. Venue tour: Drammens Teater walk-through (5–7 min)
4. "Slik bestiller du" — booking process explainer

Titles must use Norwegian keywords from llms.txt nøkkelbegreper section.

---

## Ongoing / Backlog

### 🟢 33. Disable WordPress RSS Feeds
**Effort:** 30 minutes | No editorial value for this non-blog site
```php
add_action('do_feed', 'disable_feeds', 1);
function disable_feeds() { wp_redirect(home_url()); exit; }
remove_action('wp_head', 'feed_links', 2);
```

### 🟢 34. Remove Duplicate Vary Headers
**Effort:** 1 hour | **Impact:** Caching hygiene
Identify and remove the three extra `Vary: Accept-Encoding` headers from the response stack. Check Cloudflare Transform Rules, WP Engine nginx config, and caching plugins.

### 🟢 35. Remove Redundant HTML Meta Tag
**Effort:** 10 minutes
Remove `<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />` from header.php — superseded by `<meta charset="UTF-8">`.

### 🟢 36. Fix XFN Profile Link HTTP Reference
**Effort:** 5 minutes
In header.php: remove `<link rel="profile" href="http://gmpg.org/xfn/11">` or update to `https://`. No SEO value, minor hygiene.

### 🟢 37. Create Blog / "Arrangementstips" Content Section
**Effort:** 1 week initial setup + ongoing
**Why:** Builds topical authority, generates recurring crawl activity, creates internal linking opportunities.
**Minimum 6 initial posts:**
- "Slik planlegger du konferansen for 100 personer i Drammen"
- "Beste tips til bedriftens julebord i Drammen"
- "5 grunner til å velge Drammens Teater for din gallamiddag"
- "Hva skiller Union Scene fra andre eventlokaler i Østlandet?"
- "Komplett guide til arrangementslokaler i Drammen"
- "Miljøvennlig konferanse: slik velger du grønt lokale"

### 🟢 38. Add hreflang Tags
**Effort:** 30 minutes | Site is monolingual (nb-NO)
Add `<link rel="alternate" hreflang="nb" href="[page-url]">` and `<link rel="alternate" hreflang="x-default" href="[page-url]">` via Yoast settings. Currently absent on all pages.

### 🟢 39. Register with Drammen Naeringsliv (Chamber of Commerce)
**Effort:** 1 hour | **Impact:** Local authority signal + business directory listing
Membership in Drammen Chamber of Commerce provides both a citation and a community trust signal relevant to B2B clients.

---

## Implementation Roadmap Summary

| Week | Actions | Expected Score Gain |
|---|---|---|
| Week 1 | Actions 1–8 (security, H1, /saler/ meta, schema, noindex) | +8 points → 52/100 |
| Week 1–2 | Actions 9–14 (meta descriptions, IndexNow, performance, NAP) | +4 points → 56/100 |
| Week 2–4 | Actions 15–21 (content expansion, FAQ, trust signals, titles) | +8 points → 64/100 |
| Month 2 | Actions 22–31 (schema, citations, GBP, reviews, service pages) | +6 points → 70/100 |
| Month 3+ | Actions 32–39 (YouTube, blog, hygiene) | +3 points → 73/100 |

---

*Action Plan generated by Claude Code SEO Audit System*
*Full findings: FULL-AUDIT-REPORT.md*
