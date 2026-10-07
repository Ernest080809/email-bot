# -*- coding: utf-8 -*-
# Canvas auf Design v1.5 bringen (Fragmente tauschen, Texte anpassen, Taschen-Board neu)
import sys, os, json, io, contextlib
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "design")
sys.path.insert(0, D)
os.chdir(D)
with contextlib.redirect_stdout(io.StringIO()):
    import build15 as N
os.chdir(os.path.dirname(os.path.abspath(__file__)))
P = "project/"
def rd(fn): return open(fn, encoding="utf-8").read()
def old(n): return rd(os.path.join(D, "old14", n + ".svgfrag"))
def rep(s, a, b, cnt=1):
    assert s.count(a) == cnt, (a[:80], s.count(a))
    return s.replace(a, b)

# ---------- Vorderansicht ----------
M = rd(P + "Main.dc.html")
OUTL = '<rect x="284" y="176.8" width="40" height="40" style="fill: none; stroke: #142236; stroke-width: 1.2px"></rect>'
STIT = '<path d="M 288.0 181.6 L 320.0 181.6" style="fill: none; stroke: #d4ab52; stroke-width: 1.2px; stroke-dasharray: 3 2.5"></path>'
ob, oc = old("front_band"), old("front_coin")
seq = ob + "\n" + oc + "\n" + STIT + "\n" + OUTL
assert M.count(seq) == 1, "Sequenz in der Platzierungsgruppe nicht gefunden"
M = M.replace(seq, N.FRONT_COIN + "\n" + N.COIN_STITCH + "\n" + N.COIN_OUTLINE + "\n" + N.FRONT_BAND)
M = rep(M, OUTL, N.COIN_OUTLINE)
M = rep(M, STIT, N.COIN_STITCH)
M = rep(M, "<b>A</b> · Vyshyvanka-Band 28 mm · feiner Kreuzstich · entlang der Taschenöffnung",
        "<b>A</b> · Vyshyvanka-Band 23 mm (v1.5, vorher 28) · feiner Kreuzstich · entlang der Taschenöffnung")
M = rep(M, "<b>E</b> · Münztasche komplett bestickt · feiner Kreuzstich · 49 × 49 mm",
        "<b>E</b> · Münztasche komplett bestickt · 60 × 60 mm auf 62-mm-Tasche (v1.5, vorher 49)")
M = rep(M, "Links und rechts gelten so, wie du die Hose vor dir liegen siehst.",
        "Links und rechts gelten immer vom Träger aus. A und E sitzen an der rechten Vordertasche, in dieser Zeichnung also links. Die untere rechte Ecke der Münztasche verschwindet unter dem Band, wie bei deiner Eightyfive.")
open(P + "Main.dc.html", "w", encoding="utf-8").write(M)

# ---------- Rückansicht ----------
R = rd(P + "Rueckansicht.dc.html")
R = rep(R, old("back_scene"), N.BACK_B)
R = rep(R, old("back_ears"), N.BACK_B2)
R = rep(R, old("back_alatyr"), N.BACK_C)
R = rep(R, "Platzierung von Serp mit Garbe, Alatyr auf der Passe und Lebensbaum-Patch",
        "Platzierung: Serp schneidet in die Garbe auf der linken Gesäßtasche, Alatyr auf der rechten Gesäßtasche, Lebensbaum-Patch am Bund")
R = rep(R, "<span>Serp mit Garbe · ca. 48 × 76 mm · rechte Gesäßtasche. Die Klingenspitze schneidet in die Halme. Darüber an der Taschenkante zwei Ähren, eine rote Linie mit weißem Rand und darunter die Goldfäden</span>",
        "<span>Serp schneidet in die Garbe · realistisch · ca. 44 × 75 mm · <b>linke</b> Gesäßtasche. Die Klinge greift hinter die Halme, zwei Halme sind durchtrennt. Darüber zwei Ähren auf einer roten Kreuzstich-Linie, darunter neun Goldfäden</span>")
R = rep(R, "<span>Alatyr · 36 mm · feiner Kreuzstich · Passe hinten links, über der Gesäßtasche, zwischen den Gürtelschlaufen</span>",
        "<span>Alatyr · 36 mm · feiner Kreuzstich · <b>rechte</b> Gesäßtasche, waagerecht mittig, Mitte auf Höhe der roten Linie links (v1.5, vorher Passe)</span>")
R = rep(R, "Goldfäden: Variante 2, entschieden am 29.09. Sie hängen 9–16 mm unter der roten Linie, werden nach der Wäsche von Hand gesetzt und innen in der Tasche verknotet.",
        "Goldfäden: Variante 2 (29.09.), seit v1.5 länger und dicker: 9 Fäden, 18–30 mm, dreifach gezwirnt, sie reichen bis in die Ähren der Garbe. Nach der Wäsche von Hand gesetzt, innen in der Tasche verknotet.")
