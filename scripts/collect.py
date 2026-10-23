#!/usr/bin/env python3
"""Samler harde SEO-målinger for én eller alle kunder og skriver
clients/<slug>/<YYYY-MM>/metrics.json (+ pages.json med per-side-data).

Kun standardbibliotek, slik at skriptet kjører likt lokalt og i skyrutinen.

  python3 scripts/collect.py --all
  python3 scripts/collect.py --client moss --month 2026-10
  python3 scripts/collect.py --client moss --no-perf

Ytelse: bruker PageSpeed Insights-API (+ CrUX-feltdata) når GOOGLE_API_KEY er satt,
ellers lokal Lighthouse via npx hvis Chrome finnes, ellers hoppes ytelse over.
"""
import argparse, concurrent.futures as cf, datetime as dt, hashlib, json, os, re, shutil
import statistics, subprocess, sys, tempfile, time, tomllib, urllib.error, urllib.parse
import urllib.request, urllib.robotparser
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (compatible; SEO-audit/1.0; +https://breakfast.no)"
SCHEMA_VERSION = 2
WEIGHTS = {"technical": 22, "content": 23, "onpage": 20, "schema": 10,
           "performance": 10, "ai": 10, "images": 5}
AI_BOTS = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-User",
           "PerplexityBot", "Google-Extended", "Applebot-Extended", "CCBot"]
ORG_TYPES = {"Organization", "LocalBusiness", "PerformingArtsTheater", "PerformingGroup",
             "EntertainmentBusiness", "CivicStructure", "MusicVenue", "EventVenue",
             "Corporation", "ProfessionalService", "NGO", "GovernmentOrganization"}
EVENT_TYPES = {"Event", "MusicEvent", "TheaterEvent", "ComedyEvent", "DanceEvent",
               "Festival", "ChildrensEvent", "ScreeningEvent", "LiteraryEvent",
               "EducationEvent", "SocialEvent", "ExhibitionEvent", "VisualArtsEvent"}
GENERIC_TYPES = {"WebSite", "WebPage", "CollectionPage", "BreadcrumbList", "ListItem",
                 "SearchAction", "EntryPoint", "PropertyValueSpecification", "ReadAction",
                 "ImageObject", "Person", "ContactPage", "AboutPage"}
DEFAULT_EVENT_PATTERNS = ["/event/", "/arrangement/", "/forestilling/", "event-sitemap"]
THIN_WORDS = 150


# ---------------------------------------------------------------- HTTP
def fetch(url, timeout=30, method="GET", follow=True):
    """Returnerer (status, final_url, headers(dict, lower), body str). Feil -> status 0."""
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "nb-NO,nb;q=0.9"},
                                 method=method)
    opener = urllib.request.build_opener() if follow else urllib.request.build_opener(_NoRedirect)
    try:
        with opener.open(req, timeout=timeout) as r:
            body = r.read().decode("utf-8", "replace") if method == "GET" else ""
            return r.status, r.geturl(), {k.lower(): v for k, v in r.headers.items()}, body
    except urllib.error.HTTPError as e:
        return e.code, url, {k.lower(): v for k, v in (e.headers or {}).items()}, ""
    except Exception as e:  # noqa: BLE001 – nettverksfeil registreres som status 0
        return 0, url, {"error": str(e)}, ""


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


