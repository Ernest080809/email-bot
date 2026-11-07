// node papier.mjs <ordner>  → papiertest_zipper.html als PDF (A4 hoch) und Vorschaubilder der Seiten
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { chromium } = require('playwright');
const dir = process.argv[2] || '.';
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: 1.5 });
await p.goto('file://' + dir + '/papiertest_zipper.html');
await p.waitForTimeout(800);
const n = await p.evaluate(() => document.querySelectorAll('.pg').length);
for (let i = 0; i < n; i++) {
  const r = await p.evaluate(k => { const e = document.querySelectorAll('.pg')[k].getBoundingClientRect(); return { x: e.x, y: e.y + window.scrollY, w: e.width, h: e.height }; }, i);
  await p.screenshot({ path: `${dir}/papier_s${i + 1}.png`, fullPage: true, clip: { x: r.x, y: r.y, width: r.w, height: r.h } });
}
await p.pdf({ path: `${dir}/NVL-TT-02_Papiertest_Zipper.pdf`, preferCSSPageSize: true, printBackground: true });
await b.close();
console.log('ok', n);
