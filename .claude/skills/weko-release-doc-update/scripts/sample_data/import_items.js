// Bulk-import a ZIP (TSV + files) through the admin Import screen and optionally capture the Result tab.
// Used for screenshot sample items and for the "Result" tab screenshot (v2.1.0: JA image88 / EN image86).
// usage: WEKO_CRED=<.cred> node import_items.js <zip> <lang ja|en> [go <out.png>]
//   without "go": upload + check only (writes probe/import_check.png)
//   with "go"   : also run the import, open the Result tab and save a full-page screenshot to <out.png>
// Record every imported item (recid, title, index) in sample_data_log.md.
const { start } = require('./lib');
const fs = require('fs');
(async () => {
  const [zip, lang = 'ja', mode, out] = process.argv.slice(2);
  const { browser, page, go, context } = await start(lang);
  await context.route(/google-analytics\.com|googletagmanager\.com/, r => r.abort());
  fs.mkdirSync('probe', { recursive: true });
  await go('/admin/items/import/');
  await page.setInputFiles('input.input-file', zip);
  await page.waitForTimeout(800);
  await page.click(lang === 'ja' ? 'button:has-text("次へ")' : 'button:has-text("Next")');
  await page.waitForTimeout(15000);
  await page.screenshot({ path: 'probe/import_check.png', fullPage: true });
  if (mode === 'go') {
    await page.click((lang === 'ja' ? 'button:has-text("インポート")' : 'button:has-text("Import")') + ' >> visible=true');
    await page.waitForTimeout(3000);
    const b = page.locator('.modal.in .btn-primary');
    if (await b.count()) await b.first().click();
    await page.waitForTimeout(20000);
    const rt = page.locator('a:has-text("Result")');
    if (await rt.count()) { await rt.first().click(); await page.waitForTimeout(15000); }
    await page.screenshot({ path: out || 'probe/import_result.png', fullPage: true });
  }
  await browser.close();
})();
