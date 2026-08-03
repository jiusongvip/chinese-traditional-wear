import os, re, json

base = r"D:\workspaces\website\chinese-traditional-wear\dist"
pages = []
for root, dirs, files in os.walk(base):
    for f in files:
        if f == "index.html" and "_astro" not in root:
            rel = os.path.relpath(os.path.join(root, f), base).replace("\\", "/")
            url_path = "/" + rel.replace("index.html", "")
            if url_path.endswith("/"): url_path = url_path[:-1]
            if url_path == "": url_path = "/"
            if url_path in ["/qipao", "/tang"]: continue
            pages.append((url_path, os.path.join(root, f)))

thin = 0
no_sources = 0
total = len(pages)
no_schema = 0
no_h2 = 0
min_words = 99999

for url, fp in sorted(pages):
    with open(fp, "r", encoding="utf-8") as f:
        html = f.read()
    visible = re.sub(r"<[^>]+>", " ", html)
    visible = re.sub(r"\s+", " ", visible).strip()
    words = len(visible.split())
    if words < min_words: min_words = words
    if words < 200: thin += 1
    
    h2s = len(re.findall(r"<h2[^>]*>", html))
    if h2s == 0 and url != "/": no_h2 += 1
    
    schemas = re.findall(r'<script type="application/ld\+json"[^>]*>(.*?)</script>', html, re.DOTALL)
    has_article = any("Article" in s for s in schemas)
    if not has_article and url != "/" and url != "/privacy":
        no_schema += 1
    
    has_sources = "Palace Museum" in html or "Silk Museum" in html
    if not has_sources and url not in ["/", "/privacy", "/contact"] and not url.startswith("/plan-trip"):
        no_sources += 1

print(f"Total pages: {total}")
print(f"Thin (<200w): {thin}")
print(f"No H2: {no_h2}")
print(f"No Article schema: {no_schema}")
print(f"No sources: {no_sources}")
print(f"Min words: {min_words}w")
