/* SEO-oversikt – statisk dashboard. Leser window.SEO_DATA (bygges av scripts/build_dashboard.py). */
(() => {
  "use strict";
  const DATA = window.SEO_DATA || { clients: [] };
  const app = document.getElementById("app");
  const tip = document.getElementById("tooltip");

  const CATS = [
    ["technical", "Teknisk"], ["content", "Innhold"], ["onpage", "On-page"], ["schema", "Schema"],
    ["performance", "Ytelse"], ["ai", "AI-søk"], ["images", "Bilder"],
  ];
  const SEV = { critical: "Kritisk", high: "Høy", medium: "Middels", low: "Lav" };
  const SEV_ORDER = ["critical", "high", "medium", "low"];
  // [nøkkel, etikett, høyere er bedre?, format]
  const KPIS = [
    ["pages_ok", "Sider (200)", null, "n"],
    ["thin_pages", "Tynne sider", false, "n"],
    ["median_unique_words", "Median unike ord", true, "n"],
    ["repeated_brand_titles", "Titler m/ dobbelt segment", false, "n"],
    ["missing_h1", "Mangler H1", false, "n"],
    ["missing_meta_description", "Mangler meta description", false, "n"],
    ["missing_og_image", "Mangler og:image", false, "n"],
    ["event_pages_with_schema", "Arrangementer m/ Event-schema", true, "n", "event_pages"],
    ["security_headers_ok", "Sikkerhetsheadere", true, "n", "security_headers_total"],
    ["img_alt_coverage", "Alt-tekst-dekning", true, "pct"],
    ["img_lazy_coverage", "Lazy-loading", true, "pct"],
    ["perf_score", "Lighthouse ytelse", true, "n"],
    ["lcp_ms", "LCP (verste side)", false, "s"],
    ["cls", "CLS (verste side)", false, "cls"],
  ];
  const REPORT_TABS = [["summary", "Sammendrag"], ["changes", "Endringer"], ["plan", "Handlingsplan"], ["report", "Full rapport"]];

  // ------------------------------------------------------------------ helpers
  const h = (tag, attrs = {}, ...kids) => {
    const n = document.createElement(tag);
    for (const [k, v] of Object.entries(attrs)) {
      if (v == null || v === false) continue;
      if (k === "class") n.className = v;
      else if (k === "html") n.innerHTML = v;
      else if (k.startsWith("on")) n.addEventListener(k.slice(2), v);
      else n.setAttribute(k, v === true ? "" : v);
    }
    for (const k of kids.flat()) if (k != null && k !== false) n.append(k instanceof Node ? k : document.createTextNode(String(k)));
    return n;
  };
  const svg = (tag, attrs = {}) => {
    const n = document.createElementNS("http://www.w3.org/2000/svg", tag);
    for (const [k, v] of Object.entries(attrs)) if (v != null) n.setAttribute(k, v);
    return n;
  };
  const monthFmt = new Intl.DateTimeFormat("nb-NO", { month: "short", year: "numeric" });
  const monthShort = new Intl.DateTimeFormat("nb-NO", { month: "short" });
  const fmtMonth = (m) => monthFmt.format(new Date(m + "-15"));
  const fmtMonthShort = (m) => monthShort.format(new Date(m + "-15")).replace(".", "") + (m.endsWith("-01") ? " " + m.slice(2, 4) : "");
  const fmtVal = (v, f) => {
    if (v == null) return "–";
    if (f === "pct") return Math.round(v * 100) + " %";
    if (f === "s") return (v / 1000).toLocaleString("nb-NO", { maximumFractionDigits: 1 }) + " s";
    if (f === "cls") return v.toLocaleString("nb-NO", { maximumFractionDigits: 2 });
    return Number(v).toLocaleString("nb-NO");
  };
  const status = (s) => s == null ? { cls: "low", label: "Ingen data" }
    : s >= 80 ? { cls: "good", label: "God" } : s >= 60 ? { cls: "medium", label: "OK" }
    : s >= 40 ? { cls: "high", label: "Svak" } : { cls: "critical", label: "Kritisk" };
  const badge = (cls, label) => h("span", { class: `badge ${cls}` }, h("span", { class: "dot", "aria-hidden": "true" }), label);
  const seriesColor = (i) => `var(--series-${(i % 8) + 1})`;

  function delta(cur, prev, higherBetter = true, f = "n") {
    if (cur == null || prev == null || higherBetter === null) return null;
    const d = cur - prev;
    if (Math.abs(d) < 1e-9) return h("span", { class: "delta flat" }, "± 0");
    const good = (d > 0) === higherBetter;
    const txt = f === "pct" ? Math.round(d * 100) + " pp" : f === "s" ? (d / 1000).toFixed(1) + " s" : f === "cls" ? d.toFixed(2) : Math.round(d * 10) / 10;
    return h("span", { class: `delta ${good ? "up" : "down"}`, title: good ? "Bedre enn forrige måling" : "Dårligere enn forrige måling" },
      d > 0 ? "▲ +" : "▼ ", String(txt).replace("-", "−"));
  }

  const clients = DATA.clients.map((c, i) => {
    const snaps = [...c.snapshots].sort((a, b) => a.month.localeCompare(b.month));
    return { ...c, color: seriesColor(i), snaps, latest: snaps.at(-1), prev: snaps.at(-2) };
  });
  // Sammenhengende månedsakse, slik at avstand på x-aksen tilsvarer faktisk tid
  const monthRange = (ms) => {
    if (!ms.length) return [];
    const out = [], [a, b] = [ms[0], ms.at(-1)];
    let [y, m] = a.split("-").map(Number);
    while (`${y}-${String(m).padStart(2, "0")}` <= b) { out.push(`${y}-${String(m).padStart(2, "0")}`); m++; if (m > 12) { m = 1; y++; } }
    return out;
  };
  // Scorer kan bare sammenlignes når metode og formelversjon er lik
  const comparable = (a, b) => !!(a && b && a.method === b.method && (a.method === "manual" || a.schema_version === b.schema_version));
  const allMonths = monthRange([...new Set(clients.flatMap((c) => c.snaps.map((s) => s.month)))].sort());

  // ------------------------------------------------------------------ tooltip
  function showTip(x, y, head, rows) {
    tip.replaceChildren(h("div", { class: "h" }, head),
      ...rows.map((r) => h("div", { class: "r" }, h("i", { style: `background:${r.color}` }), h("span", {}, r.label), h("b", {}, r.value))));
    tip.hidden = false;
    const w = tip.offsetWidth, ht = tip.offsetHeight;
    tip.style.left = Math.min(window.innerWidth - w - 8, x + 14) + "px";
    tip.style.top = Math.max(8, y - ht - 12) + "px";
  }
  const hideTip = () => { tip.hidden = true; };

  // ------------------------------------------------------------------ line chart
  function lineChart({ months, series, height = 260, yMax = 100, label }) {
    const wrap = h("div", { class: "chart", tabindex: "0", role: "img", "aria-label": label });
    const draw = () => {
      const W = Math.max(280, wrap.clientWidth || 600);
      const m = { t: 10, r: 14, b: 26, l: 30 };
      const iw = W - m.l - m.r, ih = height - m.t - m.b;
      const x = (i) => m.l + (months.length === 1 ? iw / 2 : (i / (months.length - 1)) * iw);
      const y = (v) => m.t + ih - (v / yMax) * ih;
      const s = svg("svg", { width: W, height, viewBox: `0 0 ${W} ${height}`, "aria-hidden": "true" });
      for (const v of [0, 25, 50, 75, 100]) {
        s.append(svg("line", { class: v === 0 ? "baseline" : "gridline", x1: m.l, x2: W - m.r, y1: y(v), y2: y(v) }));
        const t = svg("text", { class: "tick", x: m.l - 8, y: y(v) + 4, "text-anchor": "end" }); t.textContent = v; s.append(t);
      }
      const step = Math.ceil(months.length / Math.max(2, Math.floor(iw / 70)));
      months.forEach((mo, i) => {
        if (i % step && i !== months.length - 1) return;
        const t = svg("text", { class: "tick", x: x(i), y: height - 6, "text-anchor": "middle" });
        t.textContent = fmtMonthShort(mo); s.append(t);
      });
      const cross = svg("line", { class: "crosshair", y1: m.t, y2: m.t + ih, visibility: "hidden" });
      s.append(cross);
      for (const se of series) {
        const pts = se.points.map((p) => ({ ...p, i: months.indexOf(p.month) })).filter((p) => p.i >= 0 && p.y != null);
        for (let k = 1; k < pts.length; k++) {
          const a = pts[k - 1], b = pts[k];
          s.append(svg("path", { class: "line" + (a.manual || b.manual ? " dashed" : ""), d: `M${x(a.i)},${y(a.y)}L${x(b.i)},${y(b.y)}`, stroke: se.color }));
        }
        for (const p of pts) s.append(svg("circle", { class: "pt" + (p.manual ? " manual" : ""), cx: x(p.i), cy: y(p.y), r: 4.5, fill: se.color, style: p.manual ? `stroke:${se.color}` : null }));
      }
      const hit = svg("rect", { class: "hit", x: m.l - 10, y: 0, width: iw + 20, height });
      const at = (i, cx, cy) => {
        cross.setAttribute("x1", x(i)); cross.setAttribute("x2", x(i)); cross.setAttribute("visibility", "visible");
        const rows = series.map((se) => {
          const p = se.points.find((q) => q.month === months[i]);
          return p && p.y != null ? { color: se.color, label: se.name + (p.manual ? " (manuell)" : ""), value: p.y, y: p.y } : null;
        }).filter(Boolean).sort((a, b) => b.y - a.y);
        if (rows.length) showTip(cx, cy, fmtMonth(months[i]), rows); else hideTip();
      };
      hit.addEventListener("pointermove", (e) => {
        const r = s.getBoundingClientRect();
        const px = e.clientX - r.left;
        let best = 0;
        months.forEach((_, i) => { if (Math.abs(x(i) - px) < Math.abs(x(best) - px)) best = i; });
        wrap.dataset.idx = best;
        at(best, e.clientX, e.clientY);
      });
      hit.addEventListener("pointerleave", () => { cross.setAttribute("visibility", "hidden"); hideTip(); });
      s.append(hit);
      wrap.onkeydown = (e) => {
        if (!["ArrowLeft", "ArrowRight"].includes(e.key)) return;
        e.preventDefault();
        let i = Number(wrap.dataset.idx ?? months.length - 1) + (e.key === "ArrowRight" ? 1 : -1);
        i = Math.max(0, Math.min(months.length - 1, i));
        wrap.dataset.idx = i;
        const r = s.getBoundingClientRect();
        at(i, r.left + x(i), r.top + m.t + 20);
      };
      wrap.onblur = () => { cross.setAttribute("visibility", "hidden"); hideTip(); };
      wrap.replaceChildren(s);
    };
    wrap._draw = draw;
    requestAnimationFrame(draw);
    return wrap;
  }

  function legend(series, extra = []) {
    return h("div", { class: "legend" },
      ...series.map((se) => h("span", { class: "k" }, h("span", { class: "sw", style: `background:${se.color}` }), se.name)),
      ...extra);
  }

  function sparkline(c) {
    const W = 140, H = 36, pts = c.snaps.filter((s) => s.score != null);
    const s = svg("svg", { width: W, height: H, viewBox: `0 0 ${W} ${H}`, class: "spark", "aria-hidden": "true" });
    if (pts.length < 2) {
      const t = svg("text", { x: 0, y: H / 2 + 4, class: "tick", fill: "var(--muted)", "font-size": 11 }); t.textContent = "1 måling"; s.append(t);
      return s;
    }
    const x = (i) => 4 + (i / (pts.length - 1)) * (W - 8), y = (v) => H - 4 - (v / 100) * (H - 8);
    s.append(svg("path", { d: pts.map((p, i) => `${i ? "L" : "M"}${x(i)},${y(p.score)}`).join(""), fill: "none", stroke: c.color, "stroke-width": 2, "stroke-linejoin": "round", "stroke-linecap": "round" }));
    s.append(svg("circle", { cx: x(pts.length - 1), cy: y(pts.at(-1).score), r: 4, fill: c.color, stroke: "var(--surface)", "stroke-width": 2 }));
    return s;
  }

  function scoreRing(score) {
    const r = 56, C = 2 * Math.PI * r, v = score ?? 0;
    const s = svg("svg", { width: 132, height: 132, viewBox: "0 0 132 132", "aria-hidden": "true" });
    s.append(svg("circle", { cx: 66, cy: 66, r, fill: "none", stroke: "var(--surface-2)", "stroke-width": 10 }));
    s.append(svg("circle", { cx: 66, cy: 66, r, fill: "none", stroke: "var(--series-1)", "stroke-width": 10, "stroke-linecap": "round", "stroke-dasharray": `${(v / 100) * C} ${C}` }));
    return h("div", { class: "score-ring" }, s, h("div", { class: "v" }, h("div", {}, h("b", {}, score ?? "–"), h("span", {}, "av 100"))));
  }

  const issueCounts = (snap) => {
    const c = { critical: 0, high: 0, medium: 0, low: 0 };
    for (const i of snap?.issues || []) c[i.severity]++;
    return c;
  };

  // ------------------------------------------------------------------ overview
  function renderOverview() {
    const latestScores = clients.map((c) => c.latest?.score).filter((v) => v != null);
    const avg = latestScores.length ? Math.round(latestScores.reduce((a, b) => a + b, 0) / latestScores.length) : null;
    const withPrev = clients.filter((c) => comparable(c.latest, c.prev));
    const avgPrev = withPrev.length ? Math.round(withPrev.reduce((a, c) => a + c.prev.score, 0) / withPrev.length) : null;
    const avgCurSame = withPrev.length ? Math.round(withPrev.reduce((a, c) => a + c.latest.score, 0) / withPrev.length) : null;
    const crit = clients.reduce((a, c) => a + issueCounts(c.latest).critical, 0);
    const high = clients.reduce((a, c) => a + issueCounts(c.latest).high, 0);
    const lastDate = clients.map((c) => c.latest?.date).filter(Boolean).sort().at(-1);
    const improving = withPrev.filter((c) => c.latest.score > c.prev.score).length;

    const series = clients.map((c) => ({ name: c.name, color: c.color, points: c.snaps.map((s) => ({ month: s.month, y: s.score, manual: s.method === "manual" })) }));
    const sorted = [...clients].sort((a, b) => (a.latest?.score ?? -1) - (b.latest?.score ?? -1));

    app.replaceChildren(
      h("div", { class: "page-head" }, h("div", {},
        h("h1", {}, "Kundeoversikt"),
        h("div", { class: "sub" }, `${clients.length} kunder · månedlig SEO-audit`))),
      h("div", { class: "grid cols-4" },
        h("div", { class: "card stat" }, h("div", { class: "label" }, "Snittscore"), h("div", { class: "value" }, avg ?? "–"),
          h("div", { class: "foot" }, delta(avgCurSame, avgPrev), avgPrev != null ? "mot forrige måling" : "")),
        h("div", { class: "card stat" }, h("div", { class: "label" }, "Forbedret siden sist"), h("div", { class: "value" }, withPrev.length ? `${improving}/${withPrev.length}` : "–"),
          h("div", { class: "foot" }, withPrev.length ? "kunder med høyere score" : "trenger to automatiske målinger")),
        h("div", { class: "card stat" }, h("div", { class: "label" }, "Kritiske funn"), h("div", { class: "value" }, crit),
          h("div", { class: "foot" }, badge("critical", "Kritisk"), `+ ${high} høy`)),
        h("div", { class: "card stat" }, h("div", { class: "label" }, "Siste måling"),
          h("div", { class: "value", style: "font-size:24px;margin-top:10px" }, lastDate ? new Date(lastDate).toLocaleDateString("nb-NO", { day: "numeric", month: "short", year: "numeric" }) : "–"),
          h("div", { class: "foot" }, "neste kjøres automatisk 1. i måneden"))),
      h("div", { class: "card section" },
        h("div", { class: "card-head" }, h("h2", {}, "Helsescore over tid"), h("span", { class: "hint" }, "Hul markør og stiplet linje = manuell audit")),
        legend(series),
        lineChart({ months: allMonths, series, label: "Helsescore per kunde over tid" })),
      h("div", { class: "section" },
        h("div", { class: "card-head", style: "padding:0 4px" }, h("h2", {}, "Kunder"), h("span", { class: "hint" }, "Sortert etter score, lavest først")),
        h("div", { class: "client-list-head", "aria-hidden": "true" }, h("span", {}, "Kunde"), h("span", {}, "Score"), h("span", {}, "Utvikling"), h("span", {}, "Kategorier"), h("span", {}, "Åpne funn"), h("span", {})),
        h("div", { class: "client-list" }, ...sorted.map(clientRow))),
    );
  }

  function clientRow(c) {
    const L = c.latest, st = status(L?.score), ic = issueCounts(L);
    return h("a", { class: "client-row", href: `#/c/${c.slug}` },
      h("div", { style: "min-width:0" }, h("div", { class: "name" }, c.name), h("div", { class: "domain" }, c.url.replace(/^https?:\/\/(www\.)?/, "").replace(/\/$/, ""))),
      h("div", {}, h("div", { class: "score" }, L?.score ?? "–"), h("div", { style: "margin-top:4px;display:flex;gap:6px;align-items:center" },
        (comparable(L, c.prev) && delta(L?.score, c.prev.score)) || badge(st.cls, st.label))),
      h("div", { class: "spark" }, sparkline(c)),
      h("div", { class: "cats", title: CATS.map(([k, l]) => `${l}: ${L?.categories?.[k] ?? "–"}`).join(" · ") },
        ...CATS.map(([k, l]) => h("div", { class: "c", "aria-label": `${l} ${L?.categories?.[k] ?? "ingen data"}` },
          h("i", { style: `height:${L?.categories?.[k] ?? 0}%` })))),
      h("div", { class: "issues" },
        ic.critical ? badge("critical", `${ic.critical} kritisk`) : null,
        ic.high ? badge("high", `${ic.high} høy`) : null,
        !ic.critical && !ic.high ? (L?.method === "manual" ? badge("manual", "Manuell") : badge("good", "Ingen alvorlige")) : null),
      h("span", { class: "chev", "aria-hidden": "true" }, "→"));
  }

  // ------------------------------------------------------------------ client
  function renderClient(slug, month) {
    const c = clients.find((x) => x.slug === slug);
    if (!c) return app.replaceChildren(h("div", { class: "empty" }, "Fant ikke kunden. ", h("a", { href: "#/" }, "Til oversikten")));
    const idx = month ? c.snaps.findIndex((s) => s.month === month) : c.snaps.length - 1;
    const S = c.snaps[idx], P = c.snaps[idx - 1];
    if (!S) return app.replaceChildren(h("div", { class: "empty" }, "Ingen målinger ennå."));
    const st = status(S.score);
    const lastAuto = [...c.snaps.slice(0, idx)].reverse().find((s) => s.method === "automated");

    const monthSel = h("select", { class: "select", "aria-label": "Velg måned", onchange: (e) => { location.hash = `#/c/${slug}/${e.target.value}`; } },
      ...[...c.snaps].reverse().map((s) => h("option", { value: s.month, selected: s.month === S.month }, fmtMonth(s.month) + (s.method === "manual" ? " (manuell)" : ""))));

    // Kategorier
    const catCard = h("div", { class: "card" },
      h("div", { class: "card-head" }, h("h2", {}, "Kategorier")),
      h("div", { class: "legend" }, h("span", { class: "k" }, h("span", { class: "sw rect", style: "background:var(--series-1)" }), fmtMonth(S.month)),
        P ? h("span", { class: "k" }, h("span", { class: "sw tick" }), fmtMonth(P.month) + (P.method === "manual" ? " (manuell)" : "")) : null),
      h("div", { class: "catbars" }, ...CATS.map(([k, l]) => {
        const v = S.categories?.[k], pv = P?.categories?.[k];
        const row = h("div", { class: "catbar" }, h("span", {}, l),
          h("div", { class: "track" }, h("div", { class: "fill", style: `width:${v ?? 0}%` }), pv != null ? h("div", { class: "prev", style: `left:calc(${pv}% - 1px)` }) : null),
          h("span", { class: "val" }, v ?? "–", " ", (comparable(S, P) && delta(v, pv)) || ""));
        row.addEventListener("pointermove", (e) => showTip(e.clientX, e.clientY, l, [
          { color: "var(--series-1)", label: fmtMonth(S.month), value: v ?? "–" },
          ...(P ? [{ color: "var(--ink-2)", label: fmtMonth(P.month), value: pv ?? "–" }] : [])]));
        row.addEventListener("pointerleave", hideTip);
        return row;
      })));

    // Trend
    const trendSeries = [{ name: "Total", color: "var(--series-1)", points: c.snaps.map((s) => ({ month: s.month, y: s.score, manual: s.method === "manual" })) }];
    const months = monthRange(c.snaps.map((s) => s.month));
    const trendCard = h("div", { class: "card" },
      h("div", { class: "card-head" }, h("h2", {}, "Helsescore over tid"), h("span", { class: "hint" }, "Hul markør = manuell audit")),
      lineChart({ months, series: trendSeries, height: 220, label: `Helsescore for ${c.name} over tid` }));

    // KPI-er
    const K = S.kpis, PK = P?.kpis;
    const kpiCard = K ? h("div", { class: "card section" },
      h("div", { class: "card-head" }, h("h2", {}, "Nøkkeltall"), PK ? h("span", { class: "hint" }, `Endring mot ${fmtMonth(P.month)}`) : null),
      h("div", { class: "kpis" }, ...KPIS.filter(([k]) => k in K).map(([k, l, hb, f, of]) => h("div", { class: "kpi" },
        h("div", { class: "l" }, l),
        h("div", { class: "v" }, fmtVal(K[k], f), of && K[of] != null ? h("span", { class: "muted", style: "font-size:14px;font-weight:500" }, ` / ${K[of]}`) : null),
        h("div", { class: "d" }, PK ? delta(K[k], PK[k], hb, f) : null))))) : null;

    // Ytelse
    const perf = (S.performance || []).filter((p) => p.score != null);
    const lcpB = (v) => v == null ? null : v <= 2500 ? badge("good", "God") : v <= 4000 ? badge("medium", "Middels") : badge("critical", "Dårlig");
    const clsB = (v) => v == null ? null : v <= 0.1 ? badge("good", "God") : v <= 0.25 ? badge("medium", "Middels") : badge("critical", "Dårlig");
    const perfCard = perf.length ? h("div", { class: "card section" },
      h("div", { class: "card-head" }, h("h2", {}, "Ytelse (mobil)"), h("span", { class: "hint" }, perf[0].source === "psi" ? "PageSpeed Insights" : "Lighthouse lokalt (lab)")),
      h("table", { class: "perf-table" },
        h("thead", {}, h("tr", {}, h("th", {}, "Side"), h("th", {}, "Score"), h("th", {}, "LCP"), h("th", {}), h("th", {}, "CLS"), h("th", {}), h("th", {}, "Felt-LCP (CrUX)"))),
        h("tbody", {}, ...perf.map((p) => {
          const f = p.field_origin || p.field_page;
          const flcp = f?.LARGEST_CONTENTFUL_PAINT_MS?.p75;
          return h("tr", {},
            h("td", { class: "url", title: p.url }, p.url.replace(/^https?:\/\/[^/]+/, "") || "/"),
            h("td", {}, h("b", {}, p.score)),
            h("td", {}, fmtVal(p.lcp_ms, "s")), h("td", {}, lcpB(p.lcp_ms)),
            h("td", {}, fmtVal(p.cls, "cls")), h("td", {}, clsB(p.cls)),
            h("td", {}, flcp ? fmtVal(flcp, "s") : h("span", { class: "muted" }, "–")));
        })))) : null;

    // Funn
    const prevIds = new Set((lastAuto?.issues || []).map((i) => i.id));
    const curIds = new Set((S.issues || []).map((i) => i.id));
    const resolved = S.method === "automated" ? (lastAuto?.issues || []).filter((i) => !curIds.has(i.id)) : [];
    const issues = [...(S.issues || [])].sort((a, b) => SEV_ORDER.indexOf(a.severity) - SEV_ORDER.indexOf(b.severity) || b.count - a.count);
    const issuesCard = S.method === "automated" ? h("div", { class: "card section" },
      h("div", { class: "card-head" }, h("h2", {}, "Funn"), h("span", { class: "hint" }, `${issues.length} åpne · ${resolved.length} løst siden forrige måling`)),
      issues.length ? h("div", { class: "issues-list" }, ...issues.map((i) => h("details", { class: "issue" },
        h("summary", {}, badge(i.severity, SEV[i.severity]),
          h("span", { class: "t" }, i.title, lastAuto && !prevIds.has(i.id) ? h("span", { class: "tag" }, "Ny") : null),
          h("span", { class: "count" }, i.of && i.of > 1 ? `${i.count} av ${i.of}` : i.count > 1 ? i.count : "")),
        h("div", { class: "body" }, i.fix ? h("div", {}, i.fix) : null,
          i.examples?.length ? h("ul", {}, ...i.examples.map((u) => h("li", {}, /^https?:/.test(u) ? h("a", { href: u, target: "_blank", rel: "noopener" }, u.replace(/^https?:\/\/[^/]+/, "") || "/") : u))) : null,
          i.count > (i.examples?.length || 0) ? h("div", { class: "note" }, `+ ${i.count - i.examples.length} flere`) : null)))) : h("div", { class: "empty" }, "Ingen funn 🎉"),
      resolved.length ? h("div", { class: "resolved" }, h("h3", {}, "Løst siden forrige måling"), h("ul", {}, ...resolved.map((i) => h("li", {}, "✓ ", i.title))) ) : null)
      : h("div", { class: "card section" }, h("div", { class: "card-head" }, h("h2", {}, "Funn")), h("p", { class: "ink-2", style: "margin:0" }, S.note || "Manuell audit. Se rapportene under."));

    // Rapporter
    const tabs = REPORT_TABS.filter(([k]) => S.reports?.[k]);
    let reportsCard = null;
    if (tabs.length) {
      const body = h("div", { class: "md" });
      const btns = tabs.map(([k, l], i) => h("button", { class: "tab", role: "tab", type: "button", "aria-selected": i === 0 ? "true" : "false",
        onclick: (e) => { btns.forEach((b) => b.setAttribute("aria-selected", "false")); e.currentTarget.setAttribute("aria-selected", "true"); renderMd(body, S.reports[k]); } }, l));
      renderMd(body, S.reports[tabs[0][0]]);
      reportsCard = h("div", { class: "card section" }, h("div", { class: "card-head" }, h("h2", {}, "Rapporter")), h("div", { class: "tabs", role: "tablist" }, ...btns), body);
    }

    app.replaceChildren(
      h("a", { class: "back", href: "#/" }, "← Alle kunder"),
      h("div", { class: "page-head" },
        h("div", {}, h("h1", {}, c.name), h("div", { class: "sub" }, h("a", { href: c.url, target: "_blank", rel: "noopener" }, c.url.replace(/^https?:\/\//, "").replace(/\/$/, "")))),
        h("div", { class: "actions" }, monthSel)),
      h("div", { class: "grid split" },
        h("div", { class: "card" }, h("div", { class: "hero" }, scoreRing(S.score), h("div", { class: "hero-meta" },
          h("div", {}, badge(st.cls, st.label)),
          comparable(S, P) ? h("div", { class: "ink-2", style: "font-size:14px" }, delta(S.score, P.score), ` mot ${fmtMonth(P.month)}`)
            : h("div", { class: "muted", style: "font-size:14px" }, P ? `Ny målemetode – ikke sammenlignbar med ${fmtMonth(P.month)} (${P.score})` : "Første måling"),
          h("div", { class: "muted", style: "font-size:13px" }, S.method === "manual" ? "Manuell audit" : "Automatisk måling", " · ", new Date(S.date).toLocaleDateString("nb-NO")),
          S.sampled ? h("div", { class: "muted", style: "font-size:13px" }, `Utvalg: ${S.kpis.pages_crawled} av ${S.kpis.pages_in_sitemap} sider`) : null))),
        trendCard),
      h("div", { class: "section" }, catCard),
      kpiCard, perfCard, issuesCard, reportsCard);
    window.scrollTo(0, 0);
  }

  function renderMd(target, md) {
    const html = window.marked ? window.marked.parse(md) : md.replace(/[&<>]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;" }[c]));
    target.innerHTML = window.DOMPurify ? window.DOMPurify.sanitize(html) : html;
    target.querySelectorAll("a[href^='http']").forEach((a) => { a.target = "_blank"; a.rel = "noopener"; });
  }

  // ------------------------------------------------------------------ router
  function route() {
    hideTip();
    const [, view, slug, month] = location.hash.split("/");
    if (view === "c" && slug) renderClient(decodeURIComponent(slug), month);
    else renderOverview();
  }

  document.getElementById("generated").textContent = DATA.generated ? "Oppdatert " + new Date(DATA.generated).toLocaleDateString("nb-NO", { day: "numeric", month: "short", year: "numeric" }) : "";
  document.getElementById("theme-toggle").addEventListener("click", () => {
    const dark = document.documentElement.dataset.theme ? document.documentElement.dataset.theme === "dark" : matchMedia("(prefers-color-scheme: dark)").matches;
    const next = dark ? "light" : "dark";
    document.documentElement.dataset.theme = next;
    try { localStorage.setItem("seo-theme", next); } catch (e) { /* privat modus */ }
  });
  let rt;
  window.addEventListener("resize", () => { clearTimeout(rt); rt = setTimeout(() => document.querySelectorAll(".chart").forEach((c) => c._draw?.()), 120); });
  window.addEventListener("hashchange", route);
  route();
})();
