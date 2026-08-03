import os, re

src = r"D:\workspaces\website\chinese-traditional-wear\src\pages"

# 1. Transport page
fp = os.path.join(src, "plan-trip", "transport", "index.astro")
with open(fp, "r", encoding="utf-8") as f: c = f.read()
old = """    <h2 class="font-serif-sc text-2xl font-bold text-stone-900 mt-14 mb-4">High-Speed Trains</h2>"""
new_extra = """    <h2 class="font-serif-sc text-2xl font-bold text-stone-900 mt-14 mb-4">High-Speed Trains</h2>
    <p class="text-stone-600 leading-relaxed">China's high-speed rail network is the world's largest and most efficient. G-class trains run at 300-350 km/h between major cities. Book via Trip.com (English, no service fee) or directly at station counters. Tickets go on sale 15 days ahead and can sell out for popular routes like Beijing-Xi'an during holidays. Seat classes: Second Class (about 515 RMB Beijing-Xi'an, perfectly comfortable), First Class (about 825 RMB, wider seats), Business Class (about 1,500 RMB, lie-flat).</p>
    <h2 class="font-serif-sc text-2xl font-bold text-stone-900 mt-14 mb-4">City Transit: Metro &amp; Buses</h2>
    <p class="text-stone-600 leading-relaxed">Every major city has extensive metro systems with English signage. Fares are 3-8 RMB per ride. Buy a rechargeable transit card at any station (deposit 20 RMB, refundable). For buses: exact change needed, typically 2 RMB per ride. Metro apps: download "MetroMan" or "ExploreMetro" for offline route maps.</p>
    <h2 class="font-serif-sc text-2xl font-bold text-stone-900 mt-14 mb-4">Ride-Hailing: Didi &amp; Alternatives</h2>
    <p class="text-stone-600 leading-relaxed">Didi (Chinese Uber) is available in English via the app. Download and set up before your trip. For short trips without Didi: regular taxis are plentiful but drivers rarely speak English \u2014 have your destination written in Chinese characters. Fares: 10-15 RMB flag fall + 2-3 RMB per km.</p>"""
after_text = '<div class="mt-8"><a href="/plan-trip"'
c = re.sub(r'(<h2 class="font-serif-sc text-2xl font-bold text-stone-900 mt-14 mb-4">High-Speed Trains</h2>.*?)' + re.escape(after_text), new_extra + '\n    ' + after_text, c, flags=re.DOTALL)
with open(fp, "w", encoding="utf-8", newline="\n") as f: f.write(c)
print("Transport: added city transit + Didi sections")

# 2. Visa page - expand with application process
fp2 = os.path.join(src, "plan-trip", "visa", "index.astro")
with open(fp2, "r", encoding="utf-8") as f: c2 = f.read()
old2 = '<div class="mt-8"><a href="/plan-trip"'
visa_extra = """    <h2 class="font-serif-sc text-2xl font-bold text-stone-900 mt-14 mb-4">How to Apply for an L Visa</h2>
    <div class="space-y-3 text-sm text-stone-600">
      <p><strong>Step 1:</strong> Gather documents: passport (valid 6+ months beyond entry, 2+ blank pages), completed visa application form (Form V.2013), passport photo (33mm x 48mm, white background), flight itinerary, hotel bookings, and bank statements showing sufficient funds.</p>
      <p><strong>Step 2:</strong> Submit at your nearest Chinese Visa Application Service Center (CVASC) or Chinese embassy/consulate. Most countries now require in-person fingerprinting. Processing time: 4-5 business days standard, 2-3 days express (extra fee).</p>
      <p><strong>Step 3:</strong> Pay the fee. Single-entry L visa: ~140 USD (varies by nationality). Double-entry: ~210 USD. Multiple-entry (6-12 months): ~280-420 USD.</p>
      <p><strong>Tip:</strong> If visiting for traditional clothing experiences, list "cultural tourism" as your purpose. Include your Hanfu/qipao rental confirmations as supporting documents \u2014 this helps establish a legitimate travel itinerary.</p>
    </div>
    <h2 class="font-serif-sc text-2xl font-bold text-stone-900 mt-14 mb-4">Embassy Links by Country</h2>
    <p class="text-sm text-stone-500">Find your nearest Chinese embassy or visa center: <a href="https://www.visaforchina.cn" class="text-[#b5343a] hover:underline" target="_blank" rel="noopener">visaforchina.cn</a> (global portal). For US citizens: check your state's CVASC jurisdiction at the Chinese Embassy DC website. For EU citizens: most countries have CVASC centers in major cities.</p>
    """
c2 = c2.replace(old2, visa_extra + '\n    ' + old2)
with open(fp2, "w", encoding="utf-8", newline="\n") as f: f.write(c2)
print("Visa: added application process + embassy links")

