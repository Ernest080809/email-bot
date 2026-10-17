import * as THREE from "three";
import { EffectComposer } from "three/addons/postprocessing/EffectComposer.js";
import { RenderPass } from "three/addons/postprocessing/RenderPass.js";
import { UnrealBloomPass } from "three/addons/postprocessing/UnrealBloomPass.js";
import { OutputPass } from "three/addons/postprocessing/OutputPass.js";
import { ShaderPass } from "three/addons/postprocessing/ShaderPass.js";
import { mergeGeometries, mergeVertices } from "three/addons/utils/BufferGeometryUtils.js";

/* ==========================================================================
   CONFIG — the only block you normally touch
   ========================================================================== */
const CONFIG = {
  dropAt:  "2027-04-22T19:00:00+02:00",   // door opens for everyone (Berlin, CEST)
  earlyAt: "2027-04-22T18:00:00+02:00",   // waitlist gets the key
  // "auto" → "shopify" on the shop domain, else "endpoint" if set, else "demo"
  mode: "auto",
  shopHosts: ["novalife.store", "myshopify.com"],
  endpoint: "",                                // e.g. a Formspree URL (POST JSON)
  dropUrl: "/collections/time-travel",         // where "Enter" leads once the door is open
  privacyUrl: "/policies/privacy-policy",
  imprintUrl: "/policies/legal-notice",
};

/* ==========================================================================
   Small helpers
   ========================================================================== */
const $ = (id) => document.getElementById(id);
const params = new URLSearchParams(location.search);
const hashFlags = new Set(location.hash.replace("#", "").split(/[.,]/).filter(Boolean));
const flag = (k) => params.has(k) || hashFlags.has(k);
const store = {
  get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
  set(k, v) { try { localStorage.setItem(k, v); } catch (e) {} },
  del(k) { try { localStorage.removeItem(k); } catch (e) {} },
};
const DROP_AT = new Date(CONFIG.dropAt).getTime();
const EARLY_AT = new Date(CONFIG.earlyAt).getTime();
const isOpen = () => flag("open") || Date.now() >= DROP_AT;
const pad = (n, l = 2) => String(n).padStart(l, "0");
const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
const smooth = (a, b, x) => { const t = clamp((x - a) / (b - a), 0, 1); return t * t * (3 - 2 * t); };
const reduceMotion = matchMedia("(prefers-reduced-motion: reduce)").matches;
if (flag("reset")) store.del("tt_registered");
["privacyLink", "privacyLink2"].forEach((id) => ($(id).href = CONFIG.privacyUrl));
$("imprintLink").href = CONFIG.imprintUrl;

// seeded random so the field looks the same for everyone
let seed = 1337;
const rnd = () => { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; };
const rr = (a, b) => a + (b - a) * rnd();

// tileable value noise for procedural textures
function hash2(x, y) {
  let h = (Math.imul(x | 0, 374761393) + Math.imul(y | 0, 668265263)) | 0;
  h = Math.imul(h ^ (h >>> 13), 1274126177);
  return ((h ^ (h >>> 16)) >>> 0) / 4294967295;
}
function vnoise(x, y, px, py) {
  const xi = Math.floor(x), yi = Math.floor(y), xf = x - xi, yf = y - yi;
  const u = xf * xf * (3 - 2 * xf), v = yf * yf * (3 - 2 * yf);
  const x0 = ((xi % px) + px) % px, y0 = ((yi % py) + py) % py, x1 = (x0 + 1) % px, y1 = (y0 + 1) % py;
  const a = hash2(x0, y0), b = hash2(x1, y0), c = hash2(x0, y1), d = hash2(x1, y1);
  return a + (b - a) * u + (c - a) * v + (a - b - c + d) * u * v;
}
// u,v in [0,1); fx,fy = base lattice cells across the texture
function fbm(u, v, fx, fy, oct = 4) {
  let s = 0, a = 0.5, n = 0;
  for (let i = 0; i < oct; i++) { const m = 1 << i; s += a * vnoise(u * fx * m, v * fy * m, fx * m, fy * m); n += a; a *= 0.5; }
  return s / n;
}

/* ==========================================================================
   Quality tier
   ========================================================================== */
const coarse = matchMedia("(pointer: coarse)").matches;
const lowEnd = coarse || Math.min(innerWidth, innerHeight) < 600 || (navigator.hardwareConcurrency || 8) <= 4;
const Q = lowEnd
  ? { near: 1700, far: 3400, birch: 45, pr: Math.min(devicePixelRatio, 1.25), samples: 4, shadow: 1024, bloomScale: 0.4 }
  : { near: 3800, far: 7600, birch: 70, pr: Math.min(devicePixelRatio, 1.5), samples: 4, shadow: 2048, bloomScale: 0.5 };

/* ==========================================================================
   Renderer, scene, camera
   ========================================================================== */
const canvas = $("scene");
let renderer;
try {
  renderer = new THREE.WebGLRenderer({ canvas, antialias: false, powerPreference: "high-performance" });
} catch (e) {
  document.body.insertAdjacentHTML("beforeend", '<div class="fallback"><div><div class="mark">Novalife</div><p>This browser cannot show the 3D field. You can still join the waitlist.</p></div></div>');
  $("loader").classList.add("gone");
  throw e;
}
renderer.setPixelRatio(Q.pr);
renderer.setSize(innerWidth, innerHeight, false);
renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 0.74;
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;
const ANISO = Math.min(8, renderer.capabilities.getMaxAnisotropy());

const scene = new THREE.Scene();
const FOG = new THREE.Color().setRGB(0.9, 0.66, 0.43);
scene.fog = new THREE.FogExp2(FOG, 0.0068);

const camera = new THREE.PerspectiveCamera(50, innerWidth / innerHeight, 0.1, 6000);

// Sun: low in the west, from the right of the path — golden hour
const SUN_ELEV = THREE.MathUtils.degToRad(6.5), SUN_AZ = THREE.MathUtils.degToRad(102);
const sunDir = new THREE.Vector3().setFromSphericalCoords(1, Math.PI / 2 - SUN_ELEV, SUN_AZ);

// Art-directed golden-hour sky: warm horizon, glow on the sun side, deep blue overhead
function makeSky(radius) {
  const mat = new THREE.ShaderMaterial({
    uniforms: { uSun: { value: sunDir } },
    vertexShader: `varying vec3 vDir;
      void main(){ vec4 w = modelMatrix * vec4(position, 1.0); vDir = w.xyz - cameraPosition;
        gl_Position = projectionMatrix * viewMatrix * w; gl_Position.z = gl_Position.w; }`,
    fragmentShader: `uniform vec3 uSun; varying vec3 vDir;
      void main(){
        vec3 d = normalize(vDir); float h = d.y;
        vec3 zen = vec3(0.2, 0.36, 0.62), mid = vec3(0.66, 0.64, 0.66), hor = vec3(1.05, 0.72, 0.44);
        vec3 col = mix(hor, mid, smoothstep(0.0, 0.2, h));
        col = mix(col, zen, smoothstep(0.1, 0.55, h));
        float sd = max(dot(d, uSun), 0.0);
        float az = max(dot(normalize(d.xz + 1e-5), normalize(uSun.xz)), 0.0);
        col += vec3(0.6, 0.3, 0.08) * pow(az, 2.5) * (1.0 - smoothstep(0.0, 0.45, h));
        col += vec3(1.0, 0.58, 0.25) * pow(sd, 10.0) * 1.1;
        col += vec3(1.0, 0.78, 0.48) * pow(sd, 180.0) * 5.0;
        col += vec3(1.0, 0.95, 0.85) * smoothstep(0.99955, 0.9999, sd) * 40.0;
        col = mix(col, hor * 0.82, smoothstep(0.0, -0.08, h));
        gl_FragColor = vec4(col, 1.0);
      }`,
    side: THREE.BackSide, depthWrite: false, fog: false,
  });
  const m = new THREE.Mesh(new THREE.SphereGeometry(radius, 48, 24), mat);
  m.renderOrder = -1; m.frustumCulled = false;
  return m;
}
scene.add(makeSky(4000));

const sun = new THREE.DirectionalLight("#ffc98a", 4.2);
sun.castShadow = true;
sun.shadow.mapSize.set(Q.shadow, Q.shadow);
sun.shadow.bias = -0.0004;
sun.shadow.normalBias = 0.03;
const sc = sun.shadow.camera; sc.left = -18; sc.right = 18; sc.top = 18; sc.bottom = -18; sc.near = 1; sc.far = 160;
scene.add(sun, sun.target);
const hemi = new THREE.HemisphereLight("#b9cde4", "#a27a44", 0.6);
scene.add(hemi);

/* ==========================================================================
   Canvas textures
   ========================================================================== */
function makeCanvas(w, h) { const c = document.createElement("canvas"); c.width = w; c.height = h; return c; }
function tex(c, { srgb = true, repeat = [1, 1], wrap = true } = {}) {
  const t = new THREE.CanvasTexture(c);
  if (srgb) t.colorSpace = THREE.SRGBColorSpace;
  if (wrap) { t.wrapS = t.wrapT = THREE.RepeatWrapping; }
  t.repeat.set(repeat[0], repeat[1]);
  t.anisotropy = ANISO;
  return t;
}
const mix = (a, b, t) => a + (b - a) * t;
const mixc = (c1, c2, t) => [mix(c1[0], c2[0], t), mix(c1[1], c2[1], t), mix(c1[2], c2[2], t)];
const hex = (h) => { const n = parseInt(h.slice(1), 16); return [(n >> 16) & 255, (n >> 8) & 255, n & 255]; };

const T = {};
// Per-pixel textures. Each entry is a factory returning (u, v, x, y) => [r, g, b, a?].
// They only use the noise helpers above, so they can run in Web Workers in parallel.
const PIX = {
  log: [512, 512, () => {
    const base = [hex("#4f3b2b"), hex("#7a5e45"), hex("#9c8166"), hex("#857c72")];
    return (u, v) => {
      const streak = fbm(u, v, 48, 2, 3), fine = fbm(u, v, 160, 6, 2), weather = fbm(u, v, 6, 3, 3);
      const t = clamp(0.25 + streak * 0.55 + (fine - 0.5) * 0.35, 0, 1);
      const crack = hash2(Math.floor(u * 90), 7) > 0.93 && fbm(u, v, 4, 5, 2) > 0.45 ? 0.45 : 1;
      let col = t < 0.5 ? mixc(base[0], base[1], t * 2) : mixc(base[1], base[2], (t - 0.5) * 2);
      col = mixc(col, base[3], clamp((weather - 0.45) * 1.6, 0, 0.6));
      const ao = 1 - 0.62 * smooth(0.5, 0.97, Math.abs(Math.sin(u * Math.PI * 2)));
      return [col[0] * crack * ao, col[1] * crack * ao, col[2] * crack * ao];
    };
  }],
  logEnd: [256, 256, () => (u, v) => {
    const dx = u - 0.5, dy = v - 0.5, r = Math.hypot(dx, dy) * 2, a = Math.atan2(dy, dx);
    const n = fbm(u, v, 8, 8, 3), ring = 0.5 + 0.5 * Math.sin(r * 46 + n * 5);
    let col = mixc(hex("#c49a6c"), hex("#9b744f"), ring * 0.55 + n * 0.3);
    const crack = Math.abs(Math.sin(a * 3 + n * 2)) < 0.03 && r > 0.15 ? 0.55 : 1;
    if (r > 0.9) col = mixc(col, hex("#4a3424"), smooth(0.9, 0.97, r));
    return [col[0] * crack, col[1] * crack, col[2] * crack];
  }],
  boards: [512, 512, () => (u, v) => {
    const pu = (u * 6) % 1, tone = hash2(Math.floor(u * 6), 3), grain = fbm(u, v, 96, 3, 3);
    return pu < 0.025 || pu > 0.975 ? hex("#231a13") : mixc(hex("#5d4a39"), hex("#8a7462"), clamp(tone * 0.6 + grain * 0.5, 0, 1));
  }],
  door: [512, 512, () => (u, v) => {
    const pu = (u * 6) % 1, tone = hash2(Math.floor(u * 6), 3), grain = fbm(u, v, 96, 3, 3);
    return pu < 0.025 || pu > 0.975 ? hex("#160f0a") : mixc(hex("#3b281b"), hex("#5e4430"), clamp(tone * 0.6 + grain * 0.5, 0, 1));
  }],
  path: [256, 512, () => (u, v) => {
    const n = fbm(u, v, 8, 16, 4), n2 = fbm(u, v, 32, 64, 2);
    let col = mixc(hex("#9c7c58"), hex("#c7a57b"), n);
    const rut = Math.exp(-Math.pow((u - 0.27) / 0.08, 2)) + Math.exp(-Math.pow((u - 0.73) / 0.08, 2));
    col = mixc(col, hex("#6f5640"), rut * 0.45);
    if (Math.exp(-Math.pow((u - 0.5) / 0.09, 2)) * (0.6 + n2 * 0.8) > 0.55) col = mixc(col, hex("#8d8a4c"), 0.75);
    return mixc(col, hex("#9c8448"), (smooth(0.12, 0.0, u) + smooth(0.88, 1.0, u)) * 0.85);
  }],
  ground: [256, 256, () => (u, v) => mixc(hex("#7a5d2c"), hex("#a8823d"), fbm(u, v, 8, 8, 4) * 0.85 + fbm(u, v, 64, 32, 2) * 0.12)],
  canopy: [256, 256, () => (u, v) => mixc(hex("#b48c45"), hex("#e2bd70"), clamp(fbm(u, v, 4, 4, 4) * 0.85 + fbm(u, v, 32, 16, 3) * 0.2, 0, 1))],
  yard: [256, 256, () => (u, v) => mixc(hex("#5d6330"), hex("#9b9450"), clamp(fbm(u, v, 6, 6, 4) * 0.7 + fbm(u, v, 48, 48, 2) * 0.4, 0, 1))],
  shutter: [256, 512, () => (u, v) => {
    const grain = fbm(u, v, 3, 40, 3), wear = fbm(u, v, 6, 10, 4);
    let col = mixc(hex("#244c86"), hex("#3a6aa8"), grain);
    const bx = Math.min(u, 1 - u), by = Math.min(v, 1 - v) * 0.5, r = Math.abs(u - 0.5) + Math.abs(v - 0.5) * 0.5;
    if (bx < 0.09 || by < 0.045 || (r < 0.28 && r > 0.2)) col = mixc(hex("#e9e1cf"), hex("#cfc5b0"), grain);
    if ((r < 0.12 && r > 0.07) || r < 0.03) col = hex("#a3392c");
    if (wear > 0.68) col = mixc(col, hex("#7d6a55"), (wear - 0.68) * 2.2);
    return col;
  }],
  birch: [256, 512, () => (u, v) => {
    let col = mixc(hex("#d9d4c7"), hex("#f1ede3"), fbm(u, v, 4, 16, 4));
    if (hash2(Math.floor(v * 90), Math.floor(u * 7)) > 0.82 && Math.abs(((v * 90) % 1) - 0.5) < 0.18) col = mixc(col, hex("#2a2622"), 0.85);
    const patch = fbm(u, v, 3, 6, 3);
    return patch > 0.66 ? mixc(col, hex("#3a332c"), (patch - 0.66) * 2.5) : col;
  }],
  lemekh: [512, 512, () => (u, v) => {
    const pu = (u * 6) % 1, tone = hash2(Math.floor(u * 6), 11), grain = fbm(u, v, 96, 4, 3), weather = fbm(u, v, 6, 6, 3);
    let col = mixc(hex("#7d776c"), hex("#b5afa3"), clamp(tone * 0.55 + grain * 0.55, 0, 1));
    col = mixc(col, hex("#5d5848"), clamp((weather - 0.55) * 1.8, 0, 0.5));
    return pu < 0.025 || pu > 0.975 ? [col[0] * 0.5, col[1] * 0.5, col[2] * 0.5] : col;
  }],
  cloud: [256, 256, () => (u, v) => {
    const r = Math.hypot(u - 0.5, (v - 0.5) * 1.6) * 2, n = fbm(u, v, 6, 6, 4);
    return [255, 255, 255, clamp((1 - smooth(0.1, 1, r + (n - 0.5) * 0.6)) * smooth(0.3, 0.6, n + 0.15), 0, 1) * 255];
  }],
  smoke: [64, 64, () => (u, v) => [255, 255, 255, (1 - smooth(0, 1, Math.hypot(u - 0.5, v - 0.5) * 2)) * 255]],
};

