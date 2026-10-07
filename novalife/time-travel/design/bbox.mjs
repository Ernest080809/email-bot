import { chromium } from 'playwright';
import fs from 'fs';
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const p = await b.newPage();
for (const f of ['v15/b.svg','v15/b2.svg']) {
  const svg = fs.readFileSync(f,'utf8').replace(/<rect width="\d+" height="\d+" style="fill: #2f4a6e"><\/rect>/,'');
  await p.setContent(`<html><body>${svg}</body></html>`);
  const bb = await p.evaluate(() => { const s=document.querySelector('svg'); const g=document.createElementNS('http://www.w3.org/2000/svg','g'); while(s.firstChild) g.appendChild(s.firstChild); s.appendChild(g); const r=g.getBBox(); return [r.x,r.y,r.width,r.height].map(v=>Math.round(v*10)/10); });
  console.log(f, JSON.stringify(bb));
}
await b.close();
