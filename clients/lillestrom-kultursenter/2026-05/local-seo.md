# Local SEO Audit: Lillestrøm Kultursenter
**URL:** https://www.lillestrom-kultursenter.no/  
**Audit date:** 2026-05-29  
**Auditor:** Local SEO Agent (Claude Sonnet 4.6)

---

## Overall Local SEO Score: 38 / 100

| Dimension | Weight | Score | Weighted |
|-----------|--------|-------|----------|
| GBP Signals | 25% | 20/100 | 5.0 |
| Reviews & Reputation | 20% | 25/100 | 5.0 |
| Local On-Page SEO | 20% | 55/100 | 11.0 |
| NAP Consistency & Citations | 15% | 50/100 | 7.5 |
| Local Schema Markup | 10% | 5/100 | 0.5 |
| Local Link & Authority Signals | 10% | 90/100 | 9.0 |
| **Total** | **100%** | | **38.0** |

**Score rationale:** The site has a strong physical foundation (consistent NAP, clear address visibility, genuine local authority via municipal ownership and 30-year operating history) but is missing nearly all technical local SEO infrastructure: no LocalBusiness schema of any kind, no GBP signals on-page, no review aggregation, and no dedicated local keyword landing pages. The score reflects solid raw material with very poor implementation.

---

## Business Type Detected

**Brick-and-mortar** (confirmed)

Signals:
- Street address "Kirkegata 11, 2000 Lillestrøm" present in footer, contact page, practical info page, and all hall pages
- Physical venue with named halls, capacity figures, booking calendars
- Public transit and parking directions provided
- No "we come to you" or service-area language detected
- No Google Maps iframe found on any page (gap)

---

## Industry Vertical Detected

**Performing Arts / Cultural Center**

Correct schema subtype: `PerformingArtsTheater` (schema.org)  
Secondary applicable types: `EventVenue`, `CivicStructure`

Industry signals detected:
- Named performance halls (Teatersalen 600 pax, Stjernesalen 322 pax, Universet 101 pax, Connect 200 pax, Teatertorget 150 pax, Tellus 180 pax, Sirius, Orion)
- Named meeting rooms (Lillebjørn 12 pax, Himmelrommet 6 pax, Melkeveien 8 pax, Verdensrommet 30 pax)
- Event types: concerts, theatre, musicals, stand-up comedy, lectures, drag bingo, children's shows, jazz cafés
- Conferences and venue rental services
- Mobile stage and tribune rental
- Gift cards, app, newsletter — all typical for cultural venues
- Built 1926, reopened 1991, expanded 2006 — strong heritage signals
- Owned 97% by Lillestrøm kommune through Lillestrøm Kulturbygg AS
- Operated by Stiftelsen Lillestrøm Kulturforum (foundation)

---

## NAP Consistency Audit

| Source | Name | Address | Phone | Email |
|--------|------|---------|-------|-------|
| Homepage (footer) | Lillestrøm Kultursenter | Kirkegata 11, 2000 Lillestrøm | 64 84 55 50 | billett@lillestrom-kultursenter.no |
| Contact page | Lillestrøm Kultursenter | Kirkegata 11, 2000 Lillestrøm | 64 84 55 50 | billett@lillestrom-kultursenter.no |
| Practical info page | Lillestrøm Kultursenter | Kirkegata 11, 2000 Lillestrøm | 64 84 55 50 | billett@lillestrom-kultursenter.no |
| Utleie (rental) page | Lillestrøm Kultursenter | Kirkegata 11, 2000 Lillestrøm | 64 84 55 50 | billett@lillestrom-kultursenter.no |
| Hall pages (Teatersalen, Stjernesalen) | Lillestrøm Kultursenter | Kirkegata 11, 2000 Lillestrøm | 64 84 55 50 | billett@lillestrom-kultursenter.no |
| JSON-LD schema | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT |
| Meta tags | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT |

**NAP consistency verdict: CONSISTENT across visible HTML, but entirely absent from structured data.**

### Flags
- **No country code on phone number.** The number "64 84 55 50" appears without "+47" prefix. Google's NLP and citation matching tools work better with E.164 format: +47 64 84 55 50.
- **Dual email addresses in use.** `billett@lillestrom-kultursenter.no` is the primary displayed email on all pages, but `post@lillestrom-kultursenter.no` is the room rental contact and likely appears in some external citations (e.g., Brønnøysundregistrene). This creates a soft NAP inconsistency for the email field across data sources.
- **No Google Maps embed anywhere.** The address is mentioned in plain text but never linked to or embedded from Google Maps, weakening GBP association signals.
- **Contact page URL is `/kontakt-oss/` but the sitemap shows `/kontakt/`.** Verify which is canonical and whether both exist; duplicate contact pages dilute NAP authority.

