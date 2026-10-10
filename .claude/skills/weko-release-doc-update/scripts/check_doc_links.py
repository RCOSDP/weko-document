"""Check links that build_docs.sh does not: relative links in docs outside the honkit books, and external URLs.

usage: python3 check_doc_links.py [--external]
  relative  docs/operation, docs/develop, docs/howto ... (no book.json, read on GitHub): MISSING file, ANCHOR not a
            heading (GitHub slug) or id. A link without "https://" (github.com/...) is a relative link and is MISSING.
  external  (--external) every http(s) URL in docs/**/*.md outside code, fetched with HEAD/GET. 401/403 (login, bots)
            and placeholders (FQDN, {host}, example.) are expected; 404 and connection errors need a look: find the
            page's new address, or link an Internet Archive copy (https://archive.org/wayback/available?url=...).
"""
import re, sys, os, ssl, subprocess, collections, urllib.parse, urllib.request, concurrent.futures

FILES = [f for f in subprocess.run(['git', 'ls-files', '-z', 'docs'], capture_output=True, text=True).stdout.split('\0')
         if f.endswith('.md')]
TRACKED = set(subprocess.run(['git', 'ls-files', '-z'], capture_output=True, text=True).stdout.split('\0'))
BOOKS = ('docs/spec/', 'docs/manuals/', 'docs/manuals_en/')  # checked by build_docs.sh

def strip_code(s): return re.sub(r'`[^`]*`', '', re.sub(r'```.*?```', '', s, flags=re.S))

def anchors(f, cache={}):
    if f not in cache:
        s = re.sub(r'```.*?```', '', open(f, encoding='utf-8', errors='replace').read(), flags=re.S); seen = {}; out = set()
        for h in re.findall(r'^#{1,6}\s+(.*?)\s*#*\s*$', s, re.M):
            b = re.sub(r'[^\w\- ]', '', re.sub(r'<[^>]+>', '', h).strip().lower()).replace(' ', '-')
            n = seen.get(b, 0); out.add(b if n == 0 else f'{b}-{n}'); seen[b] = n + 1
        cache[f] = out | set(re.findall(r'(?:id|name)="([^"]+)"', s))
    return cache[f]

def relative():
    bad = 0
    for f in FILES:
        if f.startswith(BOOKS): continue
        for m in re.finditer(r'!?\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+"[^"]*")?\)|(?:src|href)="([^"]+)"',
                             strip_code(open(f, encoding='utf-8', errors='replace').read())):
            u = m[1] or m[2]
            if re.match(r'(https?|mailto|ftp):|#$', u): continue
            path, _, frag = u.partition('#'); path = urllib.parse.unquote(path)
            tgt = os.path.normpath(os.path.join(os.path.dirname(f), path)) if path else f
            if path and tgt not in TRACKED and not any(t.startswith(tgt + '/') for t in TRACKED):
                bad += 1; print('MISSING', f, u)
            elif frag and tgt.endswith('.md') and urllib.parse.unquote(frag).lower() not in anchors(tgt):
                bad += 1; print('ANCHOR', f, u)
    return bad

def external():
    where = collections.defaultdict(list)
    for f in FILES:
        for i, l in enumerate(strip_code(open(f, encoding='utf-8', errors='replace').read()).split('\n'), 1):
            for u in re.findall(r'https?://[^\s)<>\]"\'`）」、。|]+', l):
                u = u.rstrip('.,;:*')
                if not re.search(r'localhost|FQDN|example\.|\{|\[|192\.168|127\.0|xxx|RCOSDP/weko/(blob|tree)', u, re.I):
                    where[u].append(f'{f}:{i}')
    ctx = ssl.create_default_context()
    def status(u):
        for meth in ('HEAD', 'GET'):
            try:
                return urllib.request.urlopen(urllib.request.Request(u, method=meth, headers={'User-Agent': 'Mozilla/5.0'}),
                                              timeout=20, context=ctx).status
            except urllib.error.HTTPError as e:
                if meth == 'GET' or e.code not in (400, 403, 405, 501): return e.code
            except Exception as e:
                if meth == 'GET': return type(e).__name__
    with concurrent.futures.ThreadPoolExecutor(16) as ex:
        res = dict(zip(where, ex.map(status, where)))
    bad = 0
    for u, c in sorted(res.items(), key=lambda x: str(x[1])):
        if c not in (200, 401, 403):
            bad += 1; print(c, u, where[u][0], f'({len(where[u])})')
    print(f'{len(res)} external URLs')
    return bad

if __name__ == '__main__':
    n = relative() + (external() if '--external' in sys.argv else 0)
    print(f'{n} problems'); sys.exit(1 if n else 0)
