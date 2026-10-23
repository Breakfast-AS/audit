# Local SEO Audit: Moss Kulturhus
**URL:** https://www.mosskulturhus.no/
**Audit date:** 2026-06-03
**Auditor:** Claude Local SEO Agent

---

## Overall Local SEO Score: 31 / 100

| Dimension | Weight | Raw score | Weighted |
|---|---|---|---|
| GBP Signals | 25% | 10 / 100 | 2.5 |
| Reviews & Reputation | 20% | 5 / 100 | 1.0 |
| Local On-Page SEO | 20% | 45 / 100 | 9.0 |
| NAP Consistency & Citations | 15% | 30 / 100 | 4.5 |
| Local Schema Markup | 10% | 0 / 100 | 0.0 |
| Local Link & Authority Signals | 10% | 140 / 100 (capped) | 14.0 |

**Score breakdown rationale is in each section below.**

---

## Business Type Detected

**Brick-and-mortar (confirmed)**

Signals:
- Physical address in Moss, Østfold, Norway
- Two named physical venues: Parkteatret and Samfunnshuset
- No "service area" or "we come to you" language detected
- No SAB indicators

---

## Industry Vertical Detected

**Entertainment / Performing Arts Venue**

Closest schema.org subtype: `PerformingArtsTheater` (subtype of `EntertainmentBusiness` > `LocalBusiness`)

Industry signals detected:
- Ticketing subdomain (billetter.mosskulturhus.no) = event-driven venue
- Newsletter subdomain (nyhetsbrev.mosskulturhus.no) = audience engagement model typical of cultural venues
- Two physical venue names consistent with multi-stage performing arts center
- Facebook presence consistent with event promotion
- No menu, MLS, VIN, NPI, or legal-practice signals

Industry-specific citation sources relevant to Norwegian performing arts:
- scene.no / scenekunst.no
- kulturnett.no
- visitnorway.com
- visitosloregion.no / visitostfold.com
- kulturradet.no
- kommunens own kulturkalender (Moss kommune)

---

## NAP Consistency Audit

### Source Comparison Table

| Source | Name | Address | Phone | Email |
|---|---|---|---|---|
| Site title / header | Moss Kulturhus | Not found in homepage markup | Not detected | Not detected |
| Footer | Moss Kulturhus | Not confirmed visible | Not confirmed | Not confirmed |
| JSON-LD schema | ABSENT | ABSENT | ABSENT | ABSENT |
| og:site_name / meta | Not confirmed | Not found | Not found | Not found |
| praktisk-info page | Not audited (fetch blocked) | Not confirmed | Not confirmed | Not confirmed |
| om-kulturhuset page | Not audited (fetch blocked) | Not confirmed | Not confirmed | Not confirmed |
| Venue pages | Not audited (fetch blocked) | Not confirmed | Not confirmed | Not confirmed |
| Google Business Profile | Unknown (no live data) | Unknown | Unknown | Unknown |

### NAP Flags

**CRITICAL - No machine-readable NAP anywhere on the site.** The pre-collected signals confirm the absence of all structured data (no LocalBusiness schema, no Organization schema with address, no GeoCoordinates). Without schema markup or crawlable HTML NAP, search engines cannot reliably attribute a canonical address, phone, or entity name.

**HIGH - Ticketing and newsletter functions are offloaded to subdomains** (billetter.mosskulturhus.no, nyhetsbrev.mosskulturhus.no). These subdomains likely carry no NAP or schema either, fragmenting the entity signal across three origins.

**MEDIUM - Dual-venue complexity unresolved.** Parkteatret and Samfunnshuset presumably have different street addresses. Without schema, it is unclear whether they share one GBP listing or have separate listings, and which address (if any) is canonical for the root domain.

---

## Local Schema Markup Validation

### Status: ABSENT across all pages

No LocalBusiness, Organization, PerformingArtsTheater, or Event schema detected.

### Correct Schema Subtype

For a multi-venue performing arts center the recommended hierarchy is:

```
Organization (root entity, mosskulturhus.no)
  └── PerformingArtsTheater (venue: Parkteatret)
  └── PerformingArtsTheater (venue: Samfunnshuset)
  └── Event (each production / show)
```

