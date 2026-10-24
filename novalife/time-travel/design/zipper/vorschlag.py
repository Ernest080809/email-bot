# -*- coding: utf-8 -*-
# Zipper NVL-TT-02 · Designvorschlag v0.1 als HTML für das PDF (A4 quer), Sa 24.10.2026
# Aufruf: python3 vorschlag.py <ausgabeordner>  → zipper_vorschlag_v01.html, danach node pdf.mjs
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import flats as FL
import teppich as TP

F = TP.F
INK, SUB, RULE = '#2b2420', '#6b5f55', '#d8cfc3'
FONT = 'font-family:Helvetica,Arial,sans-serif'
VERSION, DATE, TOTAL = 'v0.1', 'Sa 24.10.2026', 6
_n = [0]


def uid(p):
    _n[0] += 1
    return f'{p}{_n[0]}'


def svg_mm(w, vb, inner, h=None):
    h = h if h is not None else w * vb[3] / vb[2]
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{F(w)}mm" height="{F(h)}mm" '
            f'viewBox="{" ".join(F(v) for v in vb)}" preserveAspectRatio="xMidYMid meet">{inner}</svg>')


def text(x, y, lines, size=3.0, anchor='start', col=INK, weight=400):
    ts = "".join(f'<tspan x="{F(x)}" dy="{F(0 if i == 0 else size * 1.3)}">{s}</tspan>' for i, s in enumerate(lines))
    return f'<text x="{F(x)}" y="{F(y)}" style="{FONT};font-size:{F(size)}px;font-weight:{weight};fill:{col};text-anchor:{anchor}">{ts}</text>'


def leader(x1, y1, x2, y2):
    return (f'<path d="M{F(x1)} {F(y1)}L{F(x2)} {F(y2)}" style="stroke:{INK};stroke-width:0.25;fill:none"/>'
            f'<circle cx="{F(x2)}" cy="{F(y2)}" r="0.8" style="fill:#ffffff;stroke:{INK};stroke-width:0.3"/>')


def page(n, title, body):
    return (f'<section class="pg"><header><span>NOVALIFE · TIME TRAVEL · ZIPPER NVL-TT-02</span>'
            f'<span>Designvorschlag {VERSION} · {DATE}</span></header><h1>{title}</h1>{body}'
            f'<footer><span>Maße vorläufig (Größe M). Die echten Maße kommen aus deinem Messbogen RL-Zipper.</span>'
            f'<span>{n} / {TOTAL}</span></footer></section>')


def carpet_full(variant, with_fringes=True, with_zip=True):
    c = TP.PAL[variant]
    return ((TP.fringes(variant) if with_fringes else '') + TP.carpet(variant, uid=uid('c')) + TP.edge(variant)
            + (TP.zip_strip(stitch=c['edge']) if with_zip else ''))


# ---------------------------------------------------------------- 1 · Vorn
def p1():
    figs = []
    for v, lab, txt in (('oma', 'A · Wie bei Oma', 'Satte Farben, wie der Teppich noch an der Wand hängt.'),
                        ('blass', 'B · Ausgeblichen', 'Dieselbe Zeichnung, nach 30 Jahren Sonne.')):
        figs.append(f'<figure>{svg_mm(120, FL.VB_FULL, FL.front_view(v, uid("f")))}'
                    f'<figcaption><b>{lab}</b> {txt}</figcaption></figure>')
    facts = ('Naturweiß · French Terry 380–450 g/m², innen Schlaufen · Teppich 24 × 15 cm aus bedrucktem Baumwollsamt · '
             'Fransen creme · Reißverschluss Metall antik mit Kinnschutz · Anhänger Achtstern Antik-Kupfer · außen kein Name')
    return page(1, 'Vorn: derselbe Teppich in zwei Farbstimmungen',
                f'<div class="pair">{"".join(figs)}</div><p class="facts">{facts}</p>')