function runPixelJob(w, h, fn, out) {
  for (let y = 0; y < h; y++) for (let x = 0; x < w; x++) {
    const o = (y * w + x) * 4, p = fn(x / w, y / h, x, y);
    out[o] = p[0]; out[o + 1] = p[1]; out[o + 2] = p[2]; out[o + 3] = p.length > 3 ? p[3] : 255;
  }
  return out;
}
// Render all PIX textures in a small worker pool; fall back to the main thread if workers are unavailable.
function renderPixelTextures(onEach) {
  const names = Object.keys(PIX), results = {};
  const toCanvas = (name, w, h, data) => { const c = makeCanvas(w, h); c.getContext("2d").putImageData(new ImageData(data, w, h), 0, 0); results[name] = c; onEach && onEach(name); };
  const mainThread = async () => {
    for (const n of names) { if (results[n]) continue; const [w, h, f] = PIX[n]; toCanvas(n, w, h, runPixelJob(w, h, f(), new Uint8ClampedArray(w * h * 4))); await nextFrame(); }
    return results;
  };
  let pool = [];
  try {
    const src = [hash2, vnoise, fbm, runPixelJob].map((f) => f.toString()).join("\n") +
      `\nconst mix = ${mix}, clamp = ${clamp}, smooth = ${smooth}, mixc = ${mixc}, hex = ${hex};` +
      `\nconst PIX = {${names.map((n) => `${JSON.stringify(n)}: [${PIX[n][0]}, ${PIX[n][1]}, ${PIX[n][2]}]`).join(",")}};` +
      `\nonmessage = (e) => { const n = e.data, [w, h, f] = PIX[n], d = runPixelJob(w, h, f(), new Uint8ClampedArray(w * h * 4)); postMessage({ n, w, h, d }, [d.buffer]); };`;
    const url = URL.createObjectURL(new Blob([src], { type: "text/javascript" }));
    const count = Math.max(2, Math.min(4, (navigator.hardwareConcurrency || 4) - 1));
    for (let i = 0; i < count; i++) pool.push(new Worker(url));
  } catch (e) { pool = []; }
  if (!pool.length) return mainThread();
  return new Promise((resolve) => {
    const queue = names.slice().sort((a, b) => PIX[b][0] * PIX[b][1] - PIX[a][0] * PIX[a][1]);
    let pending = names.length, failed = false;
    const finish = () => { pool.forEach((w) => w.terminate()); resolve(failed ? mainThread() : results); };
    pool.forEach((w) => {
      const next = () => { const n = queue.shift(); if (n) w.postMessage(n); };
      w.onmessage = (e) => { const { n, w: tw, h, d } = e.data; toCanvas(n, tw, h, d); if (--pending === 0) finish(); else next(); };
      w.onerror = () => { failed = true; pending = 0; finish(); };
      next();
    });
  });
}

// Small vector-drawn textures: cheap, drawn on the main thread.
function drawCanvasTextures() {
  // wheat atlas: a white strip for stems and leaves (left), the ear with spikelets and awns (right)
  {
    const c = makeCanvas(128, 256), g = c.getContext("2d");
    g.fillStyle = "#ffffff"; g.fillRect(0, 0, 18, 256);
    const ear = g.createLinearGradient(24, 0, 128, 0); ear.addColorStop(0, "#c08f45"); ear.addColorStop(0.5, "#f1cf86"); ear.addColorStop(1, "#c08f45");
    g.fillStyle = ear; g.fillRect(18, 0, 110, 256);
    for (let row = 0; row < 15; row++) {
      const y = 250 - row * 12.5;
      for (let k = 0; k < 3; k++) {
        const x = 34 + k * 30 + (row % 2) * 15;
        const sg = g.createRadialGradient(x - 3, y - 4, 1, x, y, 15);
        sg.addColorStop(0, "#fbe2a6"); sg.addColorStop(0.7, "#d9ab5c"); sg.addColorStop(1, "rgba(140,96,40,.9)");
        g.fillStyle = sg; g.beginPath(); g.ellipse(x, y, 14, 9, 0, 0, Math.PI * 2); g.fill();
      }
    }
    g.fillStyle = "#e9cf8f"; g.fillRect(18, 0, 110, 66);
    g.strokeStyle = "rgba(255,240,200,.9)"; g.lineWidth = 2;
    for (let x = 24; x < 128; x += 7) { g.beginPath(); g.moveTo(x, 66); g.lineTo(x + (x - 76) * 0.12, 0); g.stroke(); }
    T.ear = tex(c, { wrap: false });
  }
  // shingles (staggered rows, used on the underlay)
  {
    const rows = 9, c = makeCanvas(512, 512), g = c.getContext("2d");
    g.fillStyle = "#2a241f"; g.fillRect(0, 0, 512, 512);
    for (let r = 0; r < rows; r++) {
      const y = r * (512 / rows); let x = (r % 2) * -20;
      while (x < 512) {
        const w = 26 + rnd() * 34, col = mixc(hex("#6d655b"), hex("#958b7e"), rnd());
        const grd = g.createLinearGradient(0, y, 0, y + 512 / rows);
        grd.addColorStop(0, `rgb(${col.map((k) => k * 0.72).join(",")})`); grd.addColorStop(0.85, `rgb(${col.join(",")})`); grd.addColorStop(1, `rgb(${col.map((k) => k * 0.55).join(",")})`);
        g.fillStyle = grd; g.fillRect(x + 1, y, w - 2, 512 / rows + 3); x += w;
      }
    }
    T.shingle = tex(c, { repeat: [2.2, 2.6] }); T.shingleBump = tex(c, { srgb: false, repeat: [2.2, 2.6] });
  }
  // window: dark room, lace curtain over the lower half, warm lamp behind
  {
    const w = makeCanvas(256, 256), g = w.getContext("2d");
    const bg = g.createRadialGradient(150, 175, 4, 150, 175, 170); bg.addColorStop(0, "#3a2614"); bg.addColorStop(1, "#0b0c0e");
    g.fillStyle = bg; g.fillRect(0, 0, 256, 256);
    g.fillStyle = "rgba(236,230,218,.9)";
    for (let y = 150; y < 256; y += 6) for (let x = (y / 6) % 2 ? 0 : 3; x < 256; x += 6) { g.beginPath(); g.arc(x, y, 1.6, 0, 7); g.fill(); }
    g.fillStyle = "rgba(236,230,218,.75)";
    for (let x = 0; x < 256; x += 12) { g.beginPath(); g.arc(x + 6, 150, 6, Math.PI, 0); g.fill(); }
    g.fillRect(0, 0, 34, 256); g.fillRect(222, 0, 34, 256);
    T.windowMap = tex(w, { wrap: false });
    const e = makeCanvas(128, 128), ge = e.getContext("2d");
    const eg = ge.createRadialGradient(75, 90, 2, 75, 90, 70); eg.addColorStop(0, "#ffb562"); eg.addColorStop(0.5, "#6b3a12"); eg.addColorStop(1, "#000");
    ge.fillStyle = eg; ge.fillRect(0, 0, 128, 128);
    T.windowGlow = tex(e, { wrap: false });
  }
  // bricks
  {
    const c = makeCanvas(256, 256), g = c.getContext("2d");
    g.fillStyle = "#cfc6b6"; g.fillRect(0, 0, 256, 256);
    for (let r = 0; r < 10; r++) for (let k = -1; k < 5; k++) {
      const col = mixc(hex("#8e4630"), hex("#b36b4c"), rnd());
      g.fillStyle = `rgb(${mixc(col, hex("#e6dccb"), rnd() > 0.55 ? 0.55 : 0.15).join(",")})`;
      g.fillRect(k * 64 + (r % 2) * 32 + 2, r * 25.6 + 2, 60, 21.6);
    }
    T.brick = tex(c, { repeat: [1, 2] });
  }
  // leaf clusters for the tree crowns: few, broad leaves around a solid centre (stable when moving)
  {
    const c = makeCanvas(256, 256), g = c.getContext("2d");
    const blob = g.createRadialGradient(128, 128, 10, 128, 128, 80); blob.addColorStop(0, "rgb(170,170,170)"); blob.addColorStop(1, "rgba(150,150,150,0)");
    g.fillStyle = blob; g.beginPath(); g.arc(128, 128, 80, 0, 7); g.fill();
    for (let i = 0; i < 34; i++) {
      const r = Math.sqrt(rnd()) * 92, a = rnd() * Math.PI * 2, x = 128 + Math.cos(a) * r, y = 128 + Math.sin(a) * r * 0.9;
      const v = 160 + rnd() * 95; g.fillStyle = `rgb(${v},${v},${v})`;
      g.save(); g.translate(x, y); g.rotate(rnd() * 6.28); g.beginPath(); g.ellipse(0, 0, 9 + rnd() * 6, 17 + rnd() * 9, 0, 0, Math.PI * 2); g.fill(); g.restore();
    }
    T.cluster = tex(c, { wrap: false });
  }
  // warm interior behind the door (visible once it opens)
  {
    const gl = makeCanvas(128, 256), g = gl.getContext("2d");
    const grd = g.createLinearGradient(0, 256, 0, 0); grd.addColorStop(0, "#ffcb7a"); grd.addColorStop(0.6, "#a85e1d"); grd.addColorStop(1, "#2a1405");
    g.fillStyle = grd; g.fillRect(0, 0, 128, 256);
    g.fillStyle = "rgba(20,10,4,.85)";
    [[22, 70, 26, 100], [53, 64, 24, 120], [84, 72, 26, 96]].forEach(([x, y, w, h]) => { g.fillRect(x + 6, y - 14, w - 12, 4); g.fillRect(x, y, w, h); });
    T.interior = tex(gl, { wrap: false });
  }
}
function texturesFromPixels(C) {
  T.log = tex(C.log); T.logBump = tex(C.log, { srgb: false });
  T.logEnd = tex(C.logEnd, { wrap: false });
  T.boards = tex(C.boards);
  T.door = tex(C.door, { wrap: false }); T.doorBump = tex(C.door, { srgb: false, wrap: false });
  T.path = tex(C.path);
  T.ground = tex(C.ground, { repeat: [90, 90] });
  T.canopy = tex(C.canopy, { repeat: [60, 60] });
  T.yard = tex(C.yard, { repeat: [7, 7] });
  T.shutter = tex(C.shutter, { wrap: false });
  T.birch = tex(C.birch, { repeat: [1, 3] });
  T.lemekh = tex(C.lemekh); T.lemekhBump = tex(C.lemekh, { srgb: false });
  T.cloud = tex(C.cloud, { wrap: false });
  T.smoke = tex(C.smoke, { wrap: false });
}

/* ==========================================================================
   Materials
   ========================================================================== */
const windU = { uTime: { value: 0 }, uWind: { value: new THREE.Vector2(0.86, -0.5).normalize() }, uGustAmp: { value: reduceMotion ? 0.3 : 1 }, uPx: { value: 0.001 } };
// Adds wind sway to any material. aH (0 = ground, 1 = tip) controls how much a vertex moves.
function windify(mat, { strength = 1, flutter = 1, sheen = true, ao = true, noBackfaceFlip = true, widen = false } = {}) {
  mat.customProgramCacheKey = () => `wind-${strength}-${flutter}-${sheen}-${ao}-${widen}`;
  mat.onBeforeCompile = (sh) => {
    sh.uniforms.uTime = windU.uTime; sh.uniforms.uWind = windU.uWind; sh.uniforms.uGustAmp = windU.uGustAmp; sh.uniforms.uPx = windU.uPx;
    sh.vertexShader = sh.vertexShader
      .replace("#include <common>", `#include <common>
        uniform float uTime; uniform vec2 uWind; uniform float uGustAmp;
        attribute float aH; varying float vH; varying float vGust;
        ${widen ? "attribute vec3 aOff; uniform float uPx;" : ""}`)
      .replace("#include <begin_vertex>", `#include <begin_vertex>
        vec3 wIpos = vec3(0.0);
        mat3 wIm = mat3(1.0);
        #ifdef USE_INSTANCING
          wIpos = (instanceMatrix * vec4(0.0, 0.0, 0.0, 1.0)).xyz;
          wIm = mat3(instanceMatrix);
        #endif
        vec3 wWp = (modelMatrix * vec4(wIpos, 1.0)).xyz;
        ${widen ? "transformed += aOff * max(1.0, distance(wWp, cameraPosition) * uPx / max(length(aOff), 1e-5));" : ""}
        float wave = sin(dot(wWp.xz, uWind) * 0.21 - uTime * 1.25) * 0.5 + 0.5;
        float wave2 = sin(dot(wWp.xz, vec2(-uWind.y, uWind.x)) * 0.09 + uTime * 0.37) * 0.5 + 0.5;
        float gust = pow(wave, 3.0) * (0.45 + 0.55 * wave2) * uGustAmp;
        float fl = sin(uTime * 2.6 + wWp.x * 1.9 + wWp.z * 1.3) * 0.6 + sin(uTime * 4.1 + wWp.z * 2.7 + wWp.x * 0.7) * 0.4;
        float k = aH * aH;
        float amt = ((0.06 + 0.36 * gust) * ${strength.toFixed(2)} + fl * 0.035 * ${flutter.toFixed(2)}) * k;
        vec3 wdir = vec3(uWind.x, 0.0, uWind.y);
        float s2 = max(dot(wIm[0], wIm[0]), 1e-4);
        vec3 ldir = (transpose(wIm) * wdir) / s2;
        transformed += ldir * amt;
        transformed.y -= amt * amt * 0.7 / sqrt(s2);
        vH = aH; vGust = gust;`);
    sh.fragmentShader = sh.fragmentShader
      .replace("#include <common>", `#include <common>
        varying float vH; varying float vGust;`)
      .replace("#include <color_fragment>", `#include <color_fragment>
        ${ao ? "diffuseColor.rgb *= 0.5 + 0.5 * smoothstep(0.0, 0.85, vH);" : ""}
        ${sheen ? "diffuseColor.rgb *= 1.0 + vGust * 0.35 * vH;" : ""}`);
    if (noBackfaceFlip) {
      sh.fragmentShader = sh.fragmentShader.replace("#include <normal_fragment_begin>",
        THREE.ShaderChunk.normal_fragment_begin.replace("normal *= faceDirection;", ""));
    }
  };
  return mat;
}

const M = {};
function buildMaterials() {
  M.log = new THREE.MeshStandardMaterial({ map: T.log, bumpMap: T.logBump, bumpScale: 2.2, roughness: 0.92, color: "#f2e6d8" });
  M.logEnd = new THREE.MeshStandardMaterial({ map: T.logEnd, roughness: 0.85 });
  M.inner = new THREE.MeshStandardMaterial({ color: "#2b2219", roughness: 1 });
  M.shingle = new THREE.MeshStandardMaterial({ map: T.shingle, bumpMap: T.shingleBump, bumpScale: 3, roughness: 0.9, color: "#e8e2da" });
  M.boards = new THREE.MeshStandardMaterial({ map: T.boards, roughness: 0.9 });
  M.paint = new THREE.MeshStandardMaterial({ color: "#ece4d3", roughness: 0.62 });
  M.blue = new THREE.MeshStandardMaterial({ color: "#2a5592", roughness: 0.7 });
  M.red = new THREE.MeshStandardMaterial({ color: "#9e2f25", roughness: 0.7 });
  M.shutter = new THREE.MeshStandardMaterial({ map: T.shutter, roughness: 0.75 });
  M.glass = new THREE.MeshStandardMaterial({ map: T.windowMap, emissiveMap: T.windowGlow, emissive: new THREE.Color("#ffb46a"), emissiveIntensity: 0.9, roughness: 0.06, metalness: 0.1, envMapIntensity: 1.4 });
  M.door = new THREE.MeshStandardMaterial({ map: T.door, bumpMap: T.doorBump, bumpScale: 2, roughness: 0.82 });
  M.iron = new THREE.MeshStandardMaterial({ color: "#1d1b19", roughness: 0.55, metalness: 0.85 });
  M.brass = new THREE.MeshStandardMaterial({ color: "#a8834a", roughness: 0.32, metalness: 0.95 });
  M.stone = new THREE.MeshStandardMaterial({ color: "#ffffff", roughness: 0.95 });
  M.brick = new THREE.MeshStandardMaterial({ map: T.brick, roughness: 0.95 });
  M.step = new THREE.MeshStandardMaterial({ map: T.boards, color: "#c9b8a6", roughness: 0.9 });
  M.ground = new THREE.MeshStandardMaterial({ map: T.ground, roughness: 1 });
  M.canopy = new THREE.MeshStandardMaterial({ map: T.canopy, roughness: 1 });
  M.path = new THREE.MeshStandardMaterial({ map: T.path, roughness: 1 });
  M.yard = new THREE.MeshStandardMaterial({ map: T.yard, roughness: 1 });
  M.stem = windify(new THREE.MeshStandardMaterial({ map: T.ear, vertexColors: true, roughness: 0.8, side: THREE.DoubleSide }), { widen: true });
  M.leaf = windify(new THREE.MeshStandardMaterial({ map: T.cluster, alphaTest: 0.5, alphaToCoverage: true, roughness: 0.8, side: THREE.DoubleSide }), { strength: 0.12, flutter: 0.5, sheen: false, ao: false });
  M.birch = new THREE.MeshStandardMaterial({ map: T.birch, roughness: 0.85 });
  M.bark = new THREE.MeshStandardMaterial({ color: "#6d5d4b", roughness: 1 });
  M.foliageCore = new THREE.MeshStandardMaterial({ vertexColors: true, roughness: 1 });
  M.interior = new THREE.MeshBasicMaterial({ map: T.interior, color: new THREE.Color(2.6, 2.1, 1.6), fog: false });
  M.lemekh = new THREE.MeshStandardMaterial({ map: T.lemekh, bumpMap: T.lemekhBump, bumpScale: 2.5, roughness: 0.88 });
  M.moss = new THREE.MeshStandardMaterial({ color: "#4f4a30", roughness: 1 });
  M.tin = new THREE.MeshStandardMaterial({ color: "#5f5c56", roughness: 0.5, metalness: 0.6 });
  Object.values(M).forEach((m) => { if (m.isMeshStandardMaterial && m !== M.glass) m.envMapIntensity = 0.5; });
}

