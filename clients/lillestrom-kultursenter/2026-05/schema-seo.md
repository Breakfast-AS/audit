# Schema Markup Audit – Lillestrøm Kultursenter
**URL:** https://www.lillestrom-kultursenter.no/
**Audit date:** 2026-05-29 | **Platform:** WordPress + Yoast SEO | **Language:** nb-NO

---

## 1. Current Schema Inventory

| Page type | Schema blocks present |
|---|---|
| Homepage | WebPage, BreadcrumbList, WebSite (single @graph) |
| Event pages | WebPage, BreadcrumbList, WebSite (@graph) + standalone Event block |
| Hall/venue pages | WebPage, ImageObject, BreadcrumbList, WebSite (@graph) |

---

## 2. Validation Results

### 2.1 Homepage @graph

| Block | Status | Notes |
|---|---|---|
| WebPage | PASS | datePublished/dateModified present |
| BreadcrumbList | PASS | Single root item is acceptable for homepage |
| WebSite | FAIL | `description` is an empty string `""` — must be removed or populated |

**Critical gap:** No Organization, LocalBusiness, or PerformingArtsTheater entity. This is the single most impactful missing schema for local SEO and Knowledge Panel eligibility.

---

### 2.2 Event Pages – @graph block

| Block | Status | Notes |
|---|---|---|
| WebPage | PASS | |
| BreadcrumbList | PASS | |
| WebSite | FAIL | Same empty `description` sitewide Yoast output |

---

### 2.3 Event Pages – standalone Event block

| Property | Status | Notes |
|---|---|---|
| `@context` | PASS | `https://schema.org` |
| `@type` | PASS | `Event` |
| `name` | PASS | |
| `startDate` / `endDate` | PASS | ISO 8601 with timezone |
| `eventAttendanceMode` | PASS | OfflineEventAttendanceMode |
| `eventStatus` | PASS | EventScheduled |
| `location.address.streetAddress` | FAIL – CRITICAL | Empty string |
| `location.address.addressLocality` | FAIL – CRITICAL | Empty string |
| `location.address.postalCode` | FAIL – CRITICAL | Empty string |
| `location.address.addressCountry` | PASS | `NO` |
| `image` | PASS | Absolute URL present |
| `offers` | MISSING | No ticket price or booking URL |
| `performer` | MISSING | No artist entity |
| `organizer` | MISSING | No organizer entity |
| `description` | MISSING | Recommended by Google |
| `url` | MISSING | Canonical page URL absent |

**Additional bug:** Some events have `datePublished: "-0001-11-30T00:00:00+00:00"` — this is a Yoast fallback for posts with no valid publish date set in WordPress. Fix by opening each affected event post and setting an explicit Published date. This invalid date can suppress rich results for those events.

---

### 2.4 Hall/Venue Pages

No venue-entity schema present. Only generic WebPage/ImageObject markup. Place and PerformingArtsTheater entity markup is absent — a missed opportunity for Knowledge Panel support and Maps integration.

---

## 3. Issue Priority Ranking

| Priority | Issue | Impact |
|---|---|---|
| P1 – Critical | No Organization/PerformingArtsTheater on homepage | Blocks local Knowledge Panel, NAP consistency, Maps integration |
| P1 – Critical | Event address fields all empty | Google will not display Event rich results without a valid location |
| P2 – High | Event missing `offers` | Ticket/booking CTA cannot appear in Event rich results |
| P2 – High | Event missing `organizer` | Required signal for Google Events experience |
| P2 – High | Invalid datePublished `-0001-11-30` on some events | May suppress rich results for those events |
| P3 – Medium | Event missing `performer` | Reduces richness of Event SERP display |
| P3 – Medium | Event missing `description` and `url` | Google recommendations; aids deduplication |
| P4 – Low | WebSite `description` is empty string | Remove the property or populate it |
| P4 – Low | No Place schema on hall pages | Missed venue-entity markup opportunity |

---

## 4. FAQ / Restricted Schema Note

FAQPage is restricted to government and healthcare sites for Google rich results (August 2023). Do not add FAQPage on this site for Google benefit. If GEO/AI citation discoverability is a priority, FAQPage markup can still benefit LLM indexing — implement at your discretion with that goal clearly stated.

---

## 5. Recommended JSON-LD

### 5.1 Homepage – Organization + PerformingArtsTheater (P1)

Add as a second `<script type="application/ld+json">` block alongside the existing Yoast @graph. Use WPCode or a custom `wp_head` hook — do not modify Yoast's output directly.

```json
{
  "@context": "https://schema.org",
  "@type": ["Organization", "PerformingArtsTheater"],
  "@id": "https://www.lillestrom-kultursenter.no/#organization",
  "name": "Lillestrøm Kultursenter",
  "url": "https://www.lillestrom-kultursenter.no/",
  "logo": {
    "@type": "ImageObject",
    "url": "https://www.lillestrom-kultursenter.no/wp-content/uploads/logo.png",
    "width": 300,
    "height": 100
  },
  "image": "https://www.lillestrom-kultursenter.no/wp-content/uploads/logo.png",
  "description": "Lillestrøm Kultursenter er et kulturhus i hjertet av Lillestrøm med konserter, teater, kino og kulturkafé.",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Kirkegata 11",
    "addressLocality": "Lillestrøm",
    "postalCode": "2000",
    "addressCountry": "NO"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 59.9557,
    "longitude": 11.0518
  },
  "telephone": "+4764845550",
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "10:00",
      "closes": "20:00"
    },
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Saturday"],
      "opens": "11:00",
      "closes": "18:00"
    }
  ],
  "sameAs": [
    "https://www.facebook.com/lillestromkultursenter",
    "https://www.instagram.com/lillestromkultursenter"
  ],
  "inLanguage": "nb-NO",
  "priceRange": "NOK"
}
```

