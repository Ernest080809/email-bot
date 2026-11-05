import { createRequire } from 'module';
const { chromium } = createRequire(import.meta.url)('playwright');
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 794, height: 1123 } });
await p.goto('file://' + process.cwd() + '/v19/artwork_en.html'); await p.waitForTimeout(400);
await p.pdf({ path: '../pdf/NVL-TT-01_Artwork_1to1_v1.9.1.pdf', preferCSSPageSize: true, printBackground: true });
await b.close(); console.log('ok');
