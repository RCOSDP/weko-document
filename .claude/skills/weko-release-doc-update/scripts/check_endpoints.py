"""Find API paths in the spec ("GET /api/..." etc.) whose literal parts do not appear in any route of the weko source.

usage: python3 check_endpoints.py <weko clone> [<ref>]     (default ref: origin/release_v2.1.0)
Collects every quoted string starting with "/" in modules/**/*.py (routes, @expose, url_prefix, endpoint
settings) and the "endpoint" of flask-admin views ("items/custom_sort" -> /admin/items/custom_sort), and reports a
documented path when one of its literal segments ({x}, <x>, api, v1... ignored) is in none of them. A rough check
(a segment found in another route passes): read the route before changing the spec.
"""
import re, subprocess, sys

def main(clone, ref):
    files = [f for f in subprocess.run(['git', 'ls-files', '-z', 'docs/spec/*.md'], capture_output=True,
                                       text=True).stdout.split('\0') if f]
    docs = {}
    for f in files:
        for i, l in enumerate(open(f, encoding='utf-8').read().split('\n'), 1):
            for m in re.finditer(r'\b(GET|POST|PUT|DELETE|PATCH|HEAD)\s+`?(/[A-Za-z0-9_\-/<>{}:.]+)', l):
                docs.setdefault(m[2], []).append(f'{f}:{i}')
    code = subprocess.run(['git', '-C', clone, 'grep', '-hoE', r"""['"]/[A-Za-z0-9_/<>:.-]*['"]""", ref, '--',
                           'modules/*.py', ':!*/tests/*'], capture_output=True, text=True).stdout
    # flask-admin views take their URL from "endpoint" ("items/custom_sort" -> /admin/items/custom_sort)
    ends = subprocess.run(['git', '-C', clone, 'grep', '-hoE', r"""endpoint['"]?\s*[:=]\s*['"][A-Za-z0-9_/.-]+['"]""", ref,
                           '--', 'modules/*.py', ':!*/tests/*'], capture_output=True, text=True).stdout
    routes = [r.strip('\'"') for r in code.split('\n')] + [re.sub(r'^.*?[:=]\s*', '', r).strip('\'"') for r in ends.split('\n')]
    segs = {s for r in routes for s in r.split('/') if s and not s.startswith('<')}
    bad = 0
    for p, locs in sorted(docs.items()):
        miss = [s for s in p.split('/') if s and not re.match(r'^[<{]|^v\d+$|^api$|^[\d.]+$', s) and s not in segs]
        if miss:
            bad += 1; print(f'{p}  not in routes: {miss}  ({", ".join(locs[:3])})')
    print(f'{bad} of {len(docs)} paths')
    sys.exit(1 if bad else 0)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else 'origin/release_v2.1.0')
