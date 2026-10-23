# Lillestrøm kultursenter — oktober 2026

**Score: 64/100** (automatisk baseline). Mai-auditen var manuell (46) og kan ikke sammenlignes direkte.
Crawlen er et utvalg på 499 av 711 sider fra sitemap.

## Sterkt
- Organization-schema er på plass, og 79 arrangementer har Event-schema.
- Ingen titler med dobbelt merkenavn. Ingen feilende URL-er i sitemap.

## Svakt
- **221 av 300** arrangementssider i utvalget mangler Event-schema. Det gjelder hovedsakelig eldre `/program/`-sider.
- **200 tynne sider** (< 150 unike ord). Median unike ord er 220.
- **497 av 499** sider mangler meta description. 132 sider mangler H1, deriblant forsiden.
- Ingen sikkerhetsheadere (0 av 5). Bare 20 % lazy-loading under folden.

## Ytelse (mobil, lab)
Forsiden: Lighthouse 70, LCP 6,0 s, CLS 0.

## Tre viktigste tiltak nå
1. Sørg for at Event-schema genereres for alle arrangementer, også de eldre.
2. Standard meta description-mal for arrangementer (`%%excerpt%%`).
3. Noindex eller utbygging av tynne arkiv- og arrangørsider.