# ---------------------------------------------------------------- HTML-parsing
class PageParser(HTMLParser):
    BLOCK = {"p", "li", "h1", "h2", "h3", "h4", "h5", "h6", "td", "th", "div", "section",
             "article", "header", "footer", "nav", "a", "span", "figcaption", "blockquote",
             "dd", "dt", "button", "label"}

    def __init__(self, base):
        super().__init__(convert_charrefs=True)
        self.base = base
        self.title, self.h1, self.h2 = "", [], 0
        self.meta, self.canonical, self.lang = {}, None, None
        self.jsonld, self.microdata = [], set()
        self.links, self.imgs = set(), []
        self.blocks, self._buf = [], []
        self._stack, self._skip, self._ld = [], 0, False

    def _flush(self):
        t = re.sub(r"\s+", " ", "".join(self._buf)).strip()
        if t:
            self.blocks.append(t)
        self._buf = []

    def handle_starttag(self, tag, attrs):
        a = {k: (v or "") for k, v in attrs}
        if tag == "html":
            self.lang = a.get("lang")
        if tag in ("script", "style", "noscript", "template", "svg"):
            self._skip += 1
            if tag == "script" and a.get("type", "").lower() == "application/ld+json":
                self._ld = True
                self.jsonld.append("")
        if tag in self.BLOCK or tag == "br":
            self._flush()
        if tag in ("title", "h1"):
            self._stack.append(tag)
            if tag == "h1":
                self.h1.append("")
        elif tag == "h2":
            self.h2 += 1
        if "itemtype" in a:
            self.microdata.add(a["itemtype"].rstrip("/").rsplit("/", 1)[-1])
        if tag == "meta":
            k = (a.get("name") or a.get("property") or "").lower()
            if k:
                self.meta[k] = a.get("content", "")
        elif tag == "link" and "canonical" in a.get("rel", "").lower().split():
            self.canonical = urllib.parse.urljoin(self.base, a.get("href", ""))
        elif tag == "a" and a.get("href"):
            self.links.add(urllib.parse.urljoin(self.base, a["href"]).split("#")[0])
        elif tag == "img":
            src = a.get("src") or a.get("data-src") or ""
            self.imgs.append({
                "src": src,
                "alt": a.get("alt"),
                "decorative": a.get("aria-hidden") == "true" or a.get("role") in ("presentation", "none"),
                "lazy": a.get("loading") == "lazy" or "data-src" in a or "lazyload" in a.get("class", ""),
                "dims": bool(a.get("width") and a.get("height")),
                "modern": bool(re.search(r"\.(webp|avif|svg)(\?|$)", src.lower())) or "image/webp" in a.get("srcset", ""),
            })

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript", "template", "svg"):
            self._skip = max(0, self._skip - 1)
            if tag == "script":
                self._ld = False
        if self._stack and self._stack[-1] == tag:
            self._stack.pop()
        if tag in self.BLOCK:
            self._flush()

    def handle_data(self, data):
        if self._ld:
            self.jsonld[-1] += data
            return
        if self._skip:
            return
        if "title" in self._stack:
            self.title += data
            return
        if "h1" in self._stack:
            self.h1[-1] += data
        self._buf.append(data)

    def close(self):
        super().close()
        self._flush()


def jsonld_types(chunks):
    types = set()

    def walk(o):
        if isinstance(o, dict):
            t = o.get("@type")
            for x in (t if isinstance(t, list) else [t]):
                if isinstance(x, str):
                    types.add(x)
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    for c in chunks:
        try:
            walk(json.loads(c))
        except Exception:  # noqa: BLE001 – ugyldig JSON-LD telles som feil
            types.add("__invalid__")
    return types


# ---------------------------------------------------------------- URL-oppdagelse
def sitemap_urls(site, robots_txt):
    """Returnerer [(sitemapnavn, url)]. Følger sitemap-indekser ett nivå ned."""
    roots = re.findall(r"(?im)^\s*sitemap:\s*(\S+)", robots_txt) or [
        urllib.parse.urljoin(site, p) for p in ("/sitemap_index.xml", "/sitemap.xml", "/wp-sitemap.xml")]
    out, seen = [], set()

    def read(sm, depth=0):
        if sm in seen or depth > 2:
            return
        seen.add(sm)
        st, _, _, body = fetch(sm)
        if st != 200 or "<" not in body:
            return
        if "<sitemapindex" in body:
            for child in re.findall(r"<sitemap>\s*<loc>\s*(.*?)\s*</loc>", body, re.S):
                read(child.strip(), depth + 1)
        else:
            name = sm.rsplit("/", 1)[-1]
            for u in re.findall(r"<url>\s*<loc>\s*(.*?)\s*</loc>", body, re.S):
                out.append((name, u.strip().replace("&amp;", "&")))
    for r in roots:
        read(r)
        if out:
            break
    return out


