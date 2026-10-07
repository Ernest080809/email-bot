import { chromium } from 'playwright';
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const p = await b.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: 2 });
await p.goto('file://' + process.cwd() + '/print15.html');
await p.waitForTimeout(300);
for (let i=0;i<2;i++) await p.screenshot({ path: `p15_${i+1}.png`, fullPage: true, clip: { x: 0, y: i*1122.52, width: 794, height: 1122 } });
await p.pdf({ path: 'NVL_Druckvorlage_v15.pdf', preferCSSPageSize: true, printBackground: true });
await b.close();
console.log('ok');
