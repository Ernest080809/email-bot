import { chromium } from 'playwright';
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const p = await b.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: 4 });
await p.goto('file://' + process.cwd() + '/print15.html');
await p.waitForTimeout(300);
const mm = 3.7795;
await p.screenshot({ path: 'z15_b.png', fullPage: true, clip: { x: 72*mm, y: 1122.52 + 84*mm, width: 72*mm, height: 128*mm } });
await b.close();
console.log('ok');