---

## GBP Optimization Checklist

| Signal | Status | Notes |
|--------|--------|-------|
| GBP listing claimed | UNKNOWN | Could not verify without authenticated Google access. Must be checked manually. |
| GBP primary category | UNKNOWN | Should be "Kultursenter" or "Performing arts theater." Wrong category = #1 negative ranking factor (Whitespark 2026). |
| GBP address matches website | UNKNOWN | Website address is consistent; GBP match unverified. |
| GBP phone matches website | UNKNOWN | Unverified. |
| GBP hours match website | UNKNOWN | Website hours are Mon-Fri 09:00-20:00, Sat 11:00-15:00, Sun closed. |
| Google Maps iframe on website | MISSING | No embed found on any page, including contact and practical info. |
| Maps/directions link in footer or contact | MISSING | No `maps.google.com` or `goo.gl/maps` links found. |
| GBP posts/updates visible | NOT DETECTED | No post widget or Google Posts feed embedded. |
| Review widget on site | MISSING | No Google review widget, aggregate rating display, or third-party review badge. |
| Place ID reference in HTML | NOT FOUND | No `data-place-id` or Maps embed with place reference detected. |
| GBP photos evidence | UNKNOWN | Cannot verify without GBP access. |
| GBP Q&A present | UNKNOWN | Unverified. |
| GBP Products/Services filled | UNKNOWN | Unverified. Cultural venues should list key event types as services. |

**GBP dimension score: 20/100.** The venue almost certainly has a GBP listing (major cultural center, 97% municipality-owned) but there are zero on-page signals connecting the website to the GBP listing. A Maps embed, a direct "Finn oss på Google Maps" link, and a review CTA would immediately strengthen this signal.

---

## Review Health Snapshot

| Source | Rating | Review Count | Response Rate | Last Review |
|--------|--------|--------------|---------------|-------------|
| Website (aggregateRating schema) | NOT PRESENT | NOT PRESENT | N/A | N/A |
| Google (on-page evidence) | NOT DETECTED | NOT DETECTED | NOT DETECTED | NOT DETECTED |
| TripAdvisor | NOT FOUND (404) | NOT FOUND | N/A | N/A |
| Facebook | NOT ACCESSIBLE | NOT ACCESSIBLE | N/A | N/A |
| Yelp | NOT ACCESSIBLE (403) | NOT ACCESSIBLE | N/A | N/A |

**Review health verdict: CRITICAL GAP.**

The website has no review signals of any kind. No `aggregateRating` in schema, no star display, no review count, no testimonials, no "read our Google reviews" link. For a cultural venue of this size and 30-year history, this is a significant missed opportunity.

**Sterling Sky 18-day review velocity rule:** If the GBP listing goes 18+ days without a new review, ranking in the local pack drops measurably. Without a review acquisition strategy (post-event email, ticket confirmation CTA, signage), velocity will stall.

**Recommendation:** Add a "Vi setter pris på din tilbakemelding" review CTA linking to the GBP review form in post-purchase ticket confirmation emails and on the practical info / contact pages.

---

## Local Schema Markup Validation

### Current state
- **LocalBusiness schema:** NOT PRESENT
- **Organization schema:** NOT PRESENT
- **PerformingArtsTheater schema:** NOT PRESENT
- **Event schema:** NOT PRESENT (despite having a full event calendar with event-sitemap.xml)
- **AggregateRating schema:** NOT PRESENT
- **OpeningHoursSpecification:** NOT PRESENT
- **Geo (latitude/longitude):** NOT PRESENT
- Only detected schema type: generic `WebPage` (via Yoast SEO default output)

### Correct schema subtype
Per schema.org, the correct type hierarchy for this venue is:

```
Thing > Place > LocalBusiness > EntertainmentBusiness > PerformingArtsTheater
```

`PerformingArtsTheater` is the most specific and correct type. Do not use the generic `LocalBusiness` as the primary type.

### Required properties (missing)
- `name` — missing from schema (present in HTML only)
- `address` (PostalAddress) — missing from schema
- `telephone` — missing from schema

