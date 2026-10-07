import { chromium } from 'playwright';
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const p = await b.newPage({ viewport: { width: 1280, height: 2120 }, deviceScaleFactor: 2 });
await p.goto('file://' + process.cwd() + '/preview.html');
await p.screenshot({ path: 'pv_front.png', clip: { x: 220, y: 120, width: 460, height: 300 } });
await p.screenshot({ path: 'pv_back.png', clip: { x: 420, y: 1060+100, width: 220, height: 300 } });
await b.close();