/* ==========================================================================
   Geometry builders
   ========================================================================== */
function geoFrom({ pos, nor, uv, col, h, idx }) {
  const g = new THREE.BufferGeometry();
  g.setAttribute("position", new THREE.Float32BufferAttribute(pos, 3));
  g.setAttribute("normal", new THREE.Float32BufferAttribute(nor, 3));
  if (uv) g.setAttribute("uv", new THREE.Float32BufferAttribute(uv, 2));
  if (col) g.setAttribute("color", new THREE.Float32BufferAttribute(col, 3));
  g.setAttribute("aH", new THREE.Float32BufferAttribute(h, 1));
  g.setIndex(idx);
  return g;
}

// Wheat clump: thin stems, a drooping leaf, ears with spikelets and awns (two crossed ribbons).
// Ribbons store their centre line in `position` and the half-width in `aOff`; the vertex shader
// widens far ribbons so none gets thinner than ~1 px on screen — that is what stops the shimmer.
function buildWheatClump(stalks, { leaves = true, segs = 5, cross = 2 } = {}) {
  const G = { pos: [], off: [], nor: [], col: [], uv: [], h: [], idx: [] };
  const up = new THREE.Vector3(0, 1, 0), white = new THREE.Color(1, 1, 1);
  const stemLow = new THREE.Color("#8f7c3c"), stemHigh = new THREE.Color("#ecc97f"), leafCol = new THREE.Color("#dcc27f");
  const ribbon = (pts, widths, side, cols, hs, uvs) => {
    const base = G.pos.length / 3, n = new THREE.Vector3().crossVectors(side, up).normalize().lerp(up, 0.55).normalize();
    for (let i = 0; i < pts.length; i++) {
      const p = pts[i];
      for (const s of [-1, 1]) {
        G.pos.push(p.x, p.y, p.z); G.off.push(side.x * widths[i] * s, side.y * widths[i] * s, side.z * widths[i] * s);
        G.nor.push(n.x, n.y, n.z); G.col.push(cols[i].r, cols[i].g, cols[i].b); G.h.push(hs[i]);
        G.uv.push(uvs ? (s < 0 ? 0.16 : 0.99) : 0.06, uvs ? uvs[i] : 0.5);
      }
      if (i > 0) { const a = base + (i - 1) * 2; G.idx.push(a, a + 1, a + 2, a + 1, a + 3, a + 2); }
    }
  };
  for (let k = 0; k < stalks; k++) {
    const ang = rnd() * Math.PI * 2, rad = Math.sqrt(rnd()) * 0.17;
    const bx = Math.cos(ang) * rad, bz = Math.sin(ang) * rad, H = rr(0.82, 1.08);
    const lx = rr(-0.12, 0.12), lz = rr(-0.12, 0.12);
    const P = (t) => new THREE.Vector3(bx + lx * t * t, t * H, bz + lz * t * t);
    const face = rnd() * Math.PI, side = new THREE.Vector3(Math.cos(face), 0, Math.sin(face));
    const pts = [], ws = [], cs = [], hs = [];
    for (let i = 0; i <= segs; i++) { const t = (i / segs) * 0.84; pts.push(P(t)); ws.push(mix(0.0045, 0.0026, t)); cs.push(stemLow.clone().lerp(stemHigh, Math.pow(t / 0.84, 0.7))); hs.push((t * H) / 1.08); }
    ribbon(pts, ws, side, cs, hs);
    if (leaves) {
      const t0 = rr(0.25, 0.5), start = P(t0), da = rnd() * Math.PI * 2, dir = new THREE.Vector3(Math.cos(da), 0, Math.sin(da));
      const lside = new THREE.Vector3().crossVectors(dir, up).normalize(), len = rr(0.18, 0.28), lp = [], lw = [], lc = [], lh = [];
      for (let i = 0; i <= 4; i++) {
        const u = i / 4;
        lp.push(start.clone().addScaledVector(dir, u * len).add(new THREE.Vector3(0, 0.07 * u - 0.16 * u * u, 0)));
        lw.push(0.009 * Math.sin(Math.PI * clamp(u * 1.05 + 0.08, 0, 1)) + 0.0008); lc.push(leafCol.clone().multiplyScalar(0.85 + 0.15 * u)); lh.push(clamp((start.y + 0.04 * u) / 1.08, 0, 1));
      }
      ribbon(lp, lw, lside, lc, lh);
    }
    // ear: spindle-shaped body, then a narrow brush of awns
    const tip = P(0.84), axis = P(1.0).sub(tip).normalize(), earL = rr(0.12, 0.16), awn = rr(0.06, 0.09), total = earL + awn;
    const profile = [[0, 0.004], [0.2, 0.0095], [0.5, 0.011], [0.8, 0.009], [1, 0.0055], [1.35, 0.004], [1.6, 0.0012]];
    for (let c = 0; c < cross; c++) {
      const sd = new THREE.Vector3(Math.cos(face + c * Math.PI / 2), 0, Math.sin(face + c * Math.PI / 2)).projectOnPlane(axis).normalize();
      const ep = [], ew = [], ec = [], eh = [], ev = [];
      for (const [f, w] of profile) {
        const d = f <= 1 ? f * earL : earL + ((f - 1) / 0.6) * awn;
        const p = tip.clone().addScaledVector(axis, d); ep.push(p); ew.push(w); ec.push(white); eh.push(clamp(p.y / 1.08, 0, 1));
        ev.push(f <= 1 ? f * 0.72 : 0.72 + ((f - 1) / 0.6) * 0.28);
      }
      ribbon(ep, ew, sd, ec, eh, ev);
    }
  }
  const g = new THREE.BufferGeometry();
  g.setAttribute("position", new THREE.Float32BufferAttribute(G.pos, 3));
  g.setAttribute("aOff", new THREE.Float32BufferAttribute(G.off, 3));
  g.setAttribute("normal", new THREE.Float32BufferAttribute(G.nor, 3));
  g.setAttribute("color", new THREE.Float32BufferAttribute(G.col, 3));
  g.setAttribute("uv", new THREE.Float32BufferAttribute(G.uv, 2));
  g.setAttribute("aH", new THREE.Float32BufferAttribute(G.h, 1));
  g.setIndex(G.idx);
  g.boundingSphere = new THREE.Sphere(new THREE.Vector3(0, 0.6, 0), 1.2);
  return g;
}

/* ==========================================================================
   World layout
   ========================================================================== */
const HOUSE_POS = new THREE.Vector3(1.4, 0, -40);
const HOUSE_ROT = 0.42;
const HW = 3.3, HD = 2.7, R = 0.16, STEP = 0.29, COURSES = 10, BASE = 0.5;
const logY = (i) => BASE + R + i * STEP;
const TOP_Y = logY(COURSES - 1) + STEP / 2 + R;
const houseToWorld = (x, y, z) => new THREE.Vector3(x, y, z).applyAxisAngle(new THREE.Vector3(0, 1, 0), HOUSE_ROT).add(HOUSE_POS);
const FRONT_N = new THREE.Vector3(Math.sin(HOUSE_ROT), 0, Math.cos(HOUSE_ROT));
const DOOR_W = houseToWorld(0, 0, HD + R);
const STOP = DOOR_W.clone().addScaledVector(FRONT_N, 4.6);
const PORCH = DOOR_W.clone().addScaledVector(FRONT_N, 1.45);

const pathCurve = new THREE.CatmullRomCurve3([
  new THREE.Vector3(-0.4, 0, -6.2),
  new THREE.Vector3(0.6, 0, -11.5),
  new THREE.Vector3(3.6, 0, -17.2),
  houseToWorld(0, 0, 16.5),
  houseToWorld(0, 0, 12.5),
  STOP.clone().addScaledVector(FRONT_N, 1.6),
  STOP.clone(),
  PORCH.clone(),
], false, "centripetal", 0.5);
const PATH_LEN = pathCurve.getLength();
const pathSamples = pathCurve.getSpacedPoints(400);
let STOP_DIST = 0;
{ let best = 1e9; pathSamples.forEach((p, i) => { const d = p.distanceTo(STOP); if (d < best) { best = d; STOP_DIST = (i / 400) * PATH_LEN; } }); }
function distToPath(x, z) {
  let best = 1e9;
  for (let i = 0; i < pathSamples.length; i += 2) { const p = pathSamples[i], dx = p.x - x, dz = p.z - z, d = dx * dx + dz * dz; if (d < best) best = d; }
  return Math.sqrt(best);
}
function inYard(x, z) {
  const l = new THREE.Vector3(x - HOUSE_POS.x, 0, z - HOUSE_POS.z).applyAxisAngle(new THREE.Vector3(0, 1, 0), -HOUSE_ROT);
  return Math.pow(Math.abs(l.x) / (HW + 6.5), 4) + Math.pow(Math.abs(l.z - 0.6) / (HD + 6), 4) < 1 ? l : null;
}

function buildGround() {
  const g = new THREE.Mesh(new THREE.PlaneGeometry(900, 900), M.ground);
  g.rotation.x = -Math.PI / 2; g.receiveShadow = true; scene.add(g);
  // distant canopy: the top of the field beyond the planted area
  const outer = new THREE.Shape(); outer.moveTo(-900, -900); outer.lineTo(900, -900); outer.lineTo(900, 900); outer.lineTo(-900, 900); outer.closePath();
  const hole = new THREE.Path(); hole.moveTo(-54, 12); hole.lineTo(54, 12); hole.lineTo(54, -96); hole.lineTo(-54, -96); hole.closePath();
  outer.holes.push(hole);
  const cg = new THREE.ShapeGeometry(outer); cg.rotateX(-Math.PI / 2);
  const uv = cg.attributes.uv; for (let i = 0; i < uv.count; i++) uv.setXY(i, uv.getX(i) / 30, uv.getY(i) / 30);
  const canopy = new THREE.Mesh(cg, M.canopy); canopy.position.y = 0.86; canopy.receiveShadow = true;
  // flip because rotateX(-90) of a shape in xy puts y → -z
  canopy.scale.z = -1; scene.add(canopy);
  // yard
  const ys = new THREE.Shape(), A2 = HW + 6.5, B2 = HD + 6;
  for (let i = 0; i < 96; i++) { const th = (i / 96) * Math.PI * 2, c = Math.cos(th), sn = Math.sin(th), x = Math.sign(c) * Math.sqrt(Math.abs(c)) * A2, y = Math.sign(sn) * Math.sqrt(Math.abs(sn)) * B2; i ? ys.lineTo(x, y) : ys.moveTo(x, y); }
  const yg = new THREE.ShapeGeometry(ys); yg.rotateX(-Math.PI / 2);
  { const yuv = yg.attributes.uv; for (let i = 0; i < yuv.count; i++) yuv.setXY(i, yuv.getX(i) / (2 * A2) + 0.5, yuv.getY(i) / (2 * B2) + 0.5); }
  const yard = new THREE.Mesh(yg, M.yard); yard.receiveShadow = true;
  const yardHolder = new THREE.Group(); yardHolder.position.copy(HOUSE_POS); yardHolder.position.y = 0.012; yardHolder.rotation.y = HOUSE_ROT;
  yard.position.z = 0.6; yardHolder.add(yard); scene.add(yardHolder);
  // path ribbon
  const segs = 260, pos = [], nor = [], uvs = [], idx = [];
  for (let i = 0; i <= segs; i++) {
    const t = i / segs, p = pathCurve.getPointAt(t), tg = pathCurve.getTangentAt(t);
    const side = new THREE.Vector3(-tg.z, 0, tg.x).normalize();
    const w = 1.05 + Math.sin(t * 40) * 0.05;
    for (const s of [-1, 1]) { pos.push(p.x + side.x * w * s, 0.02, p.z + side.z * w * s); nor.push(0, 1, 0); uvs.push(s < 0 ? 0 : 1, (t * PATH_LEN) / 6); }
    if (i < segs) { const a = i * 2; idx.push(a, a + 2, a + 1, a + 1, a + 2, a + 3); }
  }
  const pg = new THREE.BufferGeometry();
  pg.setAttribute("position", new THREE.Float32BufferAttribute(pos, 3)); pg.setAttribute("normal", new THREE.Float32BufferAttribute(nor, 3)); pg.setAttribute("uv", new THREE.Float32BufferAttribute(uvs, 2)); pg.setIndex(idx);
  const path = new THREE.Mesh(pg, M.path); path.receiveShadow = true; scene.add(path);
}

function buildWheat() {
  const nearGeo = buildWheatClump(5, { leaves: true, segs: 5, cross: 2 });
  const farGeo = buildWheatClump(5, { leaves: false, segs: 3, cross: 1 });
  const near = new THREE.InstancedMesh(nearGeo, M.stem, Q.near), far = new THREE.InstancedMesh(farGeo, M.stem, Q.far);
  const m = new THREE.Matrix4(), q = new THREE.Quaternion(), s = new THREE.Vector3(), p = new THREE.Vector3(), c = new THREE.Color(), Y = new THREE.Vector3(0, 1, 0);
  const tones = ["#f6dfa8", "#ffe7b4", "#ecd099", "#f3d69c", "#e2c48c", "#fbe3b0"].map((h) => new THREE.Color(h));
  let nn = 0, nf = 0, tries = 0;
  while ((nn < Q.near || nf < Q.far) && tries < (Q.near + Q.far) * 12) {
    tries++;
    let x, z;
    const nearPath = rnd() < 0.55;
    if (nearPath) {
      const t = rnd() * 0.97, pp = pathCurve.getPointAt(t), tg = pathCurve.getTangentAt(t);
      const off = (rnd() < 0.5 ? -1 : 1) * (1.12 + Math.pow(rnd(), 1.7) * 10);
      x = pp.x - tg.z * off; z = pp.z + tg.x * off;
    } else { x = rr(-54, 54); z = rr(-96, 12); }
    const d = distToPath(x, z);
    if (d < 1.12 + rnd() * 0.12 || inYard(x, z)) continue;
    if (!nearPath && d >= 7 && rnd() > Math.max(0.1, Math.exp(-(d - 7) / 14))) continue;
    const isNear = d < 6;
    if (isNear ? nn >= Q.near : nf >= Q.far) continue;
    const sc = rr(0.9, 1.12) * (1 + smooth(8, 30, d) * 0.45);
    m.compose(p.set(x, 0, z), q.setFromAxisAngle(Y, rnd() * Math.PI * 2), s.set(sc, rr(0.92, 1.08) * (d < 1.6 ? 0.85 : 1), sc));
    c.copy(tones[(rnd() * tones.length) | 0]).multiplyScalar(rr(0.9, 1.04));
    if (isNear) { near.setMatrixAt(nn, m); near.setColorAt(nn, c); nn++; } else { far.setMatrixAt(nf, m); far.setColorAt(nf, c); nf++; }
  }
  near.count = nn; far.count = nf;
  for (const im of [near, far]) { im.receiveShadow = true; im.frustumCulled = false; scene.add(im); }
}

