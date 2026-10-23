# Performance Audit — Lillestrøm Kultursenter

**Audit date:** 2026-05-29
**URL:** https://www.lillestrom-kultursenter.no/
**Hosting:** WP Engine + Cloudflare CDN

---

## Performance Summary

| Metric | Homepage | /program/ | /utleie/ |
|---|---|---|---|
| Server response time (TTFB) | 110ms | 75ms | 120ms |
| HTML size | 72.9 KB | 141.6 KB | 51.7 KB |
| CSS files (render-blocking) | 3 | 3 | 3 |
| JavaScript files | 11 | 11 | 11 |
| JS with async/defer | 0 | 0 | 0 |
| Total images | 6 | 3 | 3 |
| Images with lazy loading | 0 | 0 | 0 |
| WebP images | 3 | 0 | 0 |
| Preload hints | 0 | 0 | 0 |

**Overall Performance Score: 55 / 100**

---

## Critical Issues

### P1 — ALL 11 JavaScript files are render-blocking (no async or defer)

Every script loaded on all pages is synchronous, blocking the browser from rendering content until all JS is parsed and executed.

**Blocking scripts identified:**
- `jquery.min.js` (WordPress core, ver 3.7.1)
- `jquery-migrate.min.js` (ver 3.4.1)
- `scripts.min.js` (theme, ver 1.1.5.3)
- `jquery/ui/core.min.js` (ver 1.13.3)
- `jquery/ui/datepicker.min.js` (ver 1.13.3)
- Plus 6 additional scripts

**Impact:** This directly delays First Contentful Paint (FCP) and Largest Contentful Paint (LCP). For a site where the LCP element is likely an above-the-fold event image, this is a significant ranking signal impairment.

**Fix:**
```php
// Add defer to theme and plugin scripts in functions.php
add_filter('script_loader_tag', function($tag, $handle, $src) {
    $defer_scripts = ['theme-scripts', 'dx-calendar', 'complianz'];
    if (in_array($handle, $defer_scripts)) {
        return str_replace(' src=', ' defer src=', $tag);
    }
    return $tag;
}, 10, 3);
```

For jQuery: WordPress 6.x supports async loading — enable via `wp_script_add_data( 'jquery', 'defer', true )`.

---

### P2 — No lazy loading on any images

All images across all tested pages have no `loading` attribute at all. WordPress 5.5+ sets `loading="lazy"` by default for images added via the media library. The absence suggests images are hardcoded in HTML or theme templates bypassing WordPress image handling.

**Impact:** All images, including below-the-fold images, are loaded on page initialization, increasing Total Blocking Time and extending the time to interactive.

**Fix:**
- For theme images: add `loading="lazy"` to all `<img>` tags that are not the LCP candidate
- For the first/hero image: add `loading="eager"` and `fetchpriority="high"`
- Enable WordPress's native lazy loading filter if disabled:
  ```php
  add_filter('wp_lazy_loading_enabled', '__return_true');
  ```

---

### P3 — No preload hints for critical resources

No `<link rel="preload">` hints exist. The LCP candidate (first event image) and the theme CSS are not preloaded.

**Fix — add to `<head>`:**
```html
<link rel="preload" as="style" href="/wp-content/themes/theme-lillestrom-kultursenter/style.css?version=1.1.5.3">
<link rel="preload" as="image" href="[first-event-image-url]" fetchpriority="high">
```

---

## High Issues

### P4 — /program/ page is 141.6 KB HTML (2× homepage)

The program listing page is significantly larger than other pages, likely because it renders all visible event cards as full HTML server-side. This increases parse time and DOM complexity.

**Fix:**
- Implement pagination or virtual scrolling for event listings (show 12–20 events initially, load more on scroll)
- Alternatively, defer off-screen event cards with Intersection Observer
- Consider a JavaScript-fetched event grid that renders after initial page load

---

### P5 — Event images served from third-party Google Cloud Storage

