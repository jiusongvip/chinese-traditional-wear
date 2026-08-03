f=r"D:\workspaces\website\chinese-traditional-wear\src\pages\index.astro"
c=open(f,"r",encoding="utf-8").read()

# Find the first </BaseLayout> (the correct end of template)
first_end=c.find("</BaseLayout>")
print(f"First </BaseLayout> at {first_end}")
print(f"Context: ...{c[first_end-30:first_end+30]}...")

# Find the second </BaseLayout>
second_end=c.find("</BaseLayout>", first_end+1)
print(f"Second </BaseLayout> at {second_end}")

# If there are duplicate sections in the template (same BaseLayout), find them
# Check for double "Major Styles" in the stats bar
import re
matches=list(re.finditer(r'Major Styles', c))
print(f'"Major Styles" found at: {[m.start() for m in matches]}')
if len(matches)>1:
    print(f"  Context around each:")
    for i,m in enumerate(matches):
        print(f"  #{i}: ...{c[m.start()-30:m.start()+50]}...")
