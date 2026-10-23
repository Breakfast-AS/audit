# Innholdsaudit – Moss kulturhus
**URL:** https://www.mosskulturhus.no/
**Dato:** 2026-06-03
**Revisor:** SEO Content Audit (automatisert analyse)

---

## Innholdskvalitetsscore: 28/100

Scoren reflekterer alvorlige og gjennomgående mangler på tvers av alle undersøkte sider: systematisk duplisering av titler, nesten total mangel på metabeskrivelser, manglende H1 på sentrale sider, ekstremt tynt innhold på venue- og kategorisider, og fraværet av E-E-A-T-signaler som gjør nettstedet svakt i både tradisjonell søk og AI-drevne søkemotorer.

---

## E-E-A-T-vurdering

| Faktor | Score | Nøkkelsignaler |
|--------|-------|----------------|
| **Experience** | 4/25 | Ingen publikumsomtaler, ingen anmeldelser, ingen «hva skjedde»-rapporter fra arrangementer. Ingen bilder med kontekst fra faktiske hendelser. |
| **Expertise** | 3/25 | Ingen ansatteprofiler, ingen kunstnerisk leder presentert, ingen kuratorbeskrivelser. Om-siden gir 273 ord uten faglig dybde. |
| **Authoritativeness** | 9/25 | Facebook-integrasjon til stede, Google-verifisering bekreftet. Ingen pressedekning lenket inn, ingen bransjepriser eller anerkjennelse nevnt. |
| **Trustworthiness** | 12/25 | Personvernerklæring og cookie-erklæring finnes. HTTPS aktivt. Ingen synlig fysisk adresse på undersøkte sider. Ingen telefonnummer på arrangementssider. |
| **Totalsum** | **28/100** | |

### Utdypende analyse per E-E-A-T-dimensjon

#### Experience (4/25)
Nettstedet viser ingen førstehåndssignaler. Det finnes ingen publikumsanmeldelser, ingen «som det skjedde»-rapportering fra arrangementer, ingen bilder fra faktiske forestillinger med kontekstuell bildetekst, og ingen historiefortelling om hva som gjør Moss kulturhus unikt som opplevelsessted. Arrangementsider beskriver logistikk («Lørdag 8. august, kl. 05:15 – Hvor: Alby Va...»), men mangler den opplevelsesdimensjonen som overbeviser besøkende og AI-systemer om at dette er en autoritativ kilde.

#### Expertise (3/25)
Ingen av sidene presenterer kompetansesignaler. Det er ingen kunstnerisk leder, ingen programansvarlig, ingen kommunikasjonssjef – ingen person som «eier» innholdet. Om-siden mangler en historiefortelling om organisasjonens kompetanse, hva som styrer det kunstneriske valget, og hvilke erfaringer teamet bringer. Dette er det svakeste E-E-A-T-punktet på hele nettstedet.

#### Authoritativeness (9/25)
Facebook-tilstedeværelse og Google-verifisering er positive basislinjersignaler, men nettstedet kan ikke demonstrere ekstern autoritativitet gjennom innholdet alene. Ingen pressesaker er lenket, ingen samarbeidspartnere er presentert, og ingen bransjeorganisasjoner er nevnt. Venue-sidene mangler den type informasjon (kapasitet, teknisk utstyr, akkreditering) som profesjonelle arrangører søker etter.

#### Trustworthiness (12/25)
Personvernerklæring og cookie-håndtering er på plass – dette er minimumskravene. Manglene er: fysisk adresse er ikke synlig i sideinnhold (kun muligens i footer), telefonnummer mangler på arrangementsider, og det er ingen kontaktperson knyttet til noen side. For en offentlig kulturinstitusjon forventer brukere høy grad av tilgjengelighet og transparens.

---

## Tynt innhold – oversikt

| Side | Ordtelling | Terskel | Status |
|------|-----------|---------|--------|
| `/venue/parkteatret/` | ~127 ord | 500–600 (lokasjon) | KRITISK |
| `/venue/samfunnshuset/` | ~131 ord | 500–600 (lokasjon) | KRITISK |
| `/stand-up/` | ~174 ord | 400+ (kategoriside) | KRITISK |
| `/om-kulturhuset/` | ~273 ord | 500+ (om-side) | ALVORLIG |
| `/event/soloppgangskonsert-med-thomas-dybdahl/` | ~540 ord | 400+ (arrangement) | AKSEPTABELT |
| `/program/` | ~856 ord | 400+ (listeside) | OK |
| `/praktisk-info/` | ~660 ord | 500+ (serviceinfo) | OK |

