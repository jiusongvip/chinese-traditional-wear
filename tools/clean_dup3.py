f=r"D:\workspaces\website\chinese-traditional-wear\src\pages\index.astro"
c=open(f,"r",encoding="utf-8").read()

# Strategy: find the FIRST </BaseLayout> (the correct template end)
# Then keep everything before it + add clean closing
first_bl_end=c.find("</BaseLayout>")+len("</BaseLayout>")
before=c[:first_bl_end]

# Check what's after
after=c[first_bl_end:]
print(f"Content after first </BaseLayout>: {repr(after[:100])}")
print(f"Has 'New Here' in after: {'New Here' in after}")

# The duplicate content is after the first </BaseLayout>
# But there's no second <BaseLayout> tag... 
# Let me check for sections in the duplicate area
import re
print(f"Sections after first BL: {len(re.findall(r'<section', after))}")

# Remove everything after the first </BaseLayout>, keep schema
schema_idx=after.find("<script")
if schema_idx>0:
    clean=before+"\n\n"+after[schema_idx:]
else:
    clean=before

open(f,"w",encoding="utf-8",newline="\n").write(clean)
c2=open(f,"r",encoding="utf-8").read()
print(f"Lines: {len(c2.splitlines())}")
print(f"Major Styles: {c2.count('Major Styles')}")
print(f"New Here: {c2.count('New Here?')}")
print(f"BaseLayout: {c2.count('<BaseLayout')}")
