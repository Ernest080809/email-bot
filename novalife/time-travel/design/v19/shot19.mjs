import { chromium } from '/opt/node-tools/node_modules/playwright/index.mjs';
const [html, png, w, h] = process.argv.slice(2);
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const p = await b.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: 1 });
await p.goto('file://' + html);
await p.waitForTimeout(500);
await p.screenshot({ path: png, clip: { x: 0, y: 0, width: +w, height: +h } });
await b.close(); console.log('ok');
