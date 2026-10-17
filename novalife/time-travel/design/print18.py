# -*- coding: utf-8 -*-
# Druckvorlage 1:1 · Design v1.8 (17.10.2026) · ohne Serp · alle Teile für Papiertest und Fabrik
#   1 Übersicht · 2 vorn A, E, Knopf, Nieten · 3 hinten links B2 · 4 hinten rechts C
#   5 Patch D · 6 Polo · 7 Zipper
import base64, io, contextlib, math, os
with contextlib.redirect_stdout(io.StringIO()):
    import build as B
    import build15 as N15
    import build16 as N16
    import v16 as V16
import fine as FN
from PIL import Image

F = FN.F
WHITE = FN.WHITE; REDD = FN.REDD; REDL = FN.REDL; WHT2 = FN.WHT2; RED = FN.RED
INK = "#1d2330"; GREY = "#8a8f99"; SUB = "#353a46"; DEN = "#2f4a6e"
COP, COPD, COPL = "#a8643a", "#6f3d1f", "#d39a6c"
FLEECE = "#ece6d8"; BORD = "#7a1f2b"; BLK = "#2a2421"; GOLD = "#c9a14a"
FONT = "font-family: Helvetica, Arial, sans-serif"
PAGES = 5
HERE = os.path.dirname(os.path.abspath(__file__))
SKIZZEN = os.path.join(HERE, "..", "rev6", "skizzen")
OUT = os.path.join(HERE, "v18")
os.makedirs(OUT, exist_ok=True)


def T(x, y, s, size=3.4, w=400, col=INK, anchor="start"):
    return f'<text x="{F(x)}" y="{F(y)}" style="{FONT}; font-size: {F(size)}px; font-weight: {w}; fill: {col}; text-anchor: {anchor}">{s}</text>'


def cut(d):
    return f'<path d="{d}" style="fill: none; stroke: {INK}; stroke-width: 0.25px; stroke-dasharray: 1.6 1.2"></path>'


def checkline(y):
    return (f'<path d="M55 {F(y)}H155M55 {F(y-2.5)}V{F(y+2.5)}M155 {F(y-2.5)}V{F(y+2.5)}" style="fill: none; stroke: {INK}; stroke-width: 0.35px"></path>'
            + T(105, y - 3.4, "Kontrolle: diese Linie muss genau 100 mm lang sein", 2.8, 700, anchor="middle")
            + T(105, y + 6, "Sonst falsch gedruckt. Im Druckdialog „Tatsächliche Größe“ bzw. „100 %“ wählen, nicht „An Seite anpassen“.", 2.6, 400, GREY, "middle"))


def header(n, title, lines, scale="1:1"):
    return ([T(12, 14, f"NOVALIFE · TIME TRAVEL · DESIGN v1.8 · STAND 17.10.2026 · {scale}", 2.8, 700, GREY),
             T(198, 14, f"Seite {n} von {PAGES}", 2.8, 400, GREY, "end"), T(12, 24, title, 6.2, 700)]
            + [T(12, 31 + i * 4.4, s, 3.0, 400, SUB) for i, s in enumerate(lines)])


def cells_path(cells, x0, y0, u):
    return FN.cells_path(sorted(cells), x0, y0, u)


def xcells(cells, x0, y0, u, fill, cross, cw=0.32):
    if not cells:
        return ""
    return (f'<path d="{cells_path(cells, x0, y0, u)}" style="fill: {fill}"></path>'
            + FN.xstitch(sorted(cells), x0, y0, u, cross, u * cw))


def star8(dx, dy, a, b):
    """Achtstern = Quadrat ∪ gedrehtes Quadrat"""
    return max(abs(dx), abs(dy)) <= a or abs(dx) + abs(dy) <= b


def img_uri(im, fmt="JPEG"):
    buf = io.BytesIO()
    im.save(buf, fmt, quality=90) if fmt == "JPEG" else im.save(buf, fmt)
    return f"data:image/{fmt.lower()};base64," + base64.b64encode(buf.getvalue()).decode()


