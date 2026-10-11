"""Check that the code the spec names (weko_xxx.module.Class.method, invenio_xxx.module.func) exists in a weko ref.

usage: python3 check_code_refs.py <weko clone> [<ref>]     (default ref: origin/release_v2.1.0)
For every "weko_.../invenio_..." dotted name in docs/spec/**/*.md, reports the name when the module is in
modules/ but does not define (def / class / assignment / import) the next part, or the class has no such method.
Not checked: packages outside modules/ (invenio_db...), "xxx.config.py"-style file names (reported; ignore them),
methods a class inherits (flask-admin's create_view, action_delete: reported; check the base class).
"""
import re, subprocess, sys, collections

def main(clone, ref):
    git = lambda *a: subprocess.run(['git', '-C', clone, *a], capture_output=True, text=True).stdout
    mods = {}
    for p in git('ls-tree', '-r', '--name-only', ref).split('\n'):
        if p.startswith('modules/') and p.endswith('.py') and '/tests/' not in p:
            d = '.'.join(p.split('/')[2:])[:-3]
            mods[d[:-9] if d.endswith('.__init__') else d] = p
    src, names = {}, {}
    def defs(p):
        if p not in names:
            s = src[p] = git('show', f'{ref}:{p}'); n = set()
            for m in re.finditer(r'^\s*(?:async\s+)?(?:def|class)\s+(\w+)|^(\w+)\s*=', s, re.M): n.add(m[1] or m[2])
            for m in re.finditer(r'^from\s+\S+\s+import\s+\(?([\w\s,]+)\)?', s, re.M): n.update(x for x in re.split(r'[\s,]+', m[1]) if x)
            n.update(re.findall(r'import\s+\w+\s+as\s+(\w+)', s)); names[p] = n
        return names[p]
    files = [f for f in subprocess.run(['git', 'ls-files', '-z', 'docs/spec/*.md'], capture_output=True,
                                       text=True).stdout.split('\0') if f]
    bad = collections.defaultdict(list)
    for f in files:
        for i, l in enumerate(open(f, encoding='utf-8').read().split('\n'), 1):
            for m in re.finditer(r'(?<![A-Za-z0-9_])((?:weko|invenio)_[a-z_]+(?:\.[a-z_][a-z0-9_]*)*)\.([A-Za-z_][A-Za-z0-9_]*)(?:\.([A-Za-z_][A-Za-z0-9_]*))?',
                                 l.replace('\\_', '_')):
                mod, name, attr = m[1], m[2], m[3]
                if f'{mod}.{name}' in mods:
                    if attr and attr not in defs(mods[f'{mod}.{name}']) and f'{mod}.{name}.{attr}' not in mods:
                        bad[f'{mod}.{name}.{attr}'].append(f'{f}:{i}')
                    continue
                if mod not in mods: continue
                if name not in defs(mods[mod]):
                    bad[f'{mod}.{name}'].append(f'{f}:{i}')
                elif attr and name[0].isupper():
                    c = re.search(r'^class\s+' + name + r'\b.*?(?=^class\s|\Z)', src[mods[mod]], re.M | re.S)
                    if c and not re.search(r'(?:def\s+|^\s+)' + attr + r'(?![A-Za-z0-9_])', c[0], re.M):
                        bad[f'{mod}.{name}.{attr}'].append(f'{f}:{i}')
    for k, v in sorted(bad.items()): print(k, ', '.join(v[:3]))
    print(f'{len(bad)} names')
    sys.exit(1 if bad else 0)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else 'origin/release_v2.1.0')