# ---------------------------------------------------------------- 2 · Teppich, Aufbau
def p2():
    s, x0, y0 = 0.62, (273 - 0.62 * TP.W) / 2, 15.0
    X = lambda x: x0 + s * x
    Y = lambda y: y0 + s * y
    g = [f'<g transform="translate({F(x0)} {F(y0)}) scale({s})">{carpet_full("oma")}</g>']
    mb = TP.FRAME + TP.G_OUT + TP.LINE + TP.MAIN / 2               # Mitte der breiten Bordüre
    left = [((36, 20), ['Kante oben und unten,', 'dunkelrot gestickt'], (12, -0.5)),
            ((36, 52), ['Fransen creme, 3–4 cm,', 'in Bündeln geknotet'], (-22, 72)),
            ((36, 88), ['Viertelmedaillon', 'in jeder Ecke'], (TP.FX0 + 9, TP.FY1 - 7))]
    right = [((237, 20), ['Breite Bordüre', 'mit Blütenranke'], (TP.W - mb, 34)),
             ((237, 44), ['Feld rot mit kleinen', 'Blüten und Ranken'], (195, 62)),
             ((237, 66), ['Medaillon persisch oval,', 'dunkelblau'], (TP.CX + 40, TP.CY)),
             ((237, 90), ['Zwei schmale Bordüren,', 'außen und innen'], (TP.W - TP.KILIM - TP.G_OUT / 2, 118))]
    for (lx, ly), lines, (px, py) in left:
        g.append(text(lx, ly, lines, 3.0, 'end'))
        g.append(leader(lx + 1.5, ly - 1.0, X(px), Y(py)))
    for (lx, ly), lines, (px, py) in right:
        g.append(text(lx, ly, lines, 3.0, 'start'))
        g.append(leader(lx - 1.5, ly - 1.0, X(px), Y(py)))
    g.append(text(X(TP.CX) + 4, 6.5, ['Der Reißverschluss teilt den Teppich. Die Innenkanten laufen direkt in die Zip-Naht.'], 3.0))
    g.append(leader(X(TP.CX) + 3, 5.5, X(TP.CX), Y(-4)))
    # Maße
    yb = Y(TP.H) + 8
    g.append(f'<path d="M{F(X(0))} {F(yb)}H{F(X(TP.W))}M{F(X(0))} {F(yb-2)}v4M{F(X(TP.W))} {F(yb-2)}v4" style="stroke:{SUB};stroke-width:0.3"/>')
    g.append(text(X(TP.CX), yb + 4.8, ['24 cm breit · 15 cm hoch'], 3.2, 'middle', SUB))
    notes = ('<div class="cols3">'
             '<p><b>Material.</b> Bedruckter Baumwollsamt, matt. Nach deiner Farbwahl bestellen wir eine Probe in A4. '
             'Der Teppich wird aufgenäht, bevor der Reißverschluss eingesetzt wird.</p>'
             '<p><b>Herkunft.</b> Die Zeichnung ist neu. Museumsteppiche dienen nur als Stimmung, übernommen ist nichts. '
             'Im Teppich stehen keine Novalife-Zeichen.</p>'
             '<p><b>Größe.</b> 24 × 15 cm ist der Mittelwert. Beim Papiertest am Mi 28.10. legst du 20, 24 und 28 cm Breite '
             'auf deinen RL, dann entscheiden wir.</p></div>')
    return page(2, 'Der Teppich: so ist er aufgebaut', svg_mm(273, (0, 0, 273, 128), "".join(g)) + notes)


