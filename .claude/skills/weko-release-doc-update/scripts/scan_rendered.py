r"""Find markdown that honkit did not render, in the visible text of the built HTML.

usage: python3 scan_rendered.py <html dir>...   (e.g. docs/build/admin/html)
Reports, per page:
  esc        backslash escapes shown as text (\< \_ \[ ...; \| in a table cell: write &#124;)
  backslash  a "\" left before a tag, a line end or a cell end: "\<name>" (honkit makes <name> a hidden HTML tag:
             write &lt;name&gt;), a "\" line break (write <br>), "\|" that split a cell (write &#124;)
  tag        "<name>" placeholders that honkit emitted as unknown HTML tags, hidden in the browser
             (GET /api/<version>/records shows "GET /api//records"): write &lt;name&gt; (fix_inline.py).
             Headings are skipped (changing them changes their anchors)
  underscore "_" made into emphasis inside a word (release_v2.1.0 -> release<em>v2.1.0...): write \_ (fix_inline.py)
  code-esc   \_ or &lt; shown as text in a code block (an escape added to a line that is in an indented code block)
  md image   ![..](..) shown as text           md link   [..](#..) shown as text
  pipe table | --- | shown as text (a table right after a paragraph line, or inside a list item:
             fix_tables.py)
  comment    <!-- shown as text (a comment that starts in the middle of a paragraph)
  fence      ``` shown as text (a fence right after a list item line, or two blank lines inside a
             fence in a list: add a blank line before it / keep one blank line)
  word       Word remnants: INDEXWORD, LINKID, ANCHORID, TBLATT, *.tif, auto-generated alt text
  code-prose paragraphs/images rendered as a code block without a language (indented text after a
             "1)" list, a table or an image that ended the list, or two blank lines in a list)
Fenced code (with a language) and <code> are not checked. The GUIDE's mermaid arrows (-->) are not comments.
"""
import re, sys, glob, html
KNOWN = set('''html head body title meta link script style div span p a img br hr h1 h2 h3 h4 h5 h6 ul ol li table thead
tbody tfoot tr th td caption colgroup col pre code em strong b i u s del ins sup sub blockquote dl dt dd nav header footer
section article aside main figure figcaption small big font center label input button form select option textarea iframe
svg path g rect circle line polyline polygon text defs use tt kbd var samp abbr cite q mark details summary wbr noscript
video source audio picture time object embed param map area rt ruby rp bdi bdo dfn address strike nobr'''.split())
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

PATS = {'esc': r'\\[<>_*\[\]#&|]', 'md image': r'!\[[^\]]*\]\([^)]*\)', 'md link': r'\]\([#./][^)]*\)',
        'pipe table': r'\|\s*:?-{3,}:?\s*\|', 'comment': r'<!--', 'fence': r'```',
        'word': r'INDEXWORD|LINKID=|ANCHORID=|TBLATT|\w\.tif\b|自動的に生成された説明'}
PROSE = re.compile(r'!\[[^\]]*\]\(|[ぁ-んァ-ン一-龥]{6,}|\b(?:Click|Select|The|appears)\b')
CODEISH = re.compile(r'\s*(?:[\[{"$<]|curl|WEKO_|metadata\.|xxxxx|-{5}|Dear |This is a message|.{0,60}\[restricted_)', re.S)  # mail templates

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
            body = re.sub(r'<(pre|code)\b.*?</\1>', '', src, flags=re.S)
            ms = list(re.finditer(r'(?<!\\)\\(?:<(?!br\b)[A-Za-z]|\r?\n|</t[dh]>)', body))
            if ms:
                found += len(ms); m = ms[0]
                print(f'{root} {rel}: backslash x{len(ms)} | {body[max(0, m.start() - 40):m.end() + 30]!r}')
            nocode = re.sub(r'<h([1-6])\b.*?</h\1>', '', body, flags=re.S)
            for k, pt in (('tag', r'</?([A-Za-z][^\s>/]*)'), ('underscore', r'[A-Za-z0-9]<em>|</em>[A-Za-z0-9]')):
                ms = [m for m in re.finditer(pt, nocode) if k != 'tag' or m[1].lower() not in KNOWN]
                if ms:
                    found += len(ms); m = ms[0]
                    print(f'{root} {rel}: {k} x{len(ms)} | {nocode[max(0, m.start() - 40):m.end() + 30]!r}')
            ms = [m for b in re.findall(r'<pre\b.*?</pre>', src, re.S) for m in re.finditer(r'\\_|&amp;lt;', b)]
            if ms:
                found += len(ms); print(f'{root} {rel}: code-esc x{len(ms)}')
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