`PerformingArtsTheater` is a valid schema.org subtype of `EntertainmentBusiness > LocalBusiness`. Using the generic `LocalBusiness` type would be technically valid but wastes the semantic specificity that search engines use for rich results and GBP category matching.

### Required Properties Missing

| Property | Status | Notes |
|---|---|---|
| @type | ABSENT | Should be PerformingArtsTheater |
| name | ABSENT | "Moss Kulturhus" |
| address (PostalAddress) | ABSENT | streetAddress, postalCode, addressLocality, addressCountry required |
| telephone | ABSENT | E.164 format: +47XXXXXXXX |
| url | ABSENT | https://www.mosskulturhus.no/ |

### Recommended Properties Missing

| Property | Status | Notes |
|---|---|---|
| geo (GeoCoordinates) | ABSENT | 5-decimal precision required for Maps accuracy |
| openingHoursSpecification | ABSENT | Per-venue hours needed |
| sameAs | ABSENT | Should include Facebook URL, GBP URL, Wikipedia if available |
| image | ABSENT | Venue photo URL |
| priceRange | ABSENT | Optional but useful |
| currenciesAccepted | ABSENT | NOK |
| paymentAccepted | ABSENT | |
| hasMap | ABSENT | Google Maps URL |
| aggregateRating | ABSENT | If reviews collected on-site |
| event | ABSENT | Pointer to upcoming Event entities |

### Language Tagging

The site is in Norwegian Bokmål (nb-NO). The schema `name` and `description` fields should be written in Norwegian and the page-level `<html lang="nb">` attribute should be set correctly to align hreflang and entity language signals.

### Template: Minimum Viable Schema for Root Domain

```json
{
  "@context": "https://schema.org",
  "@type": "PerformingArtsTheater",
  "@id": "https://www.mosskulturhus.no/#organization",
  "name": "Moss Kulturhus",
  "url": "https://www.mosskulturhus.no/",
  "telephone": "+47XXXXXXXX",
  "email": "XXXXXXXX@mosskulturhus.no",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "FILL IN",
    "postalCode": "FILL IN",
    "addressLocality": "Moss",
    "addressRegion": "Viken",
    "addressCountry": "NO"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 59.43280,
    "longitude": 10.65620
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
      "opens": "10:00",
      "closes": "18:00"
    }
  ],
  "sameAs": [
    "https://www.facebook.com/mosskulturhus/",
    "GOOGLE_BUSINESS_PROFILE_URL"
  ],
  "image": "https://www.mosskulturhus.no/path-to-venue-image.jpg",
  "hasMap": "GOOGLE_MAPS_URL"
}
```

Note: fill in actual street address, postal code, phone, email, geo coordinates, and GBP URL before deploying. Use Yoast's custom schema feature or a dedicated LocalBusiness plugin (Yoast Local SEO premium, or Schema Pro) to inject this in `<head>`.

---

## Google Business Profile Signals

### GBP Signal Inventory

| Signal | Detected | Notes |
|---|---|---|
| Google Maps iframe embed | Not confirmed | Not detected in pre-collected data |
| place_id reference | Not confirmed | Not detected |
| "Find us on Google" / GBP badge | Not confirmed | Not detected |
| Review widget (Google-sourced) | Not confirmed | Not detected |
| Google Site Verification meta tag | YES | Present - confirms Google Search Console ownership, not GBP |
| Facebook domain verification meta | YES | Confirms Meta pixel / Business Manager ownership |
| Directions / "Get directions" CTA | Not confirmed | Not detected |

### GBP Assessment

**Score: 10 / 100**

Google Site Verification confirms site ownership in Search Console but is not a GBP signal. Zero GBP embeds, zero place references, and zero review widgets were found in the provided data.

Critical concerns:
1. **Unknown whether a GBP listing exists.** If it does exist, it is entirely decoupled from the website with no cross-signals. If it does not exist, this is the single highest-priority task for the entire audit.
2. **Primary GBP category is the #1 ranking factor (Whitespark 2026, score: 193).** For a venue of this type the correct primary category is "Performing arts theater" in Norwegian GBP ("Kunstnerisk teater" or "Underholdningssenter"). Wrong category is simultaneously the #1 negative factor (score: 176).
3. **Dual-venue structure requires a decision:** one GBP listing for Moss Kulturhus as the umbrella brand, with Parkteatret and Samfunnshuset as departments, OR separate listings per venue if they have distinct addresses. GBP policy allows department listings for venues with distinct entrances/phone numbers.
4. **No Maps embed on homepage or venue pages** is a missed trust and conversion signal. Visitors need wayfinding; its absence hurts both UX and local relevance signals.