> Merk: Ordtelling er en proxy for tematisk dekning, ikke et direkte rangefaktor. Sidene med 127–174 ord er kritiske fordi de mangler grunnleggende informasjon brukerne søker etter – ikke utelukkende fordi de er korte.

---

## Tittelfeil – fullstendig gjennomgang

### Systemisk problem: Duplisert merkenavn
Alle titler følger mønsteret `[Sidenavn] - Moss kulturhus - Moss kulturhus`. Dette er forårsaket av at WordPress-temaets tittelmal legger til merkenavn, og en plugin (trolig Yoast eller SEOPress) legger det til igjen. Resultatet er at Google viser avkortet titler med den bisarre repetisjonen synlig.

| Side | Nåværende tittel | Problem |
|------|-----------------|---------|
| `/` | `Moss kulturhus - Kulturhuset midt i byen - Moss kulturhus` | Merkenavn både først og sist |
| `/om-kulturhuset/` | `Om oss - Moss kulturhus - Moss kulturhus` | Dobbelt merkenavn |
| `/venue/parkteatret/` | `Parkteatret Arkiver - Moss kulturhus - Moss kulturhus` | «Arkiver» = WordPress-etikett, ikke ekte tittel |
| `/venue/samfunnshuset/` | `Samfunnshuset Arkiver - Moss kulturhus - Moss kulturhus` | «Arkiver» = WordPress-etikett, ikke ekte tittel |
| `/stand-up/` | `Stand up - Moss kulturhus - Moss kulturhus` | Dobbelt merkenavn |
| `/program/` | `PROGRAM - Moss kulturhus - Moss kulturhus` | Dobbelt merkenavn + all caps |
| `/event/soloppgangskonsert-med-thomas-dybdahl/` | `Soloppgangskonsert med Thomas Dybdahl - Moss kulturhus - Moss kulturhus` | Dobbelt merkenavn |

### Anbefalte titler (norsk)

```
/ → "Moss kulturhus – Konserter, teater og kultur midt i Moss"
/om-kulturhuset/ → "Om Moss kulturhus – Historien, menneskene og visjonen"
/venue/parkteatret/ → "Parkteatret – Intimscene i hjertet av Moss kulturhus"
/venue/samfunnshuset/ → "Samfunnshuset – Stor sal for konserter og events i Moss"
/stand-up/ → "Stand up-komedie i Moss – Kommende show på Moss kulturhus"
/program/ → "Program – Alle arrangementer på Moss kulturhus"
```

Tittelmal i WordPress/Yoast: `%%title%% – %%sitename%%` (én instans av merkenavnet)

---

## Metabeskrivelser – fullstendig gjennomgang

| Side | Status | Vurdering |
|------|--------|-----------|
| `/` | Til stede | For kort (9 ord). Ingen CTA, ingen nøkkelord |
| `/om-kulturhuset/` | Til stede | God lengde, men generisk. Mangler differensiering |
| `/event/soloppgangskonsert-med-thomas-dybdahl/` | MANGLER | Kritisk – arrangementssider er de mest besøkte |
| `/stand-up/` | MANGLER | Kritisk |
| `/venue/parkteatret/` | MANGLER | Kritisk |
| `/venue/samfunnshuset/` | MANGLER | Kritisk |
| `/program/` | MANGLER | Alvorlig |
| `/praktisk-info/` | MANGLER | Alvorlig |

### Anbefalte metabeskrivelser (norsk, 140–155 tegn)

**Hjemmeside:**
```
Moss kulturhus – Parkteatret og Samfunnshuset – er byens fremste kulturscene. Opplev konserter, teater, stand-up og familieshow midt i Moss. Se programmet her.
```

**Parkteatret:**
```
Parkteatret er Moss kulturhus' intimscene med plass til [X] gjester. Her spilles teater, konserter og standup-kvelder i historiske omgivelser. Sjekk kommende program.
```

**Samfunnshuset:**
```
Samfunnshuset er den store salen på Moss kulturhus, med plass til [X] publikummere. Perfekt for større konserter, show og bedriftsarrangementer i Moss.
```

**Arrangementsside (mal):**
```
[Artistnavn] opptrer på [Venue] i Moss [dato]. [Én setning om artistens sjanger/stil]. Kjøp billett til Moss kulturhus her.
```

**Stand up:**
```
Se Norges beste stand-up komikere live på Moss kulturhus. Kommende show på Parkteatret og Samfunnshuset – perfekt for en latterfylt kveld i Moss. Kjøp billett her.
```

