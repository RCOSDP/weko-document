const { start } = require('./lib');
const fs = require('fs');
(async () => {
  const { browser, page, go } = await start();
  await go('/admin/jsonld-mapping/new/?url=%2Fadmin%2Fjsonld-mapping%2F');
  await page.waitForTimeout(1000);
  await page.fill('#name', 'screenshot-sample マッピング');
  await page.selectOption('#item_type', { value: '30001' });
  await page.waitForTimeout(500);
  const m = JSON.stringify(JSON.parse(fs.readFileSync('tmp/mapping_sample.json', 'utf8')), null, 4);
  await page.fill('#mapping', m);
  await page.click('#save_button');
  await page.waitForTimeout(4000);
  console.log(page.url()); const t = await page.locator('.modal.in .modal-body').allTextContents().catch(()=>[]); fs.writeFileSync('tmp/mapping_err.txt', t.join('\n'));
  await page.screenshot({ path: 'probe/jm_after.png', fullPage: true });
  await browser.close();
})();
