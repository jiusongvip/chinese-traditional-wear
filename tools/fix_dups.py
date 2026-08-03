f=r"D:\workspaces\website\chinese-traditional-wear\src\pages\index.astro"
c=open(f,"r",encoding="utf-8").read()

# Remove duplicate stats bar - find the two <section class="py-12 bg-[#b5343a]"> 
import re
# Find the first stats section
sec_pattern=r'<section class="py-12 bg-\[\#b5343a\]">'
secs=list(re.finditer(sec_pattern, c))
print(f"Found {len(secs)} stats sections at: {[m.start() for m in secs]}")

if len(secs) >= 2:
    # Find the closing of section 1
    start1=secs[0].start()
    start2=secs[1].start()
    # Find closing </section> for section 1 (between start1 and start2)
    mid=c.find("</section>", start1)
    print(f"Closing of sec1 at: {mid}")
    if mid < start2:
        # Remove section 2 (from start2 to its closing)
        end2=c.find("</section>", start2)
        if end2>0:
            end2+=len("</section>")
            # Include the trailing newline
            if c[end2:end2+1]=='\n': end2+=1
            c=c[:start1]+c[mid:]
            open(f,"w",encoding="utf-8",newline="\n").write(c)
            print(f"Removed duplicate stats section. New length: {len(c)}")

# Also remove duplicate end tags
c=open(f,"r",encoding="utf-8").read()
# Remove extra </BaseLayout> tags after the first
first_bl=c.find("</BaseLayout>")
content_after=c[first_bl+len("</BaseLayout>"):]
# Keep only content up to schema, remove extra </BaseLayout>
# Find schema
schema_pos=content_after.find("<script")
if schema_pos>0:
    before_schema=content_after[:schema_pos]
    after_schema=content_after[schema_pos:]
    # Count </BaseLayout> in after_schema
    bl_pos=after_schema.find("</BaseLayout>")
    if bl_pos>0:
        after_schema=after_schema[:bl_pos]+after_schema[bl_pos+len("</BaseLayout>"):]
    c=c[:first_bl+len("</BaseLayout>")]+"\n\n"+after_schema

c=c.replace("</BaseLayout>\n</BaseLayout>","</BaseLayout>")

open(f,"w",encoding="utf-8",newline="\n").write(c)
print(f"Final lines: {len(c.splitlines())}")
print(f"Major Styles: {c.count('Major Styles')}")
print(f"New Here: {c.count('New Here?')}")
print(f"BaseLayout: {c.count('<BaseLayout')}")
print(f"End Layout: {c.count('</BaseLayout>')}")
