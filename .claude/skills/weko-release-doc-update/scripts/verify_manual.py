"""Pre-commit checks for manuals / specs edited in a release-doc update.

usage (from the weko-document root):
  python3 verify_manual.py [--tag 【v2.1.0】] [--tag-only] <file>...
Checks, against HEAD:
  - no existing heading text was changed or removed (new headings are reported)
  - count of the tag string (if --tag) and that no heading carries it
  - with --tag-only: the file equals HEAD once the tag strings are removed
  - for manuals with a TOC (## 目次 / # Table of Contents): TOC numbers are consecutive and
    every TOC link points to a heading (honkit-like or GitHub slug) or an <a id> placed in the file
"""
import re, subprocess, sys

def slug(t):
    t = t.strip().lower()
    t = re.sub(r'[^\w\- 　-鿿＀-￯]', '', t)
    return t.replace(' ', '-')

def gh_slugs(heads):
    out, seen = set(), {}
    for h in heads:
        b = re.sub(r'[^\w\- ]', '', re.sub(r'`', '', h).lower()).replace(' ', '-')
        n = seen.get(b, 0); seen[b] = n + 1
        out.add(b if n == 0 else f'{b}-{n}')
    return out

HEAD_RE = re.compile(r'^\s*(?:\d+\.\s+)?(#{1,6}) (.*)')
TOC_RE = re.compile(r'^\[(\d+(?:\.\d+)*)\.? (.*?)( \d+)?\]\((#[^)]*)\)$')

def headings(s):
    return [m.group(2).strip() for l in s.split('\n') for m in [HEAD_RE.match(l)] if m]

def main(argv):
    tags, tag_only, files = [], False, []
    it = iter(argv)
    for a in it:
        if a == '--tag': tags.append(next(it))
        elif a == '--tag-only': tag_only = True
        else: files.append(a)
    ok = True
    for f in files:
        old = subprocess.run(['git', 'show', 'HEAD:' + f], capture_output=True).stdout.decode('utf-8', 'replace')
        new = open(f, encoding='utf-8', newline='').read()
        ho, hn = headings(old), headings(new)
        removed = [h for h in ho if h not in hn]
        added = [h for h in hn if h not in ho]
        msg = [f'{f}:', f'headings removed/renamed={len(removed)}', f'added={len(added)}']
        if removed: ok = False
        for t in tags:
            msg.append(f'{t} {old.count(t)}->{new.count(t)}')
            th = [l for l in new.split('\n') if HEAD_RE.match(l) and t in l]
            if th: ok = False; msg.append(f'TAG IN HEADINGS={len(th)}')
        if tag_only:
            stripped = new
            for t in tags: stripped = stripped.replace(t + ' ', '').replace(t, '')
            same = stripped == old
            msg.append(f'only-tags-changed={same}')
            ok &= same
        L = new.replace('\r', '').split('\n')
        toc = [m.groups() for l in L for m in [TOC_RE.match(l)] if m]
        if toc:
            slugs = {slug(h) for h in hn} | gh_slugs(hn) | set(re.findall(r'<a id="([^"]+)"', new))
            bad_link = [t[0] for t in toc if t[3][1:] not in slugs]
            prev, breaks = None, []
            for t in toc:
                cur = tuple(int(x) for x in t[0].split('.'))
                if prev:
                    good = (len(cur) == len(prev) and cur[:-1] == prev[:-1] and cur[-1] == prev[-1] + 1) or \
                           (len(cur) == len(prev) + 1 and cur[:-1] == prev and cur[-1] == 1) or \
                           (len(cur) < len(prev) and cur[:-1] == prev[:len(cur) - 1] and cur[-1] == prev[len(cur) - 1] + 1)
                    if not good: breaks.append(f'{".".join(map(str, prev))}->{t[0]}')
                prev = cur
            msg.append(f'toc={len(toc)} breaks={breaks or 0} unresolved-new-links={bad_link or 0}')
            ok &= not breaks and not bad_link
        print('  '.join(msg))
        for h in removed: print('   REMOVED/RENAMED:', h)
    sys.exit(0 if ok else 1)

if __name__ == '__main__':
    main(sys.argv[1:])
