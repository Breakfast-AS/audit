# SEO-audit — Moss kulturhus (oppfølging)
**URL:** https://www.mosskulturhus.no/
**Dato:** 2026-10-23 (forrige audit: 2026-06-03)
**Plattform:** WordPress (tema `mosskulturhus-redesign` av Breakfast) + Divi Builder + Yoast SEO + WP Engine + Cloudflare. Billettsalg via Tixly (`billetter.mosskulturhus.no`).
**Bransje:** Kulturhus / scene (fysisk lokasjon, to scener: Parkteatret og Samfunnshuset, Moss)
**Omfang:** 185 URL-er fra sitemap crawlet (alle svarte 200). Lighthouse (mobil, lokalt) på forsiden.

---

> **Merk:** Scoren 31 i denne rapporten er en skjønnsbasert vurdering, samme metode som i juni. Fra oktober 2026 bruker dashboardet en fast, automatisk formel (`metrics.json`). Med den formelen er baseline for oktober **46**. Fremover sammenlignes bare automatiske scorer med hverandre.

## SEO Health Score: 31 / 100 (juni: 30)

| Kategori | Vekt | Juni | Nå | Vektet |
|---|---|---|---|---|
| Teknisk SEO | 22 % | 47 | 52 | 11,4 |
| Innholdskvalitet | 23 % | 28 | 30 | 6,9 |
| On-page SEO | 20 % | 22 | 25 | 5,0 |
| Schema / strukturerte data | 10 % | 8 | 12 | 1,2 |
| Ytelse (CWV) | 10 % | 38* | 20 | 2,0 |
| AI-søk (GEO) | 10 % | 28 | 30 | 3,0 |
| Bilder | 5 % | 8 | 30 | 1,5 |
| **Totalt** | | **30** | | **31** |

\* Juni-tallet var et estimat uten måling. Nå er ytelsen målt med Lighthouse, og resultatet er mye svakere enn estimert. Det er hovedgrunnen til at ytelsesscoren har falt.

---

## Sammendrag

Siden juni er det gjort forbedringer i infrastrukturen: caching fungerer (Cloudflare `HIT`), bildene serveres som WebP, NAP står i footeren, BreadcrumbList ligger på alle sider og forsiden har fått egen title. **Ingen av de fem kritiske SEO-punktene fra juni er løst.** I tillegg er to nye, store problemer avdekket:

1. **70 indekserbare arkivsider er helt tomme.** Kategori-, tag-, sted- og arrangørsidene viser bare meny og footer (133 ord, alt sammen fast mal). Dette er 38 % av alle URL-ene i sitemapen.
2. **Forsiden er svært treg på mobil:** LCP er 27,1 s og CLS 1,30 i Lighthouse (mobil). Grensene for «god» er henholdsvis 2,5 s og 0,1.

### Status på kritiske punkter fra juni

| # | Tiltak | Status |
|---|---|---|
| C1 | Fjerne dobbelt merkenavn i titler | ❌ Ikke løst: 184 av 185 titler slutter fortsatt på «- Moss kulturhus - Moss kulturhus» (forsiden: «… - Kulturhuset midt i byen - Moss kulturhus») |
| C2 | H1 på forsiden | ❌ Ikke løst |
| C3 | Event-schema | ❌ Ikke løst: 0 av 75 arrangementssider |
| C4 | Organization-/teater-schema | ❌ Ikke løst |
| C5 | Sikkerhetsheadere (HSTS m.fl.) | ❌ Ikke løst |
| H2 | Sidecaching | ✅ Løst (WP Engine + Cloudflare HIT) |
| H6 | NAP i footer | ✅ Løst (begge scener + administrasjon + telefon) |
| M6 | BreadcrumbList | ✅ Løst |
| L3 | WebP | ✅ Løst (73 WebP på forsiden) |
| H4 | Noindex på tynne arkiver | ❌ Ikke løst, og problemet er nå større (arkivene er helt tomme) |
| M5 | llms.txt | ❌ 404 |
| L6 | Crawl-delay | ❌ Fortsatt `Crawl-delay: 10` |

### Topp 5 kritiske problemer
1. **Dobbelt merkenavn i 184 titler.** Én endring i malen i Yoast løser det.
2. **Ingen Event-schema på 75 arrangementer.** Arrangementene er dermed ikke kvalifisert for event-visning i Google.
3. **70 tomme arkivsider er indeksert.** Det gir tynt innhold og sløser med crawlbudsjettet.
4. **Mobilytelse: LCP 27 s og CLS 1,30.** Det skyldes 12 render-blokkerende ressurser, 4,6 MB bilder utenfor skjermen som lastes med en gang, og et programrutenett som hopper.
5. **Forsiden mangler H1, og 96 % av sidene mangler meta description.**

