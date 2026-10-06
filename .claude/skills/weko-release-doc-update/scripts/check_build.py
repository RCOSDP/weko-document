"""Check honkit HTML output for broken internal links, missing anchors and missing images.

usage: python3 check_build.py <html dir> [--baseline <html dir>] [--log <honkit log>] [--max 20] [--strict]
  <html dir>:  e.g. docs/build/admin/html
  --baseline:  the same book built from the base ref (e.g. main or the previous release).
               Issues that also exist there are counted as "existing" and do not fail the check.
Kinds:
  PAGE    link to a page of the book that does not exist
  ANCHOR  #anchor that does not exist in the target page (broken in honkit and on GitHub)
  SLUG    GitHub-style anchor of the heading text (punctuation removed, duplicates -1, -2 ...)
          that works on GitHub but not in honkit (honkit keeps full-width punctuation, drops "_"
          and does not number duplicates).
          Reported, but does not fail the check unless --strict.
  IMAGE   <img src> whose file does not exist
With --log, also reports whether honkit finished and its warn/error lines.
External links (http/https/mailto) and unparsable URLs (e.g. https://[host]/) are not checked.
Exit code 1 if a new PAGE/ANCHOR/IMAGE (or SLUG with --strict) is found or honkit did not finish.
"""
import os, re, sys, html
from urllib.parse import unquote, urlparse

ANSI = re.compile(r'\x1b\[[0-9;]*m')


def gh_slugs(heading_ids):
    """GitHub-style anchors for the headings of a page (in order)."""
    out, seen = set(), {}
    for h in heading_ids:
        b = re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-')
        n = seen.get(b, 0)
        seen[b] = n + 1
        out.add(b if n == 0 else f'{b}-{n}')
    return out


def collect(root):
    """Return (number of pages, set of (kind, page relative to root, href))."""
    pages = {}
    for d, _, fs in os.walk(root):
        if os.sep + 'gitbook' in d:
            continue
        for f in fs:
            if f.endswith('.html'):
                p = os.path.normpath(os.path.join(d, f))
                pages[p] = open(p, encoding='utf-8', errors='replace').read()
    ids = {p: set(re.findall(r'\sid="([^"]+)"', s)) for p, s in pages.items()}
    slugs = {p: gh_slugs(html.unescape(re.sub(r'<[^>]+>', '', t)).strip()
                         for t in re.findall(r'<h([1-6])[^>]*>(.*?)</h\1>', s, re.S) for t in [t[1]])
             for p, s in pages.items()}
    issues = set()
    for p, s in pages.items():  # whole page, including the sidebar summary links
        rel = os.path.relpath(p, root)
        for href in re.findall(r'<a\s[^>]*href="([^"]+)"', s):
            href = html.unescape(href)
            try:
                u = urlparse(href)
            except ValueError:
                continue
            if u.scheme or href.startswith('//'):
                continue
            target = p if not u.path else os.path.normpath(os.path.join(os.path.dirname(p), unquote(u.path)))
            if os.path.isdir(target):
                target = os.path.join(target, 'index.html')
            if target.endswith('.md'):
                target = target[:-3] + '.html'
            if target not in pages:
                if not os.path.exists(target):
                    issues.add(('PAGE', rel, href))
                continue
            frag = unquote(u.fragment)
            if frag and frag not in ids[target]:
                issues.add(('SLUG' if frag in slugs[target] else 'ANCHOR', rel, href))
        for src in re.findall(r'<img\s[^>]*src="([^"]+)"', s):
            src = html.unescape(src)
            if '://' in src or src.startswith('data:') or src.startswith('//'):
                continue
            if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(p), unquote(src.split('?')[0])))):
                issues.add(('IMAGE', rel, src))
    return len(pages), issues


def main(a):
    root = a[0]
    opt = lambda k, d=None: a[a.index(k) + 1] if k in a else d
    base, log, mx, strict = opt('--baseline'), opt('--log'), int(opt('--max', 20)), '--strict' in a
    kinds = ('PAGE', 'ANCHOR', 'SLUG', 'IMAGE')
    n, issues = collect(root)
    old = collect(base)[1] if base else set()
    new = sorted(issues - old)
    print(f'{root}: pages={n}' + (f' (baseline {base})' if base else ''))
    for k in kinds:
        print(f'  {k}: new={sum(i[0] == k for i in new)} existing={sum(i[0] == k for i in issues & old)}')
    for k in kinds:
        lst = [i for i in new if i[0] == k]
        for _, p, h in lst[:mx]:
            print(f'  {k}: {p} -> {h}')
        if len(lst) > mx:
            print(f'  {k}: ... ({len(lst) - mx} more)')
    if base:
        fixed = old - issues
        if fixed:
            print(f'  fixed since baseline: {len(fixed)}')
    finished = True
    if log and os.path.exists(log):
        lines = [ANSI.sub('', l).rstrip() for l in open(log, encoding='utf-8', errors='replace')]
        finished = any('generation finished with success' in l for l in lines)
        msgs = sorted({l.strip() for l in lines if re.match(r'\s*(warn|error):', l, re.I) or 'Error:' in l})
        print(f'  log: {"finished" if finished else "NOT FINISHED"}, distinct warn/error lines: {len(msgs)}')
        for l in msgs[:mx]:
            print('   ', l[:200])
    failed = any(i[0] != 'SLUG' or strict for i in new) or not finished
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main(sys.argv[1:])
