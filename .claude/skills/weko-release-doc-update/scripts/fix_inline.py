r"""Fix "<name>" placeholders that honkit hides as HTML tags and "_" that it turns into emphasis inside a word.

usage: python3 fix_inline.py [--apply] <md>...      (or: git ls-files -z '*.md' | python3 fix_inline.py -z [--apply])
Run from the repository root after build_docs.sh has installed honkit (docs/node_modules/kramed).
Each block (paragraph, list item...) is rendered with kramed, the markdown engine of honkit. Lines of blocks with unknown
HTML tags get &lt;name&gt;; in blocks where "_" made emphasis, lines get \_ one by one until it is gone.
Headings are only reported (changing them changes their anchors).
A block is rendered on its own, so a line in an indented code block may be escaped by mistake: rebuild, run
scan_rendered.py and undo the lines it reports as code-esc."""
import re,sys,json,subprocess,collections
SP=sys.path[0]
KNOWN=set('html head body title meta link script style div span p a img br hr h1 h2 h3 h4 h5 h6 ul ol li table thead tbody tfoot tr th td caption colgroup col pre code em strong b i u s del ins sup sub blockquote dl dt dd nav header footer section article aside main figure figcaption small big font center label input button form select option textarea iframe svg path g rect circle line polyline polygon text defs use tt kbd var samp abbr cite q mark details summary wbr noscript video source audio picture time object embed param map area rt ruby rp bdi bdo dfn address strike nobr'.split())
def render(blocks):
    r=subprocess.run(['node',SP+'/kramed_render.js'],input=json.dumps(blocks),capture_output=True,text=True,check=True); return json.loads(r.stdout)
def strip_code(h): return re.sub(r'<(pre|code)\b.*?</\1>','',h,flags=re.S)
def bad_tags(h): return [t for t in re.findall(r'</?([A-Za-z][^\s>/]*)',strip_code(h)) if t.lower() not in KNOWN]
def ems(h): return len(re.findall(r'<(?:em|strong)>',strip_code(h)))
PROT=re.compile(r'`[^`]*`|\]\([^)]*\)|<https?://[^>]*>|https?://[^\s<>)]*|&#?\w+;|\\.|<[^<>]*>')
def map_unprot(l,fn):
    out='';pos=0
    for m in PROT.finditer(l): out+=fn(l[pos:m.start()])+m[0]; pos=m.end()
    return out+fn(l[pos:])
def esc_us(l): return map_unprot(l,lambda s:s.replace('_','\\_'))
def esc_tag(l):
    parts=re.split(r'(`[^`]*`)',l)
    def r(m):
        n=m[2].lower()
        if n in KNOWN or re.match(r'(https?|mailto|ftp):',n) or '@' in m[0]: return m[0]
        return '&lt;'+m[1]+m[2]+m[3]+'&gt;'
    for i in range(0,len(parts),2): parts[i]=re.sub(r'<(/?)([A-Za-z][^<>\s=,"/]*)([^<>]*)>',r,parts[i])
    return ''.join(parts)
apply='--apply' in sys.argv; tot=collections.Counter(); heads=[]
FILES=[a for a in sys.argv[1:] if not a.startswith('--')]
if FILES==['-z']: FILES=[x for x in sys.stdin.read().split('\0') if x.endswith('.md')]
for f in FILES:
    s=open(f,encoding='utf-8',newline='').read(); nl='\r\n' if '\r\n' in s else '\n'
    L=s.split(nl); blocks=[]; cur=[]; code=False
    for i,l in enumerate(L):
        if l.lstrip().startswith('```'):
            if cur: blocks.append(cur); cur=[]
            code=not code; continue
        if code: continue
        if l.strip()=='' :
            if cur: blocks.append(cur); cur=[]
            continue
        if l.startswith('#'):
            if cur: blocks.append(cur); cur=[]
            if re.search(r'<[A-Za-z_][^>]*>',l) and bad_tags(render([l])[0]): heads.append((f,i+1,l.strip()[:80]))
            continue
        cur.append(i)
    if cur: blocks.append(cur)
    def text(b):
        ind=min(len(L[i])-len(L[i].lstrip()) for i in b)
        return '\n'.join(L[i][ind:] for i in b)
    H=render([text(b) for b in blocks]); changed=collections.Counter()
    for b,h in zip(blocks,H):
        if bad_tags(h):
            for i in b:
                n=esc_tag(L[i])
                if n!=L[i]: L[i]=n; changed['tag-lines']+=1
            h=render([text(b)])[0]
        e=ems(h)
        if e:
            noesc=ems(render(['\n'.join(esc_us(L[i][min(len(L[j])-len(L[j].lstrip()) for j in b):]) for i in b)])[0])
            if noesc<e:
                for i in b:   # escape line by line until the _-emphasis is gone
                    if '_' not in map_unprot(L[i],lambda s:s if '_' in s else ''): continue
                    L[i]=esc_us(L[i]); changed['us-lines']+=1
                    if ems(render([text(b)])[0])<=noesc: break
    if changed:
        print(dict(changed),f); tot+=changed
        if apply: open(f,'w',encoding='utf-8',newline='').write(nl.join(L))
print(dict(tot))
for h in heads: print('HEADING',*h)
