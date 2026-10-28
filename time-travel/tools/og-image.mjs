// Renders the share preview (og:image, 1200×630) from the real scene.
//   node time-travel/tools/og-image.mjs          → time-travel/og-image.jpg
//   node time-travel/tools/og-image.mjs ch4      → the same, showing chapter IV
// Needs Node 18+ and Playwright with Chromium (npm i playwright && npx playwright install chromium).
// Then run build.py: it copies the image to shopify/assets/time-travel-og.jpg.
import { createRequire } from "node:module";
import { fileURLToPath, pathToFileURL } from "node:url";
import path from "node:path";
import fs from "node:fs";

const { chromium } = createRequire(import.meta.url)("playwright");   // require() also finds a global install (NODE_PATH)
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const extra = (process.argv[2] || "").replace(/^#/, "");
const args = ["--use-gl=angle", "--enable-unsafe-swiftshader"];
if (process.env.OG_SWIFTSHADER) args.push("--use-angle=swiftshader");   // machines without a GPU
const browser = await chromium.launch({ args });
const page = await browser.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1 });
if (process.env.THREE_DIR) {   // offline: serve three.js from a local copy of the npm package
  await page.route("https://cdn.jsdelivr.net/npm/three@0.160.0/**", (r) =>
    r.fulfill({ body: fs.readFileSync(path.join(process.env.THREE_DIR, r.request().url().split("three@0.160.0/")[1])), contentType: "application/javascript" }));
}
await page.goto(pathToFileURL(path.join(root, "index.html")).href + "#door" + (extra ? "," + extra : ""));
await page.waitForFunction(() => !!window.__tt, null, { timeout: 240000 });
await page.evaluate(() => { window.__tt.setDist(13); if (window.__tt.keyRig.group) window.__tt.keyRig.group.visible = false; });   // the golden key stays a secret
await page.addStyleTag({ content: `
  .hud,.walk,.spawn,.flash,.caption,.drawer{display:none!important}
  .og{position:fixed;inset:0;z-index:30;display:grid;align-content:end;padding:0 76px 60px;color:#f3ece0;
    background:linear-gradient(0deg,rgba(21,17,13,.86),rgba(21,17,13,.5) 34%,rgba(21,17,13,0) 60%)}
  .og .m{font:600 15px Manrope;letter-spacing:.42em;text-transform:uppercase}
  .og h1{margin:16px 0 18px;font:italic 400 104px/.95 "Bodoni Moda";letter-spacing:-.01em}
  .og p{margin:0;font:500 16px "IBM Plex Mono";letter-spacing:.16em;text-transform:uppercase;color:rgba(243,236,224,.84)}` });
await page.evaluate(() => {
  const d = document.createElement("div"); d.className = "og";
  d.innerHTML = '<div class="m">Novalife</div><h1>Time Travel</h1><p>The door is closed.</p>';
  document.body.appendChild(d);
});
await page.waitForTimeout(8000);
const out = path.join(root, "og-image.jpg");
await page.screenshot({ path: out, type: "jpeg", quality: 88 });
await browser.close();
console.log("wrote", out);