def sample(rows, limit):
    """Proporsjonalt utvalg per undersitemap når det er flere URL-er enn taket."""
    if len(rows) <= limit:
        return rows
    groups = defaultdict(list)
    for r in rows:
        groups[r[0]].append(r)
    picked = []
    for name, g in groups.items():
        n = max(1, round(limit * len(g) / len(rows)))
        step = len(g) / n
        picked += [g[int(i * step)] for i in range(min(n, len(g)))]
    return picked[:limit]


# ---------------------------------------------------------------- robots
def robots_info(txt):
    rp = urllib.robotparser.RobotFileParser()
    rp.parse(txt.splitlines())
    delay = None
    m = re.search(r"(?im)^\s*crawl-delay:\s*([\d.]+)", txt)
    if m:
        delay = float(m.group(1))
    blocked = [b for b in AI_BOTS if not rp.can_fetch(b, "/")]
    return rp, {"crawl_delay": delay, "ai_bots_blocked": blocked,
                "all_blocked": not rp.can_fetch("*", "/")}


# ---------------------------------------------------------------- per side
def analyze_page(row, host):
    sm, url = row
    t0 = time.time()
    for attempt in range(3):  # forbigående 5xx/nettverksfeil skal ikke telle som feil
        st, final, hdr, body = fetch(url)
        if st and st < 500:
            break
        time.sleep(3 * (attempt + 1))
    rec = {"url": url, "sitemap": sm, "status": st, "final": final,
           "ms": round((time.time() - t0) * 1000)}
    if st != 200 or "html" not in hdr.get("content-type", "html"):
        return rec, []
    p = PageParser(final)
    p.feed(body)
    p.close()
    types = jsonld_types(p.jsonld) | p.microdata
    robots = (p.meta.get("robots", "") + "," + hdr.get("x-robots-tag", "")).lower()
    imgs = p.imgs
    rec.update({
        "title": re.sub(r"\s+", " ", p.title).strip(),
        "h1": [re.sub(r"\s+", " ", h).strip() for h in p.h1],
        "h2": p.h2,
        "desc": (p.meta.get("description") or "").strip(),
        "og_image": bool(p.meta.get("og:image")),
        "canonical": p.canonical,
        "noindex": "noindex" in robots,
        "lang": p.lang,
        "types": sorted(types),
        "internal_links": sorted(l for l in p.links if urllib.parse.urlparse(l).netloc == host),
        "img_total": len(imgs),
        "img_content": sum(not i["decorative"] for i in imgs),
        "img_alt_ok": sum(not i["decorative"] and bool((i["alt"] or "").strip()) for i in imgs),
        "img_alt_missing_attr": sum(i["alt"] is None for i in imgs),
        "img_lazy_candidates": max(0, len(imgs) - 3),
        "img_lazy": sum(i["lazy"] for i in imgs[3:]),
        "img_modern": sum(i["modern"] for i in imgs if i["src"]),
        "img_with_src": sum(bool(i["src"]) for i in imgs),
        "img_dims": sum(i["dims"] for i in imgs),
        "bytes": len(body),
    })
    return rec, p.blocks


# ---------------------------------------------------------------- ytelse
def perf_psi(url, key):
    q = urllib.parse.urlencode({"url": url, "strategy": "mobile", "key": key,
                                "category": "performance"})
    st, _, _, body = fetch("https://www.googleapis.com/pagespeedonline/v5/runPagespeed?" + q, timeout=120)
    if st != 200:
        return {"url": url, "source": "psi", "error": f"HTTP {st}"}
    d = json.loads(body)
    out = _lh_extract(d["lighthouseResult"])
    out.update({"url": url, "source": "psi"})
    for scope in ("loadingExperience", "originLoadingExperience"):
        m = d.get(scope, {}).get("metrics")
        if m:
            out["field_" + ("page" if scope == "loadingExperience" else "origin")] = {
                k: {"p75": v.get("percentile"), "category": v.get("category")} for k, v in m.items()}
    return out


