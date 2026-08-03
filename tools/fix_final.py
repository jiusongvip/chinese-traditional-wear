import os, re

src = r"D:\workspaces\website\chinese-traditional-wear\src\pages"

# Fix encoding: replace literal \uXXXX with actual chars in ALL .astro files
fixed = 0
for root, ds, files in os.walk(src):
    for f in files:
        if not f.endswith(".astro"): continue
        fp = os.path.join(root, f)
        with open(fp, "r", encoding="utf-8") as fh: c = fh.read()
        orig = c
        c = c.replace("\\u2014", "\u2014")
        c = c.replace("\\u2019", "\u2019")
        c = c.replace("\\u00b7", "\u00b7")
        c = c.replace("\\u2013", "\u2013")
        c = c.replace("&amp;", "&")
        c = c.replace("бд", " · ")
        c = c.replace("\u0431\u043a", " · ")
        if c != orig:
            with open(fp, "w", encoding="utf-8", newline="\n") as fh: fh.write(c)
            fixed += 1

print(f"Fixed encoding in {fixed} files")

# Expand gallery page
fp = os.path.join(src, "gallery", "index.astro")
with open(fp, "r", encoding="utf-8") as f: c = f.read()
old_desc = "Browse photos from Hanfu photoshoots, qipao tailoring sessions, and ethnic costume experiences across China."
new_desc = "Browse photos from Hanfu photoshoots, qipao tailoring sessions, and ethnic costume experiences across China. Each image represents a real experience you can book \u2014 click through to the destination guide for details on how to arrange yours."
c = c.replace(old_desc, new_desc)
with open(fp, "w", encoding="utf-8", newline="\n") as f: f.write(c)
print("Gallery: expanded description")

# Expand quiz page
fp2 = os.path.join(src, "quiz", "index.astro")
with open(fp2, "r", encoding="utf-8") as f: c2 = f.read()
# Find the quiz CTA and add context before it
old_q = "</h1>\n  </section>"
new_q = """</h1>
      <p class="mt-6 text-lg text-stone-500 leading-relaxed max-w-2xl">
        Hanfu, Qipao, Tang suit, or Zhongshan suit \u2014 each Chinese traditional clothing style reflects a different personality, era, and way of experiencing China. This short quiz asks about your travel preferences, aesthetic taste, and comfort level to match you with the style that fits you best.
      </p>
      <div class="mt-8 grid grid-cols-1 sm:grid-cols-2 gap-4">
        <div class="bg-stone-50 rounded-xl p-5 border border-stone-100">
          <h2 class="font-semibold text-sm text-stone-900">Hanfu</h2>
          <p class="text-xs text-stone-500 mt-1">Flowing ancient robes for history lovers, ideal for photoshoots at Xi'an city walls and classical gardens.</p>
        </div>
        <div class="bg-stone-50 rounded-xl p-5 border border-stone-100">
          <h2 class="font-semibold text-sm text-stone-900">Qipao</h2>
          <p class="text-xs text-stone-500 mt-1">Form-fitting 1920s Shanghai glamour, perfect for evening events and custom tailoring experiences.</p>
        </div>
        <div class="bg-stone-50 rounded-xl p-5 border border-stone-100">
          <h2 class="font-semibold text-sm text-stone-900">Tang Suit</h2>
          <p class="text-xs text-stone-500 mt-1">Mandarin-collar festival jacket, ideal for Beijing hutong workshops and celebration wear.</p>
        </div>
        <div class="bg-stone-50 rounded-xl p-5 border border-stone-100">
          <h2 class="font-semibold text-sm text-stone-900">Zhongshan Suit</h2>
          <p class="text-xs text-stone-500 mt-1">Revolutionary formal menswear with four pockets \u2014 a wearable, tailored souvenir from Nanjing.</p>
        </div>
      </div>
    </div>
  </section>"""
if old_q in c2:
    c2 = c2.replace(old_q, new_q)
    with open(fp2, "w", encoding="utf-8", newline="\n") as f: f.write(c2)
    print("Quiz: expanded with style cards")
else:
    print("Quiz: marker not found")
