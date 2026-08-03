with open(r"D:\workspaces\website\chinese-traditional-wear\src\pages\index.astro", "r", encoding="utf-8") as f:
    c = f.read()

# Patch hero label
c = c.replace("Cultural Travel Guide", "The Definitive Guide")

# Patch H1
old_h1 = """Wear China''s
            <span class="block text-[#b5343a]">History on</span>
            Your Journey"""
new_h1 = """Chinese Traditional Wear:
            <span class="block text-[#b5343a]">Hanfu, Qipao &amp; Beyond</span>"""
c = c.replace(old_h1, new_h1)

# Patch subtitle - use a unique anchor
old_sub = "From Hanfu photoshoots on Xi''an''s ancient city walls to qipao tailoring in Shanghai''s back lanes"
new_sub = "Explore 3,000 years of Chinese fashion through 6 iconic styles, 12 dynasties, and the cities where you can still wear them today"
c = c.replace(old_sub, new_sub)

# Patch CTA buttons
c = c.replace("Find Experiences", "Explore the Styles")
c = c.replace("Browse by Style", "Plan Your Experience")

# Add quick-jump tabs
old_cta_end = '</div>\n        </div>\n        <!-- Right: Travel scene image -->'
new_tabs = '''</div>
          <div class="mt-6 flex flex-wrap gap-2">
            <a href="#styles" class="text-xs px-3 py-1.5 bg-stone-100 rounded-full text-stone-600 hover:bg-stone-200 transition-colors">Types</a>
            <a href="#dynasties" class="text-xs px-3 py-1.5 bg-stone-100 rounded-full text-stone-600 hover:bg-stone-200 transition-colors">Dynasties</a>
            <a href="#compare-preview" class="text-xs px-3 py-1.5 bg-stone-100 rounded-full text-stone-600 hover:bg-stone-200 transition-colors">Compare</a>
            <a href="#gallery" class="text-xs px-3 py-1.5 bg-stone-100 rounded-full text-stone-600 hover:bg-stone-200 transition-colors">Gallery</a>
            <a href="#quiz" class="text-xs px-3 py-1.5 bg-stone-100 rounded-full text-stone-600 hover:bg-stone-200 transition-colors">Quiz</a>
          </div>
        </div>
        <!-- Right: Travel scene image -->'''
c = c.replace(old_cta_end, new_tabs)

with open(r"D:\workspaces\website\chinese-traditional-wear\src\pages\index.astro", "w", encoding="utf-8", newline="\n") as f:
    f.write(c)
print("Hero patch done")
