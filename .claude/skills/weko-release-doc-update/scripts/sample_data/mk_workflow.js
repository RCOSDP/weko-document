const { start } = require('./lib');
(async () => {
  const { browser, page, go } = await start();
  await go('/admin/workflowsetting/0');


  await page.fill('#txt_workflow_name', 'screenshot-sample ワークフロー'); await page.press('#txt_workflow_name', 'End');
  await page.selectOption('#txt_flow_name', { label: 'Registration Flow' });
  await page.selectOption('#txt_itemtype', { value: '30001' });
  await page.waitForTimeout(500);
  await page.screenshot({ path: 'probe/wf_before.png', fullPage: true });
  await page.click('#btn_create');
  await page.waitForTimeout(3000);
  await page.screenshot({ path: 'probe/wf_after.png', fullPage: true });
  await browser.close();
})();