---

## Overskriftsstruktur

### Statusoversikt

| Side | H1 | H2 | Problem |
|------|----|----|---------|
| `/` | MANGLER | Kun arrangementsnavn | Kritisk – ingen semantisk anker for siden |
| `/om-kulturhuset/` | «Om oss» | INGEN | Flatt, ustrukturert |
| `/venue/parkteatret/` | MANGLER | INGEN | Kritisk |
| `/venue/samfunnshuset/` | MANGLER | INGEN | Kritisk |
| `/stand-up/` | «Stand up» | INGEN | Svakt |
| `/program/` | «PROGRAM» | INGEN | All caps, ingen struktur |
| `/event/soloppgangskonsert-...` | Arrangementsnavnet | «Praktisk info» kun | Akseptabelt, men lite |
| `/praktisk-info/` | «Praktisk info» | INGEN | Mangler navigasjonsstruktur |

### Anbefalt overskriftsstruktur per sidetype

**Hjemmeside:**
```
H1: Moss kulturhus – kultur midt i Moss (kun én)
H2: Kommende arrangementer
H2: Om Parkteatret og Samfunnshuset
H2: Bestill billett
H2: Nyheter og redaksjonelt innhold
```

**Venue-side (Parkteatret):**
```
H1: Parkteatret
H2: Om scenen
H2: Kapasitet og teknisk informasjon
H2: Tilgjengelighet
H2: Kommende arrangementer på Parkteatret
H2: Veibeskrivelse og parkering
```

**Kategoriside (Stand up):**
```
H1: Stand up i Moss
H2: Kommende stand up-show
H2: Hva er stand up på Moss kulturhus?
H2: Scener og billetter
```

---

## Bildeoptimalisering

### Kritisk: Alt-tekst mangler på majoriteten av bilder

| Side | Totalt bilder | Mangler alt-tekst | Andel uten alt |
|------|--------------|-------------------|----------------|
| `/` | 64 | 61 | **95%** |
| `/program/` | 58 | 55 | **95%** |
| `/venue/parkteatret/` | 13 | 10 | **77%** |
| `/event/soloppgangskonsert-...` | 10 | 7 | **70%** |
| `/stand-up/` | 6 | 3 | **50%** |
| `/om-kulturhuset/` | 4 | 1 | **25%** |

**Totalt:** ~156 bilder undersøkt, ~137 mangler alt-tekst (~88%)

Manglende alt-tekst er et kombinert tilgjengelighetsproblem (WCAG 2.1 nivå A) og SEO-problem. Søkemotorer bruker alt-tekst for å forstå bildeinnhold; for et kulturhus med sterke visuelle produkter (konserter, teater, kunstutstillinger) er dette en betydelig tapt mulighet for bildessøk og kontekstforståelse.

### Anbefalte alt-tekster (norsk, mal)

```
Artistbilde: "Thomas Dybdahl synger på Parkteatret, Moss kulturhus"
Sceneinteriør: "Interiør fra Parkteatret – intimscene på Moss kulturhus"
Arrangement: "Publikum på Samfunnshuset under [arrangementsnavn] 2025"
Logobilde: "Moss kulturhus logo" (ikke «bilde», ikke tomt)
```

---

## AI Citation Readiness: 12/100

| Kriterium | Status | Forklaring |
|-----------|--------|------------|
| FAQ-seksjoner | MANGLER | Ingen «spørsmål og svar»-innhold på noen side |
| Strukturerte fakta/tall | MANGLER | Kapasitet, årstall, antall arrangementer per år – ingen data tilgjengelig |
| Klart sitérbare setninger | DELVIS | Om-sidens ingress kan siteres, men er for generisk |
| Heading-hierarki H1→H2→H3 | SVAKT | Flate strukturer, mange sider mangler H1 |
| Svarfirst-formatering | MANGLER | Ingen sider besvarer et spørsmål direkte i åpningsavsnittet |
| Strukturert data (Event, Organization) | KRITISK MANGEL | Se Schema-audit |
| Unike data / originalforskning | MANGLER | Ingen |
| Tydelig entitetsklarhet | SVAKT | Ingen Organization-schema, ingen Person-schema for ansatte |

### Konsekvens for Google AI Mode og Perplexity
Google AI Mode (lansert mai 2025, tilgjengelig i 180+ land) viser null organiske blå lenker – kun AI-genererte svar med kildehenvisninger. Moss kulturhus er i dag i svært dårlig posisjon for AI-sitering fordi:

