c=open(r"D:\workspaces\website\chinese-traditional-wear\src\pages\index.astro","r",encoding="utf-8").read()
first_end=c.find("</BaseLayout>")+len("</BaseLayout>")
# Find the first schema script AFTER the first </BaseLayout>
rest=c[first_end:]
schema_idx=rest.find("<script")
if schema_idx>0:
    keep=c[:first_end]+"\n\n"+rest[schema_idx:]
else:
    keep=c[:first_end]
lines=len(keep.splitlines())
# Final fix: replace set:html with is:inline
keep=keep.replace("set:html","is:inline")
open(r"D:\workspaces\website\chinese-traditional-wear\src\pages\index.astro","w",encoding="utf-8",newline="\n").write(keep)
print("Lines:",lines)
print("Wear China:", "Wear China" in keep)
print("set:html:", "set:html" in keep)
# Check braces
open_b=sum(1 for ch in keep.split("---",2)[-1] if ch=="{")
close_b=sum(1 for ch in keep.split("---",2)[-1] if ch=="}")
print("Braces: {",open_b,"}",close_b,"diff",open_b-close_b)