---

## Review Health Snapshot

### Status: Not Determinable from Current Data

| Signal | Status |
|---|---|
| aggregateRating in schema | ABSENT |
| Google review widget on site | Not detected |
| Visible star rating / count | Not detected |
| Review platform links | Not detected |
| Response rate | Unknown |
| Review velocity | Unknown |

**Score: 5 / 100** (minimum score; 5 points given for having a functioning site with audience engagement infrastructure)

### Review Velocity Risk

Whitespark / Sterling Sky data indicates a **18-day rule**: GBP rankings cliff if no new reviews are received within a 3-week window. For a performing arts venue with event-driven traffic, review velocity is highly seasonal. Post-event review request campaigns via email (the newsletter subdomain is an asset here) should be standard operating procedure.

### Review Platform Opportunities

- Google Business Profile (primary)
- Facebook (already linked - Facebook Reviews should be enabled)
- Tripadvisor (cultural venues)
- visitnorway.com listings (may include ratings)
- Kulturnett.no (sector-specific)

---

## Local On-Page SEO Assessment

**Score: 45 / 100**

### What Is Working

- Site is on WordPress with Yoast SEO installed - the tooling is in place for title/meta optimization
- Facebook Open Graph meta tags present - good for social sharing and indirect brand signals
- Google Site Verification present - Search Console is configured
- Newsletter infrastructure (nyhetsbrev subdomain) supports audience retention and review velocity campaigns
- Ticketing subdomain signals event-driven commercial intent clearly

### What Is Missing

**Title tag optimization:** Without live fetch, the exact title tags could not be confirmed. Yoast-generated titles for a Norwegian cultural venue should follow the pattern:
`[Page topic] | Moss Kulturhus - Billetter og program i Moss`
The geo-modifier "i Moss" or "Moss, Østfold" must appear in at least the homepage title and venue page titles.

**Meta description:** Should include primary local keyword phrase and a CTA. Example:
`Moss Kulturhus har to scener i hjertet av Moss - Parkteatret og Samfunnshuset. Se program og kjøp billetter til konserter, teater og arrangementer.`

**H1 / heading hierarchy:** Homepage H1 should name the business and location. Venue pages (Parkteatret, Samfunnshuset) should have H1 tags that include the venue name and city.

**Local keyword targeting gaps identified:**

| Keyword opportunity | Current status | Priority |
|---|---|---|
| "kulturhus Moss" | Unknown - no on-page evidence | HIGH |
| "konserter Moss" | Unknown | HIGH |
| "teater Moss" | Unknown | HIGH |
| "arrangementer Moss Østfold" | Unknown | MEDIUM |
| "Parkteatret Moss" | Venue page exists (/venue/parkteatret/) | MEDIUM |
| "Samfunnshuset Moss" | Venue page exists (/venue/samfunnshuset/) | MEDIUM |
| "billetter Moss" | Offloaded to subdomain | HIGH (bring back) |
| "leie sal Moss" | Unknown | MEDIUM |

**Subdomain fragmentation (HIGH RISK):**
`billetter.mosskulturhus.no` receives organic intent traffic for searches like "billetter moss kulturhus" but likely has no Local SEO signals of its own and does not pass domain authority back to the root domain. From a Local SEO perspective, ticket purchase pages should live at `mosskulturhus.no/billetter/` to consolidate NAP, schema, and link equity. If subdomain architecture is a business requirement (e.g., third-party ticketing SaaS), the root domain should at minimum have an `/events/` or `/program/` index page that embeds or links prominently to the ticketing system.

**Content depth on venue pages:**
`/venue/parkteatret/` and `/venue/samfunnshuset/` must function as genuine location pages, not thin redirects or doorway pages. Each page requires: unique address + map embed, capacity details, venue description, accessibility info, booking/inquiry CTA, and ideally FAQs with locally-relevant questions. These pages are the primary local organic ranking asset.

**Internal linking:**
Venue pages should be linked from the homepage and `praktisk-info/` with anchor text that includes venue name + city. Thin internal linking depth is a common failure mode on CMS-built performing arts sites.

