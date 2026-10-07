import { chromium } from 'playwright';
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const p = await b.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: 1.5 });
await p.goto('file://' + process.cwd() + '/print_1zu1.html');
for (let i=0;i<3;i++) await p.screenshot({ path: `p1zu1_${i+1}.png`, fullPage: true, clip: { x: 0, y: i*1122.52, width: 794, height: 1122 } });
await p.pdf({ path: 'NVL_Druckvorlage_1zu1.pdf', preferCSSPageSize: true, printBackground: true });
await b.close();