### Recommended properties (all missing)
- `geo` with 5-decimal precision: `"latitude": 59.95602, "longitude": 11.04885` (verify against GBP)
- `openingHoursSpecification` — structured hours for Mon-Fri and Sat
- `url` — canonical URL
- `image` — venue photograph
- `priceRange` — applicable for ticket sales
- `sameAs` — array linking to GBP, Facebook, Instagram, Brønnøysundregistrene
- `description` — Norwegian-language venue description
- `currenciesAccepted` — "NOK"
- `paymentAccepted`

### Recommended JSON-LD for homepage `<head>`

```json
{
  "@context": "https://schema.org",
  "@type": "PerformingArtsTheater",
  "@id": "https://www.lillestrom-kultursenter.no/#kultursenter",
  "name": "Lillestrøm Kultursenter",
  "url": "https://www.lillestrom-kultursenter.no/",
  "telephone": "+4764845550",
  "email": "billett@lillestrom-kultursenter.no",
  "description": "Lillestrøm Kultursenter er en kulturinstitusjon i hjertet av Lillestrøm med konserter, teater, musikaler, stand-up, foredrag og utleie av saler og konferanserom.",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Kirkegata 11",
    "addressLocality": "Lillestrøm",
    "postalCode": "2000",
    "addressCountry": "NO"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 59.95602,
    "longitude": 11.04885
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
      "opens": "09:00",
      "closes": "20:00"
    },
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": "Saturday",
      "opens": "11:00",
      "closes": "15:00"
    }
  ],
  "image": "https://www.lillestrom-kultursenter.no/[featured-image-url]",
  "sameAs": [
    "https://www.facebook.com/LillestromKultursenter/",
    "https://www.instagram.com/lillestromkultursenter/"
  ],
  "currenciesAccepted": "NOK",
  "inLanguage": "nb-NO",
  "foundingDate": "1991",
  "founder": {
    "@type": "Organization",
    "name": "Lillestrøm kommune"
  }
}
```

**Note:** Verify geo coordinates against the Google Maps pin for the GBP listing before publishing. The coordinates above are an approximation for Kirkegata 11, 2000 Lillestrøm.

### Event schema opportunity
The site has an `event-sitemap.xml` suggesting many individual event pages. Each event page should carry `Event` schema:

```json
{
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "[Event name]",
  "startDate": "[ISO 8601 datetime]",
  "endDate": "[ISO 8601 datetime]",
  "eventStatus": "https://schema.org/EventScheduled",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "location": {
    "@type": "Place",
    "name": "Lillestrøm Kultursenter",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "Kirkegata 11",
      "addressLocality": "Lillestrøm",
      "postalCode": "2000",
      "addressCountry": "NO"
    }
  },
  "organizer": {
    "@type": "Organization",
    "name": "Lillestrøm Kultursenter",
    "url": "https://www.lillestrom-kultursenter.no/"
  },
  "offers": {
    "@type": "Offer",
    "url": "[ticket URL]",
    "priceCurrency": "NOK",
    "availability": "https://schema.org/InStock"
  }
}
```

Yoast SEO does not generate Event schema automatically. Use The Events Calendar + Schema Pro plugin, or implement via custom code/ACF.

---

## Citation Presence Status (Norwegian Tier 1 Directories)

| Directory | Status | Notes |
|-----------|--------|-------|
| Google Business Profile | UNKNOWN | Cannot verify without live GBP API access. Priority #1 to verify. |
| Gule Sider (gulesider.no) | NOT ACCESSIBLE (403) | Blocked to scrapers; likely listed given venue age. Verify manually. |
| 1881.no | NOT FOUND (404 on search) | Verify manually at 1881.no |
| Brønnøysundregistrene (brreg.no) | LIKELY LISTED | 97% municipality-owned; organization should be in Enhetsregisteret. Operator "Stiftelsen Lillestrøm Kulturforum" should have its own org.nr. Verify NAP matches. |
| TripAdvisor | NOT FOUND (404) | Not listed or listing URL has changed. Cultural venues of this size should be on TripAdvisor. Create listing. |
| Facebook Business Page | EXISTS | facebook.com/LillestromKultursenter/ confirmed active. Rating/review data not accessible. |
| Instagram | EXISTS | instagram.com/lillestromkultursenter/ confirmed. |
| Yelp | NOT ACCESSIBLE (403) | Low priority for Norway — Yelp has minimal Norwegian market presence. |
| Eventbrite.no | UNKNOWN | Worth listing events here for additional local citations and discovery. |
| Ticketmaster.no / Billettservice | UNKNOWN | Major Norwegian ticket platforms = high-authority local citations. |
| Visit Lillestrøm / Visit Romerike | UNKNOWN | Municipal tourism sites are high-value Norwegian local citations. Verify at visitlillestrom.no or romerike.no. |
| Kulturdatabasen (kulturrad.no) | UNKNOWN | Kulturrådet maintains a database of Norwegian cultural institutions. High-authority citation for this vertical. |
| Wikipedia (Norwegian) | UNKNOWN | A venue founded in 1926 with municipal ownership warrants a Wikipedia stub. |