R = rep(R, "Hellblau angedeutet: Gesäßabrieb und Honeycombs. A und E sitzen vorn.",
        "Hellblau angedeutet: Gesäßabrieb und Honeycombs. A und E sitzen vorn. Links und rechts vom Träger aus, in der Rückansicht also wie gezeichnet.")
R = rep(R, '<rect x="562" y="292" width="20" height="20" style="fill: #c0392b; stroke: #ffffff; stroke-width: 2px"></rect><text x="572" y="306.5" style="fill: #ffffff">B</text>',
        '<rect x="298" y="292" width="20" height="20" style="fill: #c0392b; stroke: #ffffff; stroke-width: 2px"></rect><text x="308" y="306.5" style="fill: #ffffff">B</text>')
R = rep(R, '<rect x="276" y="184" width="20" height="20" style="fill: #c0392b; stroke: #ffffff; stroke-width: 2px"></rect><text x="286" y="198.5" style="fill: #ffffff">C</text>',
        '<rect x="562" y="272" width="20" height="20" style="fill: #c0392b; stroke: #ffffff; stroke-width: 2px"></rect><text x="572" y="286.5" style="fill: #ffffff">C</text>')
open(P + "Rueckansicht.dc.html", "w", encoding="utf-8").write(R)

# ---------- Board „Gesäßtaschen v1.5“ (ersetzt die Goldfäden-Varianten) ----------
G = rd(P + "Goldfaeden.dc.html")
head = G[:G.index('<div style="width: 1000px; height: 840px;')]
tail = G[G.index("</x-dc>"):]
def card(svg, label, num, title, text):
    return ('<div style="display: flex; flex-direction: column; gap: 14px; width: 430px">'
            f'<svg width="430" height="500" viewBox="-14 -14 172 200" role="img" aria-label="{label}" style="display: block">{svg}</svg>'
            '<div style="display: flex; gap: 12px; align-items: flex-start"><span style="display: flex; flex-shrink: 0; width: 26px; height: 26px; border-radius: 13px; background: #1d2330; color: #ffffff; font-family: \'IBM Plex Mono\', monospace; font-size: 13px; font-weight: 600; align-items: center; justify-content: center">'
            f'{num}</span><div style="display: flex; flex-direction: column; gap: 4px"><span style="font-size: 17px; font-weight: 700; color: #1d2330">{title}</span>'
            f'<span style="font-size: 13.5px; line-height: 1.45; color: #4a4f5c">{text}</span></div></div></div>')
body = ('<div style="width: 1000px; height: 840px; box-sizing: border-box; padding: 44px 40px 40px; display: flex; flex-direction: column; gap: 26px; background: #efece5; color: #1d2330; font-family: \'Archivo\', Helvetica, sans-serif">'
        '<div style="display: flex; flex-direction: column; gap: 8px">'
        '<div style="font-family: \'IBM Plex Mono\', monospace; font-size: 11px; letter-spacing: 0.16em; text-transform: uppercase; color: #5f6470">NVL-TT-01 · hinten · Design v1.5 · 2,5-fach vergrößert</div>'
        '<h1 style="margin: 0; font-family: \'Anton\', Impact, sans-serif; font-weight: 400; font-size: 44px; line-height: 1; text-transform: uppercase; color: #1d2330">Gesäßtaschen · v1.5</h1>'
        '</div><div style="display: flex; gap: 60px">'
        + card(N.pocket_left(), "Linke Gesäßtasche: Ähren auf roter Linie, lange Goldfäden, darunter die Garbe, in die der Serp greift", "B",
               "Linke Tasche · Serp und Garbe",
               "Realistisch statt Symbol: Die Klinge greift hinter die Halme, zwei Halme sind durchtrennt, das Strohband ist gedreht. Neun Goldfäden, 18–30 mm, reichen bis in die Ähren.")
        + card(N.pocket_right(), "Rechte Gesäßtasche: Alatyr im feinen Kreuzstich, waagerecht mittig", "C",
               "Rechte Tasche · Alatyr",
               "36 mm, waagerecht mittig, Mitte auf der Höhe der roten Linie links. Der Patch D sitzt darüber am Bund.")
        + '</div></div>\n')
G = head + body + tail
G = G.replace("<title>Goldfäden Varianten</title>", "<title>Gesäßtaschen v1.5</title>")
open(P + "Goldfaeden.dc.html", "w", encoding="utf-8").write(G)

# ---------- canvas.json ----------
C = json.loads(rd(P + "canvas.json"))
C["boards"]["Goldfaeden.dc.html"]["title"] = "Gesäßtaschen · v1.5"
C["notes"]["titel"]["text"] = "NVL-TT-01 · Projekt Slavic · Design v1.5"
open(P + "canvas.json", "w", encoding="utf-8").write(json.dumps(C, ensure_ascii=False, indent=2))
print("ok", len(M), len(R), len(G))
