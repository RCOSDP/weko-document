"""Check links to the weko source (https://github.com/RCOSDP/weko/blob/<ref>/<path>#L<a>-L<b>) against a local clone.

usage: python3 check_code_links.py <weko clone> [<md>...]      (default: every docs/**/*.md in git)
Reports NOREF (the branch/tag does not exist, e.g. v1.1.0 or 0.9.22 without "v"), NOPATH (no such file at that ref)
and MISMATCH (a "設定キー：X" within 3 lines of the link, or a key X named in the 2 lines above it that the
linked file defines as "X = ...", is not in the linked lines). Run `git fetch --tags` first.
"""
import re, subprocess, sys

def main(clone, files):
    git = lambda *a: subprocess.run(['git', '-C', clone, *a], capture_output=True, text=True)
    refs = {}
    def resolve(ref):
        if ref not in refs:
            refs[ref] = next((r for r in (ref, 'origin/' + ref, 'refs/tags/' + ref)
                              if git('rev-parse', '-q', '--verify', r + '^{commit}').returncode == 0), None)
        return refs[ref]
    bad = tot = 0
    for f in files:
        L = open(f, encoding='utf-8', errors='replace').read().split('\n')
        for i, l in enumerate(L):
            for m in re.finditer(r'https://github\.com/RCOSDP/weko/(?:blob|tree)/([^\s)>\]`]+?)/((?:modules|nginx|scripts)/'
                                 r'[^\s)#>\]`]+)(?:#L(\d+)(?:-L(\d+))?)?', l):
                tot += 1; r = resolve(m[1])
                if not r:
                    bad += 1; print(f'NOREF {f}:{i + 1} {m[1]}'); continue
                if git('cat-file', '-e', f'{r}:{m[2]}').returncode:
                    bad += 1; print(f'NOPATH {f}:{i + 1} {m[1]} {m[2]}'); continue
                if not m[3]: continue
                a, b = int(m[3]), int(m[4] or m[3]); src = git('show', f'{r}:{m[2]}').stdout.split('\n')
                keys = [k for j in range(max(0, i - 3), min(i + 4, len(L)))
                        for k in re.findall(r'設定キー[:：]\s*`?([A-Z][A-Z0-9_]+)', L[j])]
                # a key named in the 2 lines above the link ("- WEKO_X" / "パス：") that the linked file defines
                keys += [k for k in set(re.findall(r'\b([A-Z][A-Z0-9]*_[A-Z0-9_]{3,})\b', ' '.join(L[max(0, i - 2):i + 1]).replace('\\_', '_')))
                         if any(re.match(k + r'\s*=', x) for x in src)]
                if not keys: continue
                if not any(k in x for k in keys for x in src[a - 1:b]):
                    bad += 1; print(f'MISMATCH {f}:{i + 1} {m[1]} L{a}-L{b} {keys}')
    print(f'{bad} problems in {tot} links')
    sys.exit(1 if bad else 0)

if __name__ == '__main__':
    files = sys.argv[2:] or [f for f in subprocess.run(['git', 'ls-files', '-z', 'docs'], capture_output=True,
                                                         text=True).stdout.split('\0') if f.endswith('.md')]
    main(sys.argv[1], files)