**Norwegian-specific citation note:** For Norwegian local SEO, the most impactful Tier 1 citations beyond GBP are: Gule Sider, 1881.no, Brønnøysundregistrene, and vertical-specific directories like Billettservice, Ticketmaster, and Kulturrådet. Yelp and BBB are irrelevant in the Norwegian market.

---

## Local On-Page SEO Assessment

### Homepage
- **Title tag:** "Lillestrøm Kultursenter - Du kan bare begynne å glede deg!" — Brand present, no local keyword (e.g., "Lillestrøm"). Acceptable for homepage since brand = location name.
- **Meta description:** Not explicitly confirmed as present. Must be verified; Yoast SEO may have left it auto-generated.
- **H1:** Likely brand name. Not confirmed.
- **Local keyword density:** Low. Content is event-focused (individual show titles) rather than category-focused ("konserter Lillestrøm", "teater Lillestrøm").
- **Maps embed:** MISSING.

### Contact / Practical Info pages
- **Meta description on contact page:** MISSING (confirmed in audit brief).
- **Opening hours in text:** Present on praktisk-informasjon page.
- **Maps embed:** MISSING on both.
- **Directions link:** MISSING.
- **Schema on contact page:** MISSING.

### Hall pages (12 pages: Teatersalen, Stjernesalen, Universet, etc.)
- **Unique content:** YES — each hall has distinct technical specs, dimensions, capacity, and booking calendar data.
- **Schema markup:** NONE on any hall page.
- **Meta descriptions:** Not confirmed; likely auto-generated.
- **Local keyword integration:** None detected. "Teatersalen Lillestrøm" or "konferansesal Lillestrøm" not used in titles or H1s.
- **Maps embed per hall:** MISSING.
- **Doorway page risk:** LOW — content is sufficiently unique per hall (specific m², rigging specs, booking calendars).

### Rental / Conference page (`/utleie/moter-kurs-og-konferanse/`)
- **Title:** "Møte, konferanse og event - Lillestrøm Kultursenter" — Good keyword targeting; lacks city name.
- **Recommended title:** "Konferanserom & møtelokaler i Lillestrøm | Lillestrøm Kultursenter"
- **Local keyword opportunity:** "konferanselokale Lillestrøm", "møterom Lillestrøm", "event venue Lillestrøm" — none currently in visible headings.

### Missing local landing pages
The following high-value local keyword combinations have no dedicated pages:

| Target keyword (Norwegian) | Monthly intent | Status |
|---------------------------|----------------|--------|
| konserter i Lillestrøm | High | No dedicated page |
| teater Lillestrøm | Medium | No dedicated page |
| konferanselokale Lillestrøm | High commercial | Partial (/utleie/moter-kurs-og-konferanse/) |
| kultursenter Lillestrøm | Brand/navigational | Homepage |
| stand-up Lillestrøm | Medium | No dedicated page |
| selskapslokale Lillestrøm | Medium commercial | No dedicated page |
| musikal Lillestrøm | Low-medium | No dedicated page |

---

## Location Page Quality (Hall Pages)

The site has 12 hall/room pages under `/hall/[hall-name]/`. This is not a multi-location site (single physical address), but the hall pages function as sub-location/sub-service pages.

| Criterion | Status |
|-----------|--------|
| Unique content per page | YES — specs, capacity, dimensions, calendar differ per hall |
| Address/NAP on each page | YES (in footer) |
| Schema on each page | NO — none of the 12 hall pages have schema |
| Internal linking from parent page | YES — `/utleie/vare-saler/` links to all halls |
| Meta descriptions on hall pages | UNKNOWN — likely auto-generated by Yoast |
| Local keyword in title | NO — titles are just hall names ("Teatersalen", "Stjernesalen") |
| Doorway page risk | LOW — genuinely distinct content |

