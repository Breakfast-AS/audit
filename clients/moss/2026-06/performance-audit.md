# Performance Audit: mosskulturhus.no
**Date:** 2026-06-03  
**Estimated Score: 38 / 100** (mobile) | ~62 / 100 (desktop)  
**Method:** HTML source analysis + resource inspection (PageSpeed API quota exceeded)

---

## Core Web Vitals Assessment

| Metric | Estimated Status | Primary Driver |
|--------|-----------------|----------------|
| LCP    | FAIL (likely 4–6s mobile) | CSS-delivered hero image, 10 blocking scripts in `<head>` |
| INP    | NEEDS IMPROVEMENT | Divi Builder JS + jQuery + 7 blocking scripts inflate main-thread work |
| CLS    | FAIL | 64 images have no `width`/`height` attributes; no lazy-loading on any image |

> No CrUX field data available (API key required). Scores above are estimated from structural analysis.

---

## Critical Issues (High Impact)

### 1. ALL 10 External Scripts Are Render-Blocking
Every script is loaded without `defer` or `async`. Seven are injected into `<head>`, meaning the browser must download, parse, and execute all of them before it can render a single pixel.

**Blocking scripts in `<head>`:**
- `jquery.min.js` (31 KB gzipped) — loaded first, blocks everything downstream
- `jquery-migrate.min.js` — unnecessary on modern sites, pure bloat
- `tix-public.js` — ticketing plugin, not needed for initial paint
- `lazysizes 1.2.2` (from cdnjs.cloudflare.com) — ironically blocks render to lazy-load images
- `fontawesome 5daed306be.js` (use.fontawesome.com) — third-party icon kit, no `async`
- `js-cookie.min.js` (cdn.jsdelivr.net) — trivial utility, blocks render
- `theme scripts.js` (12 KB)

**Blocking scripts at end of `<body>`:**
- `divi-builder scripts.min.js` (53 KB gzipped)
- `page-links-to.js`
- `divi-builder common.js`

**Fix:** Add `defer` to all non-critical scripts. jQuery + jQuery-migrate are typically required by many WP plugins but can still be deferred in modern setups. Evaluate whether `jquery-migrate` is still needed.

---

### 2. Hero Image Is a CSS Background-Image (Not Discoverable by Preload Scanner)
The LCP element is almost certainly the full-width hero carousel image, served as a CSS `background-image` via an inline `style` attribute:

```
background-image: url(https://www.mosskulturhus.no/wp-content/uploads/2025/10/4312x1400_karusell.jpg)
```

- **148 KB JPEG at 4312×1400 px** — massively oversized for mobile viewports
- The browser's preload scanner cannot discover background-image URLs; the image does not start downloading until CSS is parsed and the style rule is applied
- No `<link rel="preload" as="image">` hint exists for this image
- The image has a 1-year cache TTL (`max-age=31536000`) which is correct, but download is still delayed

**Fix:** Either switch the hero to an `<img>` element (allowing preload scanner discovery + `fetchpriority="high"`) or add an explicit `<link rel="preload" as="image" href="...">` for the above-the-fold hero. Serve WebP/AVIF variants via `<picture>` or `imagesrcset`.

---

### 3. Zero Images Have `width`/`height` Attributes — Severe CLS Risk
All 64 images on the page are missing explicit `width` and `height` attributes. The browser cannot reserve layout space before the images load, causing layout shifts as each image downloads. With 64 images and a carousel of event thumbnails, this is a significant CLS contributor.

```html
<!-- Current (bad) -->
<img src="logo-mask-group.png" alt="Moss Kulturhus" />

<!-- Required fix -->
<img src="logo-mask-group.png" alt="Moss Kulturhus" width="200" height="80" />
```

**Fix:** Add `width` and `height` to all `<img>` tags. WordPress 5.5+ does this automatically for media library images via `wp_get_attachment_image()` — ensure the theme is calling this properly, not outputting raw `<img src>` HTML.

---