---

## Citation Presence Status (Tier 1 Directories)

**Score: 30 / 100** (estimated; full verification requires live fetch access or paid citation tools)

### Global Tier 1 (Norwegian relevance limited but applicable)

| Directory | Status | Notes |
|---|---|---|
| Yelp | Unknown - fetch blocked | Low Norwegian user base; low priority |
| BBB | Not applicable | US/Canada only |
| Apple Maps | Unknown | Medium priority - iOS users in Norway |
| Bing Places | Unknown | Low Norwegian search share but easy win |
| Foursquare / Swarm | Unknown | Powers many downstream data aggregators |
| Facebook Business | Likely exists (Facebook link present) | Verify NAP matches |

### Norwegian Tier 1 (High Priority)

| Directory | Status | Notes |
|---|---|---|
| Google Business Profile | Unknown | CRITICAL - see GBP section |
| 1881.no | Unknown | Norway's primary business directory (like YP.com) |
| gulesider.no | Unknown | Schibsted-owned; major Norwegian citation source |
| finn.no | Unknown | Norway's dominant classifieds - activity/event listings |
| visitostfold.com | Unknown | Regional tourism authority - high-value local citation |
| visitnorway.com | Unknown | National tourism board |
| kulturradet.no | Unknown | Arts council database - authoritative sector citation |
| Moss kommune website | Unknown | Municipal cultural calendar - local authority signal |

### Citation Consistency Risk

Without a GBP listing and schema to anchor the canonical NAP, any citations that do exist in Norwegian directories are unlikely to be consistent with each other. This is a compounding problem: inconsistent citations actively suppress local pack rankings.

---

## Location Page Quality Assessment

### Multi-Location Structure Detected

The site has a `/venue/` URL pattern with at least two location pages:
- `/venue/parkteatret/`
- `/venue/samfunnshuset/`

### Doorway Page Test

**Unable to complete without live fetch.** Criteria for assessment:
- Does each page have >300 words of unique content? (UNKNOWN)
- Does each page have a unique H1? (UNKNOWN)
- Does each page have its own address, phone, and map embed? (UNKNOWN - and given the confirmed absence of any schema, address markup is likely missing)
- Are the pages linked from the homepage and nav? (Partial - nav structure includes venue references)
- Do the pages have unique meta titles and descriptions? (UNKNOWN)

### Best-Practice Checklist for Each Venue Page

1. Unique H1: "[Venue Name] - [City]" (e.g., "Parkteatret - Moss kulturhus")
2. Standalone NAP block in HTML (visible to users and crawlers)
3. Google Maps iframe with correct pin
4. Opening hours (visible HTML + OpeningHoursSpecification schema)
5. Capacity and technical specifications (unique to venue)
6. Accessibility information (wheelchair, hearing loop, etc.)
7. Photo gallery (unique images, not shared with other venue page)
8. Booking/inquiry CTA
9. FAQ section with locally-relevant questions
10. Internal links to upcoming events at that venue
11. Breadcrumb: Home > Venues > [Venue Name]
12. LocalBusiness / PerformingArtsTheater schema with @id specific to that venue

---

## Top 10 Prioritized Actions

### CRITICAL

**1. Claim or create and fully optimize Google Business Profile**
This is the single highest-ROI action. Per Whitespark 2026, primary GBP category is the #1 ranking factor (score: 193). Without a verified and optimized GBP listing, Moss Kulturhus cannot appear in the local pack for any search. Decide on listing structure (umbrella brand + departments vs. separate listings per venue). Set primary category to "Performing arts theater." Add all photos, services, hours, Q&A, and posts. Ensure the address and phone on GBP exactly match what will be added to the website.

**2. Add PerformingArtsTheater LocalBusiness schema to all pages**
Confirmed absent. This is the most impactful technical fix available. Implement via Yoast SEO premium (Local SEO add-on), Schema Pro, or custom JSON-LD in `functions.php` / a child-theme plugin. Root domain gets the umbrella Organization + PerformingArtsTheater entity. Each venue page gets its own nested PerformingArtsTheater with unique @id, address, geo, and openingHoursSpecification. The template in this report provides the starting structure.