/* ---------- carved boards (white paint, holes) ---------- */
function scallopBoard(L, H, { teeth = 0.26, depth = 0.12, holes = true } = {}) {
  const s = new THREE.Shape();
  s.moveTo(0, 0); s.lineTo(L, 0); s.lineTo(L, -H);
  const n = Math.max(1, Math.round(L / teeth)), w = L / n;
  for (let i = n; i > 0; i--) { const x0 = i * w, x1 = (i - 1) * w; s.quadraticCurveTo((x0 + x1) / 2, -H - depth * 2, x1, -H); }
  s.lineTo(0, 0);
  if (holes) for (let i = 0; i < n; i++) {
    const cx = (i + 0.5) * w;
    const h = new THREE.Path(); h.absarc(cx, -H * 0.55, Math.min(0.045, w * 0.18), 0, Math.PI * 2, false); s.holes.push(h);
    if (i < n - 1) { const d = new THREE.Path(), dx = (i + 1) * w, dy = -H * 0.42, r = Math.min(0.035, w * 0.12); d.moveTo(dx, dy - r); d.lineTo(dx + r * 0.7, dy); d.lineTo(dx, dy + r); d.lineTo(dx - r * 0.7, dy); d.closePath(); s.holes.push(d); }
  }
  const g = new THREE.ExtrudeGeometry(s, { depth: 0.035, bevelEnabled: true, bevelThickness: 0.004, bevelSize: 0.004, bevelSegments: 1, curveSegments: 6 });
  return g;
}
function starPath(cx, cy, ro, ri, points = 8) {
  const p = new THREE.Path();
  for (let i = 0; i < points * 2; i++) { const a = (i / (points * 2)) * Math.PI * 2 + Math.PI / 2, r = i % 2 ? ri : ro; const x = cx + Math.cos(a) * r, y = cy + Math.sin(a) * r; i ? p.lineTo(x, y) : p.moveTo(x, y); }
  p.closePath(); return p;
}
function crownShape(W, base, peak, holeFn) {
  const s = new THREE.Shape();
  s.moveTo(-W / 2, 0); s.lineTo(W / 2, 0); s.lineTo(W / 2, base);
  s.quadraticCurveTo(W * 0.28, base * 1.15, W * 0.07, peak * 0.82);
  s.quadraticCurveTo(W * 0.035, peak * 0.98, 0, peak);
  s.quadraticCurveTo(-W * 0.035, peak * 0.98, -W * 0.07, peak * 0.82);
  s.quadraticCurveTo(-W * 0.28, base * 1.15, -W / 2, base);
  s.closePath();
  if (holeFn) holeFn(s);
  return s;
}

// rows of pointed aspen shingles (lemekh) in a local frame: x along the ridge, y up the slope, z out of the roof
function shingleRowsGeo(L, slopeLen, { rowH = 0.42, spacing = 0.3, tooth = 1 / 6, toothH = 0.11, tilt = 0.075 } = {}) {
  const geos = [], n = Math.max(1, Math.round(L / tooth)), w = L / n;
  for (let u = -0.04; u < slopeLen - 0.06; u += spacing) {
    const h = Math.min(rowH, slopeLen - u + 0.04);
    const s = new THREE.Shape();
    s.moveTo(0, 0); s.lineTo(0, -h + toothH);
    for (let k = 0; k < n; k++) { s.lineTo(k * w + w / 2, -h); s.lineTo((k + 1) * w, -h + toothH); }
    s.lineTo(L, 0); s.closePath();
    const g = new THREE.ExtrudeGeometry(s, { depth: 0.026, bevelEnabled: false, curveSegments: 1 });
    g.rotateX(-tilt); g.translate(0, u + h, 0);
    geos.push(g);
  }
  return mergeGeometries(geos);
}
// place a shingle field on one roof slope: sgn -1 = left slope rising toward +x, +1 = right slope
function onSlope(geo, sgn, E, eaveY, depth, ang, lift) {
  const c = Math.cos(ang), s = Math.sin(ang);
  const X = new THREE.Vector3(0, 0, sgn < 0 ? 1 : -1), Y = new THREE.Vector3(sgn < 0 ? c : -c, s, 0), Z = new THREE.Vector3(sgn < 0 ? -s : s, c, 0);
  const o = new THREE.Vector3(sgn * E, eaveY, sgn < 0 ? -depth / 2 : depth / 2).addScaledVector(Z, lift);
  return geo.clone().applyMatrix4(new THREE.Matrix4().makeBasis(X, Y, Z).setPosition(o));
}
function rosetteGeo(r) {
  const s = new THREE.Shape(); s.absarc(0, 0, r, 0, Math.PI * 2, false);
  for (let k = 0; k < 8; k++) { const a = (k / 8) * Math.PI * 2, h = new THREE.Path(); h.absarc(Math.cos(a) * r * 0.62, Math.sin(a) * r * 0.62, r * 0.16, 0, Math.PI * 2, true); s.holes.push(h); }
  const c = new THREE.Path(); c.absarc(0, 0, r * 0.2, 0, Math.PI * 2, true); s.holes.push(c);
  return new THREE.ExtrudeGeometry(s, { depth: 0.03, bevelEnabled: true, bevelSize: 0.005, bevelThickness: 0.005, bevelSegments: 1, curveSegments: 16 });
}
const lathe = (pts, seg) => new THREE.LatheGeometry(pts.map(([x, y]) => new THREE.Vector2(x, y)), seg);
function mesh(geo, mat, { cast = true, receive = true } = {}) { const m = new THREE.Mesh(geo, mat); m.castShadow = cast; m.receiveShadow = receive; return m; }

