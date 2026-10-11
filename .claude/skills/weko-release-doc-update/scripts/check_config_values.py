"""Compare the "現在の設定値" of the spec with the config.py of a weko ref.

usage: python3 check_config_values.py <weko clone> [<ref>] [<md>...]   (default ref: origin/release_v2.1.0,
                                                                        default md: docs/spec/**/*.md in git)
Reads every "設定キー：X" followed within 3 lines by "現在の設定値" and the value, either inline
(`X = ...`) or in the next code block, and compares it with "X = ..." in modules/*/*/config.py at <ref>
(comments, _() and quote style ignored). Reports keys whose value differs and keys that are not defined.
"""
import re, subprocess, sys

def main(clone, ref, files):
    git = lambda *a: subprocess.run(['git', '-C', clone, *a], capture_output=True, text=True).stdout
    cfgs = [p for p in git('ls-tree', '-r', '--name-only', ref).split('\n') if re.search(r'^modules/[^/]+/[^/]+/config\.py$', p)]
    src = {p: git('show', f'{ref}:{p}') for p in cfgs}
    def defn(key):
        for s in src.values():
            m = re.search(r'^' + key + r'\s*=\s*(.*?)(?=^\S|\Z)', s, re.M | re.S)
            if m: return m[1]
    def norm(v):
        v = re.sub(r'#[^\n]*', '', v); v = re.sub(r'_\(\s*("[^"]*"|\'[^\']*\')\s*\)', r'\1', v)
        return re.sub(r'\s+', '', v.replace("'", '"')).strip('()[]{},\\')
    bad = 0
    for f in files:
        L = open(f, encoding='utf-8').read().split('\n')
        for i, l in enumerate(L):
            m = re.search(r'設定キー\s*[：:]\s*`?([A-Z][A-Z0-9_]+)`?\s*$', l.strip())
            j = next((j for j in range(i + 1, min(i + 4, len(L))) if '現在の設定値' in L[j]), None)
            if not m or j is None: continue
            key = m[1]; mm = re.search('`' + key + r'\s*=\s*(.*)`', L[j])
            if mm: doc = mm[1]
            else:
                k = j + 1
                while k < len(L) and '```' not in L[k]: k += 1
                e = k + 1
                while e < len(L) and '```' not in L[e]: e += 1
                mm = re.search(key + r'\s*=\s*(.*)', '\n'.join(L[k + 1:e]), re.S)
                if not mm: continue
                doc = mm[1]
            cur = defn(key)
            if cur is None:
                bad += 1; print(f'NOKEY {f}:{i + 1} {key} is not in config.py at {ref}'); continue
            a, b = norm(doc), norm(cur)
            if a != b:
                bad += 1; n = next((n for n in range(min(len(a), len(b))) if a[n] != b[n]), min(len(a), len(b)))
                print(f'VALUE {f}:{i + 1} {key}\n  doc : ...{a[max(0, n - 40):n + 80]}\n  code: ...{b[max(0, n - 40):n + 80]}')
    print(f'{bad} problems')
    sys.exit(1 if bad else 0)

if __name__ == '__main__':
    a = sys.argv[1:]
    ref = a[1] if len(a) > 1 and not a[1].endswith('.md') else 'origin/release_v2.1.0'
    files = [x for x in a[1:] if x.endswith('.md')] or [f for f in subprocess.run(
        ['git', 'ls-files', '-z', 'docs/spec/*.md'], capture_output=True, text=True).stdout.split('\0') if f]
    main(a[0], ref, files)
