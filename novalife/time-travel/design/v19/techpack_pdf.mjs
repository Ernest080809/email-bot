// Tech Pack als PDF: Englisch mit Artwork 1:1 als Anhang, Deutsch mit Druckvorlage v1.9 (Seiten 2–5) als Anhang
import { chromium } from '/opt/node-tools/node_modules/playwright/index.mjs';
import { execFileSync } from 'node:child_process';
import { existsSync } from 'node:fs';
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const p = await b.newPage();
for (const lang of ['en', 'de']) {
  const html = lang === 'de' ? 'v19/techpack_de.html' : 'v19/techpack.html';
  if (!existsSync(html)) continue;
  await p.goto('file://' + process.cwd() + '/' + html); await p.waitForTimeout(400);
  await p.pdf({ path: `v19/techpack_main_${lang}.pdf`, preferCSSPageSize: true, printBackground: true });
  if (lang === 'en') {
    execFileSync('pdfunite', ['v19/techpack_main_en.pdf', '../pdf/NVL-TT-01_Artwork_1to1_v1.9.pdf', '../pdf/NVL-TT-01_TechPack_v1.0.pdf']);
  } else {
    execFileSync('pdfseparate', ['-f', '2', '-l', '5', '../pdf/NVL_Druckvorlage_v19_Jeans.pdf', 'v19/dv-%d.pdf']);
    execFileSync('pdfunite', ['v19/techpack_main_de.pdf', 'v19/dv-2.pdf', 'v19/dv-3.pdf', 'v19/dv-4.pdf', 'v19/dv-5.pdf', '../pdf/NVL-TT-01_TechPack_v1.0_DE.pdf']);
  }
}
await b.close();
console.log('ok');
