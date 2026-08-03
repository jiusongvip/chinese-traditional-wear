f=r"D:\workspaces\website\chinese-traditional-wear\src\pages\index.astro"
c=open(f,"r",encoding="utf-8").read()
# Fix corrupted CTA
c=c.replace("Ready to Chinese Traditional Wear: History?","Ready to Explore Chinese Traditional Wear?")
# Remove any stray standalone colon line  
import re
c=re.sub(r'\n\s+:\s*\n','\n',c)
open(f,"w",encoding="utf-8",newline="\n").write(c)
print("CTA fixed, stray colons removed")
print("Wear China''s still in file:", "Wear China''s" in c)
