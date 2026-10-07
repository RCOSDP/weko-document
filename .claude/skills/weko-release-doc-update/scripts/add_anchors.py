r"""Make GitHub-style anchors work in honkit too, without changing the headings.

usage: add_anchors.py <book src dir> <book html dir> [--apply]
  e.g. add_anchors.py docs/spec/base docs/build/spec/html --apply   (build the book first)
Runs check_build.py on the html, and for every SLUG or ANCHOR link whose fragment is the GitHub anchor
of a heading in the markdown (works on GitHub, not in honkit) inserts <a id="<GitHub anchor>"></a> and a
blank line just before that heading. honkit differs from GitHub in punctuation, "_", duplicate numbering
and backslash-escaped "<...>" in headings (honkit treats \<word ...\> as an HTML tag).
GitHub still uses the heading's own anchor; honkit gets the id. Line endings (CRLF) are kept.
Prints, per file, how many were added and which anchors had no matching heading (fix those links by hand).
"""
import os, re, sys, json, subprocess
src, out = sys.argv[1], sys.argv[2]; apply = '--apply' in sys.argv
try:  # a one-file book (manuals_en) names its main page in book.json
    README = json.load(open(os.path.join(src, 'book.json'))).get('structure', {}).get('readme', 'README.md')
except (OSError, ValueError):
    README = 'README.md'
CHK = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'check_build.py')
res = subprocess.run(['python3', CHK, out, '--max', '100000'], capture_output=True, text=True).stdout
from urllib.parse import unquote
need = {}
for l in res.splitlines():
    m = re.match(r'  (?:SLUG|ANCHOR): (\S+) -> (.*)$', l)
    if not m: continue
    page, href = m.groups()
    path, _, frag = href.partition('#')
    tgt = os.path.normpath(os.path.join(os.path.dirname(page), unquote(path))) if path else page
    tgt = README if tgt == 'index.html' else re.sub(r'(^|/)index\.html$', r'\1README.md', tgt)
    tgt = tgt[:-5] + '.md' if tgt.endswith('.html') else tgt
    if os.path.isdir(os.path.join(src, tgt)): tgt = os.path.join(tgt, README)
    need.setdefault(tgt, set()).add(unquote(frag))
def text(h):
    codes = []
    # backslash escapes (\<, \>, \_ ...) are literal text on GitHub
    h = re.sub(r'\\([\\`*_{}\[\]()#+\-.!<>|])', lambda m: codes.append(m.group(1)) or f'\x00{len(codes)-1}\x00', h)
    h = re.sub(r'`([^`]*)`', lambda m: codes.append(m.group(1)) or f'\x00{len(codes)-1}\x00', h)
    h = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', h); h = re.sub(r'<[^>]+>', '', h)
    h = h.replace('*', '')
    return re.sub(r'\x00(\d+)\x00', lambda m: codes[int(m.group(1))], h).strip()
def slug(t): return re.sub(r'[^\w\- ]', '', t.lower()).replace(' ', '-')
total = 0
for md, frags in sorted(need.items()):
    p = os.path.join(src, md)
    raw = open(p, encoding='utf-8', newline='').read()
    nl = '\r\n' if '\r\n' in raw else '\n'
    L = raw.split(nl); seen = {}; ins = {}; fence = False
    for i, l in enumerate(L):
        if l.lstrip().startswith('```'): fence = not fence
        m = None if fence else re.match(r'^(#{1,6})\s+(.*?)\s*#*\s*$', l)
        if not m: continue
        b = slug(text(m.group(2))); n = seen.get(b, 0); seen[b] = n + 1
        s = b if n == 0 else f'{b}-{n}'
        if s in frags: ins[i] = s
    miss = frags - set(ins.values())
    for i in sorted(ins, reverse=True):
        a = f'<a id="{ins[i]}"></a>'
        if i > 0 and L[i - 1].strip() == a: continue
        L[i:i] = [a, '']; total += 1
    print(f'{md}: add={len(ins)} missing={sorted(miss)}')
    if apply: open(p, 'w', encoding='utf-8', newline='').write(nl.join(L))
print('total', total)
