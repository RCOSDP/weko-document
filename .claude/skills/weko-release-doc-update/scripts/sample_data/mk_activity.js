const { start } = require('./lib');
const fs = require('fs');
(async () => {
  const { browser, page, go } = await start();
  await go('/workflow/activity/new');
  await Promise.all([page.waitForNavigation({ waitUntil: 'networkidle', timeout: 60000 }).catch(() => {}), page.click('#btn-begin-1001')]);
  await page.waitForTimeout(4000);
  console.log('URL', page.url());
  fs.writeFileSync('probe/act_detail.html', await page.content());
  await page.screenshot({ path: 'probe/act_detail.png', fullPage: true });
  await browser.close();
})();
