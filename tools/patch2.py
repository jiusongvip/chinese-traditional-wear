with open(r"D:\workspaces\website\chinese-traditional-wear\src\pages\index.astro", "r", encoding="utf-8") as f:
    c = f.read()

# === 1. Add "At a Glance" stats bar after hero section ===
old_section_end = '</section>\n\n  <!-- ============================================================'
stats_bar = '''</section>

  <section class="py-12 bg-[#b5343a]">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
        <div>
          <p class="text-3xl sm:text-4xl font-bold text-white">6</p>
          <p class="text-sm text-white/70 mt-1">Major Styles</p>
        </div>
        <div>
          <p class="text-3xl sm:text-4xl font-bold text-white">3,000+</p>
          <p class="text-sm text-white/70 mt-1">Years of History</p>
        </div>
        <div>
          <p class="text-3xl sm:text-4xl font-bold text-white">12+</p>
          <p class="text-sm text-white/70 mt-1">Dynasties Covered</p>
        </div>
        <div>
          <p class="text-3xl sm:text-4xl font-bold text-white">55</p>
          <p class="text-sm text-white/70 mt-1">Ethnic Traditions</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ============================================================'''
c = c.replace(old_section_end, stats_bar, 1)

# === 2. Insert Beginner's Guide before Categories ===
old_categories = '<!-- ============================================================\n       CATEGORIES'
beginner_guide = '''<!-- ============================================================
       NEW HERE? - Beginner''s Guide
       ============================================================ -->
  <section class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="mb-14 max-w-2xl">
        <span class="text-xs font-medium text-[#b5343a] tracking-[0.15em] uppercase">New Here?</span>
        <h2 class="font-serif-sc text-3xl sm:text-4xl font-bold tracking-tight text-stone-900">
          Chinese Traditional Wear at a Glance
        </h2>
        <p class="mt-4 text-stone-500 leading-relaxed">
          Four iconic styles, each with its own story. Tap any to explore deeper.
        </p>
      </div>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <a href="/hanfu" class="group block bg-stone-50 rounded-xl overflow-hidden border border-stone-100 hover:border-[#b5343a]/30 hover:shadow-md transition-all">
          <div class="aspect-[3/2] overflow-hidden">
            <img src="/images/cat-hanfu.webp" alt="Hanfu traditional Chinese clothing" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" loading="lazy" width="1536" height="1024" />
          </div>
          <div class="p-5">
            <span class="text-[10px] font-medium text-[#b5343a] tracking-widest uppercase">Han to Ming dynasties</span>
            <h3 class="text-lg font-semibold text-stone-900 mt-1">Hanfu</h3>
            <p class="text-sm text-stone-500 mt-2 leading-relaxed">Ancient flowing robes, crossed collars, wide sleeves. Worn for 3,000+ years.</p>
            <span class="inline-flex items-center gap-1 mt-3 text-xs font-medium text-[#b5343a] group-hover:gap-2 transition-all">Learn more <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m9 18 6-6-6-6"/></svg></span>
          </div>
        </a>
        <a href="/qipao-cheongsam" class="group block bg-stone-50 rounded-xl overflow-hidden border border-stone-100 hover:border-[#b5343a]/30 hover:shadow-md transition-all">
          <div class="aspect-[3/2] overflow-hidden">
            <img src="/images/cat-qipao.webp" alt="Qipao traditional Chinese dress" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" loading="lazy" width="1536" height="1024" />
          </div>
          <div class="p-5">
            <span class="text-[10px] font-medium text-[#b5343a] tracking-widest uppercase">Republican era to modern</span>
            <h3 class="text-lg font-semibold text-stone-900 mt-1">Qipao</h3>
            <p class="text-sm text-stone-500 mt-2 leading-relaxed">Form-fitting one-piece dress, high collar, side slits. 1920s Shanghai glamour.</p>
            <span class="inline-flex items-center gap-1 mt-3 text-xs font-medium text-[#b5343a] group-hover:gap-2 transition-all">Learn more <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m9 18 6-6-6-6"/></svg></span>
          </div>
        </a>
        <a href="/tang-suit" class="group block bg-stone-50 rounded-xl overflow-hidden border border-stone-100 hover:border-[#b5343a]/30 hover:shadow-md transition-all">
          <div class="aspect-[3/2] overflow-hidden">
            <img src="/images/cat-tang-suit.webp" alt="Tang suit traditional Chinese jacket" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" loading="lazy" width="1536" height="1024" />
          </div>
          <div class="p-5">
            <span class="text-[10px] font-medium text-[#b5343a] tracking-widest uppercase">Modern festive tradition</span>
            <h3 class="text-lg font-semibold text-stone-900 mt-1">Tang Suit</h3>
            <p class="text-sm text-stone-500 mt-2 leading-relaxed">Mandarin-collar jacket, knotted frog buttons. Perfect for festivals and celebrations.</p>
            <span class="inline-flex items-center gap-1 mt-3 text-xs font-medium text-[#b5343a] group-hover:gap-2 transition-all">Learn more <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m9 18 6-6-6-6"/></svg></span>
          </div>
        </a>
        <a href="/zhongshan" class="group block bg-stone-50 rounded-xl overflow-hidden border border-stone-100 hover:border-[#b5343a]/30 hover:shadow-md transition-all">
          <div class="aspect-[3/2] overflow-hidden">
            <img src="/images/cat-zhongshan.webp" alt="Zhongshan suit traditional Chinese menswear" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" loading="lazy" width="1536" height="1024" />
          </div>
          <div class="p-5">
            <span class="text-[10px] font-medium text-[#b5343a] tracking-widest uppercase">20th century to present</span>
            <h3 class="text-lg font-semibold text-stone-900 mt-1">Zhongshan Suit</h3>
            <p class="text-sm text-stone-500 mt-2 leading-relaxed">Revolutionary formal menswear, turned-down collar, four patch pockets.</p>
            <span class="inline-flex items-center gap-1 mt-3 text-xs font-medium text-[#b5343a] group-hover:gap-2 transition-all">Learn more <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m9 18 6-6-6-6"/></svg></span>
          </div>
        </a>
      </div>
    </div>
  </section>

  <!-- ============================================================
       CATEGORIES'''
c = c.replace(old_categories, beginner_guide, 1)

# === 3. Rename categories section ID and heading ===
c = c.replace('id="categories"', 'id="styles"')
c = c.replace('Traditional Styles', 'Explore All Styles')
c = c.replace('Six Styles, Six Journeys', 'Six Styles, Six Destinations')
c = c.replace("Each craft tradition is tied to a place. Pick a style, and you''ve picked your next destination.", "Each craft tradition is tied to a place. Pick a style, and you''ve picked where to go.")

# Change category section bg
c = c.replace('<section id="styles" class="py-24 bg-white">', '<section id="styles" class="py-24 bg-stone-50">')

# Change recommendation cards bg
c = c.replace('p-4 bg-stone-50 rounded-xl', 'p-4 bg-white rounded-xl border border-stone-200', 6)

with open(r"D:\workspaces\website\chinese-traditional-wear\src\pages\index.astro", "w", encoding="utf-8", newline="\n") as f:
    f.write(c)
print("Patch 2 (Stats + Beginner + Category rename): Done")
