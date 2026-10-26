# -*- coding: utf-8 -*-
# Zipper NVL-TT-02 · Maßtabelle (Mo 26.10.2026)
# Basis: Ernests RL-Zipper, Größe M, flach gemessen am 25.10. (Messbogen-Artefakt messungen/rl-zipper).
# Änderungen nach Ernests Antworten vom 26.10.: etwas lockerer, aber „man muss das Design noch sehen, kein Sack“,
# Schulter 2 cm pro Seite tiefer, Saumrippe zieht zusammen wie beim RL, Oberarm 22,5 cm.
# Alle Werte in cm, flach gemessen, Weiten von Kante zu Kante (nicht verdoppelt).

RL_M = {
    'brust': 57, 'weite_rippe': 50, 'saum': 50, 'oberarm': 21, 'buendchen': 11, 'laenge_vorn': 65, 'ruecken': 65,
    'schulter': 53.5, 'aermel': 60.5, 'armloch': 26, 'zip': 58, 'kapuze_hoehe': 31, 'kapuze_breite': 27,
    'kapuze_liegt': 30, 'kapuze_liegt_breite': 26, 'ausschnitt': 6.5, 'rippe_saum': 7, 'rippe_aermel': 7,
    'tasche_eingriff': 17, 'tasche_rippe': 5, 'tasche_zip': 15.5,
}

# (Nr., Schlüssel, Name, unser M, Schritt je Größe, Grund)
SPEC = [
    (1, 'brust', 'Brustweite', 60, 2, '+3: lockerer, der Teppich liegt aber noch glatt, kein Sack'),
    (2, 'weite_rippe', 'Weite über der Saumrippe', 53, 2, '+3 wie die Brust, gleiche Verjüngung wie beim RL'),
    (3, 'saum', 'Saumweite', 50, 2, 'wie RL: die Rippe zieht zusammen'),
    (4, 'oberarm', 'Oberarm', 22.5, 1, '+1,5, deine Wahl'),
    (5, 'buendchen', 'Ärmelbündchen', 11, 0.5, 'wie RL'),
    (6, 'laenge_vorn', 'Länge vorn', 65, 2, 'wie RL, Länge wie ein normaler Slim Fit'),
    (7, 'ruecken', 'Rückenlänge Mitte', 65, 2, 'wie RL'),
    (8, 'schulter', 'Schulterbreite', 57.5, 1.5, '+4: Naht 2 cm pro Seite tiefer, deine Wahl'),
    (9, 'aermel', 'Ärmellänge', 58.5, 1, '−2, weil die Schulternaht 2 cm tiefer sitzt, das Bündchen bleibt, wo es ist'),
    (10, 'armloch', 'Armloch gerade', 27, 1, '+1 wegen tieferer Schulter und weiterer Brust'),
    (11, 'zip', 'Reißverschluss', 58, 2, 'wie RL, wächst mit der Länge'),
    (12, 'kapuze_hoehe', 'Kapuzenhöhe', 31, 1, 'wie RL'),
    (13, 'kapuze_breite', 'Kapuzenbreite', 27, 0.5, 'wie RL'),
    (16, 'ausschnitt', 'Ausschnitt vorn', 6.5, 0, 'wie RL'),
    (17, 'rippe_saum', 'Saumrippe, Höhe', 7, 0, 'wie RL, der Stern passt mit Luft'),
    (18, 'rippe_aermel', 'Ärmelrippe, Höhe', 7, 0, 'wie RL'),
    (19, 'tasche_eingriff', 'Tasche, Eingriff', 17, 0, 'wie RL'),
    (20, 'tasche_rippe', 'Tasche über der Saumrippe', 5, 0, 'wie RL'),
    (21, 'tasche_zip', 'Tasche bis Reißverschluss', 15.5, 0.5, 'wie RL'),
]
SIZES = ['S', 'M', 'L', 'XL']


def graded(m, step):
    return {s: m + (i - 1) * step for i, s in enumerate(SIZES)}


def fmt(v):
    return (f'{v:.1f}'.rstrip('0').rstrip('.')).replace('.', ',')


def markdown():
    rows = ['| Nr. | Maß | RL M | S | **M** | L | XL | Warum |', '|---|---|---|---|---|---|---|---|']
    for n, k, name, m, step, why in SPEC:
        g = graded(m, step)
        rows.append(f'| {n} | {name} | {fmt(RL_M[k])} | {fmt(g["S"])} | **{fmt(g["M"])}** | {fmt(g["L"])} | {fmt(g["XL"])} | {why} |')
    return "\n".join(rows)


if __name__ == '__main__':
    print(markdown())
