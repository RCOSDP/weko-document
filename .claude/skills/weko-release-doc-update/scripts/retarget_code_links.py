"""Point links to the weko source at another ref, moving their line numbers (#L<a>-L<b>) to the same code there.

usage: python3 retarget_code_links.py <weko clone> <old ref> <new ref> [--apply] [<md>...]
       e.g. retarget_code_links.py ~/weko v0.9.22 release_v2.1.0     (default: every docs/**/*.md in git)
The new lines are found, in this order:
  key   a "設定キー：X" (or `X` on the link line) within 3 lines whose definition "X = ..." is in the old lines:
        the definition of X in the new file (up to the line before the next top-level statement or docstring)
  text  the old lines (stripped, blank lines ignored) found once in the new file
  ends  the first old line found once in the new file, and the last old line after it
  func  an old range that is a whole def/class: the whole def/class of the same name in the new file
Links whose path is gone, or whose lines cannot be found, are reported and left as they are (KEEP).
Without --apply only the report is printed. Run check_code_links.py afterwards.
"""
import re, subprocess, sys

LINK = re.compile(r'https://github\.com/RCOSDP/weko/(blob|tree)/{}/([^\s)#>\]`]+)(?:#L(\d+)(?:-L(\d+))?)?')

def main(clone, old, new, apply, files):
    git = lambda *a: subprocess.run(['git', '-C', clone, *a], capture_output=True, text=True)
    ref = lambda r: next(x for x in (r, 'origin/' + r, 'refs/tags/' + r)
                         if git('rev-parse', '-q', '--verify', x + '^{commit}').returncode == 0)
    ro, rn = ref(old), ref(new); cache = {}
    def src(r, p):
        if (r, p) not in cache:
            g = git('show', f'{r}:{p}'); cache[r, p] = g.stdout.split('\n') if g.returncode == 0 else None
        return cache[r, p]
    def exists(p):
        return git('cat-file', '-e', f'{rn}:{p}').returncode == 0
    def defn(lines, key):
        s = next((i for i, x in enumerate(lines) if re.match(key + r'\s*=', x)), None)
        if s is None: return None
        e = s
        for j in range(s + 1, len(lines)):
            x = lines[j]
            if x.strip() == '' or x.startswith((' ', '\t', ')', ']', '}')): e = j if x.strip() else e; continue
            break
        return s + 1, e + 1
    def find(lines, block):
        blk = [x.strip() for x in block if x.strip()]
        if not blk: return None
        st = [(i, x.strip()) for i, x in enumerate(lines) if x.strip()]
        hits = [k for k in range(len(st) - len(blk) + 1) if [x for _, x in st[k:k + len(blk)]] == blk]
        return (st[hits[0]][0] + 1, st[hits[0] + len(blk) - 1][0] + 1) if len(hits) == 1 else None
    def ends(lines, block):
        blk = [x for x in block if x.strip()]
        if len(blk) < 2: return None
        s = [i for i, x in enumerate(lines) if x.rstrip() == blk[0].rstrip()]
        if len(s) != 1: return None
        lim = s[0] + 3 * len(block) + 20
        e = next((i for i in range(s[0] + 1, min(lim, len(lines))) if lines[i].rstrip() == blk[-1].rstrip()), None)
        return (s[0] + 1, e + 1) if e is not None else None
    def extent(lines, i):
        ind = len(lines[i]) - len(lines[i].lstrip()); e = i
        for j in range(i + 1, len(lines)):
            if lines[j].strip() and len(lines[j]) - len(lines[j].lstrip()) <= ind and not lines[j].lstrip().startswith((')', ']', '}')): break
            if lines[j].strip(): e = j
        return e
    def func(o, n, a, b):
        h = next((x for x in o[a - 1:b] if x.strip()), '')
        if not re.match(r'\s*(?:async\s+)?(?:def|class)\s+\w+', h): return None
        if extent(o, a - 1 + o[a - 1:b].index(h)) + 1 > b + 2: return None   # only when the old range was the whole def
        s = [i for i, x in enumerate(n) if x.rstrip() == h.rstrip()]
        if len(s) != 1:
            name = re.match(r'\s*(?:async\s+)?(?:def|class)\s+(\w+)', h)[1]
            s = [i for i, x in enumerate(n) if re.match(r'\s*(?:async\s+)?(?:def|class)\s+' + name + r'\b', x)]
        return (s[0] + 1, extent(n, s[0]) + 1) if len(s) == 1 else None
    pat = re.compile(LINK.pattern.format(re.escape(old)))
    tot = moved = kept = 0
    for f in files:
        text = open(f, encoding='utf-8', newline='').read()
        L = text.split('\n'); out = []
        for i, l in enumerate(L):
            keys = [k for j in range(max(0, i - 3), min(i + 4, len(L)))
                    for k in re.findall(r'設定キー[:：]\s*`?([A-Z][A-Z0-9_]+)', L[j])] + re.findall(r'`([A-Z][A-Z0-9_]{3,})', l)
            def rep(m):
                nonlocal tot, moved, kept
                tot += 1; kind, path, a = m[1], m[2], m[3]
                if not exists(path.rstrip('/')):
                    kept += 1; print(f'KEEP {f}:{i + 1} no {path} at {new}'); return m[0]
                base = f'https://github.com/RCOSDP/weko/{kind}/{new}/{path}'
                if not a: moved += 1; return base
                a, b = int(a), int(m[4] or a); o, n = src(ro, path), src(rn, path)
                how = r = None
                for k in keys:
                    d = defn(o, k)
                    if d and a <= d[0] <= b and (r := defn(n, k)): how = 'key'; break
                if not r and (r := find(n, o[a - 1:b])): how = 'text'
                if not r and (r := ends(n, o[a - 1:b])): how = 'ends'
                if not r and (r := func(o, n, a, b)): how = 'func'
                if not r:
                    kept += 1; print(f'KEEP {f}:{i + 1} {path}#L{a}-L{b}: lines not found at {new}'); return m[0]
                moved += 1
                anchor = f'#L{r[0]}' + (f'-L{r[1]}' if m[4] or r[1] != r[0] else '')
                if (r[0], r[1]) != (a, b): print(f'{how:4} {f}:{i + 1} {path.split("/")[-1]} L{a}-L{b} -> {anchor[1:]}')
                return base + anchor
            out.append(pat.sub(rep, l))
        if apply and out != L:
            open(f, 'w', encoding='utf-8', newline='').write('\n'.join(out))
    print(f'{moved} moved, {kept} kept, of {tot} links' + ('' if apply else ' (dry run: add --apply)'))

if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if x != '--apply']
    files = a[3:] or [f for f in subprocess.run(['git', 'ls-files', '-z', 'docs'], capture_output=True,
                                                  text=True).stdout.split('\0') if f.endswith('.md')]
    main(a[0], a[1], a[2], '--apply' in sys.argv, files)