def perf_local(url):
    npx = shutil.which("npx")
    if not npx:
        return None
    with tempfile.TemporaryDirectory() as td:
        outp = Path(td) / "lh.json"
        cmd = [npx, "-y", "lighthouse@12.6.0", url, "--quiet", "--chrome-flags=--headless=new",
               "--only-categories=performance", "--output=json", f"--output-path={outp}"]
        try:
            subprocess.run(cmd, check=True, capture_output=True, timeout=300)
            out = _lh_extract(json.loads(outp.read_text()))
        except Exception as e:  # noqa: BLE001
            return {"url": url, "source": "lighthouse-local", "error": str(e)[:200]}
    out.update({"url": url, "source": "lighthouse-local"})
    return out


def _lh_extract(L):
    a = L["audits"]
    num = lambda k: a.get(k, {}).get("numericValue")
    return {
        "score": round((L["categories"]["performance"]["score"] or 0) * 100),
        "lcp_ms": num("largest-contentful-paint"), "cls": num("cumulative-layout-shift"),
        "tbt_ms": num("total-blocking-time"), "fcp_ms": num("first-contentful-paint"),
        "si_ms": num("speed-index"), "bytes": num("total-byte-weight"),
        "render_blocking_ms": a.get("render-blocking-resources", {}).get("details", {}).get("overallSavingsMs"),
        "offscreen_bytes": a.get("offscreen-images", {}).get("details", {}).get("overallSavingsBytes"),
    }


# ---------------------------------------------------------------- scoring
def share(n, d):
    return n / d if d else 0.0


def clamp(x):
    return max(0, min(100, round(x)))


def title_problems(title):
    segs = [s.strip().lower() for s in re.split(r"\s+[-|–—·:]\s+", title) if len(s.strip()) > 3]
    return {"missing": not title, "length": not (15 <= len(title) <= 65),
            "repeated_segment": len(segs) != len(set(segs))}