/* ---------- the izba ---------- */
const doorRig = { pivot: null, lock: null, glow: null, light: null, hit: [] };
function buildHouse() {
  const house = new THREE.Group(); house.position.copy(HOUSE_POS); house.rotation.y = HOUSE_ROT; scene.add(house);
  const sides = [], ends = [];
  const addLog = (axis, len, x, y, z) => {
    const r = R * rr(0.94, 1.06);
    const g = new THREE.CylinderGeometry(r, r, len, 18, 1, true);
    const uv = g.attributes.uv, off = rnd(), uo = axis === "x" ? 0 : -0.25;
    for (let i = 0; i < uv.count; i++) uv.setXY(i, uv.getX(i) + uo, uv.getY(i) * len / 2.4 + off * 3);
    if (axis === "x") g.rotateZ(Math.PI / 2); else g.rotateX(Math.PI / 2);
    g.translate(x, y, z); sides.push(g);
    for (const sgn of [-1, 1]) {
      const c = new THREE.CircleGeometry(r * 0.99, 18);
      const cuv = c.attributes.uv; const ro = rnd() * 6.28;
      for (let i = 0; i < cuv.count; i++) { const u = cuv.getX(i) - 0.5, v = cuv.getY(i) - 0.5; cuv.setXY(i, 0.5 + u * Math.cos(ro) - v * Math.sin(ro), 0.5 + u * Math.sin(ro) + v * Math.cos(ro)); }
      if (axis === "x") c.rotateY(sgn * Math.PI / 2); else if (sgn < 0) c.rotateY(Math.PI);
      if (axis === "x") c.translate(x + sgn * len / 2, y, z); else c.translate(x, y, z + sgn * len / 2);
      ends.push(c);
    }
  };
  const OVER = 0.36;
  // openings by course index
  const frontOpen = [{ x0: -0.55, x1: 0.55, c0: 0, c1: 6 }, { x0: -2.6, x1: -1.6, c0: 3, c1: 6 }, { x0: 1.6, x1: 2.6, c0: 3, c1: 6 }];
  const sideOpen = [{ x0: -0.5, x1: 0.5, c0: 3, c1: 6 }];
  const segments = (a, b, opens, i) => {
    let segs = [[a, b]];
    for (const o of opens) if (i >= o.c0 && i <= o.c1) segs = segs.flatMap(([s0, s1]) => (o.x1 <= s0 || o.x0 >= s1) ? [[s0, s1]] : [[s0, o.x0], [o.x1, s1]].filter(([u, v]) => v - u > 0.05));
    return segs;
  };
  for (let i = 0; i < COURSES; i++) {
    const y = logY(i);
    for (const [s0, s1] of segments(-HW - OVER, HW + OVER, frontOpen, i)) addLog("x", s1 - s0, (s0 + s1) / 2, y, HD);
    addLog("x", 2 * (HW + OVER), 0, y, -HD);
    const ys = y + STEP / 2;
    for (const [s0, s1] of segments(-HD - OVER, HD + OVER, sideOpen, i)) addLog("z", s1 - s0, -HW, ys, (s0 + s1) / 2);
    addLog("z", 2 * (HD + OVER), HW, ys, 0);
  }
  house.add(mesh(mergeGeometries(sides), M.log), mesh(mergeGeometries(ends), M.logEnd));
  // moss caulking pressed into the grooves between the logs
  {
    const moss = [];
    const addMoss = (axis, a0, a1, y, c) => {
      if (a1 - a0 < 0.1) return;
      const g = new THREE.CylinderGeometry(0.026, 0.03, a1 - a0, 5, 1, true);
      if (axis === "x") { g.rotateZ(Math.PI / 2); g.translate((a0 + a1) / 2, y, c); } else { g.rotateX(Math.PI / 2); g.translate(c, y, (a0 + a1) / 2); }
      moss.push(g);
    };
    const widen = (opens) => opens.map((o) => ({ ...o, c0: o.c0 - 1 }));
    for (let i = 0; i < COURSES - 1; i++) {
      const yf = logY(i) + STEP / 2, ys = logY(i) + STEP;
      for (const [s0, s1] of segments(-HW - 0.1, HW + 0.1, widen(frontOpen), i)) addMoss("x", s0, s1, yf, HD + R * 0.55);
      addMoss("x", -HW - 0.1, HW + 0.1, yf, -HD - R * 0.55);
      for (const [s0, s1] of segments(-HD - 0.1, HD + 0.1, widen(sideOpen), i)) addMoss("z", s0, s1, ys, -HW - R * 0.55);
      addMoss("z", -HD - 0.1, HD + 0.1, ys, HW + R * 0.55);
    }
    house.add(mesh(mergeGeometries(moss), M.moss, { cast: false }));
  }

  // dark core: shows between logs and inside openings
  const core = mesh(new THREE.BoxGeometry(2 * HW - 0.18, TOP_Y - BASE, 2 * HD - 0.18), M.inner);
  core.position.y = (TOP_Y + BASE) / 2; house.add(core);

  // stone foundation
  const stoneGeo = new THREE.IcosahedronGeometry(0.17, 2); { const sp = stoneGeo.attributes.position; for (let i = 0; i < sp.count; i++) { const v = new THREE.Vector3().fromBufferAttribute(sp, i); v.multiplyScalar(0.85 + vnoise(v.x * 9 + 3, v.y * 9 + v.z * 7, 999, 999) * 0.3); sp.setXYZ(i, v.x, v.y, v.z); } stoneGeo.computeVertexNormals(); }
  const stones = new THREE.InstancedMesh(stoneGeo, M.stone, 420);
  const m = new THREE.Matrix4(), q = new THREE.Quaternion(), e = new THREE.Euler(), sc = new THREE.Vector3(), p = new THREE.Vector3(), col = new THREE.Color();
  let si = 0;
  const edge = (ax, az, bx, bz) => {
    const len = Math.hypot(bx - ax, bz - az), n = Math.floor(len / 0.24);
    for (let k = 0; k <= n; k++) for (let row = 0; row < 3; row++) {
      if (si >= 420) return;
      const t = (k + (row ? 0.5 : 0)) / n;
      p.set(mix(ax, bx, t) + rr(-0.02, 0.02), 0.07 + row * 0.15, mix(az, bz, t) + rr(-0.02, 0.02));
      q.setFromEuler(e.set(rnd() * 3, rnd() * 3, rnd() * 3));
      sc.set(rr(0.75, 1.05), rr(0.5, 0.62), rr(0.75, 1.0));
      stones.setMatrixAt(si, m.compose(p, q, sc));
      stones.setColorAt(si, col.setHSL(rr(0.06, 0.12), rr(0.05, 0.14), rr(0.2, 0.32)));
      si++;
    }
  };
  edge(-HW, HD, HW, HD); edge(-HW, -HD, HW, -HD); edge(-HW, -HD, -HW, HD); edge(HW, -HD, HW, HD);
  stones.count = si; stones.castShadow = stones.receiveShadow = true; house.add(stones);

  // roof
  const ANG = THREE.MathUtils.degToRad(39), tanA = Math.tan(ANG);
  const E = HW + 0.78, eaveY = TOP_Y - (E - HW) * tanA, apexY = TOP_Y + HW * tanA;
  const slope = E / Math.cos(ANG) + 0.12, depth = 2 * HD + 1.6, thick = 0.14;
  for (const sgn of [-1, 1]) {
    const g = new THREE.BoxGeometry(slope, thick, depth);
    const uv = g.attributes.uv; for (let i = 0; i < uv.count; i++) uv.setXY(i, uv.getX(i), uv.getY(i));
    const r = mesh(g, M.shingle);
    r.rotation.z = -sgn * ANG;
    const mx = sgn * E / 2, my = (eaveY + apexY) / 2;
    r.position.set(mx + Math.sin(ANG) * thick / 2 * sgn * 1, my + Math.cos(ANG) * thick / 2, 0);
    house.add(r);
  }
  // pointed shingle rows (lemekh), ridge boards, rafter tails, carved front brackets
  {
    const rows = shingleRowsGeo(depth, E / Math.cos(ANG));
    house.add(mesh(mergeGeometries([-1, 1].map((sgn) => onSlope(rows, sgn, E, eaveY, depth, ANG, thick))), M.lemekh));
    const yTop = (x) => apexY + thick / Math.cos(ANG) - Math.abs(x) * tanA;
    for (const sgn of [-1, 1]) {
      const xc = sgn * 0.15 * Math.cos(ANG);
      const cap = mesh(new THREE.BoxGeometry(0.34, 0.035, depth + 0.04), M.lemekh); cap.rotation.z = -sgn * ANG; cap.position.set(xc, yTop(xc) + 0.065, 0); house.add(cap);
    }
    const tails = [], tlen = (E - HW) / Math.cos(ANG) + 0.05;
    for (const sgn of [-1, 1]) for (let z = -HD - 0.55; z <= HD + 0.6; z += 0.6) {
      const b = new THREE.BoxGeometry(tlen, 0.1, 0.07); b.rotateZ(-sgn * ANG);
      b.translate(sgn * (HW + E) / 2, TOP_Y - ((E - HW) / 2) * tanA - 0.06, z); tails.push(b);
    }
    house.add(mesh(mergeGeometries(tails), M.step));
    const s = new THREE.Shape();
    s.moveTo(0, -0.62); s.quadraticCurveTo(0.06, -0.16, 0.6, -0.05); s.lineTo(0.6, 0.03); s.lineTo(0, 0.03); s.closePath();
    const hole = new THREE.Path(); hole.absarc(0.13, -0.11, 0.04, 0, Math.PI * 2, true); s.holes.push(hole);
    const bgeo = new THREE.ExtrudeGeometry(s, { depth: 0.08, bevelEnabled: false, curveSegments: 10 }); bgeo.rotateY(-Math.PI / 2); bgeo.translate(0.04, 0, 0);
    for (const sgn of [-1, 1]) { const br = mesh(bgeo, M.paint); br.position.set(sgn * (HW + 0.2), TOP_Y - 0.2 * tanA - 0.03, HD + R); house.add(br); }
  }
  // gables (front + back)
  for (const z of [HD + 0.06, -HD - 0.06]) {
    const s = new THREE.Shape(); s.moveTo(-HW - 0.1, TOP_Y - 0.1); s.lineTo(HW + 0.1, TOP_Y - 0.1); s.lineTo(0, apexY - 0.05); s.closePath();
    if (z > 0) { const h = new THREE.Path(); const wy = TOP_Y + 1.05; h.moveTo(-0.32, wy - 0.3); h.lineTo(0.32, wy - 0.3); h.lineTo(0.32, wy + 0.22); h.lineTo(0, wy + 0.42); h.lineTo(-0.32, wy + 0.22); h.closePath(); s.holes.push(h); }
    const g = new THREE.ExtrudeGeometry(s, { depth: 0.06, bevelEnabled: false });
    const uv = g.attributes.uv; for (let i = 0; i < uv.count; i++) uv.setXY(i, uv.getX(i) / 1.1, uv.getY(i) / 1.6);
    const gm = mesh(g, M.boards); gm.position.z = z > 0 ? z - 0.06 : z; house.add(gm);
  }
  // attic window (svetyolka)
  {
    const wy = TOP_Y + 1.05;
    const glass = mesh(new THREE.PlaneGeometry(0.66, 0.74), M.glass); glass.position.set(0, wy + 0.06, HD - 0.02); house.add(glass);
    const fr = new THREE.Shape(); fr.moveTo(-0.46, wy - 0.42); fr.lineTo(0.46, wy - 0.42); fr.lineTo(0.46, wy + 0.28); fr.lineTo(0, wy + 0.6); fr.lineTo(-0.46, wy + 0.28); fr.closePath();
    const inner = new THREE.Path(); inner.moveTo(-0.32, wy - 0.3); inner.lineTo(0.32, wy - 0.3); inner.lineTo(0.32, wy + 0.22); inner.lineTo(0, wy + 0.42); inner.lineTo(-0.32, wy + 0.22); inner.closePath(); fr.holes.push(inner);
    const fg = mesh(new THREE.ExtrudeGeometry(fr, { depth: 0.05, bevelEnabled: false }), M.paint); fg.position.z = HD + 0.02; house.add(fg);
    const bar = mesh(new THREE.BoxGeometry(0.04, 0.7, 0.03), M.paint); bar.position.set(0, wy + 0.04, HD + 0.0); house.add(bar);
    const bar2 = mesh(new THREE.BoxGeometry(0.64, 0.04, 0.03), M.paint); bar2.position.set(0, wy + 0.02, HD + 0.0); house.add(bar2);
  }
  // carved sun rosettes on the gable
  for (const sgn of [-1, 1]) {
    const y = TOP_Y + 0.78;
    const ro = mesh(rosetteGeo(0.15), M.paint); ro.position.set(sgn * 0.98, y, HD + 0.065); house.add(ro);
    const bg = mesh(new THREE.CircleGeometry(0.14, 24), M.red, { cast: false }); bg.position.set(sgn * 0.98, y, HD + 0.062); house.add(bg);
  }
  // carved bargeboards (prichelina) + hanging board (polotentse)
  {
    const L = slope - 0.05;
    const right = new THREE.Group();
    const b = mesh(scallopBoard(L, 0.3, { teeth: 0.28, depth: 0.1 }), M.paint); right.add(b);
    right.position.set(0, apexY + 0.02, HD + 0.8); right.rotation.z = -ANG; house.add(right);
    const leftWrap = new THREE.Group(); leftWrap.scale.x = -1; house.add(leftWrap);
    const left = right.clone(); leftWrap.add(left);
    const pt = new THREE.Shape(); pt.moveTo(-0.17, 0); pt.lineTo(0.17, 0); pt.lineTo(0.17, -0.95); pt.quadraticCurveTo(0.09, -1.02, 0.05, -1.12); pt.lineTo(0, -1.22); pt.lineTo(-0.05, -1.12); pt.quadraticCurveTo(-0.09, -1.02, -0.17, -0.95); pt.closePath();
    pt.holes.push(starPath(0, -0.5, 0.11, 0.05));
    [[-0.32], [-0.75]].forEach(([y]) => { const h = new THREE.Path(); h.absarc(0, y, 0.035, 0, Math.PI * 2, false); pt.holes.push(h); });
    const pg = mesh(new THREE.ExtrudeGeometry(pt, { depth: 0.04, bevelEnabled: false, curveSegments: 8 }), M.paint); pg.position.set(0, apexY - 0.12, HD + 0.82); house.add(pg);
    const pb = mesh(new THREE.PlaneGeometry(0.26, 0.26), M.red); pb.position.set(0, apexY - 0.62, HD + 0.815); house.add(pb);
    // valance under the gable
    const v = mesh(scallopBoard(2 * HW + 0.9, 0.22, { teeth: 0.3, depth: 0.08 }), M.paint); v.position.set(-HW - 0.45, TOP_Y + 0.08, HD + 0.2); house.add(v);
  }
  // ridge log + horse (konek)
  {
    const ridge = mesh(new THREE.CylinderGeometry(0.13, 0.13, depth + 0.3, 14), M.log); ridge.rotation.x = Math.PI / 2; ridge.position.set(0, apexY + 0.1, 0.1); house.add(ridge);
    const s = new THREE.Shape();
    s.moveTo(0, 0); s.lineTo(0.02, 0.36); s.quadraticCurveTo(0.06, 0.6, 0.26, 0.66); s.lineTo(0.3, 0.8); s.lineTo(0.34, 0.66); s.lineTo(0.56, 0.5); s.quadraticCurveTo(0.6, 0.45, 0.54, 0.42); s.lineTo(0.36, 0.44); s.quadraticCurveTo(0.24, 0.38, 0.24, 0.2); s.lineTo(0.18, 0); s.closePath();
    const hg = new THREE.ExtrudeGeometry(s, { depth: 0.1, bevelEnabled: true, bevelSize: 0.01, bevelThickness: 0.01, bevelSegments: 1 });
    hg.rotateY(-Math.PI / 2); hg.translate(0.05, 0, 0);
    const horse = mesh(hg, M.log); horse.position.set(0, apexY + 0.12, HD + 0.75); house.add(horse);
  }
  // chimney
  {
    const ch = mesh(new THREE.BoxGeometry(0.62, 1.9, 0.62), M.brick); ch.position.set(1.05, apexY - 0.25, -0.9); house.add(ch);
    const cap = mesh(new THREE.BoxGeometry(0.78, 0.08, 0.78), M.brick); cap.position.set(1.05, apexY + 0.74, -0.9); house.add(cap);
    const band = mesh(new THREE.BoxGeometry(0.7, 0.09, 0.7), M.brick); band.position.set(1.05, apexY + 0.5, -0.9); house.add(band);
    for (const [dx, dz] of [[-0.27, -0.27], [0.27, -0.27], [-0.27, 0.27], [0.27, 0.27]]) { const p = mesh(new THREE.BoxGeometry(0.05, 0.22, 0.05), M.tin); p.position.set(1.05 + dx, apexY + 0.89, -0.9 + dz); house.add(p); }
    const hood = mesh(new THREE.ConeGeometry(0.56, 0.3, 4, 1), M.tin); hood.rotation.y = Math.PI / 4; hood.position.set(1.05, apexY + 1.15, -0.9); house.add(hood);
    house.userData.chimneyTop = new THREE.Vector3(1.05, apexY + 0.8, -0.9);
  }

  // windows: six-pane sash, carved frames (nalichniki) over a blue ground, sun rosette, flower box, hinged shutters
  const windowAt = (parent, cx, w, y0, y1, zf) => {
    const h = y1 - y0, cy = (y0 + y1) / 2, W = w + 0.42;
    const glass = mesh(new THREE.PlaneGeometry(w + 0.04, h + 0.04), M.glass, { cast: false }); glass.position.set(cx, cy, zf - R - 0.04); parent.add(glass);
    const t = 0.045, sash = [];
    [[w, t, 0, h / 2 - t / 2], [w, t, 0, -h / 2 + t / 2], [t, h, -w / 2 + t / 2, 0], [t, h, w / 2 - t / 2, 0], [t * 0.7, h, -w / 6, 0], [t * 0.7, h, w / 6, 0], [w, t * 0.8, 0, h * 0.08]]
      .forEach(([sw, sh, ox, oy]) => sash.push(new THREE.BoxGeometry(sw, sh, 0.04).translate(cx + ox, cy + oy, zf - R - 0.01)));
    parent.add(mesh(mergeGeometries(sash), M.paint));
    const sideH = h + 0.26, side = new THREE.Shape();
    side.moveTo(-0.065, -sideH / 2); side.lineTo(0.065, -sideH / 2); side.lineTo(0.065, sideH / 2); side.lineTo(-0.065, sideH / 2); side.closePath();
    for (let y = -sideH / 2 + 0.16; y < sideH / 2 - 0.12; y += 0.2) { const d = new THREE.Path(), r = 0.032; d.moveTo(0, y - r); d.lineTo(-r * 0.75, y); d.lineTo(0, y + r); d.lineTo(r * 0.75, y); d.closePath(); side.holes.push(d); }
    const sideGeo = new THREE.ExtrudeGeometry(side, { depth: 0.04, bevelEnabled: true, bevelSize: 0.005, bevelThickness: 0.005, bevelSegments: 1 });
    for (const sgn of [-1, 1]) {
      const sm = mesh(sideGeo, M.paint); sm.position.set(cx + sgn * (w / 2 + 0.065), cy, zf + 0.012); parent.add(sm);
      const bg = mesh(new THREE.PlaneGeometry(0.1, sideH - 0.04), M.blue, { cast: false }); bg.position.set(cx + sgn * (w / 2 + 0.065), cy, zf + 0.006); parent.add(bg);
    }
    const cor = mesh(new THREE.BoxGeometry(W + 0.12, 0.06, 0.12), M.paint); cor.position.set(cx, y1 + 0.16, zf + 0.06); parent.add(cor);
    const crown = crownShape(W, 0.17, 0.56, (s) => {
      const c = new THREE.Path(); c.absarc(0, 0.32, 0.06, 0, Math.PI * 2, false); s.holes.push(c);
      [-1, 1].forEach((k) => { const d = new THREE.Path(), x = k * W * 0.27, y = 0.1, r = 0.045; d.moveTo(x, y - r); d.lineTo(x + r * 0.8, y); d.lineTo(x, y + r); d.lineTo(x - r * 0.8, y); d.closePath(); s.holes.push(d); });
    });
    const cg = mesh(new THREE.ExtrudeGeometry(crown, { depth: 0.04, bevelEnabled: true, bevelSize: 0.006, bevelThickness: 0.006, bevelSegments: 1, curveSegments: 10 }), M.paint);
    cg.position.set(cx, y1 + 0.19, zf + 0.02); parent.add(cg);
    const cb = mesh(new THREE.ShapeGeometry(crownShape(W - 0.06, 0.15, 0.5)), M.blue, { cast: false }); cb.position.set(cx, y1 + 0.2, zf + 0.012); parent.add(cb);
    const ro = mesh(rosetteGeo(0.075), M.paint); ro.position.set(cx, y1 + 0.19 + 0.32, zf + 0.07); parent.add(ro);
    const sill = mesh(new THREE.BoxGeometry(W + 0.06, 0.07, 0.16), M.paint); sill.position.set(cx, y0 - 0.1, zf + 0.06); parent.add(sill);
    const apron = mesh(scallopBoard(W - 0.04, 0.16, { teeth: 0.2, depth: 0.06 }), M.paint); apron.position.set(cx - (W - 0.04) / 2, y0 - 0.14, zf + 0.02); parent.add(apron);
    // shutters with strap hinges
    const hinges = [];
    for (const sgn of [-1, 1]) {
      const sw = w / 2 + 0.04, sx = cx + sgn * (w / 2 + 0.15 + sw / 2);
      const sh = mesh(new THREE.BoxGeometry(sw, h + 0.16, 0.035), M.shutter); sh.position.set(sx, cy, zf + 0.02); parent.add(sh);
      if (sgn < 0) sh.scale.x = -1;
      for (const hy of [cy - h * 0.33, cy + h * 0.33]) hinges.push(new THREE.BoxGeometry(0.2, 0.026, 0.012).translate(sx + sgn * (sw / 2 - 0.1), hy, zf + 0.044));
    }
    parent.add(mesh(mergeGeometries(hinges), M.iron));
  };
  const wy0 = logY(2) + R - 0.02, wy1 = logY(7) - R + 0.02;
  windowAt(house, -2.1, 0.92, wy0, wy1, HD + R);
  windowAt(house, 2.1, 0.92, wy0, wy1, HD + R);
  const sideWin = new THREE.Group(); sideWin.position.set(-HW, 0, 0); sideWin.rotation.y = -Math.PI / 2; house.add(sideWin);
  windowAt(sideWin, 0, 0.92, wy0 + STEP / 2, wy1 + STEP / 2, R);

  // door: plank leaf on a hinge pivot, iron straps, ring, padlock
  {
    const dW = 1.06, dH = logY(7) - R - BASE + 0.01, z = HD + R;
    const pivot = new THREE.Group(); pivot.position.set(-dW / 2, BASE, HD - 0.02); house.add(pivot);
    const leaf = mesh(new THREE.BoxGeometry(dW, dH, 0.07), [M.door, M.door, M.door, M.door, M.door, M.door]); leaf.position.set(dW / 2, dH / 2, 0); pivot.add(leaf);
    for (const hy of [0.32, dH - 0.38]) {
      const strap = mesh(new THREE.BoxGeometry(0.72, 0.06, 0.012), M.iron); strap.position.set(0.38, hy, 0.042); pivot.add(strap);
      const tipg = new THREE.CylinderGeometry(0.045, 0.045, 0.012, 16); tipg.rotateX(Math.PI / 2);
      const tip = mesh(tipg, M.iron); tip.position.set(0.74, hy, 0.042); pivot.add(tip);
      for (let k = 0; k < 4; k++) { const rv = mesh(new THREE.SphereGeometry(0.011, 8, 6), M.iron); rv.position.set(0.1 + k * 0.17, hy, 0.05); pivot.add(rv); }
    }
    const ring = mesh(new THREE.TorusGeometry(0.06, 0.009, 8, 28), M.iron); ring.position.set(dW - 0.2, dH * 0.5, 0.06); pivot.add(ring);
    const plate = mesh(new THREE.CylinderGeometry(0.035, 0.035, 0.01, 16).rotateX(Math.PI / 2), M.iron); plate.position.set(dW - 0.2, dH * 0.5 + 0.06, 0.04); pivot.add(plate);
    // hasp + padlock (hangs from a staple on the frame, swings when you try the door)
    const staple = mesh(new THREE.TorusGeometry(0.03, 0.007, 6, 16, Math.PI), M.iron); staple.position.set(dW / 2 + 0.06, BASE + dH * 0.47, z + 0.075); house.add(staple);
    const hasp = mesh(new THREE.BoxGeometry(0.22, 0.045, 0.012), M.iron); hasp.position.set(dW - 0.08, dH * 0.47, 0.045); pivot.add(hasp);
    const lock = new THREE.Group(); lock.position.set(dW / 2 + 0.06, BASE + dH * 0.47 - 0.01, z + 0.09); house.add(lock);
    const body = new THREE.Shape(); const bw = 0.11, bh = 0.13, br = 0.025;
    body.moveTo(-bw / 2 + br, -bh); body.lineTo(bw / 2 - br, -bh); body.quadraticCurveTo(bw / 2, -bh, bw / 2, -bh + br); body.lineTo(bw / 2, -0.03); body.lineTo(-bw / 2, -0.03); body.lineTo(-bw / 2, -bh + br); body.quadraticCurveTo(-bw / 2, -bh, -bw / 2 + br, -bh);
    const kh = new THREE.Path(); kh.absarc(0, -0.075, 0.011, 0, Math.PI * 2, false); body.holes.push(kh);
    const bg = new THREE.ExtrudeGeometry(body, { depth: 0.04, bevelEnabled: true, bevelSize: 0.006, bevelThickness: 0.006, bevelSegments: 2 }); bg.translate(0, 0, -0.02);
    lock.add(mesh(bg, M.brass));
    const shackle = mesh(new THREE.TorusGeometry(0.036, 0.008, 8, 24, Math.PI), M.iron); shackle.position.set(0, -0.03, 0); lock.add(shackle);
    doorRig.pivot = pivot; doorRig.lock = lock; doorRig.hit = [leaf, ...lock.children];
    // frame + crown with the eight-pointed star (alatyr)
    for (const sgn of [-1, 1]) { const side = mesh(new THREE.BoxGeometry(0.15, dH + 0.18, 0.05), M.paint); side.position.set(sgn * (dW / 2 + 0.075), BASE + dH / 2 + 0.05, z + 0.03); house.add(side); }
    const CW = dW + 0.62;
    const crown = crownShape(CW, 0.2, 0.7, (s) => { s.holes.push(starPath(0, 0.37, 0.13, 0.065)); [-1, 1].forEach((k) => { const c = new THREE.Path(); c.absarc(k * CW * 0.28, 0.11, 0.045, 0, Math.PI * 2, false); s.holes.push(c); }); });
    const cg = mesh(new THREE.ExtrudeGeometry(crown, { depth: 0.045, bevelEnabled: true, bevelSize: 0.006, bevelThickness: 0.006, bevelSegments: 1, curveSegments: 10 }), M.paint);
    cg.position.set(0, BASE + dH + 0.12, z + 0.02); house.add(cg);
    const cb = mesh(new THREE.ShapeGeometry(crownShape(CW - 0.08, 0.17, 0.64)), M.red, { cast: false }); cb.position.set(0, BASE + dH + 0.13, z + 0.012); house.add(cb);
    // porch: deck, two steps, turned balusters, posts with finials
    {
      const dkW = 2.3, dkD = 1.3, z0 = HD + 0.1, top = BASE;
      const deck = mesh(new THREE.BoxGeometry(dkW, 0.07, dkD), M.step); deck.position.set(0, top - 0.035, z0 + dkD / 2); house.add(deck);
      const skirts = [new THREE.BoxGeometry(dkW, top - 0.07, 0.04).translate(0, (top - 0.07) / 2, z0 + dkD - 0.02)];
      for (const sgn of [-1, 1]) skirts.push(new THREE.BoxGeometry(0.04, top - 0.07, dkD).translate(sgn * (dkW / 2 - 0.02), (top - 0.07) / 2, z0 + dkD / 2));
      for (let k = 0; k < 2; k++) {
        const sTop = top - 0.167 * (k + 1), sz = z0 + dkD + 0.15 + k * 0.3;
        skirts.push(new THREE.BoxGeometry(1.16, sTop - 0.035, 0.3).translate(0, (sTop - 0.035) / 2, sz));
        const tread = mesh(new THREE.BoxGeometry(1.22, 0.035, 0.34), M.step); tread.position.set(0, sTop - 0.0175, sz + 0.02); house.add(tread);
      }
      house.add(mesh(mergeGeometries(skirts), M.boards));
      const bal = lathe([[0, 0], [0.032, 0], [0.032, 0.05], [0.02, 0.09], [0.028, 0.2], [0.042, 0.33], [0.03, 0.46], [0.018, 0.54], [0.028, 0.6], [0.028, 0.66], [0, 0.66]], 10);
      const fin = lathe([[0, 0], [0.05, 0], [0.05, 0.03], [0.075, 0.09], [0.045, 0.17], [0.018, 0.21], [0.024, 0.25], [0, 0.29]], 12);
      const bals = [], rails = [], posts = [];
      const railH = 0.74, x1 = dkW / 2 - 0.07, zf = z0 + dkD - 0.07, xo = 0.66;
      const run = (ax, az, bx, bz) => {
        const len = Math.hypot(bx - ax, bz - az), n = Math.max(1, Math.round(len / 0.14)), alongX = Math.abs(bx - ax) > Math.abs(bz - az);
        for (let k = 1; k < n; k++) bals.push(bal.clone().translate(mix(ax, bx, k / n), top + 0.06, mix(az, bz, k / n)));
        for (const [y, hgt] of [[top + 0.06, 0.05], [top + railH, 0.06]]) rails.push(new THREE.BoxGeometry(alongX ? len : 0.08, hgt, alongX ? 0.08 : len).translate((ax + bx) / 2, y, (az + bz) / 2));
      };
      run(-x1, z0 + 0.05, -x1, zf); run(x1, z0 + 0.05, x1, zf); run(-x1, zf, -xo, zf); run(xo, zf, x1, zf);
      for (const [x, z] of [[-x1, zf], [x1, zf], [-xo, zf], [xo, zf]]) { posts.push(new THREE.BoxGeometry(0.12, railH + 0.12, 0.12).translate(x, top + (railH + 0.12) / 2, z)); posts.push(fin.clone().translate(x, top + railH + 0.12, z)); }
      house.add(mesh(mergeGeometries(bals), M.paint), mesh(mergeGeometries(rails), M.step), mesh(mergeGeometries(posts), M.paint));
    }
    // warm interior, only visible when the door is open
    const glow = new THREE.Mesh(new THREE.PlaneGeometry(dW, dH), M.interior); glow.position.set(0, BASE + dH / 2, HD - 0.08); glow.visible = false; house.add(glow);
    const light = new THREE.PointLight("#ffb366", 0, 9, 1.6); light.position.set(0, BASE + 1.4, HD - 0.4); house.add(light);
    doorRig.glow = glow; doorRig.light = light;
  }

  return house;
}