# ---------------------------------------------------------------- 3 · Oma oder ausgeblichen
def p3():
    small, crops = [], []
    pad = 40.0
    for v, lab in (('oma', 'A · Wie bei Oma'), ('blass', 'B · Ausgeblichen')):
        vb = (-pad, -8, TP.W + 2 * pad, TP.H + 16)
        small.append(f'<figure><figcaption><b>{lab}</b></figcaption>{svg_mm(126, vb, carpet_full(v))}</figure>')
        cvb = (-24, -4, 120, 64)                                    # oben links, 1:1
        crops.append(f'<figure>{svg_mm(120, cvb, carpet_full(v), 64)}</figure>')
    body = (f'<div class="pair tight">{"".join(small)}</div>'
            f'<p class="lbl">Ausschnitt oben links in Originalgröße (bei 24 × 15 cm und Druck in 100 %)</p>'
            f'<div class="pair tight">{"".join(crops)}</div>'
            '<p class="rec"><b>Mein Rat: A.</b> Auf Naturweiß und im Video wirkt der kräftige Teppich. B ist leiser und sehr vintage, '
            'kann auf Creme aber flau aussehen. Endgültig zeigt es die Samtprobe. <b>Deine Wahl bis Di 27.10.</b></p>')
    return page(3, 'Oma oder ausgeblichen?', body)


# ---------------------------------------------------------------- 4 · Rücken
def swatch(scale, invert, w=60.0, h=27.0):
    u = TP_CELL * scale
    band_top = FL.PRINT_BOTTOM - FL.FN.BAND_ROWS * u
    vb = (-w / 2, band_top - h * 0.62, w, h)
    inner = (f'<rect x="{F(vb[0])}" y="{F(vb[1])}" width="{F(w)}" height="{F(h)}" style="fill:{FL.GARMENT}"/>'
             + FL.hood_print(scale, invert))
    return svg_mm(w, vb, inner, h)


def rib_star(w=60.0, h=50.0):
    cx, cy = 0.0, h / 2
    ribs = "".join(f"M{F(x)} 0V{F(h)}" for x in [-w / 2 + 0.9 + i * 1.8 for i in range(int(w / 1.8))])
    inner = (f'<rect x="{F(-w/2)}" y="0" width="{F(w)}" height="{F(h)}" style="fill:{FL.RIBC}"/>'
             f'<path d="{ribs}" style="stroke:{FL.LINE};stroke-width:0.35;opacity:0.45"/>'
             f'<path d="M{F(-w/2)} 0.3H{F(w/2)}" style="stroke:{FL.LINE};stroke-width:0.6"/>'
             + FL.star_c(cx, cy, 36))
    return svg_mm(w, (-w / 2, 0, w, h), inner, h)


TP_CELL = FL.FN.CELL


def p4():
    v_down = svg_mm(99, FL.VB_DOWN, FL.back_view('down', hidden=True))
    v_up = svg_mm(99, FL.VB_FULL, FL.back_view('up', 2))
    side = ('<div class="side">'
            f'<p class="lbl">Muster fein, wie an der Jeans (1:1)</p>{swatch(1, False)}'
            f'<p class="lbl">Muster doppelt, so gezeichnet (1:1)</p>{swatch(2, False)}'
            f'<p class="lbl">Gegenvorschlag: nur die Linien rot (1:1)</p>{swatch(2, True)}'
            f'<p class="lbl">Stern C auf der Saumrippe, 36 mm (1:1)</p>{rib_star()}</div>')
    views = (f'<div class="views"><figure><figcaption><b>Kapuze liegt</b></figcaption>{v_down}'
             '<p class="small">Man sieht nur den Stern. Die rote Strichlinie zeigt, wo darunter gedruckt ist: '
             'Kapuzenform, rundum 2 cm kleiner als die liegende Kapuze.</p></figure>'
             f'<figure><figcaption><b>Kapuze oben</b></figcaption>{v_up}</figure></div>')
    notes = ('<div class="cols2">'
             '<p><b>Druck.</b> Muster E von der Münztasche als Fläche, unten gerade abgeschlossen mit Band A. Nur Knallrot, '
             'der Stoff ist das Weiß. Siebdruck wasserbasiert, auf das Zuschnittteil vor dem Nähen. Der Rotton wird aufs Stickgarn abgestimmt.</p>'
             '<p><b>Stern.</b> Wie C an der Jeans: 36 mm, Knallrot, Plattstich, dieselbe Stickdatei. Er wird auf die Rippe gestickt, '
             'bevor sie angenäht wird. Die Mustergröße für den Druck entscheidet der Papiertest.</p></div>')
    return page(4, 'Rücken: der Stern immer, das Muster nur mit Kapuze oben',
                f'<div class="back">{views}{side}</div>{notes}')


