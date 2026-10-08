r"""Find markdown that honkit did not render, in the visible text of the built HTML.

usage: python3 scan_rendered.py <html dir>...   (e.g. docs/build/admin/html)
Reports, per page:
  esc        backslash escapes shown as text (\< \_ \[ ...)
  md image   ![..](..) shown as text           md link   [..](#..) shown as text
  pipe table | --- | shown as text (a table right after a paragraph line, or inside a list item:
             fix_tables.py)
  comment    <!-- shown as text (a comment that starts in the middle of a paragraph)
  word       Word remnants: INDEXWORD, LINKID, ANCHORID, TBLATT, *.tif, auto-generated alt text
  code-prose paragraphs/images rendered as a code block without a language (indented text after a
             "1)" list, a table or an image that ended the list, or two blank lines in a list)
Fenced code (with a language) and <code> are not checked. The GUIDE's mermaid arrows (-->) are not comments.
"""
import re, sys, glob, html
from html.parser import HTMLParser

class Text(HTMLParser):
    def __init__(s):
        super().__init__(convert_charrefs=True); s.skip = 0; s.out = []
    def handle_starttag(s, t, a):
        if t in ('pre', 'code', 'script', 'style'): s.skip += 1
    def handle_endtag(s, t):
        if t in ('pre', 'code', 'script', 'style'): s.skip = max(0, s.skip - 1)
    def handle_data(s, d):
        if not s.skip: s.out.append(d)

PATS = {'esc': r'\\[<>_*\[\]#&]', 'md image': r'!\[[^\]]*\]\([^)]*\)', 'md link': r'\]\([#./][^)]*\)',
        'pipe table': r'\|\s*:?-{3,}:?\s*\|', 'comment': r'<!--',
        'word': r'INDEXWORD|LINKID=|ANCHORID=|TBLATT|\w\.tif\b|自動的に生成された説明'}
PROSE = re.compile(r'!\[[^\]]*\]\(|[ぁ-んァ-ン一-龥]{6,}|\b(?:Click|Select|The|appears)\b')
CODEISH = re.compile(r'\s*(?:[\[{"$<]|curl|WEKO_|metadata\.|xxxxx|-{5}|Dear |This is a message)')

def main(roots):
    found = 0
    for root in roots:
        for f in sorted(glob.glob(root + '/**/*.html', recursive=True)):
            if '/gitbook/' in f: continue
            with open(f, encoding='utf-8') as fp: src = fp.read()
            p = Text(); p.feed(src); t = re.sub(r'\s+', ' ', ' '.join(p.out))
            rel = f[len(root):].lstrip('/')
            for k, pt in PATS.items():
                ms = list(re.finditer(pt, t))
                if k == 'comment' and 'mermaid' in src: continue
                if ms:
                    found += len(ms); m = ms[0]
                    print(f'{root} {rel}: {k} x{len(ms)} | {t[max(0, m.start() - 40):m.end() + 30]}')
            if '自動的に生成された説明' in src and 'word' not in t:
                found += 1; print(f'{root} {rel}: word (alt text) x{src.count("自動的に生成された説明")}')
            for m in re.finditer(r'<pre><code(?: class="lang-\w*")?>(.*?)</code></pre>', src, re.S):
                if 'class="lang-' in m.group(0): continue
                body = html.unescape(m.group(1))
                if not CODEISH.match(body) and PROSE.search(body):
                    found += 1; print(f'{root} {rel}: code-prose | {re.sub(chr(10), " ", body)[:80]}')
    sys.exit(1 if found else 0)

if __name__ == '__main__':
    main(sys.argv[1:])
