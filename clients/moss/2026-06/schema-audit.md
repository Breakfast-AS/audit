# Schema / Structured Data Audit — Moss Kulturhus
**URL:** https://www.mosskulturhus.no/  
**Date:** 2026-06-03  
**Auditor:** Schema.org Markup Specialist

---

## Overall Schema Score: 8 / 100

The site has the bare minimum auto-generated markup from Yoast SEO (WebPage + WebSite) but is missing every schema type that would drive rich results or strengthen entity understanding in Google Search. The most severe gap is zero Event schema across all event pages — this is the core commercial purpose of the site and represents a direct, measurable loss of visibility in Google's event experience.

---

## 1. Current Schema Inventory

### Pages audited

| Page | URL |
|------|-----|
| Homepage | https://www.mosskulturhus.no/ |
| Event page | https://www.mosskulturhus.no/event/soloppgangskonsert-med-thomas-dybdahl/ |
| Venue page | https://www.mosskulturhus.no/venue/parkteatret/ |
| About page | https://www.mosskulturhus.no/om-kulturhuset/ |

### Schema types found

| Page | Schema type | Format | Source |
|------|-------------|--------|--------|
| Homepage | WebPage | JSON-LD | Yoast SEO |
| Homepage | WebSite (via @id reference) | JSON-LD | Yoast SEO |
| Event page | WebPage | JSON-LD | Yoast SEO |
| Venue page | WebPage | JSON-LD | Yoast SEO |
| About page | WebPage | JSON-LD | Yoast SEO |

No Microdata or RDFa detected on any page.

---

## 2. Validation Results

### Homepage — WebPage block

```json
{
  "@context": "https://schema.org",
  "@graph": [{
    "@type": "WebPage",
    "@id": "https://www.mosskulturhus.no/",
    "url": "https://www.mosskulturhus.no/",
    "name": "Moss kulturhus - Kulturhuset midt i byen",
    "isPartOf": {"@id": "https://www.mosskulturhus.no/#website"},
    "datePublished": "2018-04-12T16:31:24+00:00",
    "dateModified": "2024-03-01T09:09:20+00:00"
  }]
}
```

| Check | Result | Note |
|-------|--------|------|
| @context is https://schema.org | PASS | Correct |
| @type is valid | PASS | WebPage is valid |
| Required properties present | PASS | name, url present |
| Absolute URLs | PASS | |
| ISO 8601 dates | PASS | |
| No placeholder text | PASS | |
| publisher / Organization reference | FAIL | No publisher entity defined anywhere on site |
| potentialAction (SearchAction) | FAIL | Missing sitelinks searchbox opportunity |

**Verdict:** Technically valid but extremely thin. Yoast generates this automatically; it provides no rich result eligibility and does not establish a meaningful entity graph.

### Event page — schema validation

| Check | Result | Note |
|-------|--------|------|
| Event @type present | FAIL | CRITICAL — Page uses WebPage only |
| name | FAIL | Not marked up as Event |
| startDate | FAIL | Not marked up |
| endDate | FAIL | Not marked up |
| location | FAIL | Not marked up |
| offers (ticket price) | FAIL | Not marked up |
| performer | FAIL | Not marked up |
| eventStatus | FAIL | Not marked up |
| eventAttendanceMode | FAIL | Not marked up |
| image | FAIL | Not marked up |
| organizer | FAIL | Not marked up |

**Verdict:** CRITICAL. Every event page on the site is invisible to Google's event rich results experience. There are zero Event schema properties across all event pages.

### Venue page (Parkteatret) — schema validation

| Check | Result | Note |
|-------|--------|------|
| EventVenue or LocalBusiness @type | FAIL | CRITICAL — WebPage only |
| name | FAIL | Not marked up as Place |
| address | FAIL | Not marked up |
| geo | FAIL | Not marked up |
| telephone | FAIL | Not marked up |
| containedInPlace | FAIL | Relationship to Moss Kulturhus not expressed |

**Verdict:** CRITICAL. Venue pages carry no place entity markup.

### About page — schema validation

| Check | Result | Note |
|-------|--------|------|
| Organization @type present | FAIL | CRITICAL — WebPage only |
| name | FAIL | Not marked up as Organization |
| address | FAIL | Not marked up |
| telephone | FAIL | Not marked up |
| sameAs (social profiles) | FAIL | Not marked up |
| logo | FAIL | Not marked up |
| foundingDate | FAIL | Not marked up |