### Topp 5 raske gevinster
1. Rett tittelmalen i Yoast (30 min).
2. Sett noindex på taksonomier og arkiver i Yoast (15 min).
3. Slå på HSTS i Cloudflare (5 min).
4. Legg `loading="lazy"` på programbildene, eller ta faktisk i bruk lazysizes (`data-src`) (1–2 t).
5. Fjern `Crawl-delay: 10` og den tomme `Disallow:`-linjen i robots.txt (5 min).

---

## 1. Teknisk SEO — 52/100

**Positivt**
- Alle de 185 sitemap-URL-ene svarer 200. Det finnes én redirect (`/publikum/` → `/praktisk-info/`), og den står fortsatt i sitemapen.
- HTTPS fungerer. Apex-domenet sender 301 til www.
- Caching fungerer: `cf-cache-status: HIT` og `x-cache: HIT`. Gjennomsnittlig responstid i crawlen var 0,53 s. Lighthouse målte TTFB til 20 ms.
- Googlebot, Bingbot, GPTBot, ClaudeBot og PerplexityBot får alle 200. Bare en helt naken `Mozilla/5.0`-UA blir blokkert av Cloudflare, og det påvirker ikke ekte crawlere.
- Sitemapen er delt etter innholdstype, og lastmod er nå oppdatert (oktober 2026).

**Problemer**
| Problem | Alvorlighet |
|---|---|
| 70 tomme arkivsider (26 kategorier, 13 tags, 4 steder, 27 arrangører) indekseres og ligger i sitemapen | Høy |
| `/publikum/` (redirect) ligger i page-sitemapen | Lav |
| Mangler HSTS, `X-Content-Type-Options`, `Referrer-Policy`, `X-Frame-Options`/CSP og `Permissions-Policy` | Middels |
| `Crawl-delay: 10` står før user-agent-blokken og har en tom `Disallow:` | Lav |
| Utdaterte sider indekseres: `/christian-frederik-dagene-2024/`, `/viken-tattoorama/` («Viken Tattoorama 2024»), `/ledig-stilling/` og `/ledige-stillinger/` (duplikat) | Middels |
| Divi Builder lastes i tillegg til det egne temaet (ekstra CSS/JS) | Middels |

## 2. Innholdskvalitet — 30/100

- **Arrangementssider:** median 525 ord (min. 374), med god og unik beskrivelse, sted, varighet, pris og arrangør. Dette er sidens sterkeste innhold.
  - Datoen vises uten årstall («Lørdag 20. februar, kl. 19:00»). Det er uklart for både brukere og AI-systemer.
  - Flere arrangementer har like titler fordi samme forestilling har flere datoer («The Wiz – Teaterkråkene» ×3 og andre). Legg dato eller tidspunkt i title.
- **Arkivsider:** 70 sider har 133 ord, og alt er fast mal. De viser ingen arrangementer.
- **Innholdssider:** median 283 ord. `/parkteatret/` (152 ord) og `/samfunnshuset/` (154 ord) er svært tynne, selv om det er sidene som burde rangere på «Parkteatret Moss» og «Samfunnshuset Moss».
- **E-E-A-T:** `/om-kulturhuset/` er på 283 ord. Den mangler historikk, kapasitet, eierskap (Moss kommune), ansatte/ledelse og presseinfo.

## 3. On-page SEO — 25/100

| Element | Funn |
|---|---|
| Title | 184/185 har dobbelt merkenavn. 75 er over 60 tegn. Arkivene har «X Arkiver» i tittelen. |
| H1 | Forsiden mangler H1. De 70 arkivsidene mangler H1. 9 sider har flere H1 (`/ledige-stillinger/` 3, `/viken-tattoorama/` 5, `/leie/` 2, `/arrangorinformasjon/` 2, …). |
| Meta description | Mangler på 178 av 185 sider (96 %). Bare 2 av 75 arrangementer har en. |
| og:image | Mangler på 99 av 185 sider. |
| Internlenking | 95 URL-er i sitemapen får ingen interne lenker fra crawlede sider. Det gjelder alle arkivene og 23 av 40 innholdssider (bl.a. `/parkteatret/`, `/samfunnshuset/`, `/stand-up/`, `/teater/`, `/julekonserter/`). |

## 4. Schema — 12/100

- Finnes: `WebSite` + `SearchAction`, `WebPage`/`CollectionPage` og `BreadcrumbList` (Yoast-standard).
- Mangler:
  - `Event` på 75 arrangementssider. Dette er det viktigste.
  - `Organization` / `PerformingArtsTheater` med adresse, telefon, logo og `sameAs`.
  - `Place` for Parkteatret og Samfunnshuset.
