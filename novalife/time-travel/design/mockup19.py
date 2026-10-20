# -*- coding: utf-8 -*-
# Mockup v1.9 (17.10.2026): Referenz-Fit (Baggy, helle Vintage-Wäsche) mit allen Teilen von Druckvorlage v1.9
#   Foto: rev6/skizzen/2026-10-17_referenz_fit_baggy.jpg, bereinigt von mock_clean.py, 2x skaliert
#   Maßstab: Bund flach ~406 mm (Gr. M) = 355 px im Original -> 0,875 px/mm, hier 1,75 px/mm
import base64, bisect, io, contextlib, math, os, subprocess, sys
with contextlib.redirect_stdout(io.StringIO()):
    import build as B
    import build15 as N15
    import v16 as V16
import fine as FN
from PIL import Image

F = FN.F
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "v19")
BASE = os.path.join(OUT, "mock_base.png")
S = 1.75                                   # px pro mm
u = FN.CELL * S                            # Kreuzstich-Zelle in px
COP, COPD, COPL = "#a8643a", "#6f3d1f", "#e0a878"
STITCH = "#d9b46a"

subprocess.run([sys.executable, os.path.join(HERE, "mock_clean.py"), BASE], check=True)
W, H = Image.open(BASE).size
import cv2, numpy as np

# Wäsche (Entscheidung 20.10.): dunkler als das Referenzfoto, mittleres Vintage-Indigo.
# Die hellen Stellen des Fotos bleiben als Waschung erhalten und treten stärker hervor.
_im = cv2.imread(BASE)
_hsv = cv2.cvtColor(_im, cv2.COLOR_BGR2HSV)
_bg = ((_hsv[..., 1] < 14) & (_hsv[..., 2] > 238)).astype(np.float32)
_keep = cv2.GaussianBlur(_bg, (0, 0), 1.2)[..., None]                      # weißer Hintergrund bleibt weiß
_lab = cv2.cvtColor(_im, cv2.COLOR_BGR2LAB).astype(np.float32)
_lab[..., 0] = 255 * (_lab[..., 0] / 255) ** 2.2
_lab[..., 0] -= 0.4 * (_lab[..., 0] - cv2.GaussianBlur(_lab[..., 0], (0, 0), 60))   # Aufhellungen vorn nur leicht ("bissl Waschung")
_lab[..., 1] = 128 + (_lab[..., 1] - 128) * 1.2
_lab[..., 2] = 128 + (_lab[..., 2] - 128) * 1.7 - 5
# Unterschenkel: fleckige, schmutzig wirkende Stellen glätten, feine Struktur bleibt
_ramp = np.clip((np.arange(H, dtype=np.float32)[:, None] - 0.62 * H) / (0.18 * H), 0, 1)
_mid = cv2.GaussianBlur(_lab[..., 0], (0, 0), 14) - cv2.GaussianBlur(_lab[..., 0], (0, 0), 70)
_lab[..., 0] -= 0.75 * _mid * _ramp
for _c in (1, 2):
    _lab[..., _c] -= 0.6 * (cv2.GaussianBlur(_lab[..., _c], (0, 0), 14) - cv2.GaussianBlur(_lab[..., _c], (0, 0), 70)) * _ramp
_dark = cv2.cvtColor(np.clip(_lab, 0, 255).astype(np.uint8), cv2.COLOR_LAB2BGR).astype(np.float32)
cv2.imwrite(BASE, np.clip(_dark * (1 - _keep) + _im.astype(np.float32) * _keep, 0, 255).astype(np.uint8))

# Licht und Falten des Fotos als Soft-Light-Ebene auf die Stickerei
_L = cv2.cvtColor(cv2.imread(BASE), cv2.COLOR_BGR2GRAY).astype(np.float32) + 1
_b1 = cv2.GaussianBlur(_L, (0, 0), 10); _b2 = cv2.GaussianBlur(_L, (0, 0), 70)
_sh = (_L / _b1) * (_b1 / _b2) ** 0.7
SHADE = os.path.join(OUT, "mock_shade.png")
cv2.imwrite(SHADE, np.clip(128 + (_sh - 1) * 420, 0, 255).astype(np.uint8))
BASE_URI, SHADE_URI = "mock_base.png", "mock_shade.png"     # liegen neben mockup19.html