### 4. Zero Images Use Lazy Loading
No `loading="lazy"` attribute is present on any of the 64 images. The lazysizes library is loaded (and blocks render to do so), but it is not being applied — `data-src` attributes are absent from all `<img>` tags. This means all 64 images are requested on page load, competing for bandwidth with the LCP image.

Additionally, lazysizes version **1.2.2** is loaded from cdnjs. The current release is **5.3.x**. This version is approximately 10 years old.

**Fix:** Use native `loading="lazy"` on all below-the-fold images (supported in all modern browsers). Remove lazysizes entirely or upgrade to 5.x if custom behavior is needed. Add `loading="eager"` + `fetchpriority="high"` only on the LCP image.

---

### 5. Caching Disabled at the WP Engine / Cloudflare Layer
From observed response headers:
- `X-Cache-Enabled: False` — WP Engine page caching is off
- `cf-cache-status: DYNAMIC` — Cloudflare is bypassing its cache and proxying every request to origin
- `Cache-Control: max-age=600` — only 10 minutes TTL on the HTML document

Every page view hits the WP Engine origin server. With no edge caching, TTFB will be elevated for all users, directly worsening LCP.

**Fix:** Enable WP Engine's page caching for the homepage (verify no cart/session cookie is preventing it). Configure Cloudflare Cache Rules to cache static HTML for anonymous users. Target `Cache-Control: max-age=3600` or higher on the HTML. Static assets (CSS/JS/fonts) already have `max-age=31536000` which is correct.

---

## Significant Issues (Medium Impact)

### 6. FontAwesome Loaded as a Blocking External Script
The icon kit `https://use.fontawesome.com/5daed306be.js` is loaded synchronously from a third-party domain. This introduces a DNS lookup + TCP handshake + download on a domain that has no preconnect hint.

There is a `dns-prefetch` for `use.fontawesome.com` but no `preconnect`. DNS-prefetch only resolves the IP; preconnect also pre-establishes the TLS connection.

**Fix options (in order of preference):**
1. Replace Font Awesome icons with inline SVGs or a local self-hosted subset
2. Self-host the Font Awesome kit (eliminates third-party dependency)
3. At minimum: add `<link rel="preconnect" href="https://use.fontawesome.com">` and add `async` or `defer` to the script tag

---

### 7. Google Fonts (Material Symbols) Loaded as Render-Blocking Stylesheet
```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded..." media="all">
```
This is a render-blocking external stylesheet. There is a `preconnect` to `fonts.gstatic.com` but no preconnect to `fonts.googleapis.com` itself.

**Fix:** Use the `media="print" onload` swap pattern or load via JavaScript asynchronously. Add `<link rel="preconnect" href="https://fonts.googleapis.com">` alongside the existing gstatic preconnect.

---

### 8. Hero Image Not Served as Next-Gen Format
The primary hero (`4312x1400_karusell.jpg`, 148 KB) is served as JPEG. Event thumbnail backgrounds are served as WebP (`*-1600x0-c-default.webp`) — so the CMS supports WebP — but the main hero was apparently uploaded as a JPEG and not re-encoded.

The hero is also 4312 px wide. A 1600 px version (matching the event thumbnails) would reduce file size by ~60–70% while remaining visually identical on all real screens.

**Fix:** Re-upload the hero image as WebP/AVIF. Use `srcset` or `<picture>` to serve appropriately sized versions per viewport.

---

### 9. HTML Document Is 190 KB
The homepage HTML payload is 190 KB (before compression). This is large for a homepage and suggests either unminified HTML, excessive inline CSS/JS blocks, or large Divi Builder JSON embedded in the page.

There are 10 inline `<style>` blocks in the `<head>`, including full Gutenberg block styles (`wp-block-heading`, `wp-block-paragraph`, `wp-emoji-styles`, `wp-block-library`) that may not all be used on this page.

**Fix:** Audit which Gutenberg block styles are actually used on the homepage and dequeue unused ones. Consider minifying HTML output (e.g., via WP Rocket or a caching plugin).

---

### 10. No `fetchpriority="high"` on LCP Image
Even if the hero image were converted to an `<img>` element, the browser needs a hint to prioritize it above other resources. Currently no image carries `fetchpriority="high"`.

