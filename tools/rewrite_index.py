import os, re

# Paths
src = r"D:\workspaces\website\chinese-traditional-wear\src\pages\index.astro"

with open(src, "r", encoding="utf-8") as f:
    content = f.read()

# === PATCH 1: Hero section - new H1, subtitle, dual CTA, quick-jump tabs ===
old_hero_label = '<span class="text-xs font-medium text-[#b5343a] tracking-[0.15em] uppercase">Cultural Travel Guide</span>'
new_hero_label = '<span class="text-xs font-medium text-[#b5343a] tracking-[0.15em] uppercase">The Definitive Guide</span>'

content = content.replace(old_hero_label, new_hero_label)

# Replace H1: old "Wear China''s History on Your Journey" 
old_h1 = (
    'Wear China''''s\n'
    '            <span class="block text-[#b5343a]">History on</span>\n'
    '            Your Journey'
)
new_h1 = (
    'Chinese Traditional Wear:\n'
    '            <span class="block text-[#b5343a]">Hanfu, Qipao &amp; Beyond</span>'
)
content = content.replace(old_h1, new_h1)

# Replace hero subtitle
old_subtitle = 'From Hanfu photoshoots on Xi''''an''''s ancient city walls to qipao tailoring in Shanghai''''s back lanes'
new_subtitle = 'Explore 3,000 years of Chinese fashion through 6 iconic styles, 12 dynasties, and the cities where you can still wear them today'
content = content.replace(old_subtitle, new_subtitle)

# Replace CTA buttons
old_cta = 'Find Experiences'
new_cta = 'Explore the Styles'
content = content.replace(old_cta, new_cta, 1)

old_cta2 = 'Browse by Style'
new_cta2 = 'Plan Your Experience'
content = content.replace(old_cta2, new_cta2, 1)

# Add quick-jump tabs after the CTA div
old_cta_end = '</div>\n        </div>\n        <!-- Right:'
new_cta_insert = '''</div>
          <!-- Quick-jump tabs -->
          <div class="mt-6 flex flex-wrap gap-2">
            <a href="#styles" class="text-xs px-3 py-1.5 bg-stone-100 rounded-full text-stone-600 hover:bg-stone-200 transition-colors">Types</a>
            <a href="#dynasties" class="text-xs px-3 py-1.5 bg-stone-100 rounded-full text-stone-600 hover:bg-stone-200 transition-colors">Dynasties</a>
            <a href="#compare-preview" class="text-xs px-3 py-1.5 bg-stone-100 rounded-full text-stone-600 hover:bg-stone-200 transition-colors">Compare</a>
            <a href="#gallery" class="text-xs px-3 py-1.5 bg-stone-100 rounded-full text-stone-600 hover:bg-stone-200 transition-colors">Gallery</a>
            <a href="#quiz" class="text-xs px-3 py-1.5 bg-stone-100 rounded-full text-stone-600 hover:bg-stone-200 transition-colors">Quiz</a>
          </div>
        </div>
        <!-- Right:'''
content = content.replace(old_cta_end, new_cta_insert)

with open(src, "w", encoding="utf-8", newline="\n") as f:
    f.write(content)
print("Patch 1 (Hero): Done")
