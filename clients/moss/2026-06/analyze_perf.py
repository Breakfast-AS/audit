import urllib.request, re, json, gzip

url = 'https://www.mosskulturhus.no/'
req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate'
})
with urllib.request.urlopen(req, timeout=30) as resp:
    raw = resp.read()
    try:
        html = gzip.decompress(raw).decode('utf-8', errors='replace')
    except Exception:
        html = raw.decode('utf-8', errors='replace')

print(f"HTML size: {len(html)} bytes ({len(html)//1024} KB)")
print()

# ---- IMAGES ----
imgs = re.findall(r'<img[^>]+>', html, re.IGNORECASE)
print(f"=== IMAGES ({len(imgs)} total) ===")
webp = sum(1 for i in imgs if '.webp' in i.lower())
avif = sum(1 for i in imgs if '.avif' in i.lower())
jpg  = sum(1 for i in imgs if re.search(r'\.jpe?g', i, re.I))
png  = sum(1 for i in imgs if '.png' in i.lower())
no_dims = sum(1 for i in imgs if 'width=' not in i.lower() and 'height=' not in i.lower())
no_alt  = sum(1 for i in imgs if 'alt=' not in i.lower())
lazy    = sum(1 for i in imgs if 'loading=' in i.lower())
fetchp  = [i for i in imgs if 'fetchpriority' in i.lower()]
print(f"  Format: WebP={webp} AVIF={avif} JPEG={jpg} PNG={png}")
print(f"  Missing width+height dims: {no_dims}")
print(f"  Missing alt text: {no_alt}")
print(f"  Has loading attr: {lazy}")
print(f"  Has fetchpriority: {len(fetchp)}")
for f in fetchp:
    print(f"    {f[:300]}")
print()
print("  First 5 img tags:")
for i in imgs[:5]:
    print(f"    {i[:300]}")

# ---- SCRIPTS ----
print()
print("=== SCRIPTS ===")
scripts_ext = re.findall(r'<script[^>]*src=["\'][^"\']+["\'][^>]*>', html, re.IGNORECASE)
print(f"  External scripts: {len(scripts_ext)}")
deferred  = [s for s in scripts_ext if 'defer'  in s.lower()]
asynced   = [s for s in scripts_ext if 'async'  in s.lower() and 'defer' not in s.lower()]
blocking  = [s for s in scripts_ext if 'defer'  not in s.lower() and 'async' not in s.lower()]
print(f"  Blocking (no defer/async): {len(blocking)}")
print(f"  Deferred: {len(deferred)}")
print(f"  Async: {len(asynced)}")
print()
print("  Blocking scripts:")
for s in blocking:
    src = re.search(r'src=["\']([^"\']+)["\']', s)
    print(f"    {src.group(1) if src else s[:150]}")
print()
print("  Deferred scripts:")
for s in deferred:
    src = re.search(r'src=["\']([^"\']+)["\']', s)
    print(f"    {src.group(1) if src else s[:150]}")
print()
print("  Async scripts:")
for s in asynced:
    src = re.search(r'src=["\']([^"\']+)["\']', s)
    print(f"    {src.group(1) if src else s[:150]}")

# ---- STYLESHEETS ----
print()
print("=== STYLESHEETS ===")
css = re.findall(r'<link[^>]+rel=["\']stylesheet["\'][^>]*>', html, re.IGNORECASE)
print(f"  Total: {len(css)}")
for c in css:
    href = re.search(r'href=["\']([^"\']+)["\']', c)
    media_m = re.search(r'media=["\']([^"\']+)["\']', c)
    print(f"    {href.group(1)[:100] if href else 'N/A'}  [media={media_m.group(1) if media_m else 'all'}]")

# ---- PRELOADS / HINTS ----
print()
print("=== RESOURCE HINTS ===")
preloads   = re.findall(r'<link[^>]+rel=["\']preload["\'][^>]*>', html, re.IGNORECASE)
preconnect = re.findall(r'<link[^>]+rel=["\']preconnect["\'][^>]*>', html, re.IGNORECASE)
dnsprefetch= re.findall(r'<link[^>]+rel=["\']dns-prefetch["\'][^>]*>', html, re.IGNORECASE)
print(f"  Preloads ({len(preloads)}):")
for p in preloads:
    print(f"    {p[:250]}")
print(f"  Preconnect ({len(preconnect)}):")
for p in preconnect:
    print(f"    {p[:250]}")
print(f"  DNS-prefetch ({len(dnsprefetch)}):")
for p in dnsprefetch:
    print(f"    {p[:200]}")

# ---- SPECULATIONRULES ----
spec = re.search(r'<script type=["\']speculationrules["\']>(.*?)</script>', html, re.DOTALL | re.IGNORECASE)
if spec:
    print()
    print("=== SPECULATION RULES ===")
    try:
        parsed = json.loads(spec.group(1))
        print(json.dumps(parsed, indent=2)[:600])
    except Exception:
        print(spec.group(1)[:500])

# ---- INLINE STYLE BLOCKS ----
inline_styles = re.findall(r'<style[^>]*>', html, re.IGNORECASE)
print()
print(f"=== INLINE STYLE BLOCKS: {len(inline_styles)} ===")

# ---- GOOGLE FONTS ----
gfonts = re.findall(r'fonts\.googleapis\.com[^\s"\'<>]+', html)
print()
print(f"=== GOOGLE FONTS REQUESTS: {len(gfonts)} ===")
for g in gfonts:
    print(f"  {g[:200]}")

# ---- THIRD PARTY DOMAINS ----
all_srcs = re.findall(r'(?:src|href)=["\']https?://([^/"\']+)', html, re.IGNORECASE)
third_party = {}
own_domain = 'mosskulturhus.no'
for d in all_srcs:
    if own_domain not in d and d:
        third_party[d] = third_party.get(d, 0) + 1
print()
print(f"=== THIRD-PARTY DOMAINS ({len(third_party)}) ===")
for d, count in sorted(third_party.items(), key=lambda x: -x[1]):
    print(f"  {d}  ({count} refs)")

# ---- DOM SIZE ESTIMATE ----
all_tags = re.findall(r'<[a-zA-Z][^>]*>', html)
print()
print(f"=== DOM ELEMENT ESTIMATE: {len(all_tags)} opening tags ===")

# ---- LAZY SIZES VERSION CHECK ----
lazysizes = re.search(r'lazysizes[^"\']*["\']', html)
if lazysizes:
    print()
    print(f"=== LAZYSIZES: {lazysizes.group(0)} ===")
    print("  WARNING: lazysizes 1.2.2 detected - very outdated (current is 5.x)")
