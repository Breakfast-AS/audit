import urllib.request, re, gzip

def get_resource_info(url, label=""):
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0',
            'Accept-Encoding': 'gzip, deflate'
        })
        req.get_method = lambda: 'HEAD'
        with urllib.request.urlopen(req, timeout=15) as resp:
            headers = dict(resp.headers)
            cl = headers.get('Content-Length', headers.get('content-length', 'unknown'))
            ct = headers.get('Content-Type', headers.get('content-type', 'unknown'))
            ce = headers.get('Content-Encoding', headers.get('content-encoding', 'none'))
            cc = headers.get('Cache-Control', headers.get('cache-control', 'none'))
            print(f"  {label or url[:80]}")
            print(f"    Size: {cl} bytes  Type: {ct[:40]}  Encoding: {ce}  Cache: {cc}")
    except Exception as e:
        print(f"  {label or url[:80]}: ERROR {e}")

print("=== HERO BACKGROUND IMAGE ===")
get_resource_info(
    "https://www.mosskulturhus.no/wp-content/uploads/2025/10/4312x1400_karusell.jpg",
    "hero-karusell.jpg (4312x1400)"
)

print()
print("=== MAIN CSS FILES ===")
get_resource_info(
    "https://www.mosskulturhus.no/wp-content/themes/mosskulturhus-redesign/style.css?version=1779787949",
    "theme style.css"
)
get_resource_info(
    "https://www.mosskulturhus.no/wp-content/et-cache/46750/et-divi-builder-dynamic-46750.css?ver=1779783740",
    "divi-builder-dynamic.css"
)
get_resource_info(
    "https://www.mosskulturhus.no/wp-content/plugins/tix/public/css/tix-public.css?ver=1.0.0",
    "tix-public.css"
)

print()
print("=== EXTERNAL SCRIPTS ===")
get_resource_info(
    "https://use.fontawesome.com/5daed306be.js",
    "fontawesome kit"
)
get_resource_info(
    "https://www.mosskulturhus.no/wp-content/plugins/divi-builder/js/scripts.min.js?ver=4.27.5",
    "divi-builder scripts.min.js"
)
get_resource_info(
    "https://www.mosskulturhus.no/wp-content/themes/mosskulturhus-redesign/assets/scripts.js?ver=3.0.0",
    "theme scripts.js"
)
get_resource_info(
    "https://cdnjs.cloudflare.com/ajax/libs/lazysizes/1.2.2/lazysizes.min.js",
    "lazysizes 1.2.2"
)

print()
print("=== CUSTOM FONTS ===")
get_resource_info(
    "https://www.mosskulturhus.no/wp-content/themes/mosskulturhus-redesign/assets/fonts/Monterio-Bold.woff2",
    "Monterio-Bold.woff2"
)
get_resource_info(
    "https://www.mosskulturhus.no/wp-content/themes/mosskulturhus-redesign/assets/fonts/Monterio.woff2",
    "Monterio.woff2"
)
