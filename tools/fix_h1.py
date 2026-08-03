f=r"D:\workspaces\website\chinese-traditional-wear\src\pages\index.astro"
c=open(f,"r",encoding="utf-8").read()
old="Wear China''s"
c=c.replace(old,"Chinese Traditional Wear:")
old2="<span class=\"block text-[#b5343a]\">History on</span>"
c=c.replace(old2,"<span class=\"block text-[#b5343a]\">Hanfu, Qipao &amp; Beyond</span>")
old3="            Your Journey"
idx=c.find(old3)
before=c[:idx]
after=c[idx+len(old3):]
c=before+after
# Also fix \u00b7 to actual HTML entity
c=c.replace("\\u00b7","&middot;")
open(f,"w",encoding="utf-8",newline="\n").write(c)
print("H1 fixed, middot fixed")
