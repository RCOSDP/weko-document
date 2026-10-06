"""Renumber Table captions 1..n in order of appearance within the given chapters, updating in-file references.
usage: python3 table_renum.py <EN manual.md> <chapter,chapter,...> [apply]"""
import re,sys
p=sys.argv[1]; targets=[int(x) for x in sys.argv[2].split(',')]; apply=len(sys.argv)>3
L=open(p,encoding='utf-8').read().split('\n')
toc=next(i for i,l in enumerate(L) if l.strip()=='# Table of Contents')
chap=[i for i,l in enumerate(L) if i>toc and re.match(r'^# ',l)]
CAP=re.compile(r'^((?:>\s*)?(?:LINKID=\S*?【参照先】)?(?:\*\*)?)Table (\d+)([‑-])([\d‑-]+?)([.\s])')
REF=re.compile(r'Table (\d+)([‑-])(\d+(?:[‑-]\d+)?)')
for n in targets:
    start=chap[n-1]; end=chap[n] if n<len(chap) else len(L)
    caps=[]
    for i in range(start,end):
        m=CAP.match(L[i].strip())
        if m and m.group(2)==str(n): caps.append((i,m.group(4)))
    mapping={}
    for k,(i,old) in enumerate(caps,1):
        mapping.setdefault(old.replace('‑','-'),str(k))
    capset={c[0] for c in caps}
    others=set()
    for i in range(len(L)):
        if i in capset: continue
        for m in REF.finditer(L[i]):
            if m.group(1)==str(n): others.add(m.group(3).replace('‑','-'))
    unknown=sorted(o for o in others if o not in mapping)
    changed={o:v for o,v in mapping.items() if o!=v}
    print(f'ch{n}: captions {len(caps)}, renumber {len(changed)}, refs not matching a caption: {unknown}')
    if apply:
        for k,(i,old) in enumerate(caps,1):
            line=L[i]; off=len(line)-len(line.lstrip()); m=CAP.match(line.strip())
            L[i]=line[:off+m.start(2)]+str(n)+m.group(3)+str(k)+line[off+m.end(4):]
        def sub(m):
            if m.group(1)!=str(n): return m.group(0)
            new=mapping.get(m.group(3).replace('‑','-'))
            return f'Table {n}{m.group(2)}{new}' if new else m.group(0)
        for i in range(len(L)):
            if i not in capset: L[i]=REF.sub(sub,L[i])
if apply: open(p,'w',encoding='utf-8').write('\n'.join(L))
