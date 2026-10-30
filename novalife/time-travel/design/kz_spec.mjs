// Maßblätter NVL-TT-01 (Kuzgunlar-Format) als PDF: node kz_spec.mjs <ausgabe.pdf>
import { createRequire } from 'module';
import path from 'path';
import { fileURLToPath } from 'url';
const { chromium } = createRequire(import.meta.url)('playwright');
const here = path.dirname(fileURLToPath(import.meta.url));
const b = await chromium.launch(); const p = await b.newPage();
await p.goto('file://' + path.join(here, 'v19', 'kz_spec.html'), { waitUntil: 'networkidle' });
await p.evaluate(() => document.fonts.ready);
await p.pdf({ path: process.argv[2], width: '210mm', height: '297mm', printBackground: true });
await b.close();
