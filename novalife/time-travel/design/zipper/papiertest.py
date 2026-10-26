# -*- coding: utf-8 -*-
# Zipper NVL-TT-02 · Papiertest für Mi 28.10.2026, Druckvorlage in Originalgröße (A4 hoch)
# Teppich A in drei Größen, Rückendruck B (Band A oben am Hals) fein und doppelt, Stern C auf der Saumrippe.
# Alles, was breiter als ein A4-Blatt ist, kommt in zwei Hälften: links und rechts der Mitte.
# Aufruf: python3 papiertest.py <ordner>  → papiertest_zipper.html, danach node papier.mjs <ordner>
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import flats as FL
import teppich as TP

F = TP.F
INK, SUB = '#2b2420', '#6b5f55'
FONT = 'font-family:Helvetica,Arial,sans-serif'
PW, PH = 210.0, 297.0
_n = [0]


def uid(p):
    _n[0] += 1
    return f'{p}{_n[0]}'


def text(x, y, s, size=3.4, anchor='start', col=INK, weight=400):
    return f'<text x="{F(x)}" y="{F(y)}" style="{FONT};font-size:{F(size)}px;font-weight:{weight};fill:{col};text-anchor:{anchor}">{s}</text>'


def scale_bar(x, y):
    """10-cm-Kontrolle mit Zentimeterstrichen: Wer anders als 100 % druckt, sieht es sofort"""
    ticks = "".join(f"M{F(x + i * 10)} {F(y)}v{F(-3 if i % 5 else -5)}" for i in range(11))
    return (f'<path d="M{F(x)} {F(y)}h100{ticks}" style="stroke:{INK};stroke-width:0.3;fill:none"/>'
            + text(x + 102, y, 'genau 10 cm?', 2.6, 'start', SUB))


def page(inner, title, sub=''):
    head = text(12, 14, title, 4.6, 'start', INK, 700) + (text(12, 20, sub, 3.0, 'start', SUB) if sub else '')
    return (f'<section class="pg"><svg xmlns="http://www.w3.org/2000/svg" width="210mm" height="297mm" viewBox="0 0 {F(PW)} {F(PH)}">'
            f'<rect width="{F(PW)}" height="{F(PH)}" style="fill:#ffffff"/>{head}{inner}{scale_bar(12, 288)}</svg></section>')


# ---------------------------------------------------------------- Teppich in Hälften
CARPETS = [('S', 210), ('M', 250), ('L', 290)]       # Breite in mm, Höhe im Verhältnis 25 : 17,5


def carpet_half(width, side):
    k = width / TP.W
    fr = 37.0                                            # Fransen samt Knoten, in Teppich-mm
    half_w = k * (TP.W / 2 + fr)
    left = (PW - half_w) / 2                             # linker Rand des sichtbaren Teils auf dem Blatt
    x0 = left + k * fr if side == 'L' else left - k * TP.W / 2   # Teppich-Nullpunkt auf dem Blatt
    y0 = 40.0
    cid = uid('h')
    clip = (f'<rect x="{F(-fr - 5)}" y="-12" width="{F(TP.W / 2 + fr + 5)}" height="{F(TP.H + 24)}"/>' if side == 'L'
            else f'<rect x="{F(TP.W / 2)}" y="-12" width="{F(TP.W / 2 + fr + 5)}" height="{F(TP.H + 24)}"/>')
    # Für Papier ohne Samtrauschen und ohne Schatten: spart Tinte und hält das PDF klein
    rug = (TP.fringes('oma').replace('filter:drop-shadow(0 0.4px 0.3px rgba(0,0,0,.25))', '')
           + TP.carpet('oma', uid=uid('c'), texture=False) + TP.edge('oma'))
    xm = x0 + k * TP.W / 2
    h = k * TP.H
    note = (text(xm - 2, y0 + h + 15, 'Mitte: hier liegt der Reißverschluss', 2.8, 'end', SUB) if side == 'L'
            else text(xm + 2, y0 + h + 15, 'Mitte: hier liegt der Reißverschluss', 2.8, 'start', SUB))
    return (f'<defs><clipPath id="{cid}">{clip}</clipPath></defs>'
            f'<g transform="translate({F(x0)} {F(y0)}) scale({F(k)})"><g clip-path="url(#{cid})">{rug}</g></g>'
            f'<path d="M{F(xm)} {F(y0 - 10)}V{F(y0 + h + 10)}" style="stroke:{INK};stroke-width:0.35;stroke-dasharray:2 1.5"/>' + note)


# ---------------------------------------------------------------- Rückendruck B in Hälften
def print_half(scale, side):
    red, u, hc, top, pg = FL.abdruck_cells(scale, 'oben')
    keep = [(r, c) for r, c in red if ((c - hc) * u <= 0 if side == 'L' else (c - hc) * u >= 0)]
    xs = [(c - hc) * u for r, c in keep]
    w = max(abs(x) for x in xs) + u
    ox = (PW - w) / 2 + (w if side == 'L' else 0)       # Mitte des Drucks auf dem Blatt
    oy = 24.0
    d = "".join(f"M{F(ox + (c - hc - 0.5) * u)} {F(oy + r * u)}h{F(u)}v{F(u)}h{F(-u)}z" for r, c in sorted(keep))
    h = (max(r for r, c in keep) + 1) * u
    # Hinweise in die freie Ecke neben der Spitze, außen auf dem Blatt
    tx = 12 if side == 'L' else PW - 12
    anchor = 'start' if side == 'L' else 'end'
    return (f'<path d="{d}" style="fill:{FL.RED}"/>'
            f'<path d="M{F(ox)} {F(oy - 3)}V{F(oy + h + 3)}" style="stroke:{INK};stroke-width:0.35;stroke-dasharray:2 1.5"/>'
            + text(tx, oy + h - 30, 'Gestrichelt: Mitte hinten', 2.8, anchor, SUB)
            + text(tx, oy + h - 25, 'Oberkante 2 cm unter der Kapuzennaht', 2.8, anchor, SUB)
            + text(tx, oy + h - 20, 'Kapuze darüber: nichts darf vorschauen', 2.8, anchor, SUB))