**Recommended improvement:** Add `@type: "Place"` or `"Room"` schema to each hall page with `containedInPlace` pointing to the main `PerformingArtsTheater` schema. Add "i Lillestrøm" to page titles where it fits naturally (e.g., "Teatersalen — Lillestrøm Kultursenter").

---

## Local Link & Authority Signals

This dimension scores highest (90/100) due to the venue's unique position:

**Strong signals:**
- 97% owned by Lillestrøm kommune — government entity ownership creates unmatched local authority
- "Kulturkvartalet" project — officially integrated into city development plans
- Regional bank sponsors listed in footer (Romerike Sparebank, Strømmen Sparebank) — likely generating .no authority links
- Operating since 1991 with continuous operations — domain age and link age
- Domain `lillestrom-kultursenter.no` contains exact local keyword — strong local relevance signal
- Active Facebook page (`facebook.com/LillestromKultursenter/`) — social citation
- Active Instagram (`instagram.com/lillestromkultursenter/`) — social citation
- Likely listed in Lillestrøm kommune's own website as cultural partner — high-authority .kommune.no link

**Gaps:**
- No Wikipedia page despite the venue's age and municipal importance
- No Kulturrådet listing confirmed
- No Ticketmaster/Billettservice profile confirmed (these would be very high-authority citation links for this vertical)

---

## Top 10 Prioritized Actions

### CRITICAL

**1. Implement PerformingArtsTheater JSON-LD schema on the homepage**
- Priority: Critical
- Effort: Low (copy-paste JSON-LD block above into `<head>` via Yoast SEO > Search Appearance > Schema, or via a custom plugin)
- Impact: Enables Knowledge Panel, rich results, local pack eligibility with correct schema type
- The site has Yoast SEO installed — use the "Organization" or "Local Business" setting under SEO > Search Appearance, or install Yoast Local SEO (paid add-on) for full local schema support
- Verify and correct geo coordinates before publishing

**2. Claim and fully optimize Google Business Profile**
- Priority: Critical
- Effort: Medium
- Impact: GBP is the #1 local ranking factor (Whitespark 2026 score: 193 for correct primary category)
- Actions: Verify listing claimed, set primary category to "Performing arts theater" (or closest Norwegian equivalent), fill all secondary categories (Concert hall, Conference center, Event venue), add full hours including "open 1 hour before shows" as special hours, upload 20+ photos, add all services, write a Norwegian-language business description
- Monitor review velocity — target minimum 1 new review per 18 days to avoid ranking cliff

**3. Add Event schema to all event pages**
- Priority: Critical
- Effort: Medium-High (requires plugin or developer work for Yoast + The Events Calendar integration)
- Impact: Event rich results in Google Search and Google Events discovery — massive visibility for a venue of this type
- Use The Events Calendar plugin with Schema Pro, or add custom JSON-LD output to the event post template
- This is the single highest-traffic opportunity given the volume of events in the sitemap

### HIGH

**4. Embed Google Maps iframe on contact and practical information pages**
- Priority: High
- Effort: Low (10 minutes)
- Impact: Strengthens GBP association, provides user value, adds a GBP signal to the page
- Add the embed from Google Maps > Share > Embed a map, using the exact GBP listing pin (not a generic address search)
- Also add a "Finn oss på Google Maps" text link in the footer next to the address

**5. Add E.164 format phone number sitewide and in all schema**
- Priority: High
- Effort: Low
- Impact: Consistent citation matching across all directories
- Change all instances of "64 84 55 50" to "+47 64 84 55 50" in footer, contact page, and schema markup

**6. Implement review acquisition strategy**
- Priority: High
- Effort: Medium
- Impact: Review velocity is confirmed as a top-3 local ranking factor (Sterling Sky 18-day rule)
- Add a review CTA to: ticket purchase confirmation emails, the practical information page, and physical signage in the lobby
- Text suggestion: "Likte du opplevelsen? Del din mening på Google — det hjelper oss nå flere!"
- Add `aggregateRating` schema once reviews accumulate (minimum 5 needed for Google rich snippets)

**7. Add country code and verify NAP on all Norwegian Tier 1 directories**
- Priority: High
- Effort: Medium
- Impact: Citation consistency is the #3-#5 AI visibility factor (Whitespark 2026)
- Directories to audit: Gule Sider, 1881.no, Brønnøysundregistrene (both Lillestrøm Kulturbygg AS and Stiftelsen Lillestrøm Kulturforum), Facebook, Ticketmaster.no, Billettservice.no, visitlillestrom.no
- Ensure NAP format is identical across all: "Lillestrøm Kultursenter, Kirkegata 11, 2000 Lillestrøm, +47 64 84 55 50"