Event page images are served from `storage.googleapis.com/pim-ambio.appspot.com/...`. This requires:
1. An additional DNS resolution
2. A new TCP connection
3. No Cloudflare optimization (third-party origin)

**Fix:**
- Proxy event images through Cloudflare Images or a WordPress media CDN
- Or configure the PIM (Ambio) to allow Cloudflare to cache these URLs
- Minimum fix: add `<link rel="preconnect" href="https://storage.googleapis.com">` to `<head>`

---

### P6 — No image dimensions set (CLS risk)

No `<img>` tags on audited pages have explicit `width` and `height` attributes. When images load after the initial render, they push content down — causing Cumulative Layout Shift (CLS).

**Fix:** Add `width` and `height` to all `<img>` tags matching the rendered dimensions:
```html
<img src="event.jpg" width="400" height="300" loading="lazy" alt="...">
```

---

## Medium Issues

### P7 — Cache TTL is only 10 minutes

`Cache-Control: max-age=600, must-revalidate` applied site-wide. For pages that change infrequently (Om oss, Utleie, hall pages), this forces Cloudflare to re-validate every 10 minutes.

**Fix via Cloudflare Cache Rules:**
- Static pages: `max-age=86400` (24 hours)
- Event pages: `max-age=3600` (1 hour)
- Homepage: `max-age=1800` (30 minutes, since it changes with new events)

---

### P8 — Moment.js loaded twice

`moment.min.js` AND `moment-with-locales.min.js` are both enqueued. The second is a complete superset (~72 KB minified+gzipped vs ~17 KB for core).

**Fix:** Dequeue `moment.min.js` from `functions.php`:
```php
wp_dequeue_script('moment');
```

---

### P9 — dx-calendar plugin CSS loaded on all pages

`dx-calendar.css` is enqueued globally, including on pages with no calendar. Minor but contributes to render-blocking CSS on non-calendar pages.

**Fix:** Conditionally enqueue only on pages that use the calendar:
```php
if (is_post_type_archive('program') || is_singular('program')) {
    wp_enqueue_style('dx-calendar');
}
```

---

## What Is Working Well

- **TTFB: Excellent** — 75–120ms is in the "Fast" category (< 200ms target). WP Engine + Cloudflare is delivering good origin performance.
- **HTML weight: Good** — Homepage at 73 KB is reasonable; /utleie/ at 52 KB is lean.
- **WebP adoption: Partial** — 3 of 6 homepage images use WebP format. Extend to all event and hall images.
- **Cloudflare CDN: Active** — Cache HIT responses confirm CDN is serving cached content.
- **No Google Fonts** — No external font CDN calls, eliminating a common render-blocking pattern.

---

## Estimated CWV Impact

| Metric | Current estimate | Target | Likely fix |
|---|---|---|---|
| LCP | ~3.0–4.5s (Poor) | < 2.5s | fetchpriority on hero image + defer JS |
| INP | ~200–350ms (Needs Improvement) | < 200ms | Reduce JS parse time (defer all non-critical JS) |
| CLS | ~0.1–0.2 (Needs Improvement) | < 0.1 | Add explicit image dimensions |

---

## Priority Action List

1. **Immediate** — Add `defer` attribute to all non-critical JS scripts
2. **Immediate** — Add `loading="lazy"` to all below-fold images
3. **Immediate** — Add `fetchpriority="high"` + `loading="eager"` to LCP hero image
4. **Short-term** — Add `<link rel="preload">` for theme CSS and hero image
5. **Short-term** — Add explicit `width` and `height` to all `<img>` tags
6. **Short-term** — Add `<link rel="preconnect" href="https://storage.googleapis.com">`
7. **Medium-term** — Increase Cloudflare cache TTL per page type
8. **Medium-term** — Implement /program/ pagination (reduce 141 KB to ~60 KB initial load)
9. **Medium-term** — Dequeue `moment.min.js` (duplicate of `moment-with-locales.min.js`)
10. **Medium-term** — Conditionally load `dx-calendar.css` only on calendar pages
