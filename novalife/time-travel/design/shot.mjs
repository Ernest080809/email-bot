import { chromium } from 'playwright';
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const p = await b.newPage({ viewport: { width: 1188, height: 840 } });
await p.goto('file://' + process.cwd() + '/sheet.svg');
await p.screenshot({ path: 'sheet.png' });
await b.close();