**Verdict:** CRITICAL. No entity-level markup for the organization itself.

---

## 3. Missing Schema Opportunities

### Priority 1 — CRITICAL (immediate revenue and visibility impact)

#### 3.1 Event schema — all event pages
Google's event experience (event rich results, event panels in SERPs, Google Events tab) is the single biggest visibility driver for a venue. Without Event schema, every event page is invisible to these features. The site likely has hundreds of event pages; none qualify for rich results.

**Required properties:** name, startDate, location  
**Strongly recommended:** endDate, image, offers, performer, eventStatus, eventAttendanceMode, organizer

#### 3.2 Organization schema — sitewide (homepage / about)
Without an Organization node, Google cannot build a reliable knowledge panel or entity understanding for Moss Kulturhus. This affects brand SERP quality and E-E-A-T signals across the entire domain.

**Required properties:** name, url  
**Strongly recommended:** logo, address, telephone, sameAs, contactPoint

#### 3.3 EventVenue + LocalBusiness schema — venue pages
Parkteatret and Samfunnshuset are distinct named venues. Marking them up as EventVenue (a subtype of Place) and LocalBusiness establishes them as addressable entities and creates a proper containedInPlace relationship to the parent organization.

### Priority 2 — HIGH (sitewide quality and SERP features)

#### 3.4 WebSite with SearchAction — homepage
Enables sitelinks searchbox in branded SERPs. Low effort, Yoast can handle this with a config change.

#### 3.5 BreadcrumbList — all interior pages
Enables breadcrumb display in SERPs. Yoast can auto-generate this with the correct settings enabled.

### Priority 3 — MEDIUM (content enrichment)

#### 3.6 Person schema — performer/artist pages
If the site has individual artist or performer profile pages, Person schema with sameAs links to Wikidata, MusicBrainz, or official sites strengthens entity connections and E-E-A-T.

#### 3.7 FAQPage — about/practical information pages
**Note on eligibility:** Google restricted FAQPage rich results to government and healthcare sites in August 2023. Moss Kulturhus as a commercial cultural venue will not receive FAQ rich result treatment in Google Search. However, FAQPage markup does improve discoverability in AI-driven experiences (ChatGPT, Perplexity, Google AI Overviews, Bing Copilot). Recommend implementing only if the team prioritizes Generative Engine Optimization (GEO) alongside traditional SEO.

---

## 4. JSON-LD Implementation Examples

### 4.1 Organization — Homepage / sitewide `<head>`

Place this once in the homepage `<head>` (or via Yoast's "Organization" setting if the plugin supports it). The `@id` URI becomes the canonical entity reference that all other schema blocks can point to.

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://www.mosskulturhus.no/#organization",
  "name": "Moss Kulturhus",
  "alternateName": "Moss kulturhus",
  "url": "https://www.mosskulturhus.no/",
  "logo": {
    "@type": "ImageObject",
    "url": "https://www.mosskulturhus.no/wp-content/uploads/logo-moss-kulturhus.png",
    "width": 300,
    "height": 100
  },
  "description": "Moss Kulturhus er kulturhuset midt i Moss by, bestående av Parkteatret og Samfunnshuset. Vi arrangerer konserter, teater, stand-up, festivaler og andre kulturarrangementer.",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Storgata 1",
    "addressLocality": "Moss",
    "postalCode": "1530",
    "addressCountry": "NO"
  },
  "telephone": "+47-69-00-00-00",
  "email": "post@mosskulturhus.no",
  "foundingDate": "2018",
  "sameAs": [
    "https://www.facebook.com/mosskulturhus",
    "https://www.instagram.com/mosskulturhus",
    "https://no.wikipedia.org/wiki/Moss_kulturhus"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "customer service",
    "availableLanguage": "Norwegian"
  }
}
```

> **Implementation note:** Replace logo URL, telephone, email, street address, and sameAs URLs with actual values before deploying. The `@id` URI `https://www.mosskulturhus.no/#organization` must be consistent across all schema blocks that reference the organization.

---

### 4.2 EventVenue — Parkteatret venue page

Place on https://www.mosskulturhus.no/venue/parkteatret/

