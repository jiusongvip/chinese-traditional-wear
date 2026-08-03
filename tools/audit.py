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

for url, fp in sorted(pages):
    with open(fp, "r", encoding="utf-8") as f:
        html = f.read()
    t = re.search(r"<title>(.*?)</title>", html)
    title = t.group(1) if t else "MISSING"
    d = re.search(r'<meta name="description" content="(.*?)"', html)
    desc = d.group(1) if d else "MISSING"
    visible = re.sub(r"<[^>]+>", " ", html)
    visible = re.sub(r"\s+", " ", visible).strip()
    words = len(visible.split())
    h1s = re.findall(r"<h1[^>]*>(.*?)</h1>", html)
    h1 = h1s[0][:80] if h1s else "MISSING"
    h2s = len(re.findall(r"<h2[^>]*>", html))
    schemas = re.findall(r'<script type="application/ld\+json"[^>]*>(.*?)</script>', html, re.DOTALL)
    schema_types = []
    for s in schemas:
        try:
            d = json.loads(s.strip())
            if isinstance(d, dict): schema_types.append(d.get("@type","?"))
            elif isinstance(d, list):
                for item in d:
                    if isinstance(item, dict): schema_types.append(item.get("@type","?"))
        except: pass
    schema_str = ",".join(schema_types) if schema_types else "NONE"
    # Has sources?
    has_sources = "Palace Museum" in html or "china.org" in html or "Silk Museum" in html
    has_external = len(re.findall(r'href="https?://', html)) > 0
    flag = " *** THIN ***" if words < 200 else ""
    flag += " *** NO SOURCES ***" if not has_sources and not url.startswith("/plan-trip") else ""
    print(f"{url} | {words}w | H2:{h2s} | Schema:{schema_str} | ExtLinks:{has_external}{flag}")
    print(f"  Title: {title[:90]}")