/* ---------- trees: a soft, dark core for volume, leaf-cluster cards for the silhouette ---------- */
const SUN_FLAT = new THREE.Vector3(sunDir.x, 0, sunDir.z).normalize();
function puff(list, cx, cy, cz, r, color, seedOff, detail = 1) {
  let g = new THREE.IcosahedronGeometry(r, detail);
  g.deleteAttribute("uv"); g.deleteAttribute("normal"); g = mergeVertices(g);
  const pos = g.attributes.position;
  for (let k = 0; k < pos.count; k++) { const v = new THREE.Vector3().fromBufferAttribute(pos, k); v.multiplyScalar(0.88 + vnoise(v.x * 1.6 / r + seedOff, (v.y + v.z) * 1.6 / r, 999, 999) * 0.24); pos.setXYZ(k, v.x, v.y, v.z); }
  g.computeVertexNormals();
  const cols = new Float32Array(pos.count * 3);
  for (let k = 0; k < pos.count; k++) { const sh = clamp(0.55 + 0.25 * (pos.getY(k) / r), 0.3, 1); cols[k * 3] = color.r * sh; cols[k * 3 + 1] = color.g * sh; cols[k * 3 + 2] = color.b * sh; }
  g.setAttribute("color", new THREE.BufferAttribute(cols, 3));
  list.push(g.translate(cx, cy, cz));
}
function crownCards(list, { x, z, cy, rx, ry, size, n, tint }) {
  for (let i = 0; i < n; i++) {
    const u = rnd() * 2 - 1, a = rnd() * Math.PI * 2, k = Math.pow(rnd(), 0.3);
    const sx = Math.sqrt(1 - u * u) * Math.cos(a), sz = Math.sqrt(1 - u * u) * Math.sin(a);
    const lumpy = 0.85 + 0.3 * vnoise(sx * 2 + x, u * 2 + z, 999, 999);
    const shade = clamp(0.5 + 0.32 * (u * 0.5 + 0.5) + 0.22 * (sx * SUN_FLAT.x + sz * SUN_FLAT.z) * k + 0.18 * (k - 0.6), 0.3, 1.2);
    list.push({ p: [x + sx * rx * k * lumpy, cy + u * ry * k * lumpy, z + sz * rx * k * lumpy], s: size * rr(0.8, 1.2), c: tint.clone().offsetHSL(rr(-0.015, 0.015), rr(-0.05, 0.05), rr(-0.04, 0.04)).multiplyScalar(shade) });
  }
}
function cardsMesh(list, mat) {
  const g = new THREE.PlaneGeometry(1, 1);
  g.setAttribute("aH", new THREE.BufferAttribute(new Float32Array([1, 1, 1, 1]), 1));
  const im = new THREE.InstancedMesh(g, mat, list.length);
  const m = new THREE.Matrix4(), q = new THREE.Quaternion(), e = new THREE.Euler(), s = new THREE.Vector3(), p = new THREE.Vector3();
  list.forEach((c, i) => { q.setFromEuler(e.set(rr(-1.1, 1.1), rnd() * 6.28, rnd() * 6.28)); im.setMatrixAt(i, m.compose(p.set(...c.p), q, s.setScalar(c.s))); im.setColorAt(i, c.c); });
  im.customDepthMaterial = new THREE.MeshDepthMaterial({ depthPacking: THREE.RGBADepthPacking, map: T.cluster, alphaTest: 0.5 });
  im.castShadow = true; im.receiveShadow = true;
  return im;
}
function buildTrees() {
  const tints = ["#55703a", "#4a6334", "#6b7a3a", "#8e8c42", "#5f7a3c"].map((h) => new THREE.Color(h));
  const trees = [];
  for (let i = 0; i < 70; i++) { const x = rr(-170, 170); trees.push({ x, z: rr(-112, -150) - Math.abs(x) * 0.05, h: rr(9, 15), birch: rnd() < 0.25 }); }
  for (let i = 0; i < 6; i++) { const w = houseToWorld(rr(-15, 13), 0, rr(-10, -17)); trees.push({ x: w.x, z: w.z, h: rr(10, 14), near: true }); }
  const cores = [], cards = [], bark = [], birch = [];
  for (const t of trees) {
    const rx = t.h * rr(0.26, 0.33), ry = t.h * rr(0.3, 0.36), cy = t.h * 0.64;
    (t.birch ? birch : bark).push(new THREE.CylinderGeometry(t.h * 0.012, t.h * 0.024, cy, 6).translate(t.x, cy / 2, t.z));
    const tint = t.birch ? new THREE.Color("#a8a447") : tints[(rnd() * tints.length) | 0];
    puff(cores, t.x, cy, t.z, rx * 0.72, tint.clone().multiplyScalar(0.55), rnd() * 50);
    crownCards(cards, { x: t.x, z: t.z, cy, rx, ry, size: t.near ? 1.3 : 2.1, n: t.near ? 170 : 55, tint });
  }
  scene.add(mesh(mergeGeometries(bark), M.bark), mesh(mergeGeometries(birch), M.birch), mesh(mergeGeometries(cores), M.foliageCore), cardsMesh(cards, M.leaf));
}

// the birch next to the izba: white trunk, fine branches, golden leaves
function buildBirch() {
  const base = houseToWorld(HW + 2.6, 0, HD + 1.6);
  const g = new THREE.Group(); g.position.copy(base); scene.add(g);
  const trunk = new THREE.CylinderGeometry(0.09, 0.2, 10, 14, 16, false), pos = trunk.attributes.position;
  for (let i = 0; i < pos.count; i++) { const y = pos.getY(i) + 5; pos.setX(i, pos.getX(i) + Math.sin(y * 0.32) * 0.22); pos.setZ(i, pos.getZ(i) + Math.sin(y * 0.21 + 1) * 0.12); }
  trunk.computeVertexNormals(); trunk.translate(0, 5, 0);
  g.add(mesh(trunk, M.birch));
  const cards = [], gold = ["#d4b343", "#bfa63f", "#a8a63f"].map((h) => new THREE.Color(h));
  for (let i = 0; i < 12; i++) {
    const y0 = rr(3.6, 8.6), a = (i / 12) * Math.PI * 2 + rr(-0.3, 0.3), len = rr(1.3, 2.4) * (1 - (y0 - 3.5) / 10);
    const start = new THREE.Vector3(Math.sin(y0 * 0.32) * 0.22, y0, Math.sin(y0 * 0.21 + 1) * 0.12);
    const end = start.clone().add(new THREE.Vector3(Math.cos(a) * len, len * rr(0.25, 0.5), Math.sin(a) * len));
    g.add(mesh(new THREE.TubeGeometry(new THREE.CatmullRomCurve3([start, start.clone().lerp(end, 0.5).add(new THREE.Vector3(0, 0.15, 0)), end]), 5, 0.04 * (1 - y0 / 12), 5, false), M.birch));
    crownCards(cards, { x: end.x, z: end.z, cy: end.y - 0.15, rx: rr(0.9, 1.2), ry: rr(1.0, 1.4), size: 0.78, n: Q.birch, tint: gold[i % 3] });
  }
  crownCards(cards, { x: 0.15, z: 0.1, cy: 8.8, rx: 1.4, ry: 1.5, size: 0.78, n: Q.birch * 2, tint: gold[0] });
  g.add(cardsMesh(cards, M.leaf));
}

function buildClouds() {
  const clouds = [];
  const addCloud = (az, el, size, op) => {
    const warm = smooth(200, 100, az);
    const mat = new THREE.SpriteMaterial({ map: T.cloud, color: new THREE.Color(1.5 + warm * 0.4, 1.3 + warm * 0.05, 1.12 - warm * 0.2), transparent: true, opacity: op, depthWrite: false, fog: false });
    const sp = new THREE.Sprite(mat); const d = 1400;
    sp.position.setFromSphericalCoords(d, Math.PI / 2 - THREE.MathUtils.degToRad(el), THREE.MathUtils.degToRad(az));
    sp.scale.set(size, size * 0.42, 1); scene.add(sp); clouds.push(sp);
  };
  for (let i = 0; i < 12; i++) addCloud(rr(120, 260), rr(4, 16), rr(260, 520), rr(0.35, 0.7));
  for (let i = 0; i < 6; i++) addCloud(rr(60, 120), rr(3, 9), rr(200, 380), rr(0.3, 0.55));
  return clouds;
}

const smoke = [];
function buildSmoke(house) {
  house.updateMatrixWorld(true);
  const top = house.localToWorld(house.userData.chimneyTop.clone());
  for (let i = 0; i < 26; i++) {
    const mat = new THREE.SpriteMaterial({ map: T.smoke, color: "#d8d0c6", transparent: true, opacity: 0, depthWrite: false });
    const sp = new THREE.Sprite(mat); sp.userData = { life: rnd() * 6, origin: top }; scene.add(sp); smoke.push(sp);
  }
}
function updateSmoke(dt) {
  for (const sp of smoke) {
    const u = sp.userData; u.life += dt; if (u.life > 6) u.life -= 6;
    const t = u.life / 6;
    sp.position.copy(u.origin).add(new THREE.Vector3(windU.uWind.value.x * t * 3.2, t * 5.5, windU.uWind.value.y * t * 3.2));
    const s = 0.5 + t * 2.6; sp.scale.set(s, s, 1);
    sp.material.opacity = Math.sin(Math.PI * t) * 0.28;
  }
}

/* ==========================================================================
   Post-processing
   ========================================================================== */
let composer, bloom, grade;
function buildPost() {
  const rt = new THREE.WebGLRenderTarget(innerWidth * Q.pr, innerHeight * Q.pr, { type: THREE.HalfFloatType, samples: Q.samples });
  composer = new EffectComposer(renderer, rt);
  composer.setPixelRatio(Q.pr); composer.setSize(innerWidth, innerHeight);
  composer.addPass(new RenderPass(scene, camera));
  bloom = new UnrealBloomPass(new THREE.Vector2(innerWidth * Q.bloomScale, innerHeight * Q.bloomScale), 0.42, 0.65, 0.92);
  composer.addPass(bloom);
  composer.addPass(new OutputPass());
  grade = new ShaderPass({
    uniforms: { tDiffuse: { value: null }, uTime: { value: 0 }, uRes: { value: new THREE.Vector2(innerWidth, innerHeight) } },
    vertexShader: "varying vec2 vUv; void main(){ vUv = uv; gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }",
    fragmentShader: `
      uniform sampler2D tDiffuse; uniform float uTime; uniform vec2 uRes; varying vec2 vUv;
      float rnd(vec2 p){ return fract(sin(dot(p, vec2(12.9898, 78.233))) * 43758.5453); }
      void main(){
        vec4 c = texture2D(tDiffuse, vUv);
        float l = dot(c.rgb, vec3(0.299, 0.587, 0.114));
        c.rgb = mix(c.rgb, c.rgb * vec3(1.05, 1.0, 0.9), 0.55);              // warm grade
        c.rgb = mix(vec3(l), c.rgb, 1.06);                                   // a touch of saturation
        c.rgb = (c.rgb - 0.5) * 1.07 + 0.5;                                  // contrast
        c.rgb = c.rgb * 0.96 + vec3(0.018, 0.012, 0.006);                    // lifted, filmic blacks
        vec2 q = vUv - 0.5; q.x *= uRes.x / uRes.y;
        c.rgb *= mix(0.62, 1.0, smoothstep(1.05, 0.25, length(q)));          // vignette
        gl_FragColor = c;
      }`,
  });
  composer.addPass(grade);
}

/* ==========================================================================
   Environment lighting from the sky
   ========================================================================== */
function buildEnvironment() {
  const pmrem = new THREE.PMREMGenerator(renderer);
  const envScene = new THREE.Scene();
  envScene.add(makeSky(50));
  scene.environment = pmrem.fromScene(envScene, 0.02).texture;
  }

/* ==========================================================================
   Sound — synthesized live in the browser, nothing is played from a file.
   Music: an original waltz in A minor written for this page (plucked
   gusli strings, a wooden flute, a soft drone). Nature: birds, crickets,
   a low breeze. No samples and no existing melody, so no rights to clear.
   ========================================================================== */
const audio = { ctx: null, on: false };
const mtof = (m) => 440 * Math.pow(2, (m - 69) / 12);
const ar = (a, b) => a + Math.random() * (b - a);
function impulse(a, dur, decay) {
  const len = Math.floor(a.sampleRate * dur), b = a.createBuffer(2, len, a.sampleRate);
  for (let ch = 0; ch < 2; ch++) { const d = b.getChannelData(ch); let lp = 0; for (let i = 0; i < len; i++) { const t = i / len; lp += (Math.random() * 2 - 1 - lp) * (0.55 - 0.45 * t); d[i] = lp * Math.pow(1 - t, decay); } }
  return b;
}
function ensureAudio() {
  if (audio.ctx) return audio.ctx;
  let a; try { a = new (window.AudioContext || window.webkitAudioContext)(); } catch (e) { return null; }
  audio.ctx = a;
  const comp = a.createDynamicsCompressor(); comp.threshold.value = -16; comp.ratio.value = 3; comp.attack.value = 0.01; comp.release.value = 0.3; comp.connect(a.destination);
  audio.master = a.createGain(); audio.master.gain.value = 0; audio.master.connect(comp);
  const verb = a.createConvolver(); verb.buffer = impulse(a, 3.6, 2.4);
  const verbOut = a.createGain(); verbOut.gain.value = 0.55; verb.connect(verbOut); verbOut.connect(audio.master);
  const bus = (gain, send, lp) => {
    const g = a.createGain(); g.gain.value = gain; let out = g;
    if (lp) { const f = a.createBiquadFilter(); f.type = "lowpass"; f.frequency.value = lp; f.Q.value = 0.5; g.connect(f); out = f; }
    out.connect(audio.master);
    const s = a.createGain(); s.gain.value = send; out.connect(s); s.connect(verb);
    return g;
  };
  audio.music = bus(0.62, 0.5, 4800);
  audio.nature = bus(0.7, 0.35, 9000);
  audio.fx = bus(0.7, 0.18);
  const len = a.sampleRate * 3, nb = a.createBuffer(1, len, a.sampleRate), d = nb.getChannelData(0);
  for (let i = 0; i < len; i++) d[i] = Math.random() * 2 - 1;
  audio.noise = nb;
  // wooden flute: strong fundamental, soft upper partials
  audio.fluteWave = a.createPeriodicWave(new Float32Array(6), new Float32Array([0, 1, 0.28, 0.1, 0.035, 0.012]));
  // the breeze: kept very low and dark so it never turns into hiss
  const w = a.createBufferSource(); w.buffer = nb; w.loop = true; w.playbackRate.value = 0.5;
  const wl = a.createBiquadFilter(); wl.type = "lowpass"; wl.frequency.value = 260; wl.Q.value = 0.3;
  audio.windGain = a.createGain(); audio.windGain.gain.value = 0.015;
  w.connect(wl); wl.connect(audio.windGain); audio.windGain.connect(audio.nature); w.start();
  return a;
}

