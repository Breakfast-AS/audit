import urllib.request, re, gzip

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

# Find the hero / slider section - look for background-image inline styles
bg_images = re.findall(r'background(?:-image)?:\s*url\(["\']?([^"\')\s]+)["\']?\)', html, re.IGNORECASE)
print(f"=== BACKGROUND IMAGES ({len(bg_images)}) ===")
for b in bg_images[:10]:
    print(f"  {b[:200]}")

# Look for data-src (lazy loading via lazysizes)
data_srcs = re.findall(r'data-src=["\']([^"\']+)["\']', html, re.IGNORECASE)
print()
print(f"=== DATA-SRC (lazysizes deferred images: {len(data_srcs)}) ===")
for d in data_srcs[:10]:
    print(f"  {d[:200]}")

# Find slider/hero HTML region
hero_match = re.search(r'(?:hero|slider|swiper|carousel)[^<]{0,200}', html, re.IGNORECASE)
if hero_match:
    start = max(0, hero_match.start() - 50)
    print()
    print("=== HERO/SLIDER REGION (context) ===")
    print(html[start:start+600])

# Check for any picture/source elements (WebP serving via picture)
pictures = re.findall(r'<picture[^>]*>.*?</picture>', html, re.DOTALL | re.IGNORECASE)
print()
print(f"=== PICTURE ELEMENTS: {len(pictures)} ===")
for p in pictures[:3]:
    print(p[:400])

# Check for srcset
srcsets = re.findall(r'<img[^>]+srcset=["\'][^"\']+["\'][^>]*>', html, re.IGNORECASE)
print()
print(f"=== IMAGES WITH SRCSET: {len(srcsets)} ===")
for s in srcsets[:5]:
    print(f"  {s[:250]}")

# Check script placements relative to </head>
head_end = html.find('</head>')
body_start = html.find('<body')
scripts_in_head = re.findall(r'<script[^>]*src=["\'][^"\']+["\'][^>]*>', html[:head_end], re.IGNORECASE)
scripts_in_body = re.findall(r'<script[^>]*src=["\'][^"\']+["\'][^>]*>', html[body_start:], re.IGNORECASE)
print()
print(f"=== SCRIPT PLACEMENT ===")
print(f"  Scripts in <head>: {len(scripts_in_head)}")
print(f"  Scripts in <body>: {len(scripts_in_body)}")
print()
print("  Head scripts:")
for s in scripts_in_head:
    src = re.search(r'src=["\']([^"\']+)["\']', s)
    print(f"    {src.group(1)[:100] if src else s[:100]}")

# Check GTM / analytics
gtm = re.findall(r'GTM-[A-Z0-9]+', html)
ga = re.findall(r'G-[A-Z0-9]+|UA-[0-9]+-[0-9]+', html)
print()
print(f"=== ANALYTICS ===")
print(f"  GTM: {list(set(gtm))}")
print(f"  GA: {list(set(ga))}")

# Check for WordPress version exposure
wp_ver = re.search(r'\?ver=([\d.]+)', html)
print()
print(f"=== WP ASSET VERSIONING ===")
print(f"  Example query string version: {wp_ver.group(1) if wp_ver else 'not found'}")

# Check cache-busting on theme CSS
theme_css = re.search(r'style\.css\?version=(\d+)', html)
if theme_css:
    import time
    ts = int(theme_css.group(1))
    from datetime import datetime
    dt = datetime.fromtimestamp(ts)
    print(f"  Theme CSS version timestamp: {ts} = {dt}")