# ================= Hardware =================
def button(cx, cy, d=17.0):
    """Knopf 17 mm, Antik-Kupfer, Achtstern vertieft"""
    r = d / 2
    pts = []
    for k in range(16):  # Achtstern als Umriss: 8 Spitzen, 8 Kerben
        ang = math.pi / 8 * k - math.pi / 2
        rr = r * 0.62 if k % 2 == 0 else r * 0.36
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    star = "M" + "L".join(f"{F(x)} {F(y)}" for x, y in pts) + "Z"
    inner = []
    for k in range(16):
        ang = math.pi / 8 * k - math.pi / 2
        rr = r * 0.30 if k % 2 == 0 else r * 0.17
        inner.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    st2 = "M" + "L".join(f"{F(x)} {F(y)}" for x, y in inner) + "Z"
    return (f'<circle cx="{F(cx)}" cy="{F(cy)}" r="{F(r)}" style="fill: {COP}; stroke: {COPD}; stroke-width: {F(d*0.02)}px"></circle>'
            f'<circle cx="{F(cx)}" cy="{F(cy)}" r="{F(r*0.84)}" style="fill: none; stroke: {COPD}; stroke-width: {F(d*0.018)}px"></circle>'
            f'<path d="{star}" style="fill: {COPD}; fill-opacity: 0.55; stroke: {COPD}; stroke-width: {F(d*0.012)}px"></path>'
            f'<path d="{st2}" style="fill: {COPL}"></path>')


def rivet(cx, cy, d=9.0):
    r = d / 2
    return (f'<circle cx="{F(cx)}" cy="{F(cy)}" r="{F(r)}" style="fill: {COP}; stroke: {COPD}; stroke-width: 0.25px"></circle>'
            f'<circle cx="{F(cx)}" cy="{F(cy)}" r="{F(r*0.45)}" style="fill: {COPL}; fill-opacity: 0.7"></circle>')


# ================= Polo: Kreuzstich-Baum (Äste statt Arme) =================
def polo_tree():
    C = 12; S = set()
    for dy in range(-3, 4):            # Kopf: Raute
        for dx in range(-3, 4):
            if abs(dx) + abs(dy) == 3:
                S.add((3 + dy, C + dx))
    S.add((3, C))
    for r in (7, 8, 9):                # Hals
        S.add((r, C))
    for k in range(1, 6):              # Äste schräg nach oben, links und rechts
        S.add((9 - k, C - 1 - k)); S.add((9 - k, C + 1 + k))
    for dx in (-1, 1):                 # Blätter als kleine Kreuze an den Astspitzen und an den Zweigen
        for (r, c) in [(4, C + dx * 7), (7, C + dx * 4)]:
            for dr, dc in [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]:
                S.add((r + dr, c + dc))
    for r in range(10, 31):            # Körper: Dreieck, Kontur
        h = (r - 10) // 2
        S.add((r, C - h)); S.add((r, C + h))
    for c in range(C - 10, C + 11):
        S.add((30, c))
    for r in range(18, 29):            # inneres A
        h = (r - 18) // 2
        S.add((r, C - h)); S.add((r, C + h))
    for c in range(C - 3, C + 4):
        S.add((25, c))
    S.add((22, C))
    for (r, c) in [(16, C), (19, C - 4), (19, C + 4), (23, C - 6), (23, C + 6), (27, C - 8), (27, C + 8)]:
        for dr, dc in [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]:
            S.add((r + dr, c + dc))
    for c in range(C - 10, C + 11):    # Saum: Zacken nach unten
        k = (c - (C - 10)) % 4
        if k == 0:
            S.add((31, c)); S.add((32, c))
        elif k in (1, 3):
            S.add((31, c))
    return {(r, c) for (r, c) in S if 0 <= c <= 24}


POLO_TREE = polo_tree()
POLO_W, POLO_H = 25, 33