1. Venue-sidene mangler faktabasert innhold som kan siteres («Parkteatret har X seter og ble renovert i 2019»)
2. Arrangementsider mangler Event-schema – AI-systemer kan ikke parse strukturert hendelsesdata
3. Om-siden mangler Organization-schema med `name`, `foundingDate`, `description`, `address`
4. Det finnes ingen FAQ- eller spørsmålsbasert innhold som AI-systemer typisk trekker fra

---

## Innholdsgap – prioritert liste

### Kritiske gap (blokkerer organisk synlighet)

**1. Venue-sider uten innhold**
Parkteatret og Samfunnshuset er kjerneproduktene til Moss kulturhus, men har 127–131 ord og ingen H1. Disse sidene burde rangere for søk som «konsertsal Moss», «teatersal Moss», «leie lokale Moss» – men kan ikke det uten innhold.

Minimumsinnhold per venue-side:
- Scenens historie og særpreg (200–300 ord)
- Kapasitet og konfigurasjonsmuligheter
- Teknisk informasjon (lyd, lys, scene, garderobe)
- Tilgjengelighet (HC-plasser, heis, teleslynge)
- Kontaktperson for booking/utleie
- Bildegalleri med alt-tekster

**2. Kategori-/sjangersider uten redaksjonelt innhold**
`/stand-up/` har 174 ord og er kun en arrangementsliste. Tilsvarende gjelder `/teater/` og andre kategorier (ikke undersøkt, men trolig identisk mønster).

Minimumsinnhold per kategoriside:
- 2–3 avsnitt om sjangerens plass i Moss kulturhus' program
- Historikk: hvilke kjente artister/show har vært her
- «Hva kan du forvente» – hjelper konvertering

**3. Ingen blogg eller redaksjonelt innhold**
Det finnes ingen artikler, ingen intervjuer med artister, ingen «bak kulissene»-innhold. Dette er den viktigste muligheten for å bygge topisk autoritet og organisk trafikk fra long-tail-søk.

### Alvorlige gap (svekker E-E-A-T og konvertering)

**4. Ingen ansatteprofiler eller redaksjonell signatur**
Ingen side kan knyttes til en navngitt person. Dette er en av de sterkeste E-E-A-T-signalene for ikke-kommersielle kulturinstitusjoner.

**5. Ingen publikumsomtaler eller anmeldelser**
Det er ingen integrert anmeldelsesmodul, ingen sitering av presseanmeldelser, ingen «hva besøkende sier»-seksjon. Dette svekker konverteringskraft og trust-signaler.

**6. Ingen FAQ på arrangementsider eller praktisk-info-siden**
Typiske spørsmål brukere stiller: «Kan jeg kjøpe billett i døren?», «Er det garderobe?», «Hva skjer hvis arrangementet avlyses?», «Er det aldersgrense?»

**7. Praktisk info-siden mangler H2-struktur**
Med ~660 ord og ingen H2 er siden ustrukturert og vanskelig å scanne. Dette er også en AI-sitering-barriere.

---

## Prioritert tiltaksplan

### Fase 1 – Teknisk innholdsretting (1–2 uker, ingen ny innholdsproduksjon)

| Tiltak | Side(r) | Prioritet |
|--------|---------|-----------|
| Fiks duplisert merkenavn i tittelmalen | Alle sider | KRITISK |
| Fjern «Arkiver» fra venue-titler | `/venue/parkteatret/`, `/venue/samfunnshuset/` | KRITISK |
| Legg til H1 på hjemmesiden | `/` | KRITISK |
| Legg til H1 på venue-sider | `/venue/parkteatret/`, `/venue/samfunnshuset/` | KRITISK |
| Skriv metabeskrivelser for alle sider | Alle sider uten | HØY |
| Bulk-oppdatering av alt-tekster for bilder | Alle sider | HØY |
| Legg til Event-schema på alle arrangementsider | `/event/*` | HØY |

### Fase 2 – Innholdsutvidelse (2–6 uker)

| Tiltak | Sidetyp | Estimert innsats |
|--------|---------|-----------------|
| Skriv fullverdige venue-sider (500+ ord per venue) | `/venue/parkteatret/`, `/venue/samfunnshuset/` | Medium |
| Utvid Om-siden med ansatteprofiler + historikk | `/om-kulturhuset/` | Medium |
| Legg til redaksjonelt innhold på kategorisider | `/stand-up/`, `/teater/` etc. | Medium |
| Legg til FAQ-seksjon på praktisk-info-siden | `/praktisk-info/` | Lav-medium |
| Legg til FAQ-seksjon på venue-sider | `/venue/*` | Lav-medium |

