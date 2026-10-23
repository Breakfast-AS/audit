import urllib.request, re, gzip as gz_module

def get_actual_size(url, label=""):
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0',
            'Accept-Encoding': 'gzip, deflate, br'
        })
        with urllib.request.urlopen(req, timeout=20) as resp:
            raw = resp.read()
            headers = dict(resp.headers)
            ct = headers.get('Content-Type', headers.get('content-type', ''))
            cc = headers.get('Cache-Control', headers.get('cache-control', 'none'))
            # Try decompressing to get uncompressed size
            try:
                uncompressed = gz_module.decompress(raw)
                print(f"  {label}")
                print(f"    Compressed: {len(raw):,} bytes | Uncompressed: {len(uncompressed):,} bytes | Cache: {cc[:50]}")
            except Exception:
                print(f"  {label}")
                print(f"    Size: {len(raw):,} bytes | Cache: {cc[:50]}")
    except Exception as e:
        print(f"  {label}: ERROR {e}")

print("=== CSS FILE SIZES ===")
get_actual_size(
    "https://www.mosskulturhus.no/wp-content/themes/mosskulturhus-redesign/style.css?version=1779787949",
    "theme style.css"
)
get_actual_size(
    "https://www.mosskulturhus.no/wp-content/et-cache/46750/et-divi-builder-dynamic-46750.css?ver=1779783740",
    "divi-builder-dynamic.css"
)
get_actual_size(
    "https://www.mosskulturhus.no/wp-content/plugins/tix/public/css/tix-public.css?ver=1.0.0",
    "tix-public.css"
)

print()
print("=== JS FILE SIZES ===")
get_actual_size(
    "https://www.mosskulturhus.no/wp-content/plugins/divi-builder/js/scripts.min.js?ver=4.27.5",
    "divi-builder scripts.min.js"
)
get_actual_size(
    "https://www.mosskulturhus.no/wp-content/themes/mosskulturhus-redesign/assets/scripts.js?ver=3.0.0",
    "theme scripts.js"
)
get_actual_size(
    "https://www.mosskulturhus.no/wp-includes/js/jquery/jquery.min.js?ver=3.7.1",
    "jquery.min.js 3.7.1"
)
get_actual_size(
    "https://www.mosskulturhus.no/wp-content/plugins/divi-builder/core/admin/js/common.js?ver=4.27.5",
    "divi-builder common.js"
)

print()
print("=== CHECKING TTFB / SERVER RESPONSE ===")
import time
req = urllib.request.Request('https://www.mosskulturhus.no/', headers={
    'User-Agent': 'Mozilla/5.0',
    'Accept-Encoding': 'gzip'
})
t0 = time.time()
with urllib.request.urlopen(req, timeout=30) as resp:
    first_byte = time.time() - t0
    headers = dict(resp.headers)
    _ = resp.read()
    total = time.time() - t0
print(f"  TTFB (approx): {first_byte*1000:.0f}ms")
print(f"  Total transfer: {total*1000:.0f}ms")
print(f"  CF-Cache-Status: {headers.get('cf-cache-status', headers.get('CF-Cache-Status', 'not found'))}")
print(f"  X-Cache-Enabled: {headers.get('X-Cache-Enabled', headers.get('x-cache-enabled', 'not found'))}")
print(f"  Cache-Control: {headers.get('Cache-Control', headers.get('cache-control', 'not found'))}")
print(f"  Server: {headers.get('Server', headers.get('server', 'not found'))}")
