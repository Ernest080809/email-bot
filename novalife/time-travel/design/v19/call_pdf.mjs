import { chromium } from '/opt/node-tools/node_modules/playwright/index.mjs';
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const p = await b.newPage();
await p.goto('file://' + process.cwd() + '/v19/call_guide.html'); await p.waitForTimeout(300);
await p.pdf({ path: '../pdf/NVL_Leitfaden_Fabrik-Calls.pdf', preferCSSPageSize: true, printBackground: true });
await b.close(); console.log('ok');
