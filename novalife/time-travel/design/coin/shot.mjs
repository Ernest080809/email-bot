import { chromium } from 'playwright';
const [,,inp,out,w,h]=process.argv;
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const p = await b.newPage({ viewport: { width: +w, height: +h } });
await p.goto('file://' + process.cwd() + '/' + inp);
await p.screenshot({ path: out });
await b.close();