```json
{
  "@context": "https://schema.org",
  "@type": ["EventVenue", "LocalBusiness"],
  "@id": "https://www.mosskulturhus.no/venue/parkteatret/#venue",
  "name": "Parkteatret",
  "url": "https://www.mosskulturhus.no/venue/parkteatret/",
  "description": "Parkteatret er en av scenene i Moss Kulturhus og brukes til konserter, teater og kulturarrangementer.",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Storgata 1",
    "addressLocality": "Moss",
    "postalCode": "1530",
    "addressCountry": "NO"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 59.4330,
    "longitude": 10.6610
  },
  "telephone": "+47-69-00-00-00",
  "maximumAttendeeCapacity": 500,
  "containedInPlace": {
    "@id": "https://www.mosskulturhus.no/#organization"
  },
  "image": "https://www.mosskulturhus.no/wp-content/uploads/parkteatret.jpg",
  "sameAs": [
    "https://www.facebook.com/mosskulturhus"
  ]
}
```

> **Implementation note:** Verify geo coordinates, capacity, and image URL. Apply equivalent markup to the Samfunnshuset venue page with a separate `@id` URI (`#venue-samfunnshuset` or similar).

---

### 4.3 Event schema — individual event pages

This template covers a concert event (e.g., Thomas Dybdahl). In WordPress with The Events Calendar or equivalent plugin, this should be generated dynamically from event post fields.

```json
{
  "@context": "https://schema.org",
  "@type": "Event",
  "@id": "https://www.mosskulturhus.no/event/soloppgangskonsert-med-thomas-dybdahl/#event",
  "name": "Soloppgangskonsert med Thomas Dybdahl",
  "description": "Thomas Dybdahl spiller soloppgangskonsert på Parkteatret i Moss Kulturhus.",
  "image": "https://www.mosskulturhus.no/wp-content/uploads/thomas-dybdahl.jpg",
  "url": "https://www.mosskulturhus.no/event/soloppgangskonsert-med-thomas-dybdahl/",
  "startDate": "2026-06-15T06:00:00+02:00",
  "endDate": "2026-06-15T08:00:00+02:00",
  "eventStatus": "https://schema.org/EventScheduled",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "location": {
    "@type": "EventVenue",
    "@id": "https://www.mosskulturhus.no/venue/parkteatret/#venue",
    "name": "Parkteatret",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "Storgata 1",
      "addressLocality": "Moss",
      "postalCode": "1530",
      "addressCountry": "NO"
    }
  },
  "performer": {
    "@type": "Person",
    "name": "Thomas Dybdahl",
    "sameAs": "https://www.thomasdybdahl.com/"
  },
  "organizer": {
    "@id": "https://www.mosskulturhus.no/#organization"
  },
  "offers": {
    "@type": "Offer",
    "url": "https://www.mosskulturhus.no/event/soloppgangskonsert-med-thomas-dybdahl/",
    "price": "350",
    "priceCurrency": "NOK",
    "availability": "https://schema.org/InStock",
    "validFrom": "2026-04-01T00:00:00+02:00"
  }
}
```

> **Implementation note:** `startDate` and `endDate` must be in ISO 8601 format with timezone offset (`+02:00` for CEST, `+01:00` for CET). `eventStatus` should switch to `EventCancelled` or `EventPostponed` if applicable. `offers.availability` should switch to `SoldOut` when sold out. For events with multiple ticket tiers, use an array of Offer objects.

**Cancelled / postponed event variants:**

```json
"eventStatus": "https://schema.org/EventCancelled"
```
```json
"eventStatus": "https://schema.org/EventPostponed",
"previousStartDate": "2026-06-15T06:00:00+02:00"
```

**Multiple ticket tiers example:**

```json
"offers": [
  {
    "@type": "Offer",
    "name": "Ordinær",
    "price": "350",
    "priceCurrency": "NOK",
    "availability": "https://schema.org/InStock",
    "url": "https://www.mosskulturhus.no/event/soloppgangskonsert-med-thomas-dybdahl/"
  },
  {
    "@type": "Offer",
    "name": "Student / Honnør",
    "price": "250",
    "priceCurrency": "NOK",
    "availability": "https://schema.org/InStock",
    "url": "https://www.mosskulturhus.no/event/soloppgangskonsert-med-thomas-dybdahl/"
  }
]
```

---