def shade(clip_id, opacity=0.85):
    return (f'<g clip-path="url(#{clip_id})" style="mix-blend-mode: soft-light; opacity: {opacity}">'
            f'<image href="{SHADE_URI}" x="0" y="0" width="{W}" height="{H}"></image></g>')


def poly(pts):
    return "M" + "L".join(f"{F(x)} {F(y)}" for x, y in pts) + "Z"


# ================= Metall =================
def rivet(cx, cy, d_mm=9.0):
    r = d_mm * S / 2
    return (f'<circle cx="{F(cx)}" cy="{F(cy+0.8)}" r="{F(r+0.6)}" style="fill: #000; opacity: 0.25"></circle>'
            f'<circle cx="{F(cx)}" cy="{F(cy)}" r="{F(r)}" style="fill: url(#cop); stroke: {COPD}; stroke-width: 0.8px"></circle>'
            f'<circle cx="{F(cx)}" cy="{F(cy)}" r="{F(r*0.42)}" style="fill: none; stroke: {COPD}; stroke-width: 0.6px; opacity: 0.6"></circle>')


def button(cx, cy, d_mm=20.0):
    r = d_mm * S / 2
    star = "".join(poly(q) for q in FN.star8_rhombi(cx, cy, r * 1.36, d_mm * S * 0.02))   # Achtstern aus 8 Rauten
    return (f'<circle cx="{F(cx)}" cy="{F(cy+1.5)}" r="{F(r+1)}" style="fill: #000; opacity: 0.28"></circle>'
            f'<circle cx="{F(cx)}" cy="{F(cy)}" r="{F(r)}" style="fill: url(#cop); stroke: {COPD}; stroke-width: 1px"></circle>'
            f'<circle cx="{F(cx)}" cy="{F(cy)}" r="{F(r*0.84)}" style="fill: none; stroke: {COPD}; stroke-width: 0.8px"></circle>'
            f'<path d="{star}" style="fill: {COPD}; fill-opacity: 0.6"></path>')


# ================= Vorn: Band A auf der Taschenöffnung des Referenz-Fits =================
Q = [(476, 360), (468, 428), (392, 464), (206, 472)]    # Taschenöffnung (= Innenkante von A), vom Bund zur Seitennaht


def bez(t):
    mt = 1 - t
    return (mt**3 * Q[0][0] + 3 * mt * mt * t * Q[1][0] + 3 * mt * t * t * Q[2][0] + t**3 * Q[3][0],
            mt**3 * Q[0][1] + 3 * mt * mt * t * Q[1][1] + 3 * mt * t * t * Q[2][1] + t**3 * Q[3][1])


PTS = [bez(i / 3000) for i in range(3001)]
ARC = [0.0]
for i in range(1, len(PTS)):
    ARC.append(ARC[-1] + math.hypot(PTS[i][0] - PTS[i - 1][0], PTS[i][1] - PTS[i - 1][1]))
