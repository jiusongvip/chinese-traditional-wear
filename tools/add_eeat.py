f=r"D:\workspaces\website\chinese-traditional-wear\src\pages\index.astro"
c=open(f,"r",encoding="utf-8").read()
# Find the first </BaseLayout> after the schema script
schema_pos=c.find("schemaHomeFAQ}")
# Find </BaseLayout> after schema
bl_pos=c.find("</BaseLayout>", schema_pos)
eeat='    <p class="text-xs text-center text-white/40 py-3">Written by ChinaStyle Editorial Team · Fact-checked against Palace Museum &amp; China National Silk Museum archives · Updated August 2026</p>\n  '
c=c[:bl_pos]+eeat+c[bl_pos:]
open(f,"w",encoding="utf-8",newline="\n").write(c)
print("EEAT added before </BaseLayout> at position", bl_pos)
print("Lines:", len(c.splitlines()))
