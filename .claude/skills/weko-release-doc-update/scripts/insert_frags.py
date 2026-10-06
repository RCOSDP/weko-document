#!/usr/bin/env python3
"""Insert EN fragments into the EN manuals and update their TOC.

usage (from the weko-document root): FRAG_DIR=<dir with A*.md / U*.md> python3 insert_frags.py
Fragments: line 1 = <!-- INSERT_BEFORE: <heading line> --> or <!-- INSERT_AFTER_SECTION: <heading line> -->,
then <!-- TOC: N.M Title --> lines, then the body. A* -> ADMIN manual, U* -> USER manual.
PRIORITY below orders fragments that share the same anchor (edit per run).

Fragments are applied bottom-up (by insertion position), so that TOC numbers
written against the original manual stay valid while earlier positions are
processed later.
"""
import re, sys, os

FRAG = os.environ.get('FRAG_DIR') or os.path.join(os.path.dirname(__file__), 'en_frag')
DOCS = os.environ.get('MANUALS_EN') or os.path.join(os.getcwd(), 'docs/manuals_en')  # run from the weko-document root
TARGETS = {'A': f'{DOCS}/ADMIN/admin_manual.md', 'U': f'{DOCS}/USER/user_manual.md'}
# fragments sharing an anchor: lower value is inserted first (ends up earlier)
PRIORITY = {}  # e.g. {'A3_2.md': 1, 'A1.md': 0}: higher is processed first = ends up earlier for the same INSERT_BEFORE anchor

HEAD = re.compile(r'^(#{1,6}) ')


def slug(text):
    t = text.strip().lower()
    t = re.sub(r'[^\w\- 　-鿿＀-￯]', '', t)
    return t.replace(' ', '-')


def parse_frag(path):
    lines = open(path, encoding='utf-8').read().split('\n')
    directive, tocs, body = None, [], []
    for i, l in enumerate(lines):
        m = re.match(r'^<!-- (INSERT_BEFORE|INSERT_AFTER_SECTION): (.*) -->$', l)
        t = re.match(r'^<!-- TOC: (.*) -->$', l)
        if m and directive is None:
            directive = (m.group(1), m.group(2))
        elif t:
            tocs.append(t.group(1).strip())
        else:
            body = lines[i:]
            break
    while body and body[0].strip() == '':
        body.pop(0)
    while body and body[-1].strip() == '':
        body.pop()
    assert directive, path
    return directive, tocs, body


def heading_level(line):
    m = HEAD.match(line)
    return len(m.group(1)) if m else None


def find_pos(lines, directive):
    kind, anchor = directive
    idx = [i for i, l in enumerate(lines) if l == anchor]
    if len(idx) != 1:
        idx = [i for i, l in enumerate(lines) if l.rstrip() == anchor.rstrip()]
    assert len(idx) == 1, (anchor, len(idx))
    i = idx[0]
    if kind == 'INSERT_BEFORE':
        return i
    lvl = heading_level(lines[i])
    in_code = False
    for j in range(i + 1, len(lines)):
        if lines[j].startswith('```'):
            in_code = not in_code
        if in_code:
            continue
        hl = heading_level(lines[j])
        if hl is not None and hl <= lvl:
            return j
    return len(lines)


TOC_RE = re.compile(r'^\[(\d+(?:\.\d+)*)\.? (.*?)(?: (\d+))?\]\((#[^)]*)\)$')


def num_tuple(s):
    return tuple(int(x) for x in s.rstrip('.').split('.'))


def fmt_num(t):
    return f'{t[0]}.' if len(t) == 1 else '.'.join(map(str, t))


def toc_bounds(lines):
    s = next(i for i, l in enumerate(lines) if l.strip() == '# Table of Contents')
    e = s + 1
    last = s
    while e < len(lines):
        if lines[e].startswith('# ') or lines[e].startswith('#   '):
            break
        if TOC_RE.match(lines[e]):
            last = e
        e += 1
    return s, last


def toc_entries(lines):
    s, e = toc_bounds(lines)
    out = []
    for i in range(s + 1, e + 1):
        m = TOC_RE.match(lines[i])
        if m:
            out.append([i, num_tuple(m.group(1)), m.group(2), m.group(3), m.group(4)])
    return out


def render(num, title, page, anchor):
    return f'[{fmt_num(num)} {title}{" " + page if page else ""}]({anchor})'


def add_toc(lines, new_entries, heading_anchor):
    """new_entries: list of 'N.M Title' strings, in document order."""
    for spec in new_entries:
        m = re.match(r'^(\d+(?:\.\d+)*)\.? (.*)$', spec)
        num, title = num_tuple(m.group(1)), m.group(2)
        ents = toc_entries(lines)
        d = len(num)
        # shift siblings (and their descendants) at >= num
        for e in ents:
            n = e[1]
            if len(n) >= d and n[:d - 1] == num[:d - 1] and n[d - 1] >= num[d - 1]:
                e[1] = n[:d - 1] + (n[d - 1] + 1,) + n[d:]
                lines[e[0]] = render(e[1], e[2], e[3], e[4])
        ents = toc_entries(lines)
        after = [e for e in ents if e[1] < num]
        pos = (after[-1][0] + 1) if after else (toc_bounds(lines)[0] + 1)
        anchor = heading_anchor.get(title, '#' + slug(title))
        lines[pos:pos] = ['', render(num, title, None, anchor)]


def main():
    for key, target in TARGETS.items():
        lines = open(target, encoding='utf-8').read().split('\n')
        frags = []
        for name in sorted(os.listdir(FRAG)):
            if not name.startswith(key):
                continue
            directive, tocs, body = parse_frag(os.path.join(FRAG, name))
            pos = find_pos(lines, directive)
            frags.append((pos, PRIORITY.get(name, 0), name, tocs, body))
        # bottom-up; for the same position insert the later-priority one first
        frags.sort(key=lambda x: (x[0], x[1]), reverse=True)
        for _, _, name, tocs, body in frags:
            directive = parse_frag(os.path.join(FRAG, name))[0]
            pos = find_pos(lines, directive)  # recompute: TOC insertions shift lines
            anchors = {}
            for l in body:
                hm = HEAD.match(l)
                if hm:
                    text = l[len(hm.group(0)):].strip()
                    anchors[text] = '#' + slug(text)
            block = [''] + body + ['']
            lines[pos:pos] = block
            if tocs:
                add_toc(lines, tocs, anchors)
            print(f'{name}: inserted {len(body)} lines at {pos}, toc {len(tocs)}')
        open(target, 'w', encoding='utf-8').write('\n'.join(lines))


if __name__ == '__main__':
    main()
