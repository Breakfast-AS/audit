# Hjertnes kulturhus — oktober 2026

**Score: 61/100** (automatisk baseline). Mai-auditen var manuell (42) og kan ikke sammenlignes direkte.

## Sterkt
- Organization-schema er på plass, og 113 arrangementer har Event-schema.
- Ingen titler med dobbelt merkenavn. Ingen feilende URL-er i sitemap.

## Svakt
- **140 av 253** arrangementssider mangler Event-schema. Det gjelder hovedsakelig `/kinoprogram/`-sidene, som bør ha `ScreeningEvent`.
- **216 tynne sider** av 432. Median unike ord er 150.
- **415 av 432** sider mangler meta description. 133 mangler H1, deriblant forsiden.
- 14 sider har canonical som peker til en annen URL. 20 dupliserte titler.
- Nesten ingen lazy-loading (0,4 %). Ingen sikkerhetsheadere.

## Ytelse (mobil, lab)
Forsiden: Lighthouse 64, **LCP 16,7 s**, CLS 0.

## Tre viktigste tiltak nå
1. `ScreeningEvent`-schema på kinoprogrammet.
2. Finn LCP-elementet på forsiden og optimaliser det (preload, riktig størrelse, ikke lazy).
3. Meta description-maler og H1 på forsiden.
