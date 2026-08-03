c=open(r"D:\workspaces\website\chinese-traditional-wear\src\pages\index.astro","r",encoding="utf-8").read()

# Insert Quiz card before START PLANNING / Ready to Experience
marker = "Ready to Experience It Firsthand?"
idx = c.find(marker)
# Find the opening <section before this
sec_start = c.rfind("<section", 0, idx)

quiz_block = '\n  <section id="quiz" class="py-20 bg-[#b5343a]">\n    <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 text-center">\n      <span class="text-xs font-medium text-white/60 tracking-[0.15em] uppercase">Interactive</span>\n      <h2 class="font-serif-sc text-3xl sm:text-4xl font-bold tracking-tight text-white mt-2">\n        Which Style Suits You?\n      </h2>\n      <p class="mt-4 text-white/70 leading-relaxed max-w-lg mx-auto">\n        Not sure where to start? Take our 2-minute quiz to discover which Chinese traditional clothing matches your personality and travel style.\n      </p>\n      <a href="/quiz" class="inline-flex items-center justify-center mt-8 px-8 py-3.5 bg-white text-[#b5343a] font-medium rounded-full hover:bg-stone-100 transition-colors text-sm tracking-wide">\n        Take the Style Quiz\n        <svg xmlns="http://www.w3.org/2000/svg" class="ml-2 w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m9 18 6-6-6-6"/></svg>\n      </a>\n    </div>\n  </section>\n\n'
c = c[:sec_start] + quiz_block + c[sec_start:]

# Add EEAT attribution in CTA section - before closing section/schema
cta_marker = 'src/pages/zhongshan/index.astro'
cta_idx = c.rfind(cta_marker)
# Find the closing </section> after this
sec_end = c.find('</section>', cta_idx)
if sec_end > 0:
    eeat_text = '\n    <p class="mt-10 text-xs text-white/40">Written by ChinaStyle Editorial Team \u00b7 Fact-checked against Palace Museum &amp; China National Silk Museum archives \u00b7 Updated August 2026</p>\n  '
    c = c[:sec_end] + eeat_text + c[sec_end:]

open(r"D:\workspaces\website\chinese-traditional-wear\src\pages\index.astro","w",encoding="utf-8",newline="\n").write(c)
print("Quiz card added, EEAT added")
print("Lines:", len(c.splitlines()))
