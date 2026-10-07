# -*- coding: utf-8 -*-
# Canvas auf Design v1.6: Serp und Garbe runter von der Tasche, drei Ähren auf rotem Band, Serp im Stoppelfeld am linken Bein
import sys, os, json, io, contextlib
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "design")
sys.path.insert(0, D)
os.chdir(D)
with contextlib.redirect_stdout(io.StringIO()):
    import build15 as N15
    import build16 as N
os.chdir(os.path.dirname(os.path.abspath(__file__)))
P = "project/"
def rd(fn): return open(fn, encoding="utf-8").read()
def rep(s, a, b, cnt=1):
    assert s.count(a) == cnt, (a[:90], s.count(a))
    return s.replace(a, b)

# ---------- Vorderansicht ----------
M = rd(P + "Main.dc.html")
gs = M.index('<g style="display: {{zoneDisplay}}">')
ge = M.index('</g>', gs)
assert '<g' not in M[gs + 5:ge], "verschachtelte Gruppe in der Platzierung"
M = M[:ge] + N.FRONT_SIDE + "\n" + M[ge:]
M = rep(M, '<text x="268" y="200.5" style="fill: #ffffff">E</text>',
        '<text x="268" y="200.5" style="fill: #ffffff">E</text>\n' + N.FRONT_SIDE_LABEL)
ICON_B = ('<svg width="36" height="16" viewBox="0 0 36 16" style="flex-shrink: 0"><rect x="0" y="0" width="36" height="16" style="fill: #2f4a6e"></rect>'
          '<path d="M5 15V11.5M9 15V12.5M13 15V11.8M27 15V12.4" style="stroke: #dcc07a; stroke-width: 1.3px"></path>'
          '<path d="M21 9C22 3 13.5 0.5 11.5 6" style="fill: none; stroke: #f4f1ea; stroke-width: 2px; stroke-linecap: round"></path>'
          '<path d="M21 9.5L21.6 15" style="stroke: #6e4a2a; stroke-width: 2.4px; stroke-linecap: round"></path></svg>')
M = rep(M, "<span><b>E</b> · Münztasche komplett bestickt · 60 × 60 mm auf 62-mm-Tasche (v1.5, vorher 49)</span></div>",
        "<span><b>E</b> · Münztasche komplett bestickt · 60 × 60 mm auf 62-mm-Tasche (v1.5, vorher 49)</span></div>\n"
        f'<div style="display: flex; gap: 12px; align-items: center">{ICON_B}<span><b>B</b> · Serp im Stoppelfeld · ca. 22 × 35 mm · linkes Bein vorn, 10 mm neben der Seitennaht, Mitte ca. 45 cm unter dem Bund (v1.6, Vorschlag nach deiner Skizze)</span></div>')
M = rep(M, "<span><b>B</b>, <b>C</b> und <b>D</b> sitzen hinten · siehe Rückansicht</span>",
        "<span><b>B2</b>, <b>C</b> und <b>D</b> sitzen hinten · siehe Rückansicht</span>")
M = rep(M, "A und E sitzen an der rechten Vordertasche, in dieser Zeichnung also links.",
        "A und E sitzen an der rechten Vordertasche, in dieser Zeichnung also links. B sitzt am linken Bein, in dieser Zeichnung also rechts.")
M = rep(M, 'aria-label="Flachzeichnung der Jeans W32 von vorn mit Messpunkten, Referenzkontur und Ornament-Platzierung"',
        'aria-label="Flachzeichnung der Jeans W32 von vorn mit Messpunkten, Referenzkontur und Ornament-Platzierung: Band und Münztasche rechts, Serp im Stoppelfeld am linken Bein"')
open(P + "Main.dc.html", "w", encoding="utf-8").write(M)

# ---------- Rückansicht ----------
R = rd(P + "Rueckansicht.dc.html")
R = rep(R, N15.BACK_B, "")
R = rep(R, N15.BACK_B2, N.BACK_B2)
R = rep(R, '<rect x="298" y="292" width="20" height="20" style="fill: #c0392b; stroke: #ffffff; stroke-width: 2px"></rect><text x="308" y="306.5" style="fill: #ffffff">B</text>',
        '<rect x="294" y="272" width="26" height="20" style="fill: #c0392b; stroke: #ffffff; stroke-width: 2px"></rect><text x="307" y="286.5" style="fill: #ffffff">B2</text>')
R = rep(R, "Platzierung: Serp schneidet in die Garbe auf der linken Gesäßtasche, Alatyr auf der rechten Gesäßtasche, Lebensbaum-Patch am Bund",
        "Platzierung: drei Ähren auf rotem Band mit Goldfäden auf der linken Gesäßtasche, Alatyr auf der rechten Gesäßtasche, Lebensbaum-Patch am Bund")
R = rep(R, 'align-items: center; justify-content: center">B</span><span>Serp schneidet in die Garbe · realistisch · ca. 44 × 75 mm · <b>linke</b> Gesäßtasche. Die Klinge greift hinter die Halme, zwei Halme sind durchtrennt. Darüber zwei Ähren auf einer roten Kreuzstich-Linie, darunter neun Goldfäden</span>',
        'align-items: center; justify-content: center; font-size: 11px">B2</span><span>Drei Ähren auf einem einfach roten Band, 48 mm, darunter neun Goldfäden · <b>linke</b> Gesäßtasche, das Band auf Höhe des Alatyr (v1.6: Serp und Garbe sind von der Tasche runter)</span>')
