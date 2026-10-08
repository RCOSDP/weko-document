r"""Make pipe tables render in honkit: add a blank line before a table that follows a paragraph line,
and convert a table inside a list item to an HTML table (honkit does not render pipe tables in list items).
usage: python3 fix_tables.py <md file>... [--apply]   (without --apply, only prints the counts)
A list item whose continuation line is not indented ("- URL" / "/api/..." ) is not recognized: indent it first.
Cells are converted to HTML (code, links, images, **bold**, backslash escapes), since markdown is not
processed inside an HTML block. Keeps CRLF."""
import re,sys,html
SEP=re.compile(r'^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$')
LIST=re.compile(r'^(\s*)([-*+]|\d+[.)])\s+')
def cells(row):
    row=row.strip()
    if row.startswith('|'): row=row[1:]
    if row.endswith('|') and not row.endswith('\\|'): row=row[:-1]
    out=[];cur='';i=0;code=False
    while i<len(row):
        c=row[i]
        if c=='\\' and i+1<len(row) and row[i+1]=='|': cur+='|'; i+=2; continue
        if c=='`': code=not code
        if c=='|' and not code: out.append(cur); cur=''
        else: cur+=c
        i+=1
    out.append(cur); return [x.strip() for x in out]
def inline(t):
    keep=[]
    def k(s): keep.append(s); return f'\x00{len(keep)-1}\x00'
    t=re.sub(r'`([^`]+)`',lambda m:k('<code>'+html.escape(m.group(1),quote=False)+'</code>'),t)
    t=re.sub(r'!\[([^\]]*)\]\(([^)\s]+)\)',lambda m:k(f'<img src="{m.group(2)}" alt="{html.escape(m.group(1))}" />'),t)
    t=re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)',lambda m:k(f'<a href="{m.group(2)}">')+m.group(1)+k('</a>'),t)
    t=re.sub(r'\*\*(.+?)\*\*',lambda m:k('<strong>')+m.group(1)+k('</strong>'),t)
    t=re.sub(r'\\([\\`*_{}\[\]()#+\-.!<>~"|])',lambda m:k(html.escape(m.group(1))),t)
    t=re.sub(r'<(/?[a-zA-Z][^<>]*)>',lambda m:k(m.group(0)),t)   # keep inline html (<br> etc.)
    t=html.escape(t,quote=False)
    return re.sub('\x00(\\d+)\x00',lambda m:keep[int(m.group(1))],t)
def in_list(L,i,ind):
    for j in range(i-1,-1,-1):
        l=L[j]
        if not l.strip(): continue
        li=len(l)-len(l.lstrip())
        if li<ind:
            return bool(LIST.match(l))
    return False
def fix(p,apply):
    with open(p,encoding='utf-8',newline='') as fp: s=fp.read()
    nl='\r\n' if '\r\n' in s else '\n'
    L=s.split(nl); out=[]; i=0; fence=False; conv=blank=0
    while i<len(L):
        l=L[i]
        if l.lstrip().startswith('```'): fence=not fence
        if not fence and i+1<len(L) and '|' in l and SEP.match(L[i+1]) and '|' in L[i+1]:
            ind=len(l)-len(l.lstrip()); pre=l[:ind]
            j=i+2
            while j<len(L) and L[j].strip().startswith('|') or (j<len(L) and '|' in L[j] and L[j].strip() and not L[j].strip().startswith(('>','#')) and len(L[j])-len(L[j].lstrip())>=ind and L[j].count('|')>=2): j+=1
            rows=L[i:j]
            if in_list(L,i,ind):
                if out and out[-1].strip(): out.append('')
                hdr=cells(rows[0]); body=[cells(r) for r in rows[2:]]
                h=[pre+'<table>',pre+'<thead>',pre+'<tr>']+[pre+f'<th>{inline(c)}</th>' for c in hdr]+[pre+'</tr>',pre+'</thead>',pre+'<tbody>']
                for r in body: h+= [pre+'<tr>']+[pre+f'<td>{inline(c)}</td>' for c in r]+[pre+'</tr>']
                h+=[pre+'</tbody>',pre+'</table>']
                out+=h; conv+=1
                if j<len(L) and L[j].strip(): out.append('')
                i=j; continue
            if out and out[-1].strip() and not out[-1].strip().startswith('|') and ind<4:
                out.append(''); blank+=1
        out.append(l); i+=1
    print(p,'converted',conv,'blank added',blank)
    if apply:
        with open(p,'w',encoding='utf-8',newline='') as fp: fp.write(nl.join(out))
args=[a for a in sys.argv[1:] if a!='--apply']
for p in args: fix(p,'--apply' in sys.argv)