### MEDIUM

**8. Optimize meta titles and descriptions for local keywords on commercial pages**
- Priority: Medium
- Effort: Low
- Impact: Click-through rate improvement for local searches
- `/utleie/moter-kurs-og-konferanse/` — change title to "Konferanserom & møtelokaler i Lillestrøm | Lillestrøm Kultursenter"
- `/kontakt-oss/` — add meta description with NAP and hours
- All 12 hall pages — append " | Lillestrøm Kultursenter" if not already present; consider "Sal til leie i Lillestrøm" framing for conference-focused halls
- Write unique meta descriptions for all hall pages

**9. Create a TripAdvisor listing**
- Priority: Medium
- Effort: Low (15-minute form submission)
- Impact: High-authority citation, review aggregation for international and domestic visitors
- The 404 result suggests the venue is not listed; submit at tripadvisor.com/GetListedNew

**10. Add `sameAs` links and build structured internal linking for local topical authority**
- Priority: Medium
- Effort: Low-Medium
- Impact: Signals brand entity completeness to Google's Knowledge Graph; supports AI Overview visibility (3 of top 5 AI visibility factors are citation-related per Whitespark 2026)
- Add `sameAs` array in schema pointing to: Facebook page, Instagram profile, Brønnøysundregistrene org.nr page, Wikipedia (once created), Kulturrådet profile
- Create a Wikipedia stub article about the venue (1926 founding, municipal ownership, 2006 expansion) — this is achievable given the documented history
- Review internal linking: ensure `/program/` links to each event category, and `/utleie/` links to all 12 hall pages with anchor text containing hall name + "Lillestrøm"

---

## Proximity Note

Proximity accounts for 55.2% of local pack ranking variance (Search Atlas ML study, 2025). This is outside the venue's control — the physical location at Kirkegata 11, 2000 Lillestrøm is fixed. However, precise geo coordinates in schema (5-decimal precision) and a correctly pinned GBP listing ensure Google uses the most accurate proximity calculation. Do not rely on proximity alone; the above actions address the 44.8% of variance that is within optimization scope.

---

## Limitations Disclaimer

The following could not be assessed without paid tools or authenticated access:

- **GBP listing status, category, completeness, and review data** — requires Google Business Profile Manager access or DataForSEO `local_business_data` API
- **Local pack ranking positions** — requires DataForSEO `google_local_pack_serp` or similar rank tracking tool
- **Gule Sider listing details** — 403 Forbidden to scrapers
- **1881.no listing details** — 404 on search endpoint tested
- **Facebook page metrics** (rating, review count, follower count) — requires authenticated access
- **Yelp listing** — 403 Forbidden (low priority for Norway market)
- **Actual meta tags rendered by WordPress/Yoast** — the WebFetch tool received processed content, not raw `<head>` HTML; meta descriptions should be verified via browser DevTools or a site crawler (Screaming Frog)
- **Backlink profile depth** — requires Ahrefs, Moz, or Semrush
- **Core Web Vitals and technical SEO** — requires PageSpeed Insights or Google Search Console access
- **Google Search Console impressions/clicks for local keywords** — requires GSC access
- **Exact GBP coordinates** — geo coordinates in recommended schema are approximations; verify against the actual GBP pin

---

## Technical Implementation Notes (WordPress + Yoast SEO)

The site runs WordPress with Yoast SEO. Recommended implementation path:

1. **Yoast Local SEO add-on** (paid, ~€79/yr) — adds `LocalBusiness` schema, opening hours, and map embed automatically. Most pragmatic path for a non-developer.
2. **Manual JSON-LD in `<head>`** — paste the schema block above into Yoast SEO > Search Appearance > Schema or via a "Header/Footer Scripts" plugin. Full control, no recurring cost.
3. **Event schema** — The Events Calendar (free) + Schema Pro (~$79/yr) is the standard WordPress stack for event schema. Alternatively, Yoast Local SEO + Yoast News SEO handles some event markup.
4. **Google Maps embed** — Use the "Embed a Map" iframe from Google Maps. Do not use the Maps JavaScript API (requires billing setup) for a simple contact page embed.
5. **Review schema** — Once GBP reviews accumulate, use a plugin like WP Review Pro or embed Google Reviews via a widget that outputs `aggregateRating` schema.