def band_cells(cols, rows=9):
    """Kragen- und Bündchenband: Rand oben und unten, dazwischen Rauten im Wechsel mit Punkten"""
    S = set()
    for c in range(cols):
        S.add((0, c)); S.add((rows - 1, c))
        m = c % 8
        dx = m - 3
        if m < 7:
            for dy in range(-2, 3):
                if abs(dx) + abs(dy) == 2:
                    S.add((rows // 2 + dy, c))
        if m == 7:
            S.add((rows // 2, c))
    return S


# ================= Zipper: Teppich-Feld vorn, links und rechts vom Reißverschluss =================
ZC, ZR, ZGAP = 89, 55, 9            # Zellen à 2 mm: 178 × 110 mm, Lücke 18 mm für den Reißverschluss


def carpet():
    Bc, Kc, Gc = set(), set(), set()
    cx, cy = ZC // 2, ZR // 2
    for r in range(ZR):
        for c in range(ZC):
            dx, dy = c - cx, r - cy
            edge = min(r, c, ZR - 1 - r, ZC - 1 - c)
            if edge <= 1:
                Bc.add((r, c)); continue
            if edge == 3:
                Kc.add((r, c)); continue
            if 4 <= edge <= 6:                       # Zickzackband im Rahmen
                t = (c if r < 4 + 3 or r > ZR - 8 else r) % 4
                z = {0: 4, 1: 5, 2: 6, 3: 5}[t]
                if edge == z:
                    Gc.add((r, c))
                continue
            if edge == 8:
                Kc.add((r, c)); continue
            d = abs(dx) + abs(dy)                     # Medaillon
            if d in (22, 23):
                Bc.add((r, c))
            elif d == 19:
                Kc.add((r, c))
            elif star8(dx, dy, 8, 12) and not star8(dx, dy, 6, 9):
                Gc.add((r, c))
            elif star8(dx, dy, 4, 6) and not star8(dx, dy, 3, 4):
                Bc.add((r, c))
            elif abs(dx) + abs(dy) <= 1:
                Bc.add((r, c))
    for (sr, sc) in [(15, 16), (15, ZC - 17), (ZR - 16, 16), (ZR - 16, ZC - 17)]:   # Eck-Achtsterne
        for r in range(sr - 5, sr + 6):
            for c in range(sc - 5, sc + 6):
                dx, dy = c - sc, r - sr
                if star8(dx, dy, 3, 5) and not star8(dx, dy, 2, 3):
                    Gc.add((r, c))
                elif abs(dx) + abs(dy) <= 1:
                    Bc.add((r, c))
    gap = set(range(ZC // 2 - ZGAP // 2, ZC // 2 + ZGAP // 2 + 1))
    f = lambda S: {(r, c) for (r, c) in S if c not in gap}
    return f(Bc), f(Kc), f(Gc), gap


# ================= Patch D: Foto 1:1 und 4-Farben-Fassung =================
src = Image.open(os.path.join(SKIZZEN, "2026-10-16_baum_referenz_patch_d.jpg")).convert("RGB")
crop = src.crop((80, 118, 948, 884)).resize((760, 670), Image.LANCZOS)
PATCH_PHOTO = img_uri(crop)
q = crop.quantize(colors=5, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
pal = q.getpalette()[:15]
PATCH_4 = img_uri(q.convert("RGB"), "PNG")
PAL = [f"#{pal[i]:02x}{pal[i+1]:02x}{pal[i+2]:02x}" for i in range(0, 15, 3)]

# ================= Seiten =================
pages = []

# ---- 1 Übersicht
rows = [
    ("A", "Taschenband vorn rechts", "23 mm breit, 17 Kreuzstiche, Bogen an der Taschenöffnung", "Rot, Weiß", "Jeansfabrik"),
    ("E", "Münztasche voll bestickt", "62 × 62 mm Tasche, Stickerei 60 × 60 mm, 45 × 45 Stiche", "Rot, Weiß", "Jeansfabrik"),
    ("B2", "Drei Ähren, rotes Band, Goldfäden", "linke Gesäßtasche, Band 48 mm, 9 Fäden 18–30 mm von Hand", "Gold, Rot, Weiß", "Jeansfabrik"),
    ("C", "Achtstern", "rechte Gesäßtasche, 36 × 36 mm, 27 × 27 Stiche, Höhe wie B2-Band", "Rot, Weiß", "Jeansfabrik"),
    ("D", "Patch = hintere Gürtelschlaufe", "76 × 67 mm, Naturleinen, 4 Kupfernieten, „NL“, max. 4 Garnfarben", "4 Garnfarben", "Patch-Hersteller"),
    ("K", "Knopf", "Shank Button 17 mm, Antik-Kupfer, Achtstern vertieft", "Kupfer", "Fabrik (Knopf-Lieferant)"),
    ("N", "Nieten", "9 mm Antik-Kupfer, glatt: 6 vorn + 4 am Patch", "Kupfer", "Fabrik"),
    ("P, Z", "Polo und Zipper", "folgen als eigene Vorlage, sobald deine Vorlagen da sind (Canva-Entwurf 2, Omas Teppich)", "—", "Berliner Sticker"),
]
p = header(1, "Übersicht · was wohin gehört", [
    "Seiten 2–5 sind 1:1. Für den Papiertest: ausdrucken, ausschneiden, mit Malerkrepp auf die Eightyfive kleben.",
    "Für die Fabrik: dieselben Seiten gehen als PDF mit dem Tech Pack raus. Die Fabrik digitalisiert daraus die Stickdatei.",
    "Seit 11.10. ohne Serp. Das linke Vorderbein bleibt leer. Alle Metallteile in Antik-Kupfer, passend zu den Patch-Nieten.",
], "ÜBERSICHT")
y = 52
p.append(f'<rect x="12" y="{y-4.5}" width="186" height="6.5" style="fill: #eef0f3"></rect>')
for x, s in [(14, "Teil"), (24, "Was"), (80, "Maß und Lage"), (148, "Farben"), (172, "Geht an")]:
    p.append(T(x, y, s, 2.9, 700))
y += 8
for k, a, b, c, d in rows:
    p.append(T(14, y, k, 3.2, 700))
    p.append(T(24, y, a, 2.8, 700))
    words = b.split(" "); line = ""; yy = y
    for wd in words:
        if len(line + " " + wd) > 38:
            p.append(T(80, yy, line.strip(), 2.7, 400, SUB)); yy += 3.6; line = ""
        line += " " + wd
    p.append(T(80, yy, line.strip(), 2.7, 400, SUB))
    p.append(T(148, y, c, 2.7, 400, SUB))
    p.append(T(172, y, d, 2.6, 400, SUB))
    y = max(yy, y) + 7.5
    p.append(f'<path d="M12 {F(y-5.2)}H198" style="stroke: #e2e5ea; stroke-width: 0.3px"></path>')
y += 4
p.append(T(12, y, "Garnfarben (Polyester, nicht metallisiert)", 3.4, 700)); y += 6
for i, (col, name) in enumerate([(RED, "Rot, L* 38–42"), (WHITE, "Weiß, L* 85–88"), ("#d2a53a", "Gold (Ähren)"), ("#e6c463", "Goldfaden, 3-fach gezwirnt, ~1 mm")]):
    xx = 12 + (i % 3) * 62; yy = y + (i // 3) * 7
    p.append(f'<rect x="{F(xx)}" y="{F(yy-3.6)}" width="6" height="4.6" style="fill: {col}; stroke: #c9ccd2; stroke-width: 0.25px"></rect>')
    p.append(T(xx + 8, yy, name, 2.8, 400, SUB))
y += 17
p.append(T(12, y, "Was noch offen ist (mit meinem Rat)", 3.4, 700)); y += 6
for s in ["Zipper-Front: gestickt (Rat) oder Chenille · Entscheidung Di 01.12. nach dem Berliner Muster.",
          "Zipper-Teppich: Dafür brauche ich ein Foto von Omas Teppich. Polo-Logo: dein Canva-Entwurf 2 als Bild.",
          "Polo-Kragen und Bündchen: Webband aufgenäht (Rat, sauberer auf Rippstrick) oder gestickt.",
          "Knopf: eigener Knopf mit Achtstern hat beim Lieferanten eine Mindestmenge. Preis und Menge fragst du am Mo 19.10. bei den Fabriken.",
          "Baum-Bild von Patch D: Woher stammt es? Ist es KI oder aus dem Netz, brauchen wir die Rechte oder eine eigene Fassung."]:
    p.append(T(14, y, "· " + s, 2.8, 400, SUB)); y += 5
pages.append(p)

# ---- 2 Vorn
UF = B.UF; NF = B.NF; LEADF = B.LEADF; ROWS = FN.BAND_ROWS


def corners(col, row):
    s_ = LEADF + (col + 0.5) * UF; x, y_, tx, ty, nx, ny = B.at(s_); off = (row - (ROWS - 11)) * UF
    cx, cy = x + nx * off, y_ + ny * off; h = UF / 2 + 0.06
    return [(cx - tx*h - nx*h, cy - ty*h - ny*h), (cx + tx*h - nx*h, cy + ty*h - ny*h), (cx + tx*h + nx*h, cy + ty*h + ny*h), (cx - tx*h + nx*h, cy - ty*h + ny*h)]


def lerp(a, b, t):
    return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)


Wb = FN.band_white(NF, (3 - NF // 2) % FN.RAP)
fill = {"r": [], "w": []}; xs = {"r": [], "w": []}
for col in range(NF):
    for row in range(ROWS):
        k = "w" if (row, col) in Wb else "r"
        c = corners(col, row)
        fill[k].append("M" + "L".join(f"{F(a)} {F(b)}" for a, b in c) + "Z")
        i = 0.12
        p0 = lerp(c[0], c[2], i); p2 = lerp(c[0], c[2], 1 - i); p1 = lerp(c[1], c[3], i); p3 = lerp(c[1], c[3], 1 - i)
        xs[k].append(f"M{F(p0[0])} {F(p0[1])}L{F(p2[0])} {F(p2[1])}M{F(p1[0])} {F(p1[1])}L{F(p3[0])} {F(p3[1])}")
band = (f'<path d="{"".join(fill["r"])}" style="fill: {REDD}"></path>'
        f'<path d="{"".join(fill["w"])}" style="fill: {WHT2}"></path>'
        f'<path d="{"".join(xs["r"])}" style="fill: none; stroke: {REDL}; stroke-width: {F(UF*0.3)}px; stroke-linecap: round"></path>'
        f'<path d="{"".join(xs["w"])}" style="fill: none; stroke: {WHITE}; stroke-width: {F(UF*0.34)}px; stroke-linecap: round"></path>')
band_cut = B.offset_poly(N15.O_LO - 0.4, N15.O_HI + 0.4)
CS = N15.COIN_MM; CX0, CY0 = 14, 57
E = FN.stitched(FN.coin_white(), None, N15.COIN_N, N15.COIN_N, CX0 + (CS - N15.COIN_N * FN.CELL) / 2, CY0 + (CS - N15.COIN_N * FN.CELL) / 2, FN.CELL)
p = header(2, "Vorn · Band A, Münztasche E, Knopf, Nieten", [
    "A und E gehören an die Vordertasche mit der Münztasche (vom Träger aus rechts). Innere Bogenkante von A auf die Taschenöffnung.",
    "E: oben bündig an die Münztaschen-Naht, die untere rechte Ecke darf unter das Band rutschen.",
    "Knopf: auf deinen Bundknopf kleben. Nieten: an die Ecken der Vordertaschen und der Münztasche, wie bei jeder Jeans.",
])
p += [f'<rect x="{F(CX0)}" y="{F(CY0)}" width="{F(CS)}" height="{F(CS)}" style="fill: #34506f"></rect>', E,
      cut(f"M{F(CX0)} {F(CY0)}h{F(CS)}v{F(CS)}h{F(-CS)}z"),
      T(CX0 + CS + 5, CY0 + 6, "E · Münztasche", 3.4, 700), T(CX0 + CS + 5, CY0 + 11, "62 × 62 mm, Stickerei 60 × 60 mm", 3, 400, SUB),
      T(CX0 + CS + 5, CY0 + 15.5, "45 × 45 Kreuzstiche, Rot und Weiß", 3, 400, SUB),
      button(165, 70), cut("M154.5 59.5h21v21h-21z"),
      T(165, 87, "K · Knopf 17 mm", 3, 700, anchor="middle"), T(165, 91.5, "Antik-Kupfer, Achtstern vertieft", 2.7, 400, SUB, "middle"),
      rivet(150, 106), rivet(162, 106), rivet(174, 106), rivet(186, 106), rivet(156, 118), rivet(168, 118),
      T(168, 129, "N · 6 Nieten 9 mm, Antik-Kupfer", 3, 700, anchor="middle"),
      f'<g transform="translate(11 120) scale(1.25) translate(-240 -160)">{band}{cut(band_cut)}</g>',
      T(14, 142, "A · Taschenband", 3.4, 700),
      T(14, 147, "23 mm breit, 17 Kreuzstiche, Rot und Weiß", 3, 400, SUB),
      T(14, 151.5, "Die innere Kante des Bogens kommt auf die Taschenöffnung.", 3, 400, SUB),
      checkline(272)]
pages.append(p)

# ---- 3 Hinten links: B2
PX, PY = 33, 62
pocket = (f'<path d="{N16.L_SHAPE}" style="fill: {DEN}"></path>'
          f'<path d="{N16.L_STITCH}" style="fill: none; stroke: #d4ab52; stroke-width: 0.7px; stroke-dasharray: 2.2 1.8"></path>'
          f'<g transform="translate({F(N16.B2_POS[0])} {F(N16.B2_POS[1])})">{V16.B2_V16}</g>')
p = header(3, "Hinten links · drei Ähren, rotes Band, Goldfäden (B2)", [
    "Ganze Tasche ausschneiden, Oberkante an Oberkante auf deine linke Gesäßtasche (vom Träger aus links).",
    "Goldfäden echt machen: 9 Stücke gelbes Garn, 18–30 mm, unterschiedlich lang, direkt unter das rote Band kleben.",
    "In der Fabrik: Ähren und Band gestickt, die 9 Fäden nach der Wäsche von Hand gesetzt und innen in der Tasche verknotet.",
])
p += [f'<g transform="translate({PX} {PY})">{pocket}{cut("M-0.6 -0.6L144.6 15.5L144.6 144.4L72 172.7L-0.6 144.4Z")}</g>',
      T(PX + 72, PY + 181, "B2 · Tasche 144 × 172 mm · Band 48 mm · 9 Fäden 18–30 mm", 3, 700, anchor="middle"),
      checkline(272)]
pages.append(p)

# ---- 4 Hinten rechts: C
AW, AR = FN.alatyr_fine()
cxm, cym = N15.C_CENTER
x0c, y0c = cxm - 27 * FN.CELL / 2, cym - 27 * FN.CELL / 2
pocketR = (f'<path d="{N16.R_SHAPE}" style="fill: {DEN}"></path>'
           f'<path d="{N16.R_STITCH}" style="fill: none; stroke: #d4ab52; stroke-width: 0.7px; stroke-dasharray: 2.2 1.8"></path>'
           + FN.stitched(AW, AR, 27, 27, x0c, y0c, FN.CELL))
p = header(4, "Hinten rechts · Achtstern (C)", [
    "Ganze Tasche ausschneiden, Oberkante an Oberkante auf deine rechte Gesäßtasche (vom Träger aus rechts).",
    "Der Stern sitzt waagerecht mittig, seine Mitte 52 mm unter der Oberkante, auf gleicher Höhe wie das rote Band links.",
    "Nach außen heißt er „eight-point star“, nicht „Alatyr“.",
])
p += [f'<g transform="translate({PX} {PY})">{pocketR}{cut("M144.6 -0.6L-0.6 15.5L-0.6 144.4L72 172.7L144.6 144.4Z")}</g>',
      T(PX + 72, PY + 181, "C · Tasche 144 × 172 mm · Stern 36 × 36 mm, 27 × 27 Stiche", 3, 700, anchor="middle"),
      checkline(272)]
pages.append(p)

# ---- 5 Patch D
p = header(5, "Hinten Mitte · Patch D als Gürtelschlaufe", [
    "Dein Baum-Bild 1:1. Die 4 Garnfarben legt der Patch-Hersteller mit dir fest: Gold, Kupfer, Dunkelbraun, Rot.",
    "Der Patch ersetzt die hintere Mittelschlaufe: nur links und rechts genäht und genietet, oben und unten offen, der Gürtel läuft dahinter.",
    "Papiertest: Bild auf Pappe kleben, ausschneiden, mittig hinten mit Krepp nur links und rechts fixieren, Gürtel durchziehen.",
])
px, py = 14, 56
p += [f'<image href="{PATCH_PHOTO}" x="{px}" y="{py}" width="76" height="67" preserveAspectRatio="none"></image>',
      cut(f"M{px} {py}h76v67h-76z"), T(px + 38, py + 73, "D · 76 × 67 mm · Foto 1:1", 3, 700, anchor="middle")]
by = 150
p += [T(14, by, "Bauplan für die Fabrik", 3.6, 700),
      f'<rect x="14" y="{by+5}" width="76" height="67" style="fill: #efe7d6; stroke: {INK}; stroke-width: 0.3px"></rect>',
      f'<rect x="14" y="{by+5}" width="8" height="67" style="fill: url(#hatch)"></rect>',
      f'<rect x="82" y="{by+5}" width="8" height="67" style="fill: url(#hatch)"></rect>',
      rivet(18, by + 11, 6), rivet(86, by + 11, 6), rivet(18, by + 66, 6), rivet(86, by + 66, 6),
      f'<rect x="22" y="{by+29}" width="60" height="19" style="fill: none; stroke: #4a6fa5; stroke-width: 0.5px; stroke-dasharray: 2 1.4"></rect>',
      T(52, by + 37, "Gürtel läuft dahinter", 2.8, 700, "#4a6fa5", "middle"),
      T(52, by + 41.5, "Tunnel innen ca. 60 mm breit", 2.6, 400, "#4a6fa5", "middle")]
for i, s in enumerate(["Schraffiert: je 8 mm Nahtzone links und rechts, dort genäht", "und mit je 2 Kupfernieten (6 mm) gesichert.",
                       "Oben und unten offen, keine Naht.", "Kante umgeschlagen und gesteppt, Grund Naturleinen.",
                       "Linien mind. 0,8 mm, Einrollungen mind. 2,5 mm.", "Muster vom Patch-Hersteller ist Pflicht vor 100 Stück.",
                       "Sitz: mittig über der hinteren Mittelnaht,", "Oberkante bündig mit der Bundoberkante."]):
    p.append(T(98, by + 10 + i * 5, s, 2.8, 400, SUB))
p.append(checkline(272))
pages.append(p)

# ---- 6 Polo
u = FN.CELL
p = header(6, "Polo · Brust-Logo, Kragen, Bündchen, Nacken", [
    "Brust-Logo: Kreuzstich-Baum mit Ästen statt Armen, einfarbig Rot, ohne Buchstaben. Links auf der Brust (vom Träger aus),",
    "Mitte 80 mm neben der Knopfleiste, Oberkante 50 mm unter der Schulternaht. Band: um den Kragen und beide Ärmelbündchen.",
    "Nacken hinten: kleine Ähren, mittig 15 mm unter der Kragennaht.",
])
tx, ty = 24, 60
p += [f'<rect x="{tx-6}" y="{ty-6}" width="{F(POLO_W*u+12)}" height="{F(POLO_H*u+12)}" style="fill: #f7f5f0; stroke: #d8d4ca; stroke-width: 0.3px"></rect>',
      xcells(POLO_TREE, tx, ty, u, REDD, REDL),
      cut(f"M{tx-6} {ty-6}h{F(POLO_W*u+12)}v{F(POLO_H*u+12)}h{F(-(POLO_W*u+12))}z"),
      T(tx + POLO_W * u / 2, ty + POLO_H * u + 12, f"P · Brust-Logo {F(POLO_W*u)} × {F(POLO_H*u)} mm · {POLO_W} × {POLO_H} Stiche", 3, 700, anchor="middle")]
BCOLS = 120
bc = band_cells(BCOLS)
bx, byy = 14, 130
p += [f'<rect x="{bx}" y="{byy}" width="{F(BCOLS*u)}" height="{F(9*u)}" style="fill: #f7f5f0"></rect>',
      xcells(bc, bx, byy, u, REDD, REDL), cut(f"M{bx} {byy}h{F(BCOLS*u)}v{F(9*u)}h{F(-BCOLS*u)}z"),
      T(bx, byy + 18, "P · Band für Kragen und Bündchen · 12 mm hoch · Rapport 8 Stiche (10,7 mm)", 3, 700),
      T(bx, byy + 22.5, "Kragen ca. 420 mm, Bündchen je ca. 340 mm. Hier 160 mm zum Anhalten.", 2.8, 400, SUB)]
EARS = B.EARS_T
p += [f'<g transform="translate(120 66) scale(0.42)">{EARS}</g>',
      T(140, 100, "Nacken · Ähren ca. 20 mm", 3, 700, anchor="middle"),
      T(140, 104.5, "Gold auf Naturweiß", 2.7, 400, SUB, "middle")]
p.append(checkline(272))
pages.append(p)

# ---- 7 Zipper
Bc, Kc, Gc, gap = carpet()
zu = 2.0; zx, zy = 16, 62
gx0 = zx + min(gap) * zu; gw = len(gap) * zu
p = header(7, "Zipper · Teppich-Feld vorn (Entwurf)", [
    "Auf die Brust, links und rechts vom Reißverschluss, Oberkante 60 mm unter der Halsnaht. Die Lücke in der Mitte ist der Reißverschluss:",
    "18 mm frei, weil die Stickmaschine nicht näher an die Zähne kommt. Beide Hälften sind gespiegelt und treffen sich optisch.",
    "Entwurf nach der Drei-von-vier-Regel (Raute, Achtstern, Zickzack). Mit einem Foto von Omas Teppich passe ich ihn an.",
])
p += [f'<rect x="{zx}" y="{zy}" width="{F(ZC*zu)}" height="{F(ZR*zu)}" style="fill: {FLEECE}"></rect>',
      xcells(Bc, zx, zy, zu, BORD, "#9a3341", 0.3), xcells(Kc, zx, zy, zu, BLK, "#4a403b", 0.3), xcells(Gc, zx, zy, zu, GOLD, "#e0bd6a", 0.3),
      f'<rect x="{F(gx0)}" y="{zy}" width="{F(gw)}" height="{F(ZR*zu)}" style="fill: #ffffff"></rect>',
      f'<path d="M{F(gx0+gw/2)} {zy}V{F(zy+ZR*zu)}" style="stroke: {GREY}; stroke-width: 1.2px; stroke-dasharray: 1 0.8"></path>',
      cut(f"M{zx} {zy}H{F(gx0)}V{F(zy+ZR*zu)}H{zx}Z"), cut(f"M{F(gx0+gw)} {zy}H{F(zx+ZC*zu)}V{F(zy+ZR*zu)}H{F(gx0+gw)}Z"),
      T(zx, zy + ZR * zu + 7, f"Z · Teppich-Feld {F(ZC*zu)} × {F(ZR*zu)} mm, Lücke {F(gw)} mm · Zellen 2 mm · offen gestickt, der Stoff ist das Beige", 3, 700)]
sx, sy = 40, 210
S = set(); RS = set()
for r in range(15):
    for c in range(15):
        dx, dy = c - 7, r - 7
        if star8(dx, dy, 5, 7) and not star8(dx, dy, 3, 5):
            S.add((r, c))
        elif abs(dx) + abs(dy) <= 2:
            RS.add((r, c))
p += [xcells(S, sx, sy, u, GOLD, "#e0bd6a"), xcells(RS, sx, sy, u, BORD, "#9a3341"),
      T(sx + 10, sy + 27, "Achtstern 20 mm", 3, 700, anchor="middle"),
      T(sx + 10, sy + 31.5, "unten links am Saum", 2.7, 400, SUB, "middle"),
      button(120, 220, 20), T(120, sy + 27, "Zipper-Zieher mit Achtstern", 3, 700, anchor="middle"),
      T(120, sy + 31.5, "Metall, Antik-Kupfer (wie der Knopf)", 2.7, 400, SUB, "middle")]
p.append(checkline(272))
pages.append(p)

DEFS = ('<defs><pattern id="hatch" width="2" height="2" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
        '<rect width="2" height="2" style="fill: #efe7d6"></rect><path d="M0 0V2" style="stroke: #b9a98a; stroke-width: 0.6px"></path></pattern></defs>')


def page(parts):
    return (f'<div class="pg"><svg xmlns="http://www.w3.org/2000/svg" width="210mm" height="297mm" viewBox="0 0 210 297">{DEFS}'
            f'<rect width="210" height="297" style="fill: #ffffff"></rect>{"".join(parts)}</svg></div>')


html = ('<!doctype html><html lang="de"><head><meta charset="utf-8"><title>NVL Druckvorlage v1.8</title>'
        '<style>@page{size:210mm 297mm;margin:0}html,body{margin:0;padding:0}.pg{width:210mm;height:297mm;overflow:hidden;break-after:page}.pg svg{display:block}</style></head><body>'
        + "".join(page(pp) for pp in pages[:PAGES]) + '</body></html>')
open(os.path.join(OUT, "print18.html"), "w").write(html)
print(len(html), "Seiten", len(pages), "Palette", PAL)
