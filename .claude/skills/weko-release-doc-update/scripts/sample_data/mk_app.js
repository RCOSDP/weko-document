const { start } = require('./lib');
const fs = require('fs');
(async () => {
  const { browser, page, go } = await start();
  await go('/account/settings/applications/clients/new/');
  console.log(await page.$$eval('#is_confidential option', os => os.map(o => o.value + ':' + o.textContent)));
  // GUIDE screenshot: example values from the guide text (not submitted)
  await page.fill('#name', 'GRDM_JAIROCloud_XXUniversity');
  await page.fill('#description', 'GakuNin RDMのJAIRO Cloud連携用（XX大学リポジトリ）');
  await page.fill('#website', 'https://rdm.nii.ac.jp');
  await page.fill('#redirect_uris', 'https://rdm.nii.ac.jp/oauth/callback/weko/xx.repo.nii.ac.jp/');
  await page.selectOption('#is_confidential', { index: 0 });
  await page.evaluate(() => document.activeElement.blur());
  fs.mkdirSync('out/ja_guide', { recursive: true });
  await page.screenshot({ path: 'out/ja_guide/app_setting_1.png', fullPage: true });
  if (process.argv[2] === 'register') {
    await page.fill('#name', 'screenshot-sample アプリケーション');
    await page.fill('#description', 'screenshot-sample（マニュアル撮影用）');
    await page.fill('#website', 'https://example.org/screenshot-sample');
    await page.fill('#redirect_uris', 'https://example.org/screenshot-sample/callback');
    await Promise.all([page.waitForNavigation({ waitUntil: 'networkidle' }).catch(() => {}), page.click('button[type="submit"].btn-primary')]);
    console.log('after', page.url());
    await page.screenshot({ path: 'probe/app_after.png', fullPage: true });
  }
  await browser.close();
})();