# ---------------------------------------------------------------- 5 · Details
def crop(vb, w, inner):
    return svg_mm(w, vb, f'<rect x="{F(vb[0])}" y="{F(vb[1])}" width="{F(vb[2])}" height="{F(vb[3])}" style="fill:#ffffff"/>{inner}')


def labels_svg():
    tl = (f'<rect x="2" y="4" width="46" height="18" rx="1" style="fill:#f6f1e7;stroke:{FL.LINE};stroke-width:0.4"/>'
          f'<path d="M2 6.5H48M2 19.5H48" style="stroke:{FL.LINE};stroke-width:0.25;stroke-dasharray:1 0.8"/>'
          + text(25, 12.3, ['Baum (vereinfacht)'], 2.6, 'middle', SUB) + text(25, 16.4, ['Entwurf folgt'], 2.2, 'middle', SUB)
          + text(25, 27.5, ['Nackenlabel, gewebt, innen'], 2.6, 'middle'))
    care = [('Material', 'nach Angebot'), ('Pflege', 'Symbole'), ('Größe', 'M · Brust 62 cm'), ('Nummer', 'Nr. 001'), ('Hersteller', 'Name, Land')]
    cl = [f'<rect x="60" y="2" width="28" height="56" rx="0.6" style="fill:#ffffff;stroke:{FL.LINE};stroke-width:0.4"/>']
    for i, (k, v) in enumerate(care):
        cl.append(text(63, 9 + i * 9.5, [k], 2.3, 'start', SUB))
        cl.append(text(63, 12.6 + i * 9.5, [v], 2.5, 'start', INK, 700 if k in ('Größe', 'Nummer') else 400))
    cl.append(text(74, 63, ['Pflegeetikett in der Seitennaht'], 2.6, 'middle'))
    return svg_mm(80, (0, 0, 92, 66), tl + "".join(cl))


def p5():
    front = lambda: FL.front_view('oma', uid('d'))
    zip_top = crop((-60, 62, 120, 130), 64, front())
    eyelet = crop((22, 6, 90, 90), 48, FL.front_view('oma', uid('d'), carpet=False))
    aglet = crop((22, 270, 90, 90), 48, front())
    pocket = crop((0, 400, 300, 300), 62, FL.front_view('oma', uid('d'), carpet=False))
    figs = [
        (zip_top, 'Reißverschluss oben', 'Kinnschutz, Schieber dunkel/antik, Band naturweiß. Der Anhänger ist ein fertiger Achtstern aus Metall '
                                         'in Antik-Kupfer, etwa 25 mm, an einem Ring.'),
        (f'<div class="stack">{eyelet}{aglet}</div>', 'Kapuze und Kordeln', 'Kapuze doppellagig. Kordeln naturweiß, Ösen und Metallenden '
                                                                            'in Antik-Kupfer.'),
        (pocket, 'Taschen und Rippe', 'Eine Tasche links, eine rechts, keine Kängurutasche. Art und Lage wie bei deinem RL, '
                                      'gezeichnet ist ein Platzhalter. Rippe an Ärmel und Saum in Naturweiß.'),
    ]
    cells = "".join(f'<figure class="det">{svg}<figcaption><b>{t}.</b> {d}</figcaption></figure>' for svg, t, d in figs)
    row2 = (f'<div class="det2">{labels_svg()}'
            '<p><b>Etiketten.</b> Nummeriert wie die Jeans, auf dem Innenetikett. Auf dem Etikett steht die echte Brustweite, '
            'z. B. „M · Brust 62 cm“. Hangtag und Verpackung wie bei der Jeans, das Design klären wir nach dem Tech Pack.</p>'
            '<p><b>Schnitt.</b> Eigener Schnitt nach deinem weißen RL-Zipper: Schultern 3–5 cm überschnitten, Länge wie ein normaler '
            'Slim Fit, Ärmel normal lang. Saumrippe mindestens 5 cm, damit der Stern draufpasst. Nähte Ton in Ton. '
            'Stoff schwer, 380–450 g/m², innen Schlaufen.</p></div>')
    return page(5, 'Details', f'<div class="dets">{cells}</div>{row2}')