LTOT = ARC[-1]; NF = int(LTOT // u); LEAD = (LTOT - NF * u) / 2; ROWS = FN.BAND_ROWS


def at(s):
    s = max(0, min(LTOT, s)); i = min(max(bisect.bisect_left(ARC, s), 1), len(ARC) - 1)
    x, y = PTS[i - 1]; x2, y2 = PTS[i]; tx, ty = x2 - x, y2 - y; l = math.hypot(tx, ty) or 1
    tx, ty = tx / l, ty / l
    return x, y, tx, ty, -ty, tx               # Normale zeigt zur Münztasche


def corners(col, row):
    x, y, tx, ty, nx, ny = at(LEAD + (col + 0.5) * u)
    off = (row - ROWS + 0.5) * u               # Reihe 16 an der Öffnung, Band liegt auf dem Vorderteil
    cx, cy = x + nx * off, y + ny * off; h = u / 2 + 0.08
    return [(cx - tx*h - nx*h, cy - ty*h - ny*h), (cx + tx*h - nx*h, cy + ty*h - ny*h),
            (cx + tx*h + nx*h, cy + ty*h + ny*h), (cx - tx*h + nx*h, cy - ty*h + ny*h)]


def edge(off, n=160):
    q = []
    for j in range(n + 1):
        x, y, tx, ty, nx, ny = at(j * LTOT / n); q.append((x + nx * off, y + ny * off))
    return q


Wb = FN.band_white(NF, (3 - NF // 2) % FN.RAP)
fill = {"r": [], "w": []}; xs = {"r": [], "w": []}
for col in range(NF):
    for row in range(ROWS):
        k = "w" if (row, col) in Wb else "r"; c = corners(col, row)
        fill[k].append(poly(c)); i = 0.12
        L = lambda a, b, t: (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)
        p0, p2, p1, p3 = L(c[0], c[2], i), L(c[0], c[2], 1 - i), L(c[1], c[3], i), L(c[1], c[3], 1 - i)
        xs[k].append(f"M{F(p0[0])} {F(p0[1])}L{F(p2[0])} {F(p2[1])}M{F(p1[0])} {F(p1[1])}L{F(p3[0])} {F(p3[1])}")
BAND = (f'<g style="filter: url(#emb)"><path d="{"".join(fill["r"])}" style="fill: {FN.REDD}"></path>'
        f'<path d="{"".join(fill["w"])}" style="fill: {FN.WHT2}"></path>'
        f'<path d="{"".join(xs["r"])}" style="fill: none; stroke: {FN.REDL}; stroke-width: {F(u*0.3)}px; stroke-linecap: round"></path>'
        f'<path d="{"".join(xs["w"])}" style="fill: none; stroke: {FN.WHITE}; stroke-width: {F(u*0.34)}px; stroke-linecap: round"></path></g>')
INNER = edge(0); OUTER = edge(-ROWS * u)
A_MM = round(LTOT / S)

# Münztasche E, 62 x 62 mm, oben an der Bundnaht; der untere Teil steckt hinter dem Vorderteil
EX, EY = 2 * (172 - N15.COIN_MM * 0.875 / 2), 2 * 176   # waagerecht mittig zwischen Seitennaht (103) und Taschenniete (238)
CS = N15.COIN_MM * S
E = FN.stitched(FN.coin_white(), None, N15.COIN_N, N15.COIN_N, EX + (CS - N15.COIN_N * u) / 2, EY + (CS - N15.COIN_N * u) / 2, u)
FACING = poly(INNER + [(Q[3][0] - 60, Q[3][1]), (Q[3][0] - 60, 0), (Q[0][0], 0)])

front = [f'<clipPath id="facing"><path d="{FACING}"></path></clipPath>',
         f'<clipPath id="bandA"><path d="{poly(INNER + OUTER[::-1])}"></path></clipPath>',
         f'<clipPath id="coinE"><rect x="{F(EX)}" y="{F(EY)}" width="{F(CS)}" height="{F(CS)}" clip-path="url(#facing)"></rect></clipPath>',
         f'<g clip-path="url(#facing)"><rect x="{F(EX)}" y="{F(EY)}" width="{F(CS)}" height="{F(CS)}" style="fill: #6d87a8; opacity: 0.55"></rect>',
         f'<g style="filter: url(#emb)">{E}</g>',
         f'<path d="M{F(INNER[0][0])} {F(INNER[0][1])}' + "".join(f"L{F(x)} {F(y)}" for x, y in INNER[1:]) +
         '" style="fill: none; stroke: #0d1f3a; stroke-width: 7px; opacity: 0.35; filter: url(#soft)"></path></g>',
         shade("coinE"),
         BAND, shade("bandA"),
         f'<path d="M{F(OUTER[0][0])} {F(OUTER[0][1])}' + "".join(f"L{F(x)} {F(y)}" for x, y in OUTER[1:]) +
         f'" style="fill: none; stroke: {STITCH}; stroke-width: 1.1px; stroke-dasharray: 3 2.4; opacity: 0.9"></path>',
         rivet(*Q[0]), rivet(Q[3][0] + 6, Q[3][1] - 4), rivet(EX + 5, EY + 5), rivet(EX + CS - 5, EY + 5),
         rivet(752, 358), rivet(950, 446),
         button(624, 320)]

# ================= Hinten: unsere Gesäßtaschen, B2, C, Patch D =================
POCKET_TOP, POCKET_BOT, SIDE_IN, SIDE_OUT, TIP_EDGE = 160.0, 130.0, 125.0, 120.0, 70.0
MOTIF_C = (80.0, 47.0)


def pocket_shape(inner_right):
    dx = (POCKET_TOP - POCKET_BOT) / 2
    h_in = math.sqrt(SIDE_IN**2 - dx**2); h_out = math.sqrt(SIDE_OUT**2 - dx**2)
    tip_d = math.sqrt(TIP_EDGE**2 - (POCKET_BOT / 2)**2); yb = h_in
    tl, tr = ((0, h_in - h_out), (POCKET_TOP, 0)) if inner_right else ((0, 0), (POCKET_TOP, h_in - h_out))
    return [tl, tr, (POCKET_TOP - dx, yb), (POCKET_TOP / 2, yb + tip_d), (dx, yb)]


def inset(pts, d):
    n = len(pts); lines = []
    for i in range(n):
        (x1, y1), (x2, y2) = pts[i], pts[(i + 1) % n]
        ex, ey = x2 - x1, y2 - y1; l = math.hypot(ex, ey); nx, ny = -ey / l, ex / l
        lines.append(((x1 + nx * d, y1 + ny * d), (ex, ey)))
    out = []
    for i in range(n):
        (p, r), (q, s) = lines[i - 1], lines[i]
        den = r[0] * s[1] - r[1] * s[0]; t = ((q[0] - p[0]) * s[1] - (q[1] - p[1]) * s[0]) / den
        out.append((p[0] + r[0] * t, p[1] + r[1] * t))
    return out


def open_path(pts):
    """Seiten und Spitze ohne Oberkante: von oben rechts über die Spitze nach oben links"""
    q = pts[1:] + pts[:1]
    return "M" + "L".join(f"{F(x)} {F(y)}" for x, y in q)


def pocket(pts, motif, x0, y0, cid):
    st1, st2 = inset(pts, 2.0), inset(pts, 6.0)
    gp = [(x0 + x * S, y0 + y * S) for x, y in pts]
    hem = [inset(pts, d) for d in (12.0, 15.0)]
    lines = "".join(f"M{F(h[0][0])} {F(h[0][1])}L{F(h[1][0])} {F(h[1][1])}" for h in hem)
    sw = 1 / S
    return (f'<clipPath id="{cid}"><path d="{poly(gp)}"></path></clipPath>'
            f'<path d="{poly(gp)}" style="fill: #0d1f3a; opacity: 0.55; filter: url(#soft)" transform="translate(1.5 3)"></path>'
            f'<image href="{BASE_URI}" x="0" y="0" width="{W}" height="{H}" clip-path="url(#{cid})"></image>'
            f'<g transform="translate({F(x0)} {F(y0)}) scale({S})">'
            f'<path d="{poly(pts)}" style="fill: none; stroke: #f2f5f8; stroke-width: {F(1.4*sw)}px; opacity: 0.5"></path>'
            f'<path d="{open_path(st1)}{open_path(st2)}{lines}" style="fill: none; stroke: {STITCH}; stroke-width: {F(1.9*sw)}px; '
            f'stroke-dasharray: {F(1.6)} {F(1.2)}; opacity: 0.95"></path>'
            f'<g style="filter: url(#embmm)">{motif}</g></g>' + shade(cid, 0.35))


L_PTS, R_PTS = pocket_shape(True), pocket_shape(False)
b2x, b2y = MOTIF_C[0] - 24.0, MOTIF_C[1] - 24.55
STAR = FN.star8_svg(MOTIF_C[0], MOTIF_C[1], 36.0, 1.0)      # Achtstern aus 8 Rauten (Vorlage 17.10.)

buf = io.BytesIO(); Image.open(os.path.join(OUT, "patch_d.png")).resize((400, 355), Image.LANCZOS).save(buf, "PNG")
PATCH = "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()   # freigestellt, oben und unten gewölbt
PW, PH = 80 * S, 71 * S; PX, PY = 2 * 974 - PW / 2, 2 * 110   # hinten rechts, zwischen Mittel- und rechter Schlaufe

# Honeycombs hinter den Knien (Entscheidung 20.10.): 5 unregelmäßige Falten je Bein, Enden laufen weich aus
HONEY = []
for cx, flip in ((1462, 1), (2000, -1)):
    for dy, hw, tilt, bend in [(0, 46, -3, 8), (27, 64, 2, 12), (55, 72, -1, 14), (86, 58, 3, 10), (113, 38, -2, 6)]:
        y = 1484 + dy; t = tilt * flip
        d = f"M{cx-hw} {y+t}Q{cx} {y-bend} {cx+hw} {y-t}"
        HONEY.append(f'<path d="{d}" transform="translate(0 8)" style="fill: none; stroke: url(#hcd); stroke-width: 6; opacity: 0.35; filter: url(#hcblur); mix-blend-mode: multiply"></path>')
        HONEY.append(f'<path d="{d}" style="fill: none; stroke: url(#hcl); stroke-width: 9; opacity: 0.6; filter: url(#hcblur); mix-blend-mode: screen"></path>')

back = HONEY + [pocket(L_PTS, f'<g transform="translate({F(b2x)} {F(b2y)})">{V16.B2_V16}</g>', 2 * 749.5 - 80 * S, 2 * 233, "pkL"),
        pocket(R_PTS, STAR, 2 * 970 - 80 * S, 2 * 233, "pkR"),
        f'<image href="{PATCH}" x="{F(PX)}" y="{F(PY)}" width="{F(PW)}" height="{F(PH)}" preserveAspectRatio="none" style="filter: url(#patchshadow)"></image>']
for dx in (7.0, 73.0):                     # 4 Ringfeder-Druckknöpfe 10 mm, Raster 66 x 46 mm
    for dy in (12.5, 58.5):
        back.append(rivet(PX + dx * S, PY + dy * S, 10.0))

DEFS = ('<defs><radialGradient id="cop" cx="0.38" cy="0.32" r="0.75"><stop offset="0" stop-color="#e9b58a"></stop>'
        '<stop offset="0.45" stop-color="#b06c40"></stop><stop offset="1" stop-color="#6f3d1f"></stop></radialGradient>'
        '<filter id="emb" x="-5%" y="-5%" width="110%" height="115%"><feDropShadow dx="0" dy="1.2" stdDeviation="1" flood-color="#0d1f3a" flood-opacity="0.45"></feDropShadow></filter>'
        '<filter id="embmm" x="-5%" y="-5%" width="110%" height="115%"><feDropShadow dx="0" dy="0.6" stdDeviation="0.5" flood-color="#0d1f3a" flood-opacity="0.45"></feDropShadow></filter>'
        '<filter id="patchshadow" x="-10%" y="-10%" width="120%" height="125%"><feDropShadow dx="1.5" dy="3" stdDeviation="2.5" flood-color="#000" flood-opacity="0.35"></feDropShadow></filter>'
        '<filter id="soft"><feGaussianBlur stdDeviation="2.5"></feGaussianBlur></filter>'
        '<filter id="hcblur" x="-20%" y="-80%" width="140%" height="260%"><feGaussianBlur stdDeviation="4.5"></feGaussianBlur></filter>'
        '<linearGradient id="hcl"><stop offset="0" stop-color="#e4ecf7" stop-opacity="0"></stop><stop offset="0.5" stop-color="#e4ecf7"></stop><stop offset="1" stop-color="#e4ecf7" stop-opacity="0"></stop></linearGradient>'
        '<linearGradient id="hcd"><stop offset="0" stop-color="#0b1a33" stop-opacity="0"></stop><stop offset="0.5" stop-color="#0b1a33"></stop><stop offset="1" stop-color="#0b1a33" stop-opacity="0"></stop></linearGradient>'
        '<filter id="softmm"><feGaussianBlur stdDeviation="0.9"></feGaussianBlur></filter></defs>')
TXT = "font-family: Helvetica, Arial, sans-serif"
title = (f'<text x="60" y="110" style="{TXT}; font-size: 44px; font-weight: 700; fill: #1d2330; letter-spacing: 2px">NOVALIFE · TIME TRAVEL · NVL-TT-01</text>'
         f'<text x="60" y="160" style="{TXT}; font-size: 28px; fill: #6b717c">Mockup Design v1.9 · Straight wie Eightyfive · mittleres Indigo, Honeycombs, vorn leicht gewaschen</text>')

svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{DEFS}'
       f'<image href="{BASE_URI}" x="0" y="0" width="{W}" height="{H}"></image>{title}{"".join(front)}{"".join(back)}</svg>')
html = f'<!doctype html><html><head><meta charset="utf-8"><style>html,body{{margin:0;padding:0;background:#fff}}</style></head><body>{svg}</body></html>'
open(os.path.join(OUT, "mockup19.html"), "w").write(html)
print("Band A Innenkante", A_MM, "mm, Spalten", NF, "Bild", W, H)