- Arrangementssidene har allerede alle feltene Event-schema trenger: navn, dato og klokkeslett, sted, pris, arrangør, bilde og billettlenke til Tixly.

## 5. Ytelse — 20/100 (Lighthouse mobil, forsiden)

| Måling | Verdi | Mål |
|---|---|---|
| Performance-score | **31** | ≥ 90 |
| LCP | **27,1 s** | ≤ 2,5 s |
| CLS | **1,295** | ≤ 0,1 |
| FCP | 6,4 s | ≤ 1,8 s |
| TBT | 40 ms | OK |
| Total vekt | 6,4 MB / 113 forespørsler | |

Lighthouse-score for de andre kategoriene: Tilgjengelighet 87, Beste praksis 79, SEO 100.

**Årsaker**
- **LCP-elementet** er et programkort (`figure.image` med CSS `background-image`). Fordelingen er 28 % lastforsinkelse, 27 % lastetid og 43 % render-forsinkelse.
- **12 render-blokkerende ressurser** (anslått besparelse 4,9 s): jQuery og jQuery-migrate, FontAwesome-kit, lazysizes 1.2.2 (fra 2015), js-cookie, `scripts.js`, `tix-public.js`/`.css`, Divi-CSS, Google Fonts (Roboto og Material Symbols) og `style.css`.
- **Bilder utenfor skjermen (4,6 MB)** lastes med en gang. lazysizes lastes, men brukes ikke. Karusellbildene er 4312×1400 JPG på 200–220 kB hver.
- **Material Symbols-fonten er 542 kB.** Hele variabelfonten lastes, selv om siden bare bruker noen få ikoner.
- **CLS** kommer fra `div#program`, som endrer høyde mens bilder og innhold lastes, og fra kontrollene i event-karusellen.
- Vi har ikke feltdata (CrUX), siden det ikke er satt opp en Google API-nøkkel. Lab-tallene kjøres med simulert, strupet 4G og er derfor strengere enn hva ekte brukere opplever. Tallene er likevel langt over grensene.

## 6. Bilder — 30/100

- ✅ Bildene serveres som WebP.
- Forsiden har 75 bilder med `alt=""`. De fleste er dekorative skilletegn, og det er riktig. Programbildene er derimot CSS-bakgrunner, så de har ingen alt-tekst og blir ikke indeksert i bildesøk.
- På tvers av siden har 782 bilder tom alt og 16 mangler alt-attributtet helt.
- Ingen `<img>` på forsiden har `loading="lazy"` eller `fetchpriority`.

## 7. AI-søk (GEO) — 30/100

- ✅ Alle AI-crawlere slipper til.
- ❌ `/llms.txt` gir 404.
- ❌ Det finnes ingen entitetsdata (Organization-schema, `sameAs`) som binder Moss kulturhus, Parkteatret og Samfunnshuset sammen.
- ❌ Datoer uten årstall og manglende Event-schema gjør det vanskelig for ChatGPT, Perplexity og AI Overviews å svare presist på «hva skjer på Moss kulturhus».
- ❌ Det finnes ingen FAQ eller praktisk informasjon i siterbar form (parkering, tilgjengelighet, kapasitet, garderobe). `/praktisk-info/` (712 ord) er en god kandidat til å bygges om med spørsmål og svar.

## 8. Lokal SEO (tillegg)

- ✅ NAP i footeren: Parkteatret, Dronningens gate 25, 1530 Moss · Samfunnshuset, Kirkegata 13, 1531 Moss · Administrasjon, Storgata 25 · tlf. 404 09 924.
- ❌ Ingen LocalBusiness-, Place- eller teater-schema.
- ❌ Stedssidene (`/parkteatret/`, `/samfunnshuset/` og `/venue/*`) er tynne eller tomme. De mangler kart, veibeskrivelse, kapasitet, parkering og bilder.
- Google Business Profile ble ikke verifisert i denne auditen. Ingen DataForSEO eller GBP-tilgang var tilgjengelig.

---

## Begrensninger
- PageSpeed Insights-API-et hadde brukt opp den gratis dagskvoten, og det er ikke konfigurert noen Google-nøkler. Derfor finnes det ingen CrUX-feltdata, GSC-indeksering eller GA4-tall. Ytelsen er målt med lokal Lighthouse 12.6.
- Lighthouse er bare kjørt på forsiden.
- Rådata ligger i `data/crawl.json` og `data/lighthouse-mobile-home.json`.
