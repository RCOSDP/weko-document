"""Stage current vs new screenshots in manual (document) order with an HTML review index.

usage: python3 stage2.py <manual.md> <media dir> <new dir> <out dir>
  env SKIP_REFS="image493.jpeg,..." : manual references to ignore (when the same image name exists
  with two extensions and the retake replaces only one of them).
Output: NNNN_imageXXX__current.<ext>, NNNN_imageXXX__new.png, index.html, index.json (tag/image/line/section/ext).
Keep new shots of different manuals in different folders (ADMIN and USER share names like image134)."""
import re, os, sys, shutil, html, json
manual, media, newdir, outdir = sys.argv[1:5]
L = open(manual, encoding='utf-8').read().split('\n')
heads = []  # running heading path
order = []
SKIP = {tuple(x.rsplit('.', 1)) for x in os.environ.get('SKIP_REFS', '').split(',') if x}  # v2.1.0: SKIP_REFS=image493.jpeg
seen = set()
for i, l in enumerate(L):
    m = re.match(r'^(#{1,6}) (.*)', l)
    if m:
        lvl = len(m.group(1)); heads = [h for h in heads if h[0] < lvl] + [(lvl, m.group(2).strip())]
    for im, ext in re.findall(r'media/media/(image\d+)\.(png|jpg|jpeg|PNG)', l):
        if (im, ext) in SKIP: continue
        if im not in seen:
            seen.add(im); order.append((im, i + 1, ' > '.join(h[1] for h in heads[-2:]), ext))
new = {os.path.splitext(f)[0] for f in os.listdir(newdir) if f.endswith('.png')}
os.makedirs(outdir, exist_ok=True)
rows = []
for seq, (im, line, sec, ext) in enumerate(order, 1):
    if im not in new:
        continue
    tag = f'{seq:04d}_{im}'
    cur = im + '.' + ext if os.path.exists(os.path.join(media, im + '.' + ext)) else next(f for f in os.listdir(media) if os.path.splitext(f)[0] == im)
    shutil.copy(os.path.join(media, cur), os.path.join(outdir, f'{tag}__current{os.path.splitext(cur)[1]}'))
    shutil.copy(os.path.join(newdir, im + '.png'), os.path.join(outdir, f'{tag}__new.png'))
    rows.append((tag, im, line, sec, cur))
with open(os.path.join(outdir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write('<!doctype html><meta charset="utf-8"><title>Screenshot review</title><style>body{font-family:sans-serif;margin:16px}table{border-collapse:collapse}td{border:1px solid #ccc;padding:6px;vertical-align:top}img{max-width:560px}</style>')
    f.write(f'<h1>差し替え候補（{html.escape(os.path.basename(manual))}）</h1><table><tr><th>順番 / 画像</th><th>現在</th><th>新規撮影</th></tr>')
    for tag, im, line, sec, cur in rows:
        ext = os.path.splitext(cur)[1]
        f.write(f'<tr><td><b>{tag}</b><br>{line}行目<br>{html.escape(sec)}</td><td><img src="{tag}__current{ext}"></td><td><img src="{tag}__new.png"></td></tr>')
    f.write('</table>')
json.dump([dict(tag=t, image=i, line=l, section=s, current=c) for t, i, l, s, c in rows], open(os.path.join(outdir, 'index.json'), 'w'), ensure_ascii=False, indent=1)
print(len(rows), 'staged ->', outdir)
for r in rows: print(' ', r[0], r[2], r[3][:60])
