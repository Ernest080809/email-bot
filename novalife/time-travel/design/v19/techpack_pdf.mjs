import { chromium } from '/opt/node-tools/node_modules/playwright/index.mjs';
import { execFileSync } from 'node:child_process';
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const p = await b.newPage();
await p.goto('file://' + process.cwd() + '/v19/techpack.html'); await p.waitForTimeout(400);
await p.pdf({ path: 'v19/techpack_main.pdf', preferCSSPageSize: true, printBackground: true });
await b.close();
execFileSync('pdfunite', ['v19/techpack_main.pdf', '../pdf/NVL-TT-01_Artwork_1to1_v1.9.pdf', '../pdf/NVL-TT-01_TechPack_v1.0.pdf']);
console.log('ok');