# ---------------------------------------------------------------- Seite 1
def rib_star(x, y, w=60.0, h=50.0):
    ribs = "".join(f"M{F(x + 0.9 + i * 1.8)} {F(y)}V{F(y + h)}" for i in range(int(w / 1.8)))
    return (f'<rect x="{F(x)}" y="{F(y)}" width="{F(w)}" height="{F(h)}" style="fill:{FL.RIBC};stroke:{FL.LINE};stroke-width:0.3"/>'
            f'<path d="{ribs}" style="stroke:{FL.LINE};stroke-width:0.3;opacity:0.4"/>'
            + FL.star_c(x + w / 2, y + h / 2, 36))


def first_page():
    lines = [
        ('Drucken', 'In tatsächlicher Größe, also 100 %, nicht „an Seite anpassen“. Prüf das Quadrat: genau 5 × 5 cm.'),
        ('Teppich', 'Für jede Größe zwei Blätter, links und rechts. Ausschneiden, an die Mittellinie (Reißverschluss) legen,'),
        ('', 'Oberkante 6 cm unter dem Anfang des Reißverschlusses. Mit Malerkrepp fixieren, nicht mit Tesa auf den Stoff.'),
        ('', 'Je ein Foto von vorn aus 2 m und eins angezogen im Spiegel. Dann sagst du mir, welche Größe: S, M oder L.'),
        ('Rücken', 'Rückendruck B in fein und doppelt, je zwei Hälften. An der Mittellinie zusammenkleben, Oberkante'),
        ('', '2 cm unter der Kapuzennaht. Erst Kapuze darüberklappen: Es darf nichts vorschauen. Dann Kapuze hoch, Foto.'),
        ('', 'Der Umriss ist noch vorläufig, aus deinen Maßen 14 und 15. Der echte Abdruck kommt von dir (Punkt Abdruck).'),
        ('Stern', 'Unten ausschneiden und hinten links auf die Saumrippe legen, Mitte 20 cm von der hinteren Mitte.'),
        ('Abdruck', 'Zwei A4-Blätter zusammenkleben, oben auf den Rücken legen, Kapuze glatt darüber. Mit Bleistift rundum'),
        ('', 'an der Kante der Kapuze entlangfahren. Blatt flach fotografieren, das 5-cm-Quadrat daneben. Foto an mich.'),
    ]
    out = [text(12, 34, 'So gehst du vor', 3.8, 'start', INK, 700)]
    y = 42.0
    for k, s in lines:
        if k:
            y += 2.5
            out.append(text(12, y, k, 3.2, 'start', INK, 700))
        out.append(text(34, y, s, 3.0))
        y += 5.2
    y += 6
    out.append(f'<rect x="12" y="{F(y)}" width="50" height="50" style="fill:none;stroke:{INK};stroke-width:0.4"/>')
    out.append(text(37, y + 27, '5 × 5 cm', 3.2, 'middle', SUB))
    out.append(rib_star(80, y))
    out.append(text(80, y + 56, 'Stern C, 36 mm, auf der Saumrippe (7 cm hoch, hier 5 cm gezeigt)', 2.8, 'start', SUB))
    out.append(text(12, y + 72, 'Sende mir danach: deine Teppichgröße, fein oder doppelt, Fotos und den Abdruck.', 3.2, 'start', INK, 700))
    return page("".join(out), 'Papiertest Zipper NVL-TT-02', 'Mi 28.10.2026 · alles in Originalgröße · Teppich A, Rückendruck B, Stern C')


def build():
    pages = [first_page()]
    for size, w in CARPETS:
        h = w * TP.H / TP.W
        for side, lab in (('L', 'linke Hälfte'), ('R', 'rechte Hälfte')):
            pages.append(page(carpet_half(w, side), f'Teppich {size} · {F(w / 10).replace(".", ",")} × {F(round(h) / 10).replace(".", ",")} cm · {lab}',
                              'Zum Ausschneiden. Die Hälften treffen sich am Reißverschluss.'))
    for sc, name in ((1, 'fein, Zelle 1,33 mm wie an der Jeans'), (2, 'doppelt, Zelle 2,67 mm')):
        for side, lab in (('L', 'linke Hälfte'), ('R', 'rechte Hälfte')):
            pages.append(page(print_half(sc, side), f'Rückendruck B · {name} · {lab}'))
    return pages


if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '.'
    css = ('@page{size:210mm 297mm;margin:0}html,body{margin:0;padding:0;background:#fff}'
           '.pg{width:210mm;height:297mm;overflow:hidden;break-after:page}.pg svg{display:block}')
    html = (f'<!doctype html><html lang="de"><head><meta charset="utf-8"><title>Papiertest Zipper NVL-TT-02</title><style>{css}</style></head>'
            f'<body>{"".join(build())}</body></html>')
    path = os.path.join(out, 'papiertest_zipper.html')
    open(path, 'w', encoding='utf-8').write(html)
    print('ok', path, round(len(html) / 1e6, 1), 'MB')