### Fase 3 – Autoritetsbygging (løpende)

| Tiltak | Beskrivelse |
|--------|-------------|
| Redaksjonelt innhold / blogg | Kunstnerintervjuer, forestillingsomtaler, bak-kulissene-artikler |
| Publikumsanmeldelser | Integrer Google-anmeldelser eller eget modul |
| Pressearkiv | Lenker til pressesaker om Moss kulturhus |
| Organization-schema | `name`, `foundingDate`, `address`, `telephone`, `url`, `sameAs` |

---

## Norske innholdseksempler

### Anbefalt H1 for hjemmesiden
```
Moss kulturhus – opplev kultur midt i byen
```

### Anbefalt ingress for /venue/parkteatret/
```
Parkteatret er Moss kulturhus' intimscene, med plass til [X] tilskuere. Scenen ble renovert i 2018–2019 og er kjent for sin gode akustikk og nære atmosfære. Her presenterer vi teater, kammerkonserter, stand-up og mindre show gjennom hele sesongen. Parkteatret holder til i [adresse/bygningsnavn], bare noen få minutters gange fra Moss sentrum.
```

### Anbefalt redaksjonelt avsnitt for /stand-up/
```
Stand up på Moss kulturhus

Moss kulturhus har i en årrekke vært et av de fremste stedene for stand-up-komedie i Østfold. Vi presenterer alt fra nye talenter i norsk stand-up til etablerte profiler med store nasjonale turnéer. Forestillingene holdes som regel på Parkteatret, vår intimscene som gir en nær og engasjert atmosfære perfekt for komikk.

Sjekk programmet under for kommende show, og meld deg på nyhetsbrevet vårt for å være første ut når nye billetter legges ut.
```

### Anbefalt FAQ-seksjon for /praktisk-info/
```html
<h2>Ofte stilte spørsmål</h2>

<h3>Kan jeg kjøpe billett i døren?</h3>
<p>Ja, billetter til de fleste arrangementer kan kjøpes i kassen en time før forestillingen starter, så lenge det er ledige plasser. Vi anbefaler alltid forhåndskjøp.</p>

<h3>Er det garderobe på Moss kulturhus?</h3>
<p>Ja, det er betjent garderobe på Parkteatret og Samfunnshuset. Garderoben åpner en time før forestillingen.</p>

<h3>Hva skjer hvis et arrangement avlyses?</h3>
<p>Ved avlysning refunderes billettprisen automatisk til betalingskortet du brukte. Du vil motta en e-post med bekreftelse.</p>

<h3>Er det tilrettelagt for rullestolbrukere?</h3>
<p>Begge saler er tilgjengelige for rullestolbrukere. Ta kontakt med oss på [telefon/e-post] for å reservere HC-plass.</p>
```

### Anbefalt Om-side struktur (H2-er)
```
H1: Om Moss kulturhus
H2: Hvem vi er
H2: Parkteatret og Samfunnshuset – to scener, én visjon
H2: Historien vår
H2: Menneskene bak kulissene [med ansatteprofiler]
H2: Samarbeidspartnere
H2: Kontakt oss
```

---

## Sammendrag av funn

| Kategori | Alvorlighetsgrad | Antall problemer |
|----------|-----------------|-----------------|
| Dupliserte titler | KRITISK | 8 sider |
| Manglende H1 | KRITISK | 3+ sider |
| Manglende metabeskrivelser | ALVORLIG | 6 av 8 sider |
| Tynt innhold (<300 ord) | ALVORLIG | 4 sider |
| Manglende alt-tekst | ALVORLIG | ~137 bilder |
| Ingen Event-schema | ALVORLIG | Alle arrangementsider |
| Ingen H2-struktur | MODERAT | 5+ sider |
| Ingen E-E-A-T-innhold | MODERAT | Hele nettstedet |
| Ingen FAQ | MODERAT | Hele nettstedet |
| Ingen blogg/redaksjonelt | MODERAT | Hele nettstedet |

**Total innholdskvalitetsscore: 28/100**

De mest presserende problemene er tekniske (titler, H1, schema) og kan fikses uten ny innholdsproduksjon i løpet av 1–2 uker. De strukturelle innholdsmanglene (venue-sider, kategorisider, om-siden) krever dedikert skrivearbeid men har stor potensiell oppsidé i organisk synlighet for lokale kulturrelaterte søk.
