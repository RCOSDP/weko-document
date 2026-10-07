"""List chapters whose Table/Figure captions are not 1..n in order or carry another chapter number.
usage: python3 caption_check.py <EN manual.md>"""
import re,sys
p=sys.argv[1]
L=open(p,encoding='utf-8').read().split('\n')
toc=next(i for i,l in enumerate(L) if l.strip()=='# Table of Contents')
chap=[i for i,l in enumerate(L) if i>toc and re.match(r'^# ',l)]
# captions may follow "> ", images or a leftover Word file name ("zu0824070.tif"); "5.‑10" is a typo to fix
CAP=re.compile(r'^(?:>\s*)?(?:LINKID=\S*?【参照先】)?(?:!\[[^\]]*\]\([^)]*\)|\S*?\.tif)*(?:\*\*)?(Table|Figure) (\d+)(\.?)[‑-]([\d‑-]+)[.\s]')
for n,start in enumerate(chap,1):
    end=chap[n] if n<len(chap) else len(L)
    for kind in ('Table','Figure'):
        caps=[(i+1,m.group(2)+m.group(3),m.group(4)) for i in range(start,end) for m in [CAP.match(L[i].strip())] if m and m.group(1)==kind]
        nums=[c[2] for c in caps]
        seq=[str(k) for k in range(1,len(caps)+1)]
        if nums!=seq or any(c[1]!=str(n) for c in caps):
            print(f'ch{n} {kind}: {[(c[0],c[1]+"-"+c[2]) for c in caps]}')
