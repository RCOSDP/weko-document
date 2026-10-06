const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const BASE = process.env.WEKO_BASE || 'https://localhost:8443';
const CHROME = process.env.CHROME || `${process.env.HOME}/.cache/ms-playwright/chromium-1234/chrome-linux/chrome`;
function readCred() {
  const kv = {};
  for (const l of fs.readFileSync(process.env.WEKO_CRED || path.join(process.cwd(), '.cred'), 'utf8').split('\n')) {
    const i = l.indexOf('='); if (i > 0) kv[l.slice(0, i)] = l.slice(i + 1);
  }
  return kv;
}
async function start(lang = 'ja') {
  const browser = await chromium.launch({ executablePath: CHROME });
  const context = await browser.newContext({ ignoreHTTPSErrors: true, viewport: { width: 1180, height: 600 },
    locale: lang === 'ja' ? 'ja-JP' : 'en-US', extraHTTPHeaders: { 'Accept-Language': lang }, acceptDownloads: true });
  const page = await context.newPage();
  page.on('dialog', d => { console.error('dialog:', d.message()); d.accept().catch(() => {}); });
  const cred = readCred();
  await page.goto(`${BASE}/login/?next=/admin/`, { waitUntil: 'networkidle' });
  await page.fill('input[name="email"]', cred.email);
  await page.fill('input[name="password"]', cred.password);
  await Promise.all([page.waitForNavigation({ waitUntil: 'networkidle' }).catch(() => {}),
    page.click('button[type="submit"], input[type="submit"]')]);
  await page.goto(`${BASE}/lang/${lang}?next=/admin/`, { waitUntil: 'networkidle' }).catch(() => {});
  const go = (u) => page.goto(`${BASE}${u}`, { waitUntil: 'networkidle', timeout: 60000 });
  return { browser, context, page, go, BASE };
}
module.exports = { start };