// plucked string (Karplus–Strong), rendered once per note and cached
const pluckCache = new Map();
function pluckBuffer(midi, variant) {
  const key = midi * 2 + variant; if (pluckCache.has(key)) return pluckCache.get(key);
  const a = audio.ctx, sr = a.sampleRate, f = mtof(midi);
  const len = Math.floor(sr * (midi < 50 ? 4.2 : midi < 64 ? 3.2 : 2.4));
  const N = Math.max(2, Math.round(sr / f - 0.5)), t60 = midi < 50 ? 3.2 : midi < 64 ? 2.4 : 1.7;
  const rho = Math.pow(0.001, 1 / (f * t60));
  const ring = new Float32Array(N); let prev = 0, mean = 0;
  for (let i = 0; i < N; i++) { prev += (Math.random() * 2 - 1 - prev) * 0.6; ring[i] = prev; mean += prev; }
  mean /= N; for (let i = 0; i < N; i++) ring[i] -= mean;
  const buf = a.createBuffer(1, len, sr), out = buf.getChannelData(0);
  let idx = 0, peak = 1e-6;
  for (let n = 0; n < len; n++) {
    const nx = idx + 1 === N ? 0 : idx + 1, cur = ring[idx];
    out[n] = cur; ring[idx] = rho * 0.5 * (cur + ring[nx]); idx = nx;
    const ab = Math.abs(cur); if (ab > peak) peak = ab;
  }
  const fade = Math.floor(sr * 0.25);
  for (let n = 0; n < len; n++) { out[n] /= peak; if (n > len - fade) out[n] *= (len - n) / fade; }
  pluckCache.set(key, buf); return buf;
}
function pluck(midi, t, vel = 0.5, pan = 0) {
  const a = audio.ctx;
  for (let v = 0; v < 2; v++) {   // two strings per course, a hair apart, like a gusli
    const s = a.createBufferSource(); s.buffer = pluckBuffer(midi, v); s.playbackRate.value = v ? 1.0016 : 1;
    const g = a.createGain(); g.gain.value = vel * 0.2;
    const p = a.createStereoPanner(); p.pan.value = clamp(pan + (v ? 0.08 : -0.08), -1, 1);
    s.connect(g); g.connect(p); p.connect(audio.music); s.start(t + v * 0.004);
  }
}
function flute(midi, t, dur, vel = 1) {
  const a = audio.ctx, f = mtof(midi), end = t + dur + 0.5;
  const o = a.createOscillator(); o.setPeriodicWave(audio.fluteWave);
  o.frequency.setValueAtTime(f * 0.988, t); o.frequency.exponentialRampToValueAtTime(f, t + 0.07);
  const vib = a.createOscillator(), vd = a.createGain(); vib.frequency.value = 5.2;
  vd.gain.setValueAtTime(0, t); vd.gain.linearRampToValueAtTime(f * 0.0055, t + Math.min(0.7, dur * 0.7));
  vib.connect(vd); vd.connect(o.frequency);
  const g = a.createGain(), peak = 0.1 * vel;
  g.gain.setValueAtTime(0.0001, t); g.gain.linearRampToValueAtTime(peak, t + 0.09); g.gain.setTargetAtTime(peak * 0.78, t + 0.09, 0.4); g.gain.setTargetAtTime(0.0001, t + dur - 0.06, 0.08);
  o.connect(g); g.connect(audio.music);
  const n = a.createBufferSource(); n.buffer = audio.noise; n.loop = true;
  const bp = a.createBiquadFilter(); bp.type = "bandpass"; bp.frequency.value = f * 1.5; bp.Q.value = 1.4;
  const ng = a.createGain(); ng.gain.setValueAtTime(0.0001, t); ng.gain.linearRampToValueAtTime(0.014 * vel, t + 0.04); ng.gain.setTargetAtTime(0.003 * vel, t + 0.05, 0.12); ng.gain.setTargetAtTime(0.0001, t + dur - 0.06, 0.06);
  n.connect(bp); bp.connect(ng); ng.connect(audio.music);
  o.start(t); vib.start(t); n.start(t, Math.random() * 2); o.stop(end); vib.stop(end); n.stop(end);
}
function drone(root, t, dur) {
  const a = audio.ctx;
  for (const [m, lvl] of [[root, 1], [root + 7, 0.55], [root + 12, 0.3]]) {
    const o = a.createOscillator(); o.type = "triangle"; o.frequency.value = mtof(m); o.detune.value = ar(-4, 4);
    const lp = a.createBiquadFilter(); lp.type = "lowpass"; lp.frequency.value = 520;
    const g = a.createGain(); g.gain.setValueAtTime(0.0001, t); g.gain.linearRampToValueAtTime(0.02 * lvl, t + 0.9); g.gain.setValueAtTime(0.02 * lvl, t + dur - 0.2); g.gain.linearRampToValueAtTime(0.0001, t + dur + 0.9);
    o.connect(lp); lp.connect(g); g.connect(audio.music); o.start(t); o.stop(t + dur + 1);
  }
}

// "Pole" — waltz, 76 bpm, A minor. Intro (4 bars), then verse with flute and an interlude of strings, alternating.
const BEAT = 60 / 76, BAR = BEAT * 3;
const CHORDS = { Am: [45, [57, 60, 64]], Dm: [50, [57, 62, 65]], G: [43, [55, 59, 62]], C: [48, [55, 60, 64]], F: [41, [57, 60, 65]], E: [40, [56, 59, 64]] };
const INTRO = ["Am", "Dm", "Am", "E"];
const PROG = ["Am", "Am", "Dm", "Dm", "G", "C", "Dm", "E", "Am", "Am", "F", "C", "Dm", "E", "E", "Am"];
const MELODY = [
  [[69, 1], [72, 1], [76, 1]], [[81, 2], [79, 1]], [[77, 1.5], [76, 0.5], [74, 1]], [[69, 3]],
  [[71, 1], [74, 1], [79, 1]], [[79, 2], [77, 0.5], [76, 0.5]], [[77, 1], [76, 1], [74, 1]], [[76, 3]],
  [[69, 1], [72, 1], [76, 1]], [[81, 2], [79, 1]], [[77, 1.5], [76, 0.5], [74, 1]], [[76, 2], [72, 1]],
  [[74, 1], [77, 1], [81, 1]], [[76, 1], [80, 1], [83, 1]], [[74, 1], [72, 1], [71, 1]], [[69, 3]],
];
const song = { next: 0, bar: 0, part: "intro" };
function playBar(t) {
  const intro = song.part === "intro", chord = intro ? INTRO[song.bar] : PROG[song.bar];
  const [bass, tones] = CHORDS[chord];
  pluck(bass, t, 0.85, -0.15); drone(bass + 12, t, BAR);
  if (song.part === "verse") {
    tones.forEach((m, i) => pluck(m, t + BEAT + i * 0.018, 0.4, 0.15));
    tones.slice(1).forEach((m, i) => pluck(m, t + 2 * BEAT + i * 0.018, 0.3, 0.15));
    let o = 0; MELODY[song.bar].forEach(([m, d]) => { flute(m, t + o * BEAT, d * BEAT, 0.9); o += d; });
  } else {
    [tones[0], tones[1], tones[2], tones[0] + 12, tones[2]].forEach((m, i) => pluck(m, t + (i + 1) * BEAT / 2, i % 2 ? 0.32 : 0.42, 0.2));
  }
}
function advanceBar() {
  song.bar++;
  if (song.bar >= (song.part === "intro" ? INTRO.length : PROG.length)) { song.bar = 0; song.part = song.part === "verse" ? "interlude" : "verse"; }
}

function tweet(t, f0, f1, dur, vol, out, fm = 0) {
  const a = audio.ctx, o = a.createOscillator(), g = a.createGain();
  o.frequency.setValueAtTime(f0, t); o.frequency.exponentialRampToValueAtTime(f1, t + dur);
  if (fm) { const l = a.createOscillator(), lg = a.createGain(); l.frequency.value = fm; lg.gain.value = f0 * 0.04; l.connect(lg); lg.connect(o.frequency); l.start(t); l.stop(t + dur + 0.02); }
  g.gain.setValueAtTime(0.0001, t); g.gain.exponentialRampToValueAtTime(vol, t + dur * 0.3); g.gain.exponentialRampToValueAtTime(0.0001, t + dur);
  o.connect(g); g.connect(out); o.start(t); o.stop(t + dur + 0.02);
}
function birdCall(t) {
  const a = audio.ctx, p = a.createStereoPanner(), g = a.createGain();
  p.pan.value = ar(-0.85, 0.85); g.gain.value = ar(0.35, 1); p.connect(g); g.connect(audio.nature);
  const kind = Math.random();
  if (kind < 0.45) {            // thrush-like whistles
    let tt = t; const n = 3 + ((Math.random() * 3) | 0), base = ar(1900, 2700);
    for (let i = 0; i < n; i++) { const f = base * ar(0.85, 1.3), d = ar(0.1, 0.24); tweet(tt, f, f * ar(0.8, 1.25), d, 0.07, p, ar(18, 32)); tt += d + ar(0.04, 0.12); }
  } else if (kind < 0.85) {     // finch-like chirps ending in a short trill
    let tt = t; const n = 3 + ((Math.random() * 4) | 0);
    for (let i = 0; i < n; i++) { const f = ar(3800, 5200); tweet(tt, f, f * ar(0.55, 0.7), ar(0.05, 0.08), 0.05, p); tt += ar(0.08, 0.13); }
    for (let i = 0; i < 6; i++) { tweet(tt, 4200, 3300, 0.035, 0.035, p); tt += 0.045; }
  } else {                      // a lark, high and far away
    const o = a.createOscillator(), og = a.createGain(), l = a.createOscillator(), lg = a.createGain(), d = ar(1.4, 2.4);
    o.frequency.value = ar(3600, 4400); l.frequency.value = ar(14, 22); lg.gain.value = 700; l.connect(lg); lg.connect(o.frequency);
    og.gain.setValueAtTime(0.0001, t); og.gain.exponentialRampToValueAtTime(0.02, t + 0.2); og.gain.setValueAtTime(0.02, t + d - 0.3); og.gain.exponentialRampToValueAtTime(0.0001, t + d);
    o.connect(og); og.connect(p); o.start(t); l.start(t); o.stop(t + d + 0.05); l.stop(t + d + 0.05);
  }
}
function cricket(t, pan) {
  const a = audio.ctx, o = a.createOscillator(), g = a.createGain(), p = a.createStereoPanner();
  o.frequency.value = 4500 + pan * 120; p.pan.value = pan;
  g.gain.setValueAtTime(0, t);
  for (let k = 0; k < 3; k++) { const s = t + k * 0.026; g.gain.setValueAtTime(0, s); g.gain.linearRampToValueAtTime(0.0055, s + 0.004); g.gain.linearRampToValueAtTime(0, s + 0.016); }
  o.connect(g); g.connect(p); p.connect(audio.nature); o.start(t); o.stop(t + 0.1);
}
const nature = { bird: 0, crickets: [0, 0] };
function schedule() {
  const a = audio.ctx; if (!a || !audio.on || a.state !== "running") return;
  const horizon = a.currentTime + 0.6;
  while (song.next < horizon) { playBar(song.next); song.next += BAR; advanceBar(); }
  if (nature.bird < horizon) { birdCall(Math.max(nature.bird, a.currentTime + 0.05)); nature.bird = a.currentTime + 0.6 + ar(3, 8); }
  nature.crickets.forEach((tn, i) => { if (tn < horizon) { const t = Math.max(tn, a.currentTime + 0.02); cricket(t, i ? 0.55 : -0.5); nature.crickets[i] = t + ar(0.45, 0.95); } });
}
setInterval(schedule, 120);

function burst({ dur = 0.1, type = "lowpass", freq = 800, q = 0.7, gain = 0.3, when = 0 }) {
  const a = audio.ctx; if (!a || !audio.on) return;
  const s = a.createBufferSource(); s.buffer = audio.noise;
  const f = a.createBiquadFilter(); f.type = type; f.frequency.value = freq; f.Q.value = q;
  const g = a.createGain(), t0 = a.currentTime + when;
  g.gain.setValueAtTime(0.0001, t0); g.gain.exponentialRampToValueAtTime(gain, t0 + 0.006); g.gain.exponentialRampToValueAtTime(0.0001, t0 + dur);
  s.connect(f); f.connect(g); g.connect(audio.fx); s.start(t0, Math.random() * 2); s.stop(t0 + dur + 0.05);
}
function ping(freq, dur, gain, when = 0) {
  const a = audio.ctx; if (!a || !audio.on) return;
  const o = a.createOscillator(), g = a.createGain(), t0 = a.currentTime + when;
  o.type = "sine"; o.frequency.value = freq; g.gain.setValueAtTime(gain, t0); g.gain.exponentialRampToValueAtTime(0.0001, t0 + dur);
  o.connect(g); g.connect(audio.fx); o.start(t0); o.stop(t0 + dur);
}
const sfx = {
  step() { burst({ dur: 0.12, freq: 420, gain: 0.14 }); burst({ dur: 0.05, type: "bandpass", freq: 1800, q: 1.5, gain: 0.025, when: 0.012 }); },
  rattle() { [0, 0.13, 0.24, 0.42].forEach((w, i) => { burst({ dur: 0.14, freq: 160, gain: 0.7, when: w }); [523, 811, 1307].forEach((f) => ping(f * (1 + i * 0.01), 0.3, 0.035, w + 0.01)); }); },
  chime() { const a = audio.ctx; if (!a || !audio.on) return; [57, 60, 64, 69, 72, 76].forEach((m, i) => pluck(m, a.currentTime + 0.05 + i * 0.09, 0.5 - i * 0.04, -0.3 + i * 0.12)); },
};
function setSound(on) {
  audio.on = on;
  const a = ensureAudio();
  if (a) {
    if (a.state === "suspended") a.resume();
    if (on && song.next < a.currentTime) { song.next = a.currentTime + 0.25; nature.bird = a.currentTime + 2.5; nature.crickets = [a.currentTime + 1, a.currentTime + 1.4]; }
    audio.master.gain.cancelScheduledValues(a.currentTime);
    audio.master.gain.setTargetAtTime(on ? 2.6 : 0, a.currentTime, on ? 0.8 : 0.25);
  }
  $("soundLabel").textContent = on ? "Sound on" : "Sound off";
  $("soundBtn").setAttribute("aria-pressed", String(on));
  store.set("tt_sound", on ? "1" : "0");
}
$("soundBtn").addEventListener("click", () => setSound(!audio.on));
document.addEventListener("visibilitychange", () => { if (!audio.ctx) return; if (document.hidden) audio.ctx.suspend(); else if (audio.on) audio.ctx.resume(); });


/* ==========================================================================
   Walking, looking, the door
   ========================================================================== */
const S = {
  dist: 0, vel: 0, scrollVel: 0, holding: false, bob: 0, lastStep: 0,
  lookX: 0, lookY: 0, tLookX: 0, tLookY: 0,
  arrived: false, drawer: false, shake: 0, opened: false, doorAngle: 0, spawnAt: -1, spawnDone: false, fovKick: false, busy: false,
};
const WALK = 3.2;
const walkBtn = $("walkBtn"), backBtn = $("backBtn");

const uiCache = {};
const setUI = (id, prop, v) => { const k = id + prop; if (uiCache[k] !== v) { uiCache[k] = v; $(id)[prop] = v; } };
function renderControl() {
  const remaining = Math.max(0, STOP_DIST - S.dist);
  $("walkBar").style.transform = `scaleX(${(S.dist / STOP_DIST).toFixed(4)})`;
  walkBtn.classList.toggle("door", S.arrived);
  if (S.arrived) {
    setUI("walkLabel", "textContent", isOpen() ? "Enter" : "Open the door");
  } else {
    setUI("walkLabel", "textContent", "Hold to walk");
    setUI("walkDist", "textContent", Math.ceil(remaining) + " m");
  }
  if (backBtn.disabled !== S.dist < 0.05) backBtn.disabled = S.dist < 0.05;
}

function doorAction() {
  if (S.busy || S.drawer) return;
  if (isOpen()) { location.href = CONFIG.dropUrl; return; }
  S.busy = true; S.shake = 1.4; sfx.rattle();
  $("captionText").textContent = "The door is closed.";
  $("captionSub").textContent = "Opens 22.04.2027 · 19:00 CEST";
  setTimeout(() => $("caption").classList.add("on"), 450);
  setTimeout(() => { $("caption").classList.remove("on"); openDrawer(); S.busy = false; }, 2900);
}

function openDrawer() {
  S.drawer = true; S.holding = false; walkBtn.classList.remove("down");
  const d = $("drawer"); d.classList.add("open"); d.setAttribute("aria-hidden", "false");
  renderRegistered(); tick(); sfx.chime();
  setTimeout(() => { if ($("wlDone").hidden && !coarse) $("wlEmail").focus({ preventScroll: true }); }, 700);
}
function closeDrawer() {
  S.drawer = false; const d = $("drawer"); d.classList.remove("open"); d.setAttribute("aria-hidden", "true");
  walkBtn.focus({ preventScroll: true });
}
$("closeBtn").addEventListener("click", closeDrawer);
$("skipBtn").addEventListener("click", () => (S.drawer ? closeDrawer() : openDrawer()));