# ---------------------------------------------------------------- 6 · Fragen
def p6():
    q = ('<div class="qa"><div>'
         '<h2>Fragen an dich</h2><ol>'
         '<li><b>Teppichfarbe: A oder B?</b> Bis Di 27.10. Mein Rat: A, siehe Seite 3. Wählst du früher, drucke ich den Papiertest '
         'gleich in dieser Farbe.</li>'
         '<li><b>Die Zeichnung.</b> Passen Medaillon, Feld, Ecken und Bordüren so? Was soll mehr nach dem Teppich bei deiner Oma aussehen?</li>'
         '<li><b>Rückendruck.</b> Roter Grund wie an der Münztasche (gezeichnet) oder nur die Linien rot? Mein Rat: wie gezeichnet. '
         'Dann ist es dasselbe Muster wie an der Jeans.</li>'
         '<li><b>Kordeln vor dem Teppich.</b> Sie hängen über den Teppich, so wie beim RL. Ist das okay, oder willst du kürzere Kordeln?</li>'
         '</ol>'
         '<h2>Annahmen</h2><p class="small">Habe ich so gezeichnet. Sag Bescheid, wenn du es anders willst.</p><ul>'
         '<li>Teppich 24 × 15 cm, Oberkante 6 cm unter dem Zip-Anfang. Für den Papiertest: 20, 24 und 28 cm breit.</li>'
         '<li>Stern-Anhänger etwa 25 mm, an einem Ring am Schieber.</li>'
         '<li>Druckfläche: eine Reihe Rot als saubere Kante, eine Reihe frei zwischen Muster E und Band A, '
         'das Stern-Motiv von Band A in der Mitte.</li>'
         '<li>Stern C sitzt 20 cm links von der hinteren Mitte, mittig auf der Rippe.</li>'
         '</ul></div><div>'
         '<h2>Worauf ich beim Tech Pack achte</h2><ul>'
         '<li><b>Versatz am Zip.</b> Die beiden Teppichhälften müssen genau auf einer Höhe liegen. Schon 3 mm Versatz sieht man '
         'am Medaillon sofort. Das wird ein Prüfpunkt für die Fabrik.</li>'
         '<li><b>Fransen in der Wäsche.</b> Geknotete Fransen können ausfransen. Ich plane eine fertige Fransenborte mit gewebtem Rand, '
         'die unter dem Samt mitgenäht wird, und eine Testwäsche am Muster.</li>'
         '<li><b>Samt auf Sweat.</b> Der Samt dehnt sich nicht, der Sweat schon. Damit nichts wellt, kommt beim Aufnähen ein Vlies dahinter.</li>'
         '<li><b>Kosten.</b> Der Teppich ist das aufwendigste Teil: Samtdruck, Fransen, Stickkante, Aufnähen. Was er kostet, sehen wir erst in den Angeboten.</li>'
         '</ul>'
         '<h2>Nächste Schritte</h2><table>'
         '<tr><td>Sa/So 24./25.10.</td><td>du</td><td>RL-Zipper ausmessen (Messbogen), Fotos schicken</td></tr>'
         '<tr><td>Mo 26.10.</td><td>ich</td><td>Papiertest-Drucke, Sweat-Fabriken in Portugal, Druckereien für Baumwollsamt</td></tr>'
         '<tr><td>Di 27.10.</td><td>du</td><td>Teppichfarbe wählen, Fragen beantworten</td></tr>'
         '<tr><td>Mi 28.10.</td><td>du</td><td>Papiertest auf deinem RL</td></tr>'
         '</table></div></div>')
    return page(6, 'Fragen, Annahmen und nächste Schritte', q)


