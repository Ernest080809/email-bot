import { chromium } from '/opt/node-tools/node_modules/playwright/index.mjs';
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const p = await b.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: 1 });
await p.goto('file://' + process.cwd() + '/v19/print19.html');
await p.waitForTimeout(400);
await p.pdf({ path: '../pdf/NVL_Druckvorlage_v19_Jeans.pdf', preferCSSPageSize: true, printBackground: true });
await b.close(); console.log('ok');
