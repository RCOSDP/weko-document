"""Renumber the Japanese captions (表/図 N-M) of a manual 1..n per chapter in order of appearance,
write them as "表 N-M 題名" (space, ASCII hyphen), and rewrite the references to them
(matched by title, else by the nearest caption with the old number). usage: <md> [--apply]
N is the chapter number in the table of contents ("[16. 設定](#設定)" -> the "## 設定" chapter), not
the number the caption had: captions copied from an older edition keep old chapter numbers.
A caption in a table header (<th>表 1-3 …</th>) counts too."""
import re,sys
f=sys.argv[1]; apply='--apply' in sys.argv
s=open(f,encoding='utf-8',newline='').read()
nl='\r\n' if '\r\n' in s else '\n'
L=s.split(nl)
CAP=re.compile(r'^(\s*(?:>\s*)?(?:<th>)?(?:!\[[^\]]*\]\([^)]*\)\s*)*\**)(表|図) ?(\d+)[‑-](\d+(?:[‑-]\d+|[a-z])?)[ 　\t]*(.*)$')
def norm(t):
    t=re.sub(r'</t[hd]>.*$','',t)
    t=t.replace('\\','').replace('[','［').replace(']','］')
    return re.sub(r'[\s「」『』*]','',t)
def slug(t):
    return re.sub(r'[^\w\- ]','',t.strip().lower()).replace(' ','-')
toc={}
for l in L:
    m=re.match(r'^\s*[-*]?\s*\[(\d+)\.? [^\]]+\]\(#([^)]+)\)',l)
    if m: toc.setdefault(m[2],int(m[1]))
caps=[]  # [line, kind, old chap, old num, title, new chap, new num]
fence=False; chap=None
for i,l in enumerate(L):
    if l.lstrip().startswith('```'): fence=not fence
    if fence: continue
    h=re.match(r'^## (.*)',l)
    if h and slug(h[1]) in toc: chap=toc[slug(h[1])]
    m=CAP.match(l)
    if m: caps.append([i,m[2],int(m[3]),m[4].replace('‑','-'),m[5],chap or int(m[3])])
cnt={}
for c in caps:
    k=(c[1],c[5]); cnt[k]=cnt.get(k,0)+1; c.append(cnt[k])
capline={c[0]:c for c in caps}
REF=re.compile(r'(表|図) ?(\d+)[‑-](\d+(?:[‑-]\d+|[a-z])?)(?![\d‑-])([ 　]?)')
changes=[]
for i,l in enumerate(L):
    if i in capline:
        c=capline[i]; m=CAP.match(l)
        title=m[5]
        new=f'{m[1]}{c[1]} {c[5]}-{c[6]}'+(' '+title if title else '')
        if new!=l: changes.append((i,l,new))
        L[i]=new; continue
    def rep(m):
        kind,ch,old=m[1],int(m[2]),m[3].replace('‑','-')
        after=l[m.end():]
        t=re.split(r'」|を参照|を参考|の説明|に示す|に記載|$',after,maxsplit=1)[0]
        nt=norm(t)
        pool=[c for c in caps if c[1]==kind]
        cand=[c for c in pool if nt and norm(c[4])==nt] or [c for c in pool if len(nt)>=3 and (norm(c[4]).startswith(nt[:max(3,min(len(nt),len(norm(c[4]))))]) )]
        how='title'
        if not cand:
            cand=[c for c in pool if c[2]==ch and c[3]==old]; how='num'
        if not cand:
            print(f'  ?? {i+1}: no caption for {m[0]!r} | {l.strip()[:80]}'); return m[0]
        c=min(cand,key=lambda c:abs(c[0]-i))
        out=f'{kind} {c[5]}-{c[6]}'+(m[4] and ' ')
        if (c[5],str(c[6]))!=(ch,old): print(f'  {i+1}: {kind}{ch}-{old} -> {c[5]}-{c[6]} [{how}] {l.strip()[:70]}')
        return out
    nl2=REF.sub(rep,l)
    if nl2!=l: changes.append((i,l,nl2)); L[i]=nl2
moved=sorted({(c[1],c[2],c[5]) for c in caps if c[2]!=c[5]})
if moved: print('  chapter changed:',', '.join(f'{k}{a}->{b}' for k,a,b in moved))
print(f,'captions',len(caps),'changed lines',len(changes))
if apply: open(f,'w',encoding='utf-8',newline='').write(nl.join(L))