R = rep(R, "Goldfäden: Variante 2 (29.09.), seit v1.5 länger und dicker: 9 Fäden, 18–30 mm, dreifach gezwirnt, sie reichen bis in die Ähren der Garbe. Nach der Wäsche von Hand gesetzt, innen in der Tasche verknotet.",
        "Goldfäden: Variante 2 (29.09.), seit v1.5 länger und dicker: 9 Fäden, 18–30 mm, dreifach gezwirnt. Nach der Wäsche von Hand gesetzt, innen in der Tasche verknotet. <b>B</b>, der Serp im Stoppelfeld, sitzt vorn am linken Bein an der Seitennaht, siehe Vorderansicht.")
open(P + "Rueckansicht.dc.html", "w", encoding="utf-8").write(R)

# ---------- Board „Details · v1.6“ ----------
G = rd(P + "Goldfaeden.dc.html")
head = G[:G.index('<div style="width: 1000px; height: 840px;')]
tail = G[G.index("</x-dc>"):]
def card(svg, vb, label, num, title, text):
    return ('<div style="display: flex; flex-direction: column; gap: 14px; width: 280px">'
            f'<svg width="280" height="326" viewBox="{vb}" role="img" aria-label="{label}" style="display: block">{svg}</svg>'
            '<div style="display: flex; gap: 12px; align-items: flex-start"><span style="display: flex; flex-shrink: 0; width: 28px; height: 28px; border-radius: 14px; background: #1d2330; color: #ffffff; font-family: \'IBM Plex Mono\', monospace; font-size: 12px; font-weight: 600; align-items: center; justify-content: center">'
            f'{num}</span><div style="display: flex; flex-direction: column; gap: 4px"><span style="font-size: 16px; font-weight: 700; color: #1d2330">{title}</span>'
            f'<span style="font-size: 13px; line-height: 1.45; color: #4a4f5c">{text}</span></div></div></div>')
body = ('<div style="width: 1000px; height: 840px; box-sizing: border-box; padding: 44px 40px 40px; display: flex; flex-direction: column; gap: 26px; background: #efece5; color: #1d2330; font-family: \'Archivo\', Helvetica, sans-serif">'
        '<div style="display: flex; flex-direction: column; gap: 8px">'
        '<div style="font-family: \'IBM Plex Mono\', monospace; font-size: 11px; letter-spacing: 0.16em; text-transform: uppercase; color: #5f6470">NVL-TT-01 · hinten und an der Seite · Design v1.6</div>'
        '<h1 style="margin: 0; font-family: \'Anton\', Impact, sans-serif; font-weight: 400; font-size: 44px; line-height: 1; text-transform: uppercase; color: #1d2330">Details · v1.6</h1>'
        '</div><div style="display: flex; gap: 40px">'
        + card(N.pocket_left(), "-14 -14 172 200", "Linke Gesäßtasche: drei Ähren auf einem einfach roten Band, darunter neun Goldfäden", "B2",
               "Linke Tasche · Ähren und Fäden",
               "Drei Ähren wie in v1.4, Band einfach rot, 48 mm. Darunter neun Goldfäden, 18–30 mm, von Hand nach der Wäsche. Serp und Garbe sind von der Tasche runter.")
        + card(N.pocket_right(), "-14 -14 172 200", "Rechte Gesäßtasche: Alatyr im feinen Kreuzstich, waagerecht mittig", "C",
               "Rechte Tasche · Alatyr",
               "36 mm, waagerecht mittig, auf Höhe des roten Bands links. Der Patch D sitzt darüber am Bund.")
        + card(N.side_detail(), "-12 -6 60 70", "Linkes Bein vorn an der Seitennaht: kleiner Serp über abgeschnittenen Halmen", "B",
               "Linkes Bein · Serp im Stoppelfeld",
               "Vorschlag nach deiner Skizze: kleiner Serp, abgeschnittene Halme, 2–5 mm hoch. Ca. 22 × 35 mm, 10 mm neben der Seitennaht, Mitte ca. 45 cm unter dem Bund. Klinge weiß, ohne Rot. Hier stärker vergrößert als die Taschen.")
        + '</div></div>\n')
G = head + body + tail
G = G.replace("<title>Gesäßtaschen v1.5</title>", "<title>Details v1.6</title>")
open(P + "Goldfaeden.dc.html", "w", encoding="utf-8").write(G)

# ---------- canvas.json ----------
C = json.loads(rd(P + "canvas.json"))
C["boards"]["Goldfaeden.dc.html"]["title"] = "Details · v1.6"
C["notes"]["titel"]["text"] = "NVL-TT-01 · Projekt Slavic · Design v1.6"
open(P + "canvas.json", "w", encoding="utf-8").write(json.dumps(C, ensure_ascii=False, indent=2))
print("ok", len(M), len(R), len(G))