function tick() {
  const now = Date.now(), diff = Math.max(0, DROP_AT - now), s = Math.floor(diff / 1000);
  const d = Math.floor(s / 86400), h = Math.floor((s % 86400) / 3600), m = Math.floor((s % 3600) / 60), sec = s % 60;
  $("cdD").textContent = pad(d, 3); $("cdH").textContent = pad(h); $("cdM").textContent = pad(m); $("cdS").textContent = pad(sec);
  if (isOpen()) { $("drawerTitle").innerHTML = "The door is <em>open</em>."; }
  else if (now >= EARLY_AT) { $("drawerTitle").innerHTML = "The waitlist is <em>inside</em>."; }
}
setInterval(tick, 1000);

/* waitlist */
function resolveMode() {
  if (CONFIG.mode !== "auto") return CONFIG.mode;
  if (CONFIG.shopHosts.some((h) => location.hostname === h || location.hostname.endsWith("." + h))) return "shopify";
  return CONFIG.endpoint ? "endpoint" : "demo";
}
function renderRegistered() { const reg = store.get("tt_registered") === "1"; $("wlWrap").hidden = reg; $("wlDone").hidden = !reg; }
$("wlForm").addEventListener("submit", async (e) => {
  const email = $("wlEmail").value.trim(), err = $("wlErr"), btn = $("wlSubmit"), label = $("wlSubmitLabel");
  err.textContent = "";
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email)) { e.preventDefault(); err.textContent = "Enter a full email address, like name@domain.com."; $("wlEmail").focus(); return; }
  if (!$("wlConsent").checked) { e.preventDefault(); err.textContent = "Tick the box so we are allowed to email you the key."; return; }
  const mode = resolveMode();
  if (mode === "shopify") { label.textContent = "Sending…"; return; }   // native Shopify post → ?customer_posted=true
  e.preventDefault();
  btn.disabled = true; label.textContent = "Sending…";
  try {
    if (mode === "endpoint") {
      const r = await fetch(CONFIG.endpoint, { method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" }, body: JSON.stringify({ email, source: "time-travel-door", consent: true, ts: new Date().toISOString() }) });
      if (!r.ok) throw new Error("HTTP " + r.status);
    } else {
      const list = JSON.parse(store.get("tt_demo_list") || "[]"); list.push({ email, ts: Date.now() }); store.set("tt_demo_list", JSON.stringify(list));
    }
    store.set("tt_registered", "1"); renderRegistered();
  } catch (ex) {
    err.textContent = "The key could not be sent. Check your connection and try again.";
  } finally { btn.disabled = false; label.textContent = "Request the key"; }
});
if (params.get("customer_posted") === "true") { store.set("tt_registered", "1"); history.replaceState(null, "", location.pathname); S.dist = STOP_DIST; }
if (flag("door")) S.dist = STOP_DIST;

/* input */
let pressAtDoor = false;
const startHold = () => { if (S.drawer || S.arrived) return; S.holding = true; walkBtn.classList.add("down"); if (audio.on) ensureAudio(); };
const endHold = () => { S.holding = false; walkBtn.classList.remove("down"); };
walkBtn.addEventListener("pointerdown", (e) => { pressAtDoor = S.arrived; if (!S.arrived) { walkBtn.setPointerCapture(e.pointerId); startHold(); } });
["pointerup", "pointercancel", "lostpointercapture"].forEach((ev) => walkBtn.addEventListener(ev, endHold));
walkBtn.addEventListener("click", (e) => { if (S.arrived && (pressAtDoor || e.detail === 0)) doorAction(); pressAtDoor = false; });
walkBtn.addEventListener("contextmenu", (e) => e.preventDefault());
const startBack = () => { if (S.drawer) return; S.holdingBack = true; backBtn.classList.add("down"); };
const endBack = () => { S.holdingBack = false; backBtn.classList.remove("down"); };
backBtn.addEventListener("pointerdown", (e) => { backBtn.setPointerCapture(e.pointerId); startBack(); });
["pointerup", "pointercancel", "lostpointercapture"].forEach((ev) => backBtn.addEventListener(ev, endBack));
backBtn.addEventListener("click", (e) => { if (e.detail === 0) S.scrollVel = -WALK; });
backBtn.addEventListener("contextmenu", (e) => e.preventDefault());

const ray = new THREE.Raycaster(), ndc = new THREE.Vector2();
let downAt = null;
canvas.addEventListener("pointerdown", (e) => {
  downAt = { x: e.clientX, y: e.clientY, t: performance.now() };
  if (!S.arrived) { canvas.setPointerCapture(e.pointerId); startHold(); }
});
canvas.addEventListener("pointerup", (e) => {
  endHold();
  if (e.pointerType === "touch") { S.tLookX = 0; S.tLookY = 0; }
  if (S.arrived && downAt && Math.hypot(e.clientX - downAt.x, e.clientY - downAt.y) < 8 && hitsDoor(e)) doorAction();
  downAt = null;
});
canvas.addEventListener("pointercancel", endHold);
canvas.addEventListener("pointermove", (e) => {
  S.tLookX = (e.clientX / innerWidth - 0.5) * 2; S.tLookY = (e.clientY / innerHeight - 0.5) * 2;
  if (S.arrived) canvas.classList.toggle("hover-door", hitsDoor(e));
});
function hitsDoor(e) {
  ndc.set((e.clientX / innerWidth) * 2 - 1, -(e.clientY / innerHeight) * 2 + 1);
  ray.setFromCamera(ndc, camera);
  return ray.intersectObjects(doorRig.hit, false).length > 0;
}
addEventListener("wheel", (e) => { if (S.drawer || (S.arrived && e.deltaY > 0)) return; S.scrollVel = clamp(S.scrollVel + clamp(e.deltaY, -120, 120) * 0.012, -WALK, WALK * 1.3); }, { passive: true });
let touchY = null;
canvas.addEventListener("touchstart", (e) => { touchY = e.touches[0].clientY; }, { passive: true });
canvas.addEventListener("touchmove", (e) => { if (touchY === null || S.drawer) return; const y = e.touches[0].clientY; if (S.arrived && touchY - y > 0) { touchY = y; return; } S.scrollVel = clamp(S.scrollVel + (touchY - y) * 0.03, -WALK, WALK * 1.3); touchY = y; }, { passive: true });
addEventListener("keydown", (e) => {
  if (S.drawer) { if (e.key === "Escape") closeDrawer(); return; }
  if (["ArrowUp", "w", "W"].includes(e.key)) { e.preventDefault(); startHold(); }
  if (["ArrowDown", "s", "S"].includes(e.key)) { e.preventDefault(); startBack(); }
  if (S.arrived && ["e", "E", "Enter", " "].includes(e.key) && e.target !== walkBtn) { e.preventDefault(); doorAction(); }
});
addEventListener("keyup", (e) => { if (["ArrowUp", "w", "W"].includes(e.key)) endHold(); if (["ArrowDown", "s", "S"].includes(e.key)) endBack(); });
addEventListener("blur", () => { endHold(); endBack(); });

/* ==========================================================================
   Frame loop
   ========================================================================== */
const clock = new THREE.Clock();
const UP = new THREE.Vector3(0, 1, 0);
const doorLook = DOOR_W.clone().add(new THREE.Vector3(0, 1.75, 0));
const tmpV = new THREE.Vector3(), tmpL = new THREE.Vector3();
let houseRef = null;

function update(dt, t) {
  windU.uTime.value = t;
  // gusts in the audio follow the visual wind
  if (audio.ctx && audio.on) {
    const gust = Math.pow(Math.sin(t * 0.37) * 0.5 + 0.5, 2);
    audio.windGain.gain.setTargetAtTime(0.01 + gust * 0.028, audio.ctx.currentTime, 0.5);
  }
  // walking
  const remaining = STOP_DIST - S.dist;
  S.scrollVel *= Math.pow(0.08, dt); if (Math.abs(S.scrollVel) < 0.02) S.scrollVel = 0;
  const target = S.drawer ? 0 : S.holdingBack ? -WALK * 0.8 : S.holding ? WALK : S.scrollVel;
  S.vel += (target - S.vel) * Math.min(1, dt * (Math.abs(target) > Math.abs(S.vel) ? 1.8 : 3.2));
  if (S.dist <= 0 && S.vel < 0) S.vel = 0;
  const brake = smooth(0, 3.2, remaining) * 0.9 + 0.1;
  S.dist = clamp(S.dist + S.vel * (S.vel > 0 ? brake : 1) * dt, 0, STOP_DIST);
  if (STOP_DIST - S.dist < 0.03 && !S.arrived) { S.dist = STOP_DIST; S.arrived = true; S.vel = 0; S.scrollVel = 0; endHold(); canvas.classList.add("at-door"); renderControl(); }
  if (S.arrived && STOP_DIST - S.dist > 0.25) { S.arrived = false; canvas.classList.remove("at-door", "hover-door"); $("caption").classList.remove("on"); }
  // arrival: the flash clears, one line fades in and out (driven here so it stays in sync with the landing)
  if (S.spawnAt >= 0 && !S.spawnDone) {
    const st = t - S.spawnAt, fl = 1 - smooth(0, 2.2, st);
    const op = smooth(0.8, 2.1, st) * (1 - smooth(4.4, 5.6, st)) * (1 - smooth(0.3, 1.4, S.dist));
    $("flash").style.opacity = fl.toFixed(3); $("spawn").style.opacity = op.toFixed(3);
    if (st > 5.7 || (S.dist > 1.4 && fl <= 0)) { S.spawnDone = true; $("flash").hidden = true; $("spawn").style.opacity = "0"; }
  }
  // camera on the path with a gentle gait
  const speed = Math.abs(S.vel);
  S.bob += dt * speed * 2.35;
  const stepPhase = Math.floor(S.bob / Math.PI);
  if (stepPhase !== S.lastStep) { S.lastStep = stepPhase; if (speed > 0.3) sfx.step(); }
  const gait = reduceMotion ? 0 : Math.min(1, speed / WALK);
  const u = S.dist / PATH_LEN;
  const p = pathCurve.getPointAt(u), tg = pathCurve.getTangentAt(Math.min(u + 0.01, 1));
  const land = S.spawnAt < 0 ? 1 : smooth(0, 2.6, t - S.spawnAt), drop = (1 - land) * (1 - land);
  camera.position.set(p.x, 1.63 + drop * 1.1 + Math.abs(Math.sin(S.bob)) * 0.045 * gait - 0.02 * gait, p.z);
  if (drop > 0.0005 || S.fovKick) { camera.fov = baseFov + drop * 16; camera.updateProjectionMatrix(); S.fovKick = drop > 0.0005; }
  const side = tmpV.set(-tg.z, 0, tg.x).normalize();
  camera.position.addScaledVector(side, Math.sin(S.bob) * 0.025 * gait);
  tmpL.copy(camera.position).addScaledVector(tg, 12).add(new THREE.Vector3(0, -0.55, 0));
  const f = smooth(16, 1.5, remaining);
  tmpL.lerp(doorLook, 0.35 + 0.65 * f);
  camera.lookAt(tmpL);
  // free look with the pointer (smaller near the door)
  S.lookX += (S.tLookX - S.lookX) * Math.min(1, dt * 3); S.lookY += (S.tLookY - S.lookY) * Math.min(1, dt * 3);
  const range = mix(0.2, 0.08, f);
  camera.rotateY(-S.lookX * range); camera.rotateX(-S.lookY * range * 0.45);
  camera.rotateZ(Math.sin(S.bob * 0.5) * 0.004 * gait);
  renderControl();
  // door
  if (S.shake > 0) S.shake = Math.max(0, S.shake - dt);
  const k = S.shake / 1.4;
  if (doorRig.pivot) {
    const target = S.opened ? -1.35 : 0;
    S.doorAngle += (target - S.doorAngle) * Math.min(1, dt * 1.2);
    doorRig.pivot.rotation.y = S.doorAngle + Math.sin(S.shake * 38) * 0.018 * k;
    doorRig.lock.rotation.z = Math.sin(S.shake * 11) * 0.45 * k;
    doorRig.lock.rotation.x = -Math.abs(Math.sin(S.shake * 9)) * 0.25 * k;
  }
  updateSmoke(dt);
}

let baseFov = 48;
function resize() {
  const w = innerWidth, h = innerHeight;
  baseFov = w / h < 0.8 ? 64 : w / h < 1.2 ? 56 : 48;
  camera.aspect = w / h; camera.fov = baseFov; camera.updateProjectionMatrix();
  renderer.setSize(w, h, false);
  windU.uPx.value = 0.6 * (2 * Math.tan(THREE.MathUtils.degToRad(baseFov) / 2)) / (h * renderer.getPixelRatio());
  if (composer) { composer.setSize(w, h); bloom.setSize(w * Q.bloomScale, h * Q.bloomScale); grade.uniforms.uRes.value.set(w, h); }
}
addEventListener("resize", resize);

function setOpenState() {
  if (!isOpen() || S.opened) return;
  S.opened = true; doorRig.glow.visible = true; doorRig.light.intensity = 9; doorRig.lock.visible = false;
}

// Adaptive quality: measure real frame time in 1.5 s windows and step the
// resolution down (then switch off bloom) until the device keeps up.
const perf = { acc: 0, n: 0, warm: 2.5, pr: Q.pr };
function adapt(raw) {
  if (perf.warm > 0) { perf.warm -= raw; return; }
  perf.acc += raw; perf.n++;
  if (perf.acc < 1.5) return;
  const avg = perf.acc / perf.n; perf.acc = 0; perf.n = 0;
  if (avg < 0.022) return;
  if (perf.pr > 0.8) { perf.pr = Math.max(0.75, perf.pr - 0.25); renderer.setPixelRatio(perf.pr); composer.setPixelRatio(perf.pr); resize(); }
  else if (bloom.enabled) bloom.enabled = false;
}
let sdt = 1 / 60;
function loop() {
  const raw = clock.getDelta(), t = clock.elapsedTime;
  sdt += (Math.min(0.05, raw) - sdt) * 0.2;   // smoothed step: no jumps when a frame comes late
  adapt(raw);            // may resize — do it before drawing so no blank frame is shown
  update(sdt, t);
  composer.render(sdt);
  requestAnimationFrame(loop);
}

/* ==========================================================================
   Boot
   ========================================================================== */
const nextFrame = () => new Promise((r) => requestAnimationFrame(() => r()));
async function boot() {
  window.__timing = [];
  const tm = (name, t0) => window.__timing.push([name, Math.round(performance.now() - t0)]);
  const bar = (f) => { $("loaderBar").style.transform = `scaleX(${f.toFixed(3)})`; };
  const tTex = performance.now();
  let made = 0; const total = Object.keys(PIX).length;
  const pixels$ = renderPixelTextures(() => bar((++made / total) * 0.6));
  drawCanvasTextures();
  texturesFromPixels(await pixels$); tm("textures", tTex);
  const progress = () => {};
  { const t0 = performance.now();buildMaterials(); tm("materials", t0); progress(); }
  bar(0.68); await nextFrame();
  { const t0 = performance.now();buildEnvironment(); buildGround(); houseRef = buildHouse(); tm("house", t0); progress(); }
  bar(0.78); await nextFrame();
  { const t0 = performance.now();buildWheat(); tm("wheat", t0); progress(); }
  bar(0.88); await nextFrame();
  { const t0 = performance.now();buildTrees(); buildBirch(); buildClouds(); buildSmoke(houseRef); tm("trees", t0); progress(); }
  // sun + shadow camera centred on the house
  sun.position.copy(HOUSE_POS).addScaledVector(sunDir, 70); sun.target.position.copy(HOUSE_POS); sun.target.updateMatrixWorld();
  buildPost(); resize(); progress();
  bar(0.95); await nextFrame();
  setOpenState();
  update(0.016, 0);
  { const t0 = performance.now(); if (renderer.compileAsync) await renderer.compileAsync(scene, camera); else renderer.compile(scene, camera); tm("compile", t0); }
  composer.render(0.016); bar(1);
  renderControl(); tick();
  $("loader").classList.add("gone");
  clock.start(); loop();
  // arrival: you drop in through a warm flash, one line, then the field is yours
  S.spawnAt = flag("door") || params.get("customer_posted") === "true" ? -1 : 0.05;
  if (S.spawnAt < 0) $("flash").hidden = true;
  if (params.get("customer_posted") === "true" || flag("waitlist")) setTimeout(openDrawer, 900);
  window.__tt = { S, audio, song, openDrawer, setDist: (d) => { S.dist = clamp(d, 0, STOP_DIST); S.arrived = false; }, STOP_DIST, doorAction, renderer };
}
boot().catch((e) => { console.error(e); $("loaderText").textContent = "The field could not load. Reload the page."; });
