// node pdf.mjs <ordner> [version]  → liest zipper_vorschlag_v02.html, schreibt PDF und je Seite ein PNG
import { chromium } from '/opt/node-tools/node_modules/playwright/index.mjs';
const dir = process.argv[2] || '.';
const ver = process.argv[3] || '0.2';
const W = 1122.52, H = 793.7;               // A4 quer bei 96 dpi
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const p = await b.newPage({ viewport: { width: Math.ceil(W), height: Math.ceil(H) }, deviceScaleFactor: 2 });
await p.goto('file://' + dir + `/zipper_vorschlag_v${ver.replace('.', '')}.html`);
await p.waitForTimeout(800);
const n = await p.evaluate(() => document.querySelectorAll('.pg').length);
for (let i = 0; i < n; i++) {
  const r = await p.evaluate(k => { const e = document.querySelectorAll('.pg')[k].getBoundingClientRect(); return { x: e.x, y: e.y + window.scrollY, w: e.width, h: e.height }; }, i);
  await p.screenshot({ path: `${dir}/vorschlag_v${ver}_s${i + 1}.png`, fullPage: true, clip: { x: r.x, y: r.y, width: r.w, height: r.h } });
}
await p.pdf({ path: `${dir}/NVL-TT-02_Zipper_Designvorschlag_v${ver}.pdf`, preferCSSPageSize: true, printBackground: true });
await b.close();
console.log('ok', n);
