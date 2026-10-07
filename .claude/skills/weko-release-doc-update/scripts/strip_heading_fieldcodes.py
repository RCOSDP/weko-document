r"""Remove Word field codes from the headings of a Word-converted manual and rewrite the links to them.

usage: python3 strip_heading_fieldcodes.py <markdown file> [--apply]
  Removes LINKID=...【参照先】, \<INDEXWORD ...\> and \</INDEXWORD\> from heading lines (also headings
  inside list items), and joins a blank chapter heading ("#   ") with the chapter name on the next line.
  The GitHub-style anchors of the headings change, so every link in the file (](#...) and href="#...")
  to an old anchor, or to an <a id> placed just before a heading, is rewritten to the new anchor, and
  those <a id> lines are removed. Without --apply, only prints the counts.
  Then build the book and run add_anchors.py for the anchors honkit still lacks (duplicate headings).
  Links from other files are not rewritten: grep the repository for "<file>#" first.
"""
import re, sys
FC=re.compile(r'LINKID=[^【\s]*【\**参照先\**】|\\<INDEXWORD[^>]*\\>|\\</INDEXWORD\\>')
def clean(t): return re.sub(r'\s+',' ',FC.sub('',t)).strip()
def gh_text(t):
    t=re.sub(r'\\(.)',r'\1',t); t=re.sub(r'`([^`]*)`',r'\1',t)
    t=re.sub(r'!?\[([^\]]*)\]\([^)]*\)',r'\1',t)
    return t.replace('*','').strip()
def slugs(texts):
    out,seen=[],{}
    for t in texts:
        b=re.sub(r'[^\w\- ]','',gh_text(t).lower()).replace(' ','-')
        n=seen.get(b,0); seen[b]=n+1; out.append(b if n==0 else f'{b}-{n}')
    return out
HEAD=re.compile(r'(\s*(?:(?:\d+\.|[-*])\s+)*#{1,6})(?:\s+(.*?))?\s*$')
def heads(L):
    fence=False; r=[]
    for i,l in enumerate(L):
        if l.lstrip().startswith('```'): fence=not fence
        if fence: continue
        m=HEAD.match(l.rstrip('\r'))
        if m: r.append((i,m.group(1),m.group(2) or ''))
    return r
f=sys.argv[1]; apply='--apply' in sys.argv
with open(f,encoding='utf-8',newline='') as fp: src=fp.read(); nl='\r\n' if '\r\n' in src else '\n'
L=src.split(nl)
H=heads(L); old=slugs([t for _,_,t in H])
# new heading text (merge blank chapter heading with the next line)
newt={}; drop=set()
for i,h,t in H:
    if t=='' and h.lstrip().startswith('#') and i+1<len(L) and L[i+1].strip():
        newt[i]=clean(L[i+1]); drop.add(i+1)
    else: newt[i]=clean(t)
new=slugs([newt[i] for i,_,_ in H])
mp={}
for k,(i,h,t) in enumerate(H):
    if old[k]: mp.setdefault(old[k],new[k])
# <a id> lines just before a heading (blank lines between)
aid=set()
hidx={i:k for k,(i,_,_) in enumerate(H)}
for j,l in enumerate(L):
    m=re.fullmatch(r'<a id="([^"]+)"></a>\r?',l)
    if not m: continue
    k=j+1
    while k<len(L) and not L[k].strip(): k+=1
    if k in hidx and m.group(1)!=new[hidx[k]]:  # keep the ones still needed (e.g. duplicate headings)
        mp[m.group(1)]=new[hidx[k]]; aid.add(j)
        if j+1<len(L) and not L[j+1].strip(): aid.add(j+1)
newset=set(new)
unres=set(); cnt=0
def sub(m):
    global cnt
    fr=m.group(2)
    if fr in mp:
        if mp[fr]!=fr: cnt+=1
        return m.group(1)+mp[fr]+m.group(3)
    if fr not in newset: unres.add(fr)
    return m.group(0)
out=[]
for j,l in enumerate(L):
    if j in drop or j in aid: continue
    if j in hidx:
        i,h,t=H[hidx[j]]; l=f'{h} {newt[j]}'+('\r' if l.endswith('\r') else '')
    l=re.sub(r'(\]\(#)([^)\s]+)(\))',sub,l)
    l=re.sub(r'(href="#)([^"]+)(")',sub,l)
    out.append(l)
print(f,'headings',len(H),'changed',sum(1 for i,_,t in H if newt[i]!=t),'a-id removed',len([j for j in aid if L[j].strip()]),'links rewritten',cnt,'unresolved',len(unres))
for u in sorted(unres)[:30]: print('  ?',u)
if apply:
    with open(f,'w',encoding='utf-8',newline='') as fp: fp.write(nl.join(out))
