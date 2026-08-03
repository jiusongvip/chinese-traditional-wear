import re
f=r"D:\workspaces\website\chinese-traditional-wear\src\pages\index.astro"
c=open(f,"r",encoding="utf-8").read()

# Find the two "New Here?" text positions
matches=list(re.finditer(r'New Here\?', c))
if len(matches) < 2:
    print("Only one or zero New Here found")
else:
    pos1=matches[0].start()
    pos2=matches[1].start()
    print(f"New Here #1 at {pos1}, #2 at {pos2}")
    
    # Find the section containing the second one
    sec2_start=c.rfind("<section", 0, pos2)
    sec2_end=c.find("</section>", pos2)
    if sec2_end < 0:
        sec2_end=c.find("</section>", pos2+100)
    
    # Find the closing of the section
    sec2_end=c.find("</section>", sec2_start)
    
    print(f"Section 2: {sec2_start} to {sec2_end} ({sec2_end-sec2_start} chars)")
    print(f"Content: ...{c[sec2_start:sec2_start+100]}...")
    
    if sec2_start > 0 and sec2_end > 0:
        old=len(c)
        c=c[:sec2_start]+c[sec2_end+len("</section>"):]
        # Strip trailing newline between sections
        c=c.replace("\n\n\n","\n\n")
        open(f,"w",encoding="utf-8",newline="\n").write(c)
        print(f"Removed {old-len(c)} chars. New Here: {c.count('New Here?')}")
