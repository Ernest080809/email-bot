import { chromium } from '/opt/node-tools/node_modules/playwright/index.mjs';
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const p = await b.newPage();
await p.goto('file://' + process.cwd() + '/v19/quote_pack.html'); await p.waitForTimeout(400);
await p.pdf({ path: '../pdf/NVL-TT-01_Quote_Pack_v0.9.pdf', preferCSSPageSize: true, printBackground: true });
await b.close(); console.log('ok');
