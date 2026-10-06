// Draw the same annotations on an already captured PNG (for screens that cannot be re-opened
// without changing data/settings). usage: node overlay.js <spec.json> <outdir>
// spec: [{image, src: 'path/to.png', rects: {id: [x, y, w, h]}, annotate: [...], crop?: {...}, clip?: {x,y,width,height}}]
// rects become absolutely positioned <div id=...> over the image, so annotate locators are '#id'.
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const { annotate, cropRect } = require('./annotate');
const CHROME = process.env.CHROME || `${process.env.HOME}/.cache/ms-playwright/chromium-1234/chrome-linux/chrome`;
(async () => {
  const [specFile, outDir] = process.argv.slice(2);
  const specs = JSON.parse(fs.readFileSync(specFile, 'utf8'));
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch({ executablePath: CHROME });
  const page = await (await browser.newContext({ viewport: { width: 1180, height: 600 } })).newPage();
  for (const s of specs) {
    const b64 = fs.readFileSync(s.src).toString('base64');
    const divs = Object.entries(s.rects || {}).map(([id, [x, y, w, h]]) =>
      `<div id="${id}" style="position:absolute;left:${x}px;top:${y}px;width:${w}px;height:${h}px;${s.debug ? 'outline:1px solid magenta' : ''}"></div>`).join('');
    await page.setContent(`<html><body style="margin:0;position:relative"><img id="base" src="data:image/png;base64,${b64}" style="display:block">${divs}</body></html>`);
    await page.waitForFunction(() => document.getElementById('base').complete);
    const [iw, ih] = await page.evaluate(() => [document.getElementById('base').naturalWidth, document.getElementById('base').naturalHeight]);
    await page.setViewportSize({ width: iw, height: ih });
    const file = path.join(outDir, `${s.image}.png`);
    const ext = s.annotate ? await annotate(page, s.annotate) : [];
    if (s.crop) { const c = await cropRect(page, s.crop, ext); await page.screenshot({ path: file, clip: { x: Math.max(0, c.x), y: Math.max(0, c.y), width: c.w, height: c.h } }); }
    else await page.screenshot({ path: file, ...(s.clip ? { clip: s.clip } : {}) });
    console.log('wrote', file);
  }
  await browser.close();
})();
