"""List chapters whose Table/Figure captions are not 1..n in order or carry another chapter number.
usage: python3 caption_check.py <manual.md>
English manuals are split by the "# " chapters after "# Table of Contents"; Japanese manuals (表/図 N-M)
are grouped by the chapter number in the caption."""
import re,sys,collections
p=sys.argv[1]
L=open(p,encoding='utf-8').read().split('\n')
if any(l.strip()=='# Table of Contents' for l in L):
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
else:
    CAP=re.compile(r'^\s*(?:>\s*)?(?:!\[[^\]]*\]\([^)]*\)\s*)*\**(表|図) ?(\d+)[‑-](\d+(?:[‑-]\d+|[a-z])?)(.?)')
    seq=collections.defaultdict(list)
    for i,l in enumerate(L,1):
        m=CAP.match(l)
        if m: seq[(m[1],int(m[2]))].append((i,m[3],m[4]))
    for (kind,ch),caps in sorted(seq.items()):
        if [c[1] for c in caps]!=[str(k) for k in range(1,len(caps)+1)]:
            print(f'{kind}{ch}: {[(c[0],c[1]) for c in caps]}')
        bad=[c[0] for c in caps if c[2]!=' ']
        if bad: print(f'{kind}{ch}: number not followed by one space (lines {bad})')
