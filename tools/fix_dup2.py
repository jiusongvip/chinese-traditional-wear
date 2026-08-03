f=r"D:\workspaces\website\chinese-traditional-wear\src\pages\index.astro"
c=open(f,"r",encoding="utf-8").read()

import re
# Find all occurrences of "New Here?" 
matches=list(re.finditer(r'New Here\?', c))
print(f'"New Here?" found {len(matches)} times at: {[m.start() for m in matches]}')

if len(matches) >= 2:
    pos1=matches[0].start()
    pos2=matches[1].start()
    # Find the section containing pos1
    sec1_start=c.rfind("<section", 0, pos1)
    sec1_end=c.find("</section>", pos1)
    # Find section containing pos2
    sec2_start=c.rfind("<section", 0, pos2)
    sec2_end=c.find("</section>", pos2)
    print(f"Sec1: {sec1_start}-{sec1_end}")
    print(f"Sec2: {sec2_start}-{sec2_end}")
    
    if sec2_start < sec1_end:
        # Section 2 starts before section 1 ends - remove the smaller duplicate
        # Find which is the duplicate by checking nearby content
        # Remove from sec1_end to sec2_end
        old_len=len(c)
        c=c[:sec1_end]+c[sec2_end:]
        print(f"Removed chars {sec1_end} to {sec2_end} ({old_len-len(c)} chars)")
        open(f,"w",encoding="utf-8",newline="\n").write(c)

c=open(f,"r",encoding="utf-8").read()
print(f"Final: lines={len(c.splitlines())}, New Here={c.count('New Here?')}, Major Styles={c.count('Major Styles')}")
