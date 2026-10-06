"""Replace manual images with reviewed screenshots staged by stage2.py.

usage: python3 apply_screenshots.py <review dir> <media dir> [--apply] [--only image4,image418] [--rewrite-ext <manual.md>]
  <review dir>: output of stage2.py (index.json + NNNN_imageXXX__new.png)
  <media dir> : e.g. docs/manuals/ADMIN/base/media/media
Without --apply it only prints what would happen (dry run).
The new shot (PNG) overwrites the current file only when the current file is also PNG.
If the current file is .jpg/.jpeg, it is skipped unless --rewrite-ext <manual.md> is given; then the PNG
is written as imageXXX.png and the manual's references imageXXX.jpg/.jpeg are rewritten to .png
(check that no other manual references the old file before deleting it; this script never deletes).
"""
import json, os, re, shutil, sys

def main(a):
    review, media = a[0], a[1]
    apply = '--apply' in a
    only = set(a[a.index('--only') + 1].split(',')) if '--only' in a else None
    manual = a[a.index('--rewrite-ext') + 1] if '--rewrite-ext' in a else None
    entries = json.load(open(os.path.join(review, 'index.json'), encoding='utf-8'))
    text = open(manual, encoding='utf-8').read() if manual else None
    for e in entries:
        im = e['image']
        if only and im not in only:
            continue
        new = os.path.join(review, f"{e['tag']}__new.png")
        cur = e.get('current') or next(f for f in os.listdir(media) if os.path.splitext(f)[0] == im)
        ext = os.path.splitext(cur)[1].lower()
        if ext == '.png':
            print(('REPLACE ' if apply else 'would replace ') + os.path.join(media, cur))
            if apply: shutil.copy(new, os.path.join(media, cur))
        elif manual:
            dst = os.path.join(media, im + '.png')
            if os.path.exists(dst) and os.path.abspath(dst) != os.path.abspath(os.path.join(media, cur)):
                print(f'SKIP {im}: {im}.png already exists next to {cur}'); continue
            print(('WRITE ' if apply else 'would write ') + dst + f' and rewrite refs {cur} -> {im}.png in {manual}')
            if apply:
                shutil.copy(new, dst)
                text = re.sub(r'media/media/' + re.escape(cur), f'media/media/{im}.png', text)
        else:
            print(f'SKIP {im}: current is {cur} (not PNG); use --rewrite-ext <manual.md>')
    if apply and manual:
        open(manual, 'w', encoding='utf-8').write(text)

if __name__ == '__main__':
    main(sys.argv[1:])
