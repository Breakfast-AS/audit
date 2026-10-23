# Handlingsplan — Moss kulturhus SEO
**Dato:** 2026-10-23 · **Score:** 31/100 (juni: 30) · Se `FULL-AUDIT-REPORT.md` for detaljer.

---

## KRITISK: gjør umiddelbart

### K1. Rett tittelmalen (gjenstår fra juni)
**Innsats:** 30 min · Gå til **Yoast → Innstillinger → Innholdstyper / Taksonomier**. Malen inneholder `%%sitename%%` to ganger, enten i malen selv eller fordi temaet legger på merkenavnet i `<title>` i tillegg. Skal være:
- Sider og arrangementer: `%%title%% %%sep%% %%sitename%%`
- Arrangementer med flere visninger: legg til dato, f.eks. `The Wiz – Teaterkråkene, 14. nov 2026 – Moss kulturhus`
- Forsiden: `Moss kulturhus – konserter, teater og stand-up i Moss`

Merkenavnet kan også komme fra temaets `header.php`. Det ser slik ut fordi `<title>` er skrevet ut manuelt med mellomrom og linjeskift. Sjekk derfor at temaet bruker `wp_head()` / `title-tag`-støtte og ikke skriver ut sin egen title.

### K2. Event-schema på alle arrangementer (gjenstår fra juni)
**Innsats:** 4–8 t for utvikler (Breakfast). Generer JSON-LD i malen for `event`-posttypen ut fra feltene som allerede finnes:

```json
{
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "Svanesjøen",
  "startDate": "2027-02-20T19:00:00+01:00",
  "duration": "PT2H",
  "eventStatus": "https://schema.org/EventScheduled",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "image": "https://www.mosskulturhus.no/wp-content/uploads/…",
  "description": "Klassisk ballett med Etoile Ballet …",
  "location": {
    "@type": "PerformingArtsTheater",
    "name": "Parkteatret",
    "address": {"@type": "PostalAddress","streetAddress": "Dronningens gate 25","postalCode": "1530","addressLocality": "Moss","addressCountry": "NO"}
  },
  "organizer": {"@type": "Organization","name": "Kultur for folket"},
  "offers": {"@type": "AggregateOffer","lowPrice": "275","highPrice": "795","priceCurrency": "NOK","availability": "https://schema.org/InStock","url": "https://billetter.mosskulturhus.no/…"}
}
```
Når en forestilling har flere datoer, skal hver dato ha sitt eget `Event`. Bruk `SoldOut` når arrangementet er utsolgt (forsiden viser allerede «Få billetter igjen» og lignende). Valider med Rich Results Test.

### K3. Noindex og fjern de tomme arkivsidene fra sitemapen (ny)
**Innsats:** 15 min. Gå til **Yoast → Innstillinger**:
- Taksonomier → Kategorier og Tags: «Vis i søkeresultater» = **Av**
- Innholdstyper → Venue og Organizer: «Vis i søkeresultater» = **Av**, med mindre de bygges ut (se M1)

Da blir 70 URL-er med 133 ord standardtekst fjernet fra indeksen og sitemapen.
Det langsiktige alternativet er å få arkivmalene til å faktisk liste opp arrangementene. I dag er de tomme, og det bør utvikleren også se på.

### K4. Mobilytelse: LCP 27 s og CLS 1,3 (ny måling)
**Innsats:** 1–2 dager for utvikler.
1. Legg `defer` på jQuery-migrate, lazysizes, js-cookie, FontAwesome, `scripts.js` og `tix-public.js`. Fjern jQuery-migrate hvis det ikke trengs.
2. **Lazy-load programbildene.** Skriv kortene om fra `background-image` til `<img loading="lazy" width height alt="…">`. Unntaket er de første 2–3 kortene og karusellbildet, som skal ha `fetchpriority="high"`. Fjern lazysizes 1.2.2. Dette alene kutter 4,6 MB fra første lasting.
3. **Material Symbols** (542 kB): bruk `&icon_names=…` for å laste bare ikonene som brukes, eller bytt til inline SVG. Velg én ikonløsning og fjern FontAwesome-kit-et.
4. Gi `#program` og karusellen fast høyde eller `aspect-ratio` på kortene for å fjerne CLS.
5. Skaler ned karusellbildene (4312×1400 JPG) til maks. 2000 px WebP med `srcset`.
6. Sjekk om Divi Builder fortsatt trengs. Hvis ikke, fjern det.

Mål: LCP under 2,5 s og CLS under 0,1. Mål på nytt med PageSpeed Insights når API-kvoten er tilbake, eller med en API-nøkkel.