**Notes:**
- Replace the logo URL with the actual absolute path.
- Verify `geo` coordinates in Google Maps for Kirkegata 11.
- Populate `sameAs` with all verified social profile URLs.
- Update `openingHoursSpecification` to match actual box office hours.
- The dual `@type` array `["Organization", "PerformingArtsTheater"]` is valid Schema.org.
- The `@id` value `#organization` is referenced by the Event `organizer` block below, forming a cross-page entity graph.

---

### 5.2 Event Pages – Fixed and Complete Event Schema (P1 + P2)

```json
{
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "Kulturkafé – Trond Granlund Trio",
  "url": "https://www.lillestrom-kultursenter.no/program/17666-kulturkafe-trond-granlund-trio/",
  "description": "Bli med på Kulturkafé med Trond Granlund Trio. En intim konsertopplevelse med god mat og musikk i hjertelig stemning.",
  "startDate": "2027-02-18T12:00:00+01:00",
  "endDate": "2027-02-18T13:00:00+01:00",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "eventStatus": "https://schema.org/EventScheduled",
  "image": [
    "https://storage.googleapis.com/example/trond-granlund-trio.jpg"
  ],
  "location": {
    "@type": "Place",
    "name": "Lillestrøm Kultursenter",
    "url": "https://www.lillestrom-kultursenter.no/",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "Kirkegata 11",
      "addressLocality": "Lillestrøm",
      "postalCode": "2000",
      "addressCountry": "NO"
    },
    "geo": {
      "@type": "GeoCoordinates",
      "latitude": 59.9557,
      "longitude": 11.0518
    }
  },
  "organizer": {
    "@type": "Organization",
    "@id": "https://www.lillestrom-kultursenter.no/#organization",
    "name": "Lillestrøm Kultursenter",
    "url": "https://www.lillestrom-kultursenter.no/"
  },
  "performer": {
    "@type": "MusicGroup",
    "name": "Trond Granlund Trio"
  },
  "offers": {
    "@type": "Offer",
    "name": "Standard billett",
    "url": "https://www.lillestrom-kultursenter.no/program/17666-kulturkafe-trond-granlund-trio/",
    "price": "150",
    "priceCurrency": "NOK",
    "availability": "https://schema.org/InStock",
    "validFrom": "2026-01-01T00:00:00+01:00"
  }
}
```

**Notes:**
- `performer.@type`: use `MusicGroup` for bands, `Person` for solo artists, `TheaterGroup` for theatre, `DanceGroup` for dance.
- `offers.price` is a plain number string (no currency symbol). For free events use `"price": "0"`.
- `offers.availability` should switch to `https://schema.org/SoldOut` when sold out.

---

### 5.3 Hall/Venue Pages – Place Schema (P4)

```json
{
  "@context": "https://schema.org",
  "@type": "Place",
  "@id": "https://www.lillestrom-kultursenter.no/hall/stjernesalen/#place",
  "name": "Stjernesalen – Lillestrøm Kultursenter",
  "url": "https://www.lillestrom-kultursenter.no/hall/stjernesalen/",
  "description": "Stjernesalen er en av salene på Lillestrøm Kultursenter med profesjonelt sceneapparat.",
  "containedInPlace": {
    "@type": "PerformingArtsTheater",
    "@id": "https://www.lillestrom-kultursenter.no/#organization",
    "name": "Lillestrøm Kultursenter"
  },
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Kirkegata 11",
    "addressLocality": "Lillestrøm",
    "postalCode": "2000",
    "addressCountry": "NO"
  }
}
```

---

## 6. WebSite Description Fix

```php
add_filter( 'wpseo_schema_website', function( $data ) {
    if ( empty( $data['description'] ) ) {
        unset( $data['description'] );
    }
    return $data;
} );
```

Alternatively, set a site tagline under Settings > General in WordPress.

---

## 7. Implementation Checklist

- [ ] **P1** Add Organization/PerformingArtsTheater block to homepage (section 5.1)
- [ ] **P1** Fix Event address fields — streetAddress, addressLocality, postalCode (section 5.2)
- [ ] **P2** Add `offers` to all Event schema blocks
- [ ] **P2** Add `organizer` to all Event schema blocks
- [ ] **P2** Fix invalid `-0001-11-30` datePublished by setting explicit publish dates in WordPress
- [ ] **P3** Add `performer` to Event schema blocks
- [ ] **P3** Add `description` and `url` to Event schema blocks
- [ ] **P4** Fix or remove empty `description` on WebSite entity (section 6)
- [ ] **P4** Add Place schema to individual hall pages (section 5.3)

---

## 8. Validation Tools

- Google Rich Results Test: https://search.google.com/test/rich-results
- Schema.org validator: https://validator.schema.org/
- Google Search Console > Enhancements (for live coverage reports after indexing)