CSS = f"""@page{{size:297mm 210mm;margin:0}}
html,body{{margin:0;padding:0;background:#fff}}
body{{{FONT};color:{INK};-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.pg{{width:297mm;height:210mm;box-sizing:border-box;padding:8mm 12mm 0;position:relative;overflow:hidden;break-after:page}}
header{{display:flex;justify-content:space-between;font-size:7pt;letter-spacing:.08em;color:{SUB};border-bottom:.3mm solid {RULE};padding-bottom:1.6mm}}
h1{{font-size:16pt;margin:3.5mm 0 3mm;font-weight:700;letter-spacing:-.01em}}
h2{{font-size:10.5pt;margin:0 0 1.6mm;font-weight:700}}
footer{{position:absolute;left:12mm;right:12mm;bottom:5mm;display:flex;justify-content:space-between;font-size:6.5pt;color:{SUB};border-top:.3mm solid {RULE};padding-top:1.4mm}}
figure{{margin:0}} svg{{display:block}}
figcaption{{font-size:9pt;line-height:1.35;margin:1.2mm 0}}
.pair{{display:flex;justify-content:space-between;gap:8mm}} .pair figure{{flex:1;display:flex;flex-direction:column;align-items:center}}
.pair.tight{{gap:6mm}}
.facts{{font-size:8.3pt;line-height:1.45;color:{INK};margin:2mm 0 0;border-top:.3mm solid {RULE};padding-top:2mm}}
.cols3{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:7mm;font-size:8.6pt;line-height:1.42;margin-top:2mm}}
.cols2{{display:grid;grid-template-columns:1fr 1fr;gap:7mm;font-size:8.4pt;line-height:1.42;margin-top:1mm}}
.cols3 p,.cols2 p{{margin:0}}
.lbl{{font-size:7.6pt;color:{SUB};margin:1.6mm 0 1mm}}
.rec{{font-size:9pt;line-height:1.4;margin:2.5mm 0 0}}
.back{{display:flex;justify-content:space-between}}
.views{{display:flex;gap:8mm}} .views figure{{width:99mm}}
.side{{width:60mm}} .side .lbl:first-child{{margin-top:0}}
.small{{font-size:7.8pt;line-height:1.4;color:{SUB};margin:1mm 0}}
.dets{{display:grid;grid-template-columns:64mm 98mm 62mm;justify-content:space-between;align-items:start}}
.det figcaption{{font-size:8.3pt}}
.stack{{display:flex;gap:2mm}}
.det2{{display:grid;grid-template-columns:80mm 1fr 1fr;gap:8mm;margin-top:4mm;padding-top:3mm;border-top:.3mm solid {RULE};font-size:8.4pt;line-height:1.42}}
.det2 p{{margin:0}}
.qa{{display:grid;grid-template-columns:1fr 1fr;gap:10mm;font-size:8.6pt;line-height:1.42}}
.qa ol,.qa ul{{margin:0 0 3.5mm;padding-left:4.5mm}} .qa li{{margin-bottom:1.4mm}}
.qa table{{border-collapse:collapse;width:100%}} .qa td{{padding:.8mm 1.5mm .8mm 0;vertical-align:top;border-top:.25mm solid {RULE}}}
.qa td:first-child{{white-space:nowrap;font-weight:700}} .qa td:nth-child(2){{color:{SUB}}}
"""


if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '.'
    pages = [p1(), p2(), p3(), p4(), p5(), p6()]
    html = (f'<!doctype html><html lang="de"><head><meta charset="utf-8"><title>Zipper NVL-TT-02 Designvorschlag {VERSION}</title>'
            f'<style>{CSS}</style></head><body>{"".join(pages)}</body></html>')
    path = os.path.join(out, 'zipper_vorschlag_v01.html')
    open(path, 'w', encoding='utf-8').write(html)
    print('ok', path, round(len(html) / 1e6, 1), 'MB')