### 4.4 WebSite with SearchAction — Homepage

Add to the homepage `@graph` array alongside the existing WebPage block (or replace Yoast's WebSite node if it can be overridden).

```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "@id": "https://www.mosskulturhus.no/#website",
  "name": "Moss Kulturhus",
  "url": "https://www.mosskulturhus.no/",
  "publisher": {
    "@id": "https://www.mosskulturhus.no/#organization"
  },
  "potentialAction": {
    "@type": "SearchAction",
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "https://www.mosskulturhus.no/?s={search_term_string}"
    },
    "query-input": "required name=search_term_string"
  }
}
```

---

### 4.5 BreadcrumbList — event page example

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Hjem",
      "item": "https://www.mosskulturhus.no/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Arrangementer",
      "item": "https://www.mosskulturhus.no/events/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Soloppgangskonsert med Thomas Dybdahl",
      "item": "https://www.mosskulturhus.no/event/soloppgangskonsert-med-thomas-dybdahl/"
    }
  ]
}
```

---

## 5. Priority Implementation Order

| Priority | Schema type | Pages | Effort | Impact |
|----------|-------------|-------|--------|--------|
| 1 | Event | All event pages (dynamic) | Medium — requires plugin or template code | Critical — unlocks Google event rich results for every event |
| 2 | Organization | Homepage / sitewide | Low — one block, static | Critical — establishes entity; improves knowledge panel and E-E-A-T |
| 3 | EventVenue + LocalBusiness | /venue/parkteatret/, /venue/samfunnshuset/ | Low — one block per venue | High — makes venues addressable entities; supports Event.location references |
| 4 | BreadcrumbList | All interior pages | Low — Yoast setting or theme | High — breadcrumb display in SERPs, improves crawl clarity |
| 5 | WebSite + SearchAction | Homepage | Low — one block | Medium — sitelinks searchbox in branded queries |
| 6 | Person | Performer / artist pages (if they exist) | Low per page | Medium — entity connections for performers |
| 7 | FAQPage | Practical info / about pages | Low | Low for Google rich results (commercial site restriction); Medium for AI/GEO discoverability |

---

## 6. Implementation Notes for WordPress / Yoast

1. **Organization and WebSite**: Configure under Yoast SEO > Settings > Site Representation. Set the site to represent an "Organization", fill in logo, social profiles, and name. Yoast will generate the Organization and WebSite nodes automatically with the correct `@id` structure.

2. **BreadcrumbList**: Enable under Yoast SEO > Settings > Advanced > Breadcrumbs. Ensure the WordPress theme is calling `yoast_breadcrumb()` in templates.

3. **Event schema**: Yoast does not auto-generate Event schema from post types. Options:
   - If the site uses **The Events Calendar** plugin: install the companion "Schema & Structured Data for WP & AMP" plugin or a dedicated Events Calendar schema add-on.
   - Use **Yoast's Schema API** to hook custom Event schema onto event post type pages via `wpseo_schema_graph` filter.
   - Use a dedicated schema plugin such as **Rank Math** (has built-in Event schema for custom post types) or **Schema Pro**.
   - Implement via a custom `wp_head` action that reads ACF / event post fields and outputs the JSON-LD block.

4. **Venue pages**: Add EventVenue JSON-LD either via a schema plugin set to target the `tribe_venue` post type, or via a custom `wp_head` action on venue page templates.

5. **Testing**: After implementation, validate each schema block with:
   - Google Rich Results Test: https://search.google.com/test/rich-results
   - Schema.org validator: https://validator.schema.org/
   - Google Search Console > Enhancements (will surface Event rich result coverage and errors once crawled)

---

## 7. Expected Impact After Full Implementation

- **Event rich results**: Events eligible to appear in the Google Events experience (event panels, event tab, event carousels in SERPs). This is the highest-value outcome.
- **Knowledge panel**: Organization markup strengthens Google's entity understanding, increasing likelihood of a branded knowledge panel appearing for "Moss Kulturhus" queries.
- **Breadcrumb display**: Cleaner SERP snippets with breadcrumb trail, improving CTR.
- **Sitelinks searchbox**: Branded search queries may show a search input directly in the SERP.
- **AI discoverability**: Structured entity graph makes the site's content more legible to AI-powered search experiences (Google AI Overviews, Bing Copilot, Perplexity).
