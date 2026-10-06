"""Renumber the chapter part of Table/Figure captions to the containing chapter number (dominant number only).
usage: python3 caption_renum.py <EN manual.md> [apply]   (dry run without "apply")"""
import re,sys
p=sys.argv[1]; apply=len(sys.argv)>2
L=open(p,encoding='utf-8').read().split('\n')
toc=next(i for i,l in enumerate(L) if l.strip()=='# Table of Contents')
chap=[i for i,l in enumerate(L) if i>toc and re.match(r'^# ',l)]
cap=re.compile(r'\b(Table|Figure|Fig\.) (\d+)([‑-])(\d+)')
for n,start in enumerate(chap,1):
    end=chap[n] if n<len(chap) else len(L)
    title=L[start][2:].strip() or L[start+1].strip() or L[start+2].strip()
    seen={}
    for i in range(start,end):
        for m in cap.finditer(L[i]): seen[m.group(2)]=seen.get(m.group(2),0)+1
    dom=max(seen,key=seen.get) if seen else None
    if apply and dom and dom!=str(n):
        for i in range(start,end):
            L[i]=cap.sub(lambda m: f'{m.group(1)} {n}{m.group(3)}{m.group(4)}' if m.group(2)==dom else m.group(0),L[i])
    print(n, title[:40], seen, '->' if dom and dom!=str(n) else '', n if dom and dom!=str(n) else '')
if apply: open(p,'w',encoding='utf-8').write('\n'.join(L))