### K5. H1 på forsiden (gjenstår fra juni)
**Innsats:** 15 min. Eksempel: `<h1>Moss kulturhus – Parkteatret og Samfunnshuset</h1>`. Den kan være visuelt skjult hvis designet ikke har plass til den.

---

## HØY: innen 1 uke

### H1. Organization- og PerformingArtsTheater-schema
Legg inn på forsiden eller sitewide: `Organization` (Moss kulturhus, logo, telefon 404 09 924, `parentOrganization`: Moss kommune, `sameAs` med Facebook, Instagram og Wikidata hvis den finnes), med to `PerformingArtsTheater` (Parkteatret og Samfunnshuset) som `location` / `subOrganization`.

### H2. Meta description på arrangementer og hovedsider
178 av 185 mangler. Sett Yoast-malen for arrangementer til `%%excerpt%%` som standard. Skriv manuelle beskrivelser for forsiden, `/program/`, `/praktisk-info/`, `/leie/`, `/parkteatret/` og `/samfunnshuset/`.

### H3. Sikkerhetsheadere (gjenstår fra juni)
- Cloudflare → SSL/TLS → Edge Certificates → **HSTS på**
- Transform Rules: `X-Content-Type-Options: nosniff`, `Referrer-Policy: strict-origin-when-cross-origin`, `X-Frame-Options: SAMEORIGIN`

### H4. Datoer med årstall på arrangementssidene
Endre «Lørdag 20. februar, kl. 19:00» til «Lørdag 20. februar 2027, kl. 19:00» når arrangementet ikke er i inneværende år, eller alltid.

### H5. og:image på alle sider
99 sider mangler. Sett et standard delingsbilde i Yoast → Sosiale medier. Arrangementer bør bruke arrangementsbildet sitt.

---

## MIDDELS: innen 1 måned

### M1. Bygg ut stedssidene
`/parkteatret/` (152 ord) og `/samfunnshuset/` (154 ord) bør ha minst 400–600 ord. Ta med adresse, kart, parkering, kollektivtransport, kapasitet, tilgjengelighet, historikk, bilder og kommende arrangementer på scenen. Lenk til dem fra menyen. I dag har de ingen interne lenker. Slå sammen med eller 301-redirect `/venue/*`-sidene til disse.

### M2. Rydd i utdatert innhold og duplikater
- `/christian-frederik-dagene-2024/` og `/viken-tattoorama/` (2024): oppdater, eller sett noindex/arkiver
- `/ledig-stilling/` og `/ledige-stillinger/`: slå sammen. Siden har i dag 3 H1-er.
- Fjern `/publikum/` (redirect) fra sitemapen
- Rett opp sider med flere H1: `/viken-tattoorama/` (5), `/ledige-stillinger/` (3), `/leie/`, `/arrangorinformasjon/` og `/christian-frederik-dagene-2024/`

### M3. Internlenking til «foreldreløse» sider
23 innholdssider har ingen interne lenker, bl.a. `/stand-up/`, `/teater/`, `/julekonserter/`, `/barneprogram/`, `/riksteatret/` og `/kryssover-jazzfest-moss/`. Legg dem inn i menyen eller lag sjangerfiltre på `/program/` som lenker dit. Disse sidene kan rangere på søk som «stand up Moss» og «julekonsert Moss».

### M4. `/llms.txt` + FAQ på `/praktisk-info/`
Lag en llms.txt som beskriver hvem Moss kulturhus er, de to scenene, programlenken og billettsalget. Bygg ut praktisk info med spørsmål og svar: parkering, garderobe, tilgjengelighet, aldersgrenser, åpningstider og billettrefusjon.

### M5. Utvid «Om oss» med E-E-A-T-signaler
Ta med historikk, eierskap (Moss kommune), ledelse og ansatte, kapasitet, nøkkeltall og en pressekontakt.

---

## LAV: backlog
- robots.txt: fjern `Crawl-delay: 10` og den tomme `Disallow:`
- Rett tilgjengelighetsfunnene fra Lighthouse: knapper og lenker uten tilgjengelig navn, og fargekontrast
- Wikidata-oppføring for Moss kulturhus, Parkteatret og Samfunnshuset
- Sett opp en Google API-nøkkel (PSI og CrUX) og Search Console-tilgang slik at neste audit får feltdata og indekseringsstatus

---

## Forventet effekt
| Etter | Estimert score |
|---|---|
| K1–K5 | ~50 |
| + Høy | ~60 |
| + Middels | ~70 |