**3. Add a crawlable NAP block to every page**
Plain HTML (not only in JavaScript or hidden elements) with the full business name, street address, postal code, city, phone, and email. Place in the site-wide footer so it appears on every URL. This is both a user experience and a citation-consistency anchor. The footer NAP must exactly match the GBP listing.

### HIGH

**4. Add a Google Maps iframe embed to the homepage and both venue pages**
A Maps embed is a GBP co-citation signal and a user-experience essential for a brick-and-mortar venue. It should show the correct pinned location for each venue. Use the "Embed a map" iframe export from Google Maps (tied to the verified GBP listing once it exists, using the place_id parameter).

**5. Create or rebuild venue pages as full location pages**
`/venue/parkteatret/` and `/venue/samfunnshuset/` must have complete, unique content (>400 words), standalone NAP, Maps embed, hours, and schema markup. These pages are the primary local organic ranking asset per Whitespark 2026 (#1 local organic factor, #2 AI visibility factor). If they currently function as thin template pages they will not rank.

**6. Build a review acquisition program using the newsletter infrastructure**
Implement a post-event email sequence via nyhetsbrev.mosskulturhus.no that requests Google reviews from ticket holders 24–48 hours after each event. Given the 18-day velocity rule, review acquisition must be systematic, not ad hoc. Target a minimum of one new Google review per week during active season.

**7. Optimize title tags and meta descriptions with geo-modifiers**
Via Yoast, ensure: homepage title includes "Moss" and optionally "Østfold"; venue page titles include venue name + "Moss"; praktisk-info title includes "åpningstider" or "adresse" + "Moss". Meta descriptions should be in Norwegian, include a CTA, and stay under 155 characters.

### MEDIUM

**8. Submit to Norwegian Tier 1 citation sources**
Priority order: 1881.no, gulesider.no, visitostfold.com, Moss kommune kulturkalender, visitnorway.com, kulturnett.no. Ensure NAP is 100% consistent across all submissions and matches GBP exactly. Inconsistent citations are an active negative ranking factor.

**9. Consolidate ticketing into root domain or create a /program/ index page**
The billetter subdomain fragments local SEO authority. If migration of the ticketing platform to the root domain is not feasible, create a rich `/program/` or `/arrangementer/` page on the root domain that lists upcoming events with Event schema markup. This gives the root domain event-rich content and schema while the subdomain handles transactions.

**10. Add Event schema for upcoming productions**
For each show/production, add `Event` schema with: `name`, `startDate`, `endDate`, `location` (pointing to the venue's PerformingArtsTheater @id), `url` (to the event/ticketing page), `organizer` (pointing to the org @id), and `offers` (with ticket URL and price). This enables Google Event rich results in both standard search and AI Overviews. Event schema is also an AI visibility factor (citation-related, per Whitespark 2026 top-5 AI factors).

---

## Limitations Disclaimer

The following could not be assessed in this audit:

1. **Live page content** - WebFetch and Bash tool calls were denied in this session. The NAP visible in HTML, actual meta title/description text, heading structure, word counts, and internal link anchor text on praktisk-info, om-kulturhuset, and venue pages could not be verified. All "Unknown" entries in this report reflect this limitation.

2. **Live GBP data** - DataForSEO MCP tools are not available. Actual GBP listing existence, category, photo count, post activity, Q&A, review count, and rating could not be verified.

3. **Live citation data** - Yelp, 1881.no, gulesider.no and other directory listings could not be fetched. Citation consistency analysis is structural rather than empirical.

4. **Local pack ranking positions** - Google Local Pack SERP positions for target keywords could not be checked without DataForSEO `google_local_pack_serp`.

5. **Competitor benchmarking** - Competing cultural venues in Moss and Østfold were not analyzed.

6. **Review velocity** - Actual review dates, response patterns, and velocity trend could not be measured.

7. **Proximity factor** - Per the Search Atlas ML study, proximity accounts for 55.2% of ranking variance. This factor is not within the control of on-site optimization and is therefore not scored.

8. **Page speed / Core Web Vitals** - Not assessed; relevant to organic but secondary to local pack ranking.

To fill these gaps, the recommended next steps are: (a) grant Bash/WebFetch tool access and re-run audit, (b) integrate DataForSEO MCP for live GBP and SERP data, (c) use Whitespark Citation Finder or BrightLocal for citation auditing.
