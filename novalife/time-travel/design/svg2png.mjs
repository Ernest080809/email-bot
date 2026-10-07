// node svg2png.mjs in.svg out.png [scale]
import { chromium } from 'playwright';
import fs from 'fs';
const [,, inp, out, sc] = process.argv;
const scale = parseFloat(sc || '2');
const svg = fs.readFileSync(inp, 'utf8');
const m = svg.match(/width="([\d.]+)(px)?"\s+height="([\d.]+)(px)?"/);
const w = Math.ceil(parseFloat(m[1])), h = Math.ceil(parseFloat(m[3]));
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const p = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: scale });
await p.setContent(`<!doctype html><html><body style="margin:0">${svg}</body></html>`);
await p.waitForTimeout(150);
await p.screenshot({ path: out, clip: { x: 0, y: 0, width: w, height: h } });
await b.close();
console.log('ok', out, w, h, scale);