# 3. Seasons page
fp3 = os.path.join(src, "plan-trip", "seasons", "index.astro")
with open(fp3, "r", encoding="utf-8") as f: c3 = f.read()
old3 = '<div class="mt-8"><a href="/plan-trip"'
seasons_extra = """    <h2 class="font-serif-sc text-2xl font-bold text-stone-900 mt-14 mb-4">Month-by-Month Guide</h2>
    <div class="overflow-x-auto"><table class="w-full text-sm border-collapse"><thead><tr class="border-b border-stone-200 text-left"><th class="py-3 pr-4 font-semibold">Month</th><th class="py-3 pr-4 font-semibold">Best For</th><th class="py-3 font-semibold">Avg Temp</th></tr></thead><tbody>
<tr class="border-b border-stone-100"><td class="py-2.5 pr-4 font-medium">January</td><td class="py-2.5 pr-4 text-xs">Snow Hanfu photos in Xi'an and Beijing \u2014 stunning contrast</td><td class="py-2.5 text-xs">-5 to 5\u00b0C</td></tr>
<tr class="border-b border-stone-100"><td class="py-2.5 pr-4 font-medium">February</td><td class="py-2.5 pr-4 text-xs">Spring Festival (varies) \u2014 Tang suit photos in festive Beijing</td><td class="py-2.5 text-xs">0 to 10\u00b0C</td></tr>
<tr class="border-b border-stone-100"><td class="py-2.5 pr-4 font-medium">March</td><td class="py-2.5 pr-4 text-xs">Suzhou gardens begin blooming \u2014 silk qipao photos</td><td class="py-2.5 text-xs">8 to 18\u00b0C</td></tr>
<tr class="border-b border-stone-100"><td class="py-2.5 pr-4 font-medium">April</td><td class="py-2.5 pr-4 text-xs">Hanfu Culture Festival in Xi'an + Luoyang peony season</td><td class="py-2.5 text-xs">12 to 22\u00b0C</td></tr>
<tr class="border-b border-stone-100"><td class="py-2.5 pr-4 font-medium">May</td><td class="py-2.5 pr-4 text-xs">Ideal everywhere \u2014 warm but not hot, clear skies</td><td class="py-2.5 text-xs">18 to 28\u00b0C</td></tr>
<tr class="border-b border-stone-100"><td class="py-2.5 pr-4 font-medium">June</td><td class="py-2.5 pr-4 text-xs">Guizhou Miao festivals begin \u2014 ethnic minority experiences</td><td class="py-2.5 text-xs">22 to 32\u00b0C</td></tr>
<tr class="border-b border-stone-100"><td class="py-2.5 pr-4 font-medium">July</td><td class="py-2.5 pr-4 text-xs">Hangzhou lotus season \u2014 light Song dynasty Hanfu by West Lake</td><td class="py-2.5 text-xs">26 to 35\u00b0C</td></tr>
<tr class="border-b border-stone-100"><td class="py-2.5 pr-4 font-medium">August</td><td class="py-2.5 pr-4 text-xs">Evening photoshoots only \u2014 too hot for midday costumes</td><td class="py-2.5 text-xs">26 to 35\u00b0C</td></tr>
<tr class="border-b border-stone-100"><td class="py-2.5 pr-4 font-medium">September</td><td class="py-2.5 pr-4 text-xs">Perfect month \u2014 Mid-Autumn Festival, clear autumn light</td><td class="py-2.5 text-xs">20 to 28\u00b0C</td></tr>
<tr class="border-b border-stone-100"><td class="py-2.5 pr-4 font-medium">October</td><td class="py-2.5 pr-4 text-xs">Golden Week first week: AVOID. Rest of Oct: Excellent</td><td class="py-2.5 text-xs">12 to 22\u00b0C</td></tr>
<tr class="border-b border-stone-100"><td class="py-2.5 pr-4 font-medium">November</td><td class="py-2.5 pr-4 text-xs">Nanjing autumn leaves \u2014 Ming dynasty Hanfu in red forests</td><td class="py-2.5 text-xs">5 to 15\u00b0C</td></tr>
<tr><td class="py-2.5 pr-4 font-medium">December</td><td class="py-2.5 pr-4 text-xs">Moody winter shots, fewer tourists, lower hotel prices</td><td class="py-2.5 text-xs">-2 to 8\u00b0C</td></tr>
</tbody></table></div>
    <p class="text-xs text-stone-400 mt-3">Temperatures are approximate ranges for northern cities (Beijing, Xi'an). Southern cities (Shanghai, Hangzhou, Guizhou) are typically 5-8\u00b0C warmer.</p>
    """
c3 = c3.replace(old3, seasons_extra + '\n    ' + old3)
with open(fp3, "w", encoding="utf-8", newline="\n") as f: f.write(c3)
print("Seasons: added month-by-month table")

print("\nAll plan-trip subpages expanded!")