def score_and_issues(site, pages, perf, cfg):
    ok = [p for p in pages if p["status"] == 200 and "title" in p]
    n = len(ok) or 1
    host = urllib.parse.urlparse(site["final_url"]).netloc
    pats = cfg.get("event_patterns", DEFAULT_EVENT_PATTERNS)
    is_event = lambda p: any(x in p["url"] or x in p["sitemap"] for x in pats)

    # --- grunnlagstall
    non200 = [p for p in pages if p["status"] != 200]
    redirected = [p for p in pages if p["status"] == 200 and p["final"].rstrip("/") != p["url"].rstrip("/")]
    noindex = [p for p in ok if p["noindex"]]
    canon_else = [p for p in ok if p["canonical"] and p["canonical"].rstrip("/") != p["final"].rstrip("/")]
    thin = [p for p in ok if p["unique_words"] < THIN_WORDS]
    tcount = Counter(p["title"] for p in ok if p["title"])
    tp = {p["url"]: title_problems(p["title"]) for p in ok}
    bad_title = [p for p in ok if any(tp[p["url"]].values()) or tcount[p["title"]] > 1]
    repeated_brand = [p for p in ok if tp[p["url"]]["repeated_segment"]]
    dup_title = [p for p in ok if p["title"] and tcount[p["title"]] > 1]
    no_h1 = [p for p in ok if not any(p["h1"])]
    multi_h1 = [p for p in ok if len(p["h1"]) > 1]
    no_desc = [p for p in ok if not p["desc"]]
    no_og = [p for p in ok if not p["og_image"]]
    hashes = Counter(p["content_hash"] for p in ok if p["unique_words"] >= THIN_WORDS)
    dup_content = [p for p in ok if p["unique_words"] >= THIN_WORDS and hashes[p["content_hash"]] > 1]
    inbound = Counter(l.rstrip("/") for p in ok for l in p["internal_links"])
    orphans = [p for p in ok if inbound[p["url"].rstrip("/")] == 0 and p["url"].rstrip("/") != site["final_url"].rstrip("/")]
    events = [p for p in ok if is_event(p)]
    events_no_schema = [p for p in events if not EVENT_TYPES & set(p["types"])]
    home = next((p for p in ok if p["url"].rstrip("/") == site["final_url"].rstrip("/")), None)
    all_types = Counter(t for p in ok for t in p["types"])
    has_org = bool(ORG_TYPES & set(all_types))
    invalid_ld = [p for p in ok if "__invalid__" in p["types"]]
    img_content = sum(p["img_content"] for p in ok)
    img_alt_ok = sum(p["img_alt_ok"] for p in ok)
    lazy_c = sum(p["img_lazy_candidates"] for p in ok)
    lazy_ok = sum(p["img_lazy"] for p in ok)
    img_src = sum(p["img_with_src"] for p in ok)
    img_modern = sum(p["img_modern"] for p in ok)
    med_words = statistics.median([p["unique_words"] for p in ok]) if ok else 0
    sec = site["security_headers"]
    rob = site["robots"]

    # --- kategoriscorer (0–100). Formelen er fast; endres den, øk SCHEMA_VERSION.
    cats = {}
    cats["technical"] = clamp(
        10 * bool(pages)
        + 15 * (1 - share(len(non200) + len(redirected), len(pages)))
        + 10 * (1 - share(len(noindex), n))
        + 10 * (1 - share(len(canon_else), n))
        + 5 * site["https_redirect"]
        + 10 * sec["strict-transport-security"] + 5 * sec["x-content-type-options"]
        + 5 * sec["referrer-policy"] + 5 * sec["frame-protection"]
        + 5 * site["robots_found"] + 5 * (not rob["crawl_delay"] or rob["crawl_delay"] <= 2)
        + 15 * (1 - share(len(thin), n)))
    cats["content"] = clamp(
        45 * (1 - share(len(thin), n))
        + 35 * min(med_words / 400, 1)
        + 20 * (1 - share(len(dup_content), n)))
    cats["onpage"] = clamp(
        30 * (1 - share(len(bad_title), n))
        + 25 * share(sum(len(p["h1"]) == 1 for p in ok), n)
        + 25 * (1 - share(len(no_desc), n))
        + 10 * (1 - share(len(no_og), n))
        + 10 * (1 - share(len(orphans), n)))
    content_types = share(sum(bool(set(p["types"]) - GENERIC_TYPES - {"__invalid__"}) for p in ok), n)
    cats["schema"] = clamp(
        35 * has_org + 10 * ("WebSite" in all_types)
        + 10 * (share(sum("BreadcrumbList" in p["types"] for p in ok), n) > 0.5)
        + 45 * (1 - share(len(events_no_schema), len(events)) if events else min(content_types * 2, 1))
        - 10 * bool(invalid_ld))
    lab = [x for x in perf if "score" in x]
    if lab:
        lab_score = statistics.mean(x["score"] for x in lab)
        field = next((x.get("field_origin") or x.get("field_page") for x in lab
                      if x.get("field_origin") or x.get("field_page")), None)
        if field:
            pts = {"FAST": 100, "AVERAGE": 50, "SLOW": 0}
            keys = ["LARGEST_CONTENTFUL_PAINT_MS", "INTERACTION_TO_NEXT_PAINT", "CUMULATIVE_LAYOUT_SHIFT_SCORE"]
            fs = [pts.get(field.get(k, {}).get("category")) for k in keys]
            fs = [f for f in fs if f is not None]
            cats["performance"] = clamp(0.5 * lab_score + 0.5 * statistics.mean(fs)) if fs else clamp(lab_score)
        else:
            cats["performance"] = clamp(lab_score)
    else:
        cats["performance"] = None
    cats["ai"] = clamp(
        30 * (1 - share(len(rob["ai_bots_blocked"]), len(AI_BOTS)))
        + 15 * site["llms_txt"] + 20 * has_org
        + 20 * min(med_words / 300, 1)
        + 15 * (1 - share(len(no_desc), n)))
    cats["images"] = clamp(
        50 * (share(img_alt_ok, img_content) if img_content else 1)
        + 25 * (share(img_modern, img_src) if img_src else 1)
        + 25 * (share(lazy_ok, lazy_c) if lazy_c else 1))
    w = {k: v for k, v in WEIGHTS.items() if cats[k] is not None}
    total = clamp(sum(cats[k] * v for k, v in w.items()) / sum(w.values()))

    # --- issues
    issues = []

    def add(iid, sev, cat, title, items, total_n=None, fix=None):
        if items:
            issues.append({"id": iid, "severity": sev, "category": cat, "title": title,
                           "count": len(items), "of": total_n, "fix": fix,
                           "examples": [i if isinstance(i, str) else i["url"] for i in items[:10]]})
    add("events_without_schema", "critical", "schema", "Arrangementssider uten Event-schema", events_no_schema, len(events),
        "Generer Event-JSON-LD i malen for arrangementer.")
    add("ai_bots_blocked", "critical", "ai", "AI-crawlere blokkert i robots.txt", rob["ai_bots_blocked"], len(AI_BOTS))
    add("repeated_brand_title", "high", "onpage", "Titler med gjentatt segment (f.eks. dobbelt merkenavn)", repeated_brand, n,
        "Rett tittelmalen i Yoast / temaets <title>.")
    add("thin_pages", "high", "content", f"Tynne sider (< {THIN_WORDS} unike ord) som er indeksert", thin, n,
        "Noindex tomme arkiver eller bygg ut innholdet.")
    add("no_org_schema", "high", "schema", "Mangler Organization/LocalBusiness-schema", [] if has_org else [site["final_url"]], 1)
    add("non200_in_sitemap", "high", "technical", "URL-er i sitemap som ikke svarer 200", non200, len(pages))
    add("missing_h1", "high" if home in no_h1 else "medium", "onpage", "Sider uten H1", no_h1, n)
    add("missing_meta_description", "medium", "onpage", "Sider uten meta description", no_desc, n)
    add("redirect_in_sitemap", "medium", "technical", "Redirectende URL-er i sitemap", redirected, len(pages))
    add("noindex_in_sitemap", "medium", "technical", "Noindex-sider i sitemap", noindex, n)
    add("canonical_elsewhere", "medium", "technical", "Canonical peker til annen URL", canon_else, n)
    add("duplicate_titles", "medium", "onpage", "Dupliserte titler", dup_title, n)
    add("duplicate_content", "medium", "content", "Duplisert innhold (identisk unik tekst)", dup_content, n)
    add("multiple_h1", "low", "onpage", "Sider med flere H1", multi_h1, n)
    add("missing_og_image", "low", "onpage", "Sider uten og:image", no_og, n)
    add("orphan_pages", "medium", "onpage", "Sider uten interne lenker inn", orphans, n)
    add("invalid_jsonld", "high", "schema", "Ugyldig JSON-LD", invalid_ld, n)
    missing_sec = [h for h, v in sec.items() if not v]
    add("security_headers", "medium", "technical", "Manglende sikkerhetsheadere", missing_sec, len(sec))
    if rob["crawl_delay"] and rob["crawl_delay"] > 2:
        add("crawl_delay", "low", "technical", f"robots.txt har Crawl-delay: {rob['crawl_delay']:g}", ["robots.txt"], 1)
    if not site["llms_txt"]:
        add("no_llms_txt", "low", "ai", "/llms.txt mangler", ["/llms.txt"], 1)
    if img_content and share(img_alt_ok, img_content) < 0.8:
        add("img_alt", "medium", "images", "Innholdsbilder uten alt-tekst",
            [p for p in ok if p["img_content"] > p["img_alt_ok"]], n)
    if lazy_c and share(lazy_ok, lazy_c) < 0.5:
        add("img_lazy", "medium", "images", "Bilder under folden lastes ikke lat",
            [p for p in ok if p["img_lazy_candidates"] > p["img_lazy"]], n)
    for x in lab:
        if x.get("lcp_ms") and x["lcp_ms"] > 4000:
            add(f"lcp_poor:{x['url']}", "critical", "performance", f"LCP {x['lcp_ms']/1000:.1f} s (mobil)".replace(".", ","), [x["url"]], 1,
                "Mål: ≤ 2,5 s. Defer skript, lazy-load bilder, preload LCP-bilde.")
        if x.get("cls") is not None and x["cls"] > 0.25:
            add(f"cls_poor:{x['url']}", "high", "performance", f"CLS {x['cls']:.2f} (mobil)".replace(".", ","), [x["url"]], 1,
                "Mål: ≤ 0,1. Reserver plass til bilder og dynamisk innhold.")
    order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    issues.sort(key=lambda i: (order[i["severity"]], -i["count"]))

    kpis = {
        "pages_in_sitemap": site["sitemap_total"], "pages_crawled": len(pages), "pages_ok": len(ok),
        "non200": len(non200), "redirects_in_sitemap": len(redirected), "noindex": len(noindex),
        "thin_pages": len(thin), "median_unique_words": round(med_words),
        "repeated_brand_titles": len(repeated_brand), "duplicate_titles": len(dup_title),
        "missing_h1": len(no_h1), "multiple_h1": len(multi_h1), "missing_meta_description": len(no_desc),
        "missing_og_image": len(no_og), "orphan_pages": len(orphans),
        "event_pages": len(events), "event_pages_with_schema": len(events) - len(events_no_schema),
        "has_org_schema": has_org, "llms_txt": site["llms_txt"],
        "security_headers_ok": sum(sec.values()), "security_headers_total": len(sec),
        "img_alt_coverage": round(share(img_alt_ok, img_content), 3) if img_content else None,
        "img_lazy_coverage": round(share(lazy_ok, lazy_c), 3) if lazy_c else None,
        "img_modern_share": round(share(img_modern, img_src), 3) if img_src else None,
        "avg_response_ms": round(statistics.mean(p["ms"] for p in pages)) if pages else None,
        "home_has_h1": bool(home and any(home["h1"])),
        "schema_types": dict(all_types.most_common()),
    }
    if lab:
        kpis["perf_score"] = round(statistics.mean(x["score"] for x in lab))
        kpis["lcp_ms"] = round(max(x["lcp_ms"] or 0 for x in lab))
        kpis["cls"] = round(max(x["cls"] or 0 for x in lab), 3)
    return total, cats, kpis, issues


