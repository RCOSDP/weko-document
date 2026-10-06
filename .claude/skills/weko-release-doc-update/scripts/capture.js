// Capture WEKO admin screens from the local wekov2 (release_v2.1.0) for manual screenshots.
// usage: WEKO_CRED=<path to .cred outside the repo> node capture.js <targets.json> <outdir> [lang]
// env: WEKO_BASE (default https://localhost:8443), CHROME (chromium executable), WEKO_CRED (email=/password= file)
// Run from a work folder where `npm install playwright` was done (NODE_PATH or a symlinked node_modules).
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const { annotate, cropRect } = require('./annotate');

const BASE = process.env.WEKO_BASE || 'https://localhost:8443';
const CHROME = process.env.CHROME ||
  `${process.env.HOME}/.cache/ms-playwright/chromium-1234/chrome-linux/chrome`;

function readCred() {
  const kv = {};
  for (const l of fs.readFileSync(process.env.WEKO_CRED || path.join(process.cwd(), '.cred'), 'utf8').split('\n')) {
    const i = l.indexOf('=');
    if (i > 0) kv[l.slice(0, i)] = l.slice(i + 1);
  }
  return kv;
}

(async () => {
  const [targetsFile, outDir, lang = 'ja'] = process.argv.slice(2);
  const targets = JSON.parse(fs.readFileSync(targetsFile, 'utf8'));
  fs.mkdirSync(outDir, { recursive: true });
  const cred = readCred();

  const browser = await chromium.launch({ executablePath: CHROME });
  const context = await browser.newContext({
    ignoreHTTPSErrors: true,
    viewport: { width: 1180, height: 600 },
    locale: lang === 'ja' ? 'ja-JP' : 'en-US',
    extraHTTPHeaders: { 'Accept-Language': lang },
  });
  const page = await context.newPage();
  page.on('dialog', d => { console.error('dialog:', d.message()); d.accept().catch(()=>{}); });

  // log in
  await page.goto(`${BASE}/login/?next=/admin/`, { waitUntil: 'networkidle' });
  await page.fill('input[name="email"]', cred.email);
  await page.fill('input[name="password"]', cred.password);
  await Promise.all([
    page.waitForNavigation({ waitUntil: 'networkidle' }).catch(() => {}),
    page.click('button[type="submit"], input[type="submit"]'),
  ]);
  // switch UI language through WEKO's language endpoint
  await page.goto(`${BASE}/lang/${lang}?next=/admin/`, { waitUntil: 'networkidle' }).catch(() => {});

  // dismiss the cookie-consent banner on the user-facing pages (browser cookie only)
  await page.goto(`${BASE}/`, { waitUntil: 'networkidle' }).catch(() => {});
  const ok = page.locator('button:visible, a:visible', { hasText: /^\s*(同意|That's ok)\s*$/ });
  if (await ok.count()) { await ok.first().click().catch(() => {}); await page.waitForTimeout(800); }
  const results = [];
  for (const t of targets) {
    try {
      const resp = await page.goto(`${BASE}${t.url}`, { waitUntil: 'networkidle', timeout: 60000 });
      if (t.wait) await page.waitForTimeout(t.wait);
      if (t.click) for (const sel of t.click) { await page.click(sel); await page.waitForTimeout(500); }
      // generic steps: {click|fill|select|hover|check|press|eval|wait|waitFor|goto|clear}
      if (t.steps) for (const s of t.steps) {
        if (s.goto) await page.goto(`${BASE}${s.goto}`, { waitUntil: 'networkidle', timeout: 60000 });
        else if (s.clear) await page.fill(s.clear, '');
        else if (s.fill) await page.fill(s.fill, s.value);
        else if (s.type) await page.type(s.type, s.value);
        else if (s.select) await page.selectOption(s.select, s.value);
        else if (s.check) await page.check(s.check);
        else if (s.uncheck) await page.uncheck(s.uncheck);
        else if (s.hover) await page.hover(s.hover);
        else if (s.click) await page.click(s.click, s.opts || {});
        else if (s.press) await page.press(s.press, s.key);
        else if (s.eval) await page.evaluate(s.eval);
        else if (s.waitFor) await page.waitForSelector(s.waitFor, { state: s.state || 'visible', timeout: 30000 });
        if (s.wait) await page.waitForTimeout(s.wait); else await page.waitForTimeout(300);
      }
      if (t.dump) fs.writeFileSync(path.join(outDir, `${t.image}.html`), await page.content());
      const file = path.join(outDir, `${t.image}.png`);
      if (t.fullViewport) { const h = await page.evaluate(() => document.documentElement.scrollHeight); await page.setViewportSize({ width: 1180, height: h }); await page.waitForTimeout(800); }
      let ext = [];
      if (t.annotate) ext = await annotate(page, t.annotate);
      if (t.crop) { const c = await cropRect(page, t.crop, ext); await page.screenshot({ path: file, fullPage: true, clip: { x: Math.max(0, c.x), y: Math.max(0, c.y), width: c.w, height: c.h } }); }
      else await page.screenshot({ path: file, fullPage: t.fullPage !== false, ...(t.clip ? { clip: t.clip, fullPage: false } : {}) });
      if (t.fullViewport) await page.setViewportSize({ width: 1180, height: 600 });
      results.push({ image: t.image, url: t.url, status: resp ? resp.status() : null, finalUrl: page.url(), file });
    } catch (e) {
      results.push({ image: t.image, url: t.url, error: String(e).slice(0, 200) });
    }
  }
  fs.writeFileSync(path.join(outDir, 'results.json'), JSON.stringify(results, null, 2));
  console.log(JSON.stringify(results, null, 1));
  await browser.close();
})();
