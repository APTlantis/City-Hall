// Optional rendered smoke: NODE_PATH must locate Playwright; uses installed Chrome.
const { chromium } = require('playwright');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const fs = require('node:fs');
(async () => {
  const root = path.resolve(__dirname, '..');
  const browser = await chromium.launch({ channel: 'chrome', headless: true });
  try {
    const page = await browser.newPage();
    await page.goto(pathToFileURL(path.join(root, 'examples/presentation.html')).href);
    const fixture = JSON.parse(fs.readFileSync(path.join(root, 'examples/reference-data.json')));
    const counts = await page.locator('tbody tr td:nth-child(2)').allTextContents();
    if (counts.join(',') !== fixture.coverage.map(r => r.records).join(',')) throw Error('Table/fixture mismatch');
    for (const [width, height] of [[1440, 1100], [390, 844], [640, 900]]) {
      await page.setViewportSize({ width, height });
      if (await page.evaluate(() => document.documentElement.scrollWidth > innerWidth)) throw Error('Overflow at ' + width);
      await page.screenshot({ path: path.join(root, `reports/specimen-${width}.png`), fullPage: true });
    }
    await page.locator('summary').focus();
    await page.keyboard.press('Enter');
    if (await page.locator('details').getAttribute('open') !== null) throw Error('Keyboard close failed');
    await page.keyboard.press('Enter');
    if (await page.locator('details').getAttribute('open') === null) throw Error('Keyboard open failed');
    console.log('PASS: fixture/table values; 1440/390/640 widths without overflow; keyboard disclosure');
  } finally { await browser.close(); }
})().catch(e => { console.error(e); process.exit(1); });