---

## Lower Priority Issues

### 11. Speculationrules Prefetch Is Configured
A `<script type="speculationrules">` block is present and correctly scoped to exclude admin pages, uploads, and query-string URLs. This is a positive signal for navigation performance. Ensure it does not prefetch pages with dynamic session content.

### 12. Custom Fonts Are Preloaded — Correct Practice
Both `Monterio-Bold.woff2` (19 KB) and `Monterio.woff2` (17 KB) have `<link rel="preload" as="font" crossorigin>` tags at the top of `<head>`. This is implemented correctly and will prevent FOUT for the primary brand font.

### 13. IE Conditional Comments in `<html>` Tag
```html
<!--[if lt IE 7]><html class="no-js ie ie6 lt-ie9 lt-ie8 lt-ie7" lang="nb-NO">
```
These are dead code. IE has 0% market share and these comments add 300+ bytes to every page response. Minor, but worth cleaning up.

### 14. `jquery-migrate` Still Loaded
`jquery-migrate.min.js` is included alongside jQuery 3.7.1. This library exists to support code written for jQuery 1.x. If all plugins/themes are compatible with jQuery 3.x (which they should be in 2026), this script is pure overhead.

---

## Positive Findings

| Item | Status |
|------|--------|
| Brotli compression | Enabled (br) |
| HTTP/2 + HTTP/3 (QUIC) | Supported |
| Custom fonts preloaded | Correct |
| Static asset cache TTL | 1 year (correct) |
| Speculationrules prefetch | Implemented |
| Yoast SEO structured data | Present |
| Canonical tag | Correct |
| Event thumbnail images | Already WebP format |
| DOM element count | ~913 (below 1,500 threshold) |

---

## Prioritized Remediation Plan

| Priority | Fix | Expected Impact | Effort |
|----------|-----|----------------|--------|
| P1 | Add `defer` to all 10 external scripts | LCP -1 to -2s, INP improvement | Low (filter in functions.php) |
| P1 | Enable WP Engine page caching + Cloudflare HTML caching | LCP -0.5 to -1.5s (TTFB) | Low (config change) |
| P1 | Add `<link rel="preload" as="image">` for hero JPEG | LCP -0.5 to -1s | Low |
| P1 | Add `width`/`height` to all `<img>` tags | CLS: FAIL → PASS | Medium |
| P2 | Convert hero to `<img>` with `fetchpriority="high"` | LCP -0.3 to -0.8s | Medium |
| P2 | Re-encode hero as WebP, resize to ≤1600px width | LCP -0.3s, bandwidth -60% | Low |
| P2 | Add `loading="lazy"` to below-fold images | Bandwidth, INP | Low |
| P2 | Remove lazysizes or upgrade to 5.x; remove from `<head>` | LCP -0.2s | Low |
| P2 | Self-host or async-load Font Awesome | LCP -0.2s | Medium |
| P3 | Async-load Google Fonts (Material Symbols) | LCP -0.1s | Low |
| P3 | Remove `jquery-migrate.min.js` | Minor JS parse savings | Low |
| P3 | Audit and dequeue unused Gutenberg block styles | HTML size reduction | Low |

---

## Technical Summary

- **Platform:** WordPress with Divi Builder 4.27.5
- **Hosting:** WP Engine + Cloudflare (caching misconfigured)
- **HTML size:** 190 KB
- **External scripts:** 10 (all blocking, 7 in `<head>`)
- **Stylesheets:** 4 (1 external Google Fonts, render-blocking)
- **Images:** 64 total — 0 WebP/AVIF `<img>` src, 0 with dimensions, 0 lazy-loaded
- **Hero image:** 148 KB JPEG at 4312×1400 px, delivered via CSS background-image
- **Third-party domains:** 10 (fonts.googleapis.com, fonts.gstatic.com, use.fontawesome.com, cdnjs.cloudflare.com, cdn.jsdelivr.net, www.googletagmanager.com, www.moss.kommune.no, www.visitoestfold.com, uustatus.no, breakfast.no)