# ---------------------------------------------------------------- hoved
def collect(cfg, month, do_perf=True, workers=4):
    site_url = cfg["url"]
    print(f"[{cfg['slug']}] starter {site_url}", file=sys.stderr)
    st, final, hdr, _ = fetch(site_url)
    final_url = final if st == 200 else site_url
    host = urllib.parse.urlparse(final_url).netloc
    origin = f"https://{host}"
    rst, _, _, robots_txt = fetch(origin + "/robots.txt")
    robots_txt = robots_txt if rst == 200 else ""
    rp, rob = robots_info(robots_txt)
    http_st, _, http_h, _ = fetch("http://" + host + "/", follow=False)
    https_redirect = http_st in (301, 302, 307, 308) and http_h.get("location", "").startswith("https://")
    llms_st, _, llms_h, llms_body = fetch(origin + "/llms.txt")
    sec_names = ["strict-transport-security", "x-content-type-options", "referrer-policy"]
    sec = {h: h in hdr for h in sec_names}
    sec["frame-protection"] = "x-frame-options" in hdr or "frame-ancestors" in hdr.get("content-security-policy", "")
    sec["permissions-policy"] = "permissions-policy" in hdr

    rows = sitemap_urls(origin, robots_txt)
    total_sm = len(rows)
    rows = [r for r in rows if rp.can_fetch(UA, r[1])]
    rows = sample(rows, cfg.get("max_pages", 500))
    if not any(r[1].rstrip("/") == final_url.rstrip("/") for r in rows):
        rows.insert(0, ("(forside)", final_url))

    with cf.ThreadPoolExecutor(workers) as ex:
        results = list(ex.map(lambda r: analyze_page(r, host), rows))
    pages = [r for r, _ in results]
    # Malstekst = tekstblokker som går igjen på ≥ 40 % av sidene. Resten er "unikt innhold".
    df = Counter()
    for _, blocks in results:
        df.update(set(blocks))
    cutoff = max(3, 0.4 * len(results))
    for rec, blocks in results:
        if "title" not in rec:
            continue
        uniq = [b for b in blocks if df[b] < cutoff]
        text = " ".join(uniq)
        rec["unique_words"] = len(text.split())
        rec["content_hash"] = hashlib.sha1(text.lower().encode()).hexdigest()[:12]

    perf = []
    if do_perf:
        key = os.environ.get("GOOGLE_API_KEY")
        for path in cfg.get("key_pages", ["/"]):
            u = urllib.parse.urljoin(final_url, path)
            print(f"[{cfg['slug']}] ytelse {u}", file=sys.stderr)
            r = perf_psi(u, key) if key else perf_local(u)
            if r:
                perf.append(r)

    site = {"final_url": final_url, "status": st, "https_redirect": https_redirect,
            "robots_found": bool(robots_txt), "robots": rob, "llms_txt": llms_st == 200 and "<html" not in llms_body[:500].lower(),
            "security_headers": sec, "sitemap_total": total_sm, "server": hdr.get("server"),
            "cache": hdr.get("cf-cache-status") or hdr.get("x-cache")}
    total, cats, kpis, issues = score_and_issues(site, pages, perf, cfg)
    out = {"schema_version": SCHEMA_VERSION, "method": "automated",
           "date": dt.date.today().isoformat(), "month": month,
           "client": cfg["slug"], "url": final_url, "score": total, "categories": cats,
           "weights": WEIGHTS, "kpis": kpis, "site": site, "performance": perf, "issues": issues,
           "sampled": len(rows) < total_sm}
    d = ROOT / "clients" / cfg["slug"] / month
    d.mkdir(parents=True, exist_ok=True)
    (d / "metrics.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
    slim = [{k: v for k, v in p.items() if k not in ("internal_links", "content_hash")} for p in pages]
    (d / "pages.json").write_text(json.dumps(slim, ensure_ascii=False))
    print(f"[{cfg['slug']}] score {total} {cats} -> {d.relative_to(ROOT)}", file=sys.stderr)
    return out


def load_clients():
    return tomllib.loads((ROOT / "clients.toml").read_text())["client"]


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--client")
    g.add_argument("--all", action="store_true")
    ap.add_argument("--month", default=dt.date.today().strftime("%Y-%m"))
    ap.add_argument("--no-perf", action="store_true")
    a = ap.parse_args()
    clients = load_clients()
    if a.client:
        clients = [c for c in clients if c["slug"] == a.client]
        if not clients:
            sys.exit(f"Ukjent kunde: {a.client}")
    failed = []
    for c in clients:
        try:
            collect(c, a.month, do_perf=not a.no_perf)
        except Exception as e:  # noqa: BLE001 – én kunde skal ikke stoppe resten
            print(f"[{c['slug']}] FEILET: {e}", file=sys.stderr)
            failed.append(c["slug"])
    if failed:
        sys.exit(f"Feilet: {', '.join(failed)}")


if __name__ == "__main__":
    main()
