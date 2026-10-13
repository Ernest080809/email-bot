"""Baut „Time Travel Tracking“ als .xlsx (wird beim Hochladen zu einem Google Sheet)."""
import datetime as dt
import json
import pathlib
import re
import sys

from openpyxl import Workbook
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

R6 = pathlib.Path(sys.argv[1])
OUT = pathlib.Path(sys.argv[2])
kpi = json.loads((R6 / "kpi.json").read_text(encoding="utf-8"))
lib = json.loads((R6 / "research" / "content_library.json").read_text(encoding="utf-8"))
strat = (R6 / "strategie.md").read_text(encoding="utf-8")

INK, BRASS, INDIGO = "16181D", "8F6518", "1F3B66"
HEAD = PatternFill("solid", fgColor="16181D")
SUB = PatternFill("solid", fgColor="E2D9C2")
SOFT = PatternFill("solid", fgColor="EFEDE6")
GREEN = PatternFill("solid", fgColor="CFDCD3")
YELLOW = PatternFill("solid", fgColor="F1E2B8")
RED = PatternFill("solid", fgColor="E6D2CC")
thin = Side(style="thin", color="C4C1B5")
BOX = Border(bottom=thin)

wb = Workbook()
wb.remove(wb.active)


def sheet(name, title, note, headers, widths, rows=(), start_row=4, freeze=True):
    ws = wb.create_sheet(name)
    ws["A1"] = title
    ws["A1"].font = Font(bold=True, size=14, color=INK)
    ws["A2"] = note
    ws["A2"].font = Font(italic=True, size=10, color="4A4E58")
    ws["A2"].alignment = Alignment(wrap_text=False)
    for i, h in enumerate(headers, 1):
        c = ws.cell(row=start_row - 1, column=i, value=h)
        c.font = Font(bold=True, color="FFFFFF", size=10)
        c.fill = HEAD
        c.alignment = Alignment(vertical="center", wrap_text=True)
    ws.row_dimensions[start_row - 1].height = 32
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    for r, row in enumerate(rows, start_row):
        for c, v in enumerate(row, 1):
            if v is None:
                continue
            cell = ws.cell(row=r, column=c, value=v)
            cell.alignment = Alignment(vertical="top", wrap_text=isinstance(v, str) and len(v) > 40)
    if freeze:
        ws.freeze_panes = ws.cell(row=start_row, column=1)
    return ws


def dropdown(ws, col, values, first=4, last=400):
    dv = DataValidation(type="list", formula1='"' + ",".join(values) + '"', allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(f"{col}{first}:{col}{last}")


def status_colors(ws, rng, green, yellow, red):
    first = rng.split(":")[0]
    col = re.match(r"[A-Z]+", first).group(0)
    row = re.search(r"\d+", first).group(0)
    ref = f"${col}{row}"
    for words, fill in ((green, GREEN), (yellow, YELLOW), (red, RED)):
        for w in words:
            ws.conditional_formatting.add(rng, FormulaRule(formula=[f'{ref}="{w}"'], fill=fill))


def d(s):
    return dt.date.fromisoformat(s)


# ---------- Start ----------
ws = wb.create_sheet("Start")
ws.column_dimensions["A"].width = 26
ws.column_dimensions["B"].width = 100
ws["A1"] = "Time Travel Tracking · Novalife"
ws["A1"].font = Font(bold=True, size=16, color=INK)
ws["A2"] = "Gehört zum Time Travel Drop Docket (Rev. 6). Jede Aufgabe, die „Blatt …“ sagt, meint ein Blatt dieser Tabelle."
ws["A3"] = "Docket"
ws["B3"] = "https://claude.ai/artifact/RCciF8jMPSGhgdcQiHAQTm"
ws["A4"] = "Regel"
ws["B4"] = "Ethnische Herkunft nie neben Name oder E-Mail speichern (Art. 9 DSGVO). In „Gespräche“ und „Schnelltest“ nur Codes wie P1 oder G1."
ws["A5"] = "Sonntag"
ws["B5"] = "Wochenreview: zuerst „Wochen“ (4 Zahlen), dann „Kasse“ (K, V, F, R), dann „Gates“. Die gleichen 4 Zahlen trägst du auch ins Zahlen-Cockpit im Docket ein."
for r in range(2, 6):
    ws[f"A{r}"].font = Font(bold=True, color=BRASS)
    ws[f"B{r}"].alignment = Alignment(wrap_text=True, vertical="top")
ws["A7"] = "Blatt"
ws["B7"] = "Wofür"
for c in ("A7", "B7"):
    ws[c].font = Font(bold=True, color="FFFFFF")
    ws[c].fill = HEAD
INDEX = []

# ---------- Wochen (Cockpit) ----------
rows = []
for k in kpi:
    rows.append([d(k["d"]), f"W{k['w']}", k.get("wl"), k.get("wl_a"), None, k.get("fo"), None, None,
                 k.get("zu"), None, k.get("pre"), k.get("pre_a"), None, None, k.get("gate")])
ws = sheet("Wochen", "Wochen · die 4 Zahlen jeden Sonntag",
           "Soll und Alarm kommen aus der Strategie. Du trägst nur die gelben Spalten ein. Follower: Gesamtzahl TikTok + Instagram, „neu“ rechnet die Tabelle mit dem Startwert in C2.",
           ["Sonntag", "Woche", "Warteliste Soll", "Warteliste Alarm", "Warteliste Ist (bestätigt)", "Follower neu Soll", "Follower gesamt Ist", "Follower neu (Formel)",
            "Zusagen Soll", "Zusagen Ist", "Jeans bezahlt Soll", "Jeans bezahlt Alarm", "Jeans bezahlt Ist", "Status", "Gate dieser Woche"],
           [11, 8, 11, 11, 13, 11, 13, 13, 10, 10, 11, 11, 12, 13, 70], rows, start_row=5)
ws["A2"].value = ws["A2"].value
ws["A3"] = "Startwert Follower (Sa 10.10.)"
ws["A3"].font = Font(bold=True, color=BRASS)
ws.merge_cells("A3:B3")
ws["C3"].fill = YELLOW
ws["C3"].border = Border(top=thin, bottom=thin, left=thin, right=thin)
for r in range(5, 5 + len(rows)):
    ws[f"A{r}"].number_format = "DD.MM.YY"
    ws[f"H{r}"] = f'=IF(OR(G{r}="",$C$3=""),"",G{r}-$C$3)'
    ws[f"N{r}"] = (f'=IF(AND(E{r}="",H{r}="",J{r}="",M{r}=""),"offen",'
                   f'IF(OR(AND(E{r}<>"",D{r}<>"",E{r}<D{r}),AND(M{r}<>"",L{r}<>"",M{r}<L{r})),"unter Alarm",'
                   f'IF(OR(AND(E{r}<>"",E{r}<C{r}),AND(H{r}<>"",F{r}<>"",H{r}<F{r}),AND(J{r}<>"",I{r}<>"",J{r}<I{r}),AND(M{r}<>"",K{r}<>"",M{r}<K{r})),"unter Soll","im Plan")))')
    for col in "EGJM":
        ws[f"{col}{r}"].fill = YELLOW
    ws[f"O{r}"].alignment = Alignment(wrap_text=True, vertical="top")
status_colors(ws, f"N5:N{4 + len(rows)}", ["im Plan"], ["unter Soll"], ["unter Alarm"])
ws.freeze_panes = "C5"
INDEX.append(("Wochen", "Sonntags-Zahlen gegen Soll und Alarm, mit Ampel und dem Gate der Woche."))

# ---------- Kasse ----------
rows = [[d(k["d"]), f"W{k['w']}", None, None, None, None, None, None, None] for k in kpi]
ws = sheet("Kasse", "Kasse · Kassen-Ampel jeden Sonntag",
           "K = Projektkonto heute · V = Vorbestellungen bezahlt und ausgezahlt · F = fällig bis zum nächsten harten Gate · R = Rücklagen (Steuer falls fällig + 3 Paar Erstattungsreserve ~440 €). Ampel = K − F − R: grün ≥ 300 €, gelb 0–300 € (keine Ausgaben außerhalb des Plans), rot < 0 (Ausgaben-Stopp, Notfall-Leiter).",
           ["Sonntag", "Woche", "K Konto €", "V ausgezahlt €", "F fällig €", "R Rücklagen €", "Ampel K−F−R €", "Status", "Notiz (z. B. Auszahlungsdauer, Brücke, Support-Antwort)"],
           [11, 8, 12, 14, 12, 13, 14, 10, 60], rows)
for r in range(4, 4 + len(rows)):
    ws[f"A{r}"].number_format = "DD.MM.YY"
    ws[f"G{r}"] = f'=IF(C{r}="","",C{r}-N(E{r})-N(F{r}))'
    ws[f"H{r}"] = f'=IF(G{r}="","",IF(G{r}>=300,"grün",IF(G{r}>=0,"gelb","rot")))'
    for col in "CDEF":
        ws[f"{col}{r}"].fill = YELLOW
        ws[f"{col}{r}"].number_format = '#,##0 "€"'
    ws[f"G{r}"].number_format = '#,##0 "€"'
status_colors(ws, f"H4:H{3 + len(rows)}", ["grün"], ["gelb"], ["rot"])
INDEX.append(("Kasse", "Kassen-Ampel K − F − R, jeden Sonntag."))

# ---------- Budget ----------
plan = [("Entwicklung", "Schnitt + Gradierung W30–W38", 300, "Nov 26"), ("Entwicklung", "Digitizing Jeans, 5 Elemente", 320, "Nov 26"),
        ("Entwicklung", "Digitizing Zipper- und Polo-Bänder, Medaillon", 240, "Nov 26"), ("Entwicklung", "Stickproben, gewaschen", 150, "Nov 26"),
        ("Entwicklung", "Proto W32", 180, "Nov 26"), ("Entwicklung", "PP-Sample", 220, "Dez 26"),
        ("Entwicklung", "Stoffmuster, Lab Dips, Waschtests", 90, "Nov 26"), ("Entwicklung", "Labels, Hangtags, Knopf-Gravur (Setup)", 150, "Dez 26"),
        ("Entwicklung", "Label-Patch D, 3 Muster", 80, "Nov 26"), ("Entwicklung", "Blank-Muster Berlin (Zipper + Polo, 2 Sticker)", 180, "Nov 26"),
        ("Entwicklung", "Chenille-Muster (nur falls gewählt)", 120, "Jan 27"), ("Entwicklung", "Shopify bis April + Domain", 150, "Okt 26–Apr 27"),
        ("Entwicklung", "Lookbook-Shoot", 150, "Feb 27"), ("Produktion", "Label-Patch D, 110 Stück", 330, "Dez 26"),
        ("Produktion", "Anzahlung 50 % (100 × ~60 €)", 3000, "Feb 27"), ("Produktion", "Restzahlung 50 %", 3000, "Mär 27"),
        ("Launch", "Verpackung inkl. Hangtags", 240, "Feb 27"), ("Launch", "Versandmaterial", 80, "Mär 27"),
        ("Launch", "Werbung, 2 Kampagnen à 150 €", 300, "Mär–Apr 27"), ("Launch", "Puffer (Aseprite, Rechtstexte, Kleinkram)", 100, "—")]
ungeplant = [("Ungeplant", "Einfuhrumsatzsteuer (nur Türkei + Kleinunternehmer, Schätzung)", 1150, "bei Einfuhr ~27.05.–01.06."),
             ("Ungeplant", "Steuerberater", None, ""), ("Ungeplant", "Rechtstexte-Service über 80 €", None, ""),
             ("Ungeplant", "Verpackungslizenz (LUCID / System)", None, ""), ("Ungeplant", "Helferlohn (Packen)", None, ""),
             ("Ungeplant", "Abende (Getränke, Raum)", None, ""), ("Ungeplant", "EUSt + Kurier auf Proto und PP", None, ""),
             ("Ungeplant", "Fotograf und Models", None, ""), ("Ungeplant", "Shopify Email über Freikontingent", None, ""),
             ("Ungeplant", "Produkthaftpflicht", None, "")]
rows = [[a, b, c, e, None, None, None] for a, b, c, e in plan + ungeplant]
ws = sheet("Budget", "Budget · Plan gegen Ist",
           "Plan Rev. 6: Kapitalbedarf 9.380 €, Eigenbudget 4.500 €, Lücke 4.880 €. Jede ungeplante Ausgabe erhöht die Schwelle 2a: je 146 € eine Vorbestellung mehr.",
           ["Phase", "Posten", "Plan €", "Fällig", "Bezahlt am", "Ist €", "Differenz €"], [13, 52, 10, 18, 12, 10, 12], rows)
n = len(rows)
for r in range(4, 4 + n):
    ws[f"G{r}"] = f'=IF(F{r}="","",F{r}-N(C{r}))'
    for col in "CFG":
        ws[f"{col}{r}"].number_format = '#,##0 "€"'
    ws[f"E{r}"].number_format = "DD.MM.YY"
    if ws[f"A{r}"].value == "Ungeplant":
        ws[f"A{r}"].fill = SUB
end = 3 + n
p_end = 3 + len(plan)
lab = end + 2
ws[f"B{lab}"] = "Kapitalbedarf Plan"
ws[f"C{lab}"] = f"=SUM(C4:C{p_end})"
ws[f"B{lab+1}"] = "Ungeplant (Ist, sonst Schätzung)"
ws[f"C{lab+1}"] = "=" + "+".join(f"IF(F{r}<>\"\",F{r},N(C{r}))" for r in range(p_end + 1, end + 1))
ws[f"B{lab+2}"] = "Eigenbudget"
ws[f"C{lab+2}"] = 4500
ws[f"B{lab+3}"] = "Lücke (aus Vorbestellungen)"
ws[f"C{lab+3}"] = f"=C{lab}+C{lab+1}-C{lab+2}"
ws[f"B{lab+4}"] = "Zusätzliche Vorbestellungen wegen Ungeplantem (÷146 €)"
ws[f"C{lab+4}"] = f"=ROUNDUP(C{lab+1}/146,0)"
for r in range(lab, lab + 5):
    ws[f"B{r}"].font = Font(bold=True)
    ws[f"C{r}"].font = Font(bold=True)
    ws[f"C{r}"].number_format = '#,##0 "€"' if r != lab + 4 else "0"
    ws[f"B{r}"].fill = SOFT
    ws[f"C{r}"].fill = SOFT
INDEX.append(("Budget", "Plan-Posten aus Rev. 6 gegen Ist, dazu die Zeilen „ungeplant“ und ihre Wirkung auf Schwelle 2a."))

# ---------- Ausgaben ----------
ws = sheet("Ausgaben", "Ausgaben · jede Zahlung", "Eine Zeile pro Zahlung. Beleg: Dateiname oder Link (Ordner Novalife).",
           ["Datum", "Posten", "Budget-Zeile", "Betrag €", "Bezahlt mit", "Beleg", "Notiz"], [11, 40, 34, 11, 14, 30, 40])
ws["D2"].value = None
dropdown(ws, "E", ["Konto", "PayPal", "Karte", "bar"])
INDEX.append(("Ausgaben", "Jede einzelne Zahlung mit Beleg."))

# ---------- Gates ----------
def md_table(md, header):
    i = md.index(header)
    out = []
    for line in md[i:].splitlines()[2:]:
        if not line.startswith("|"):
            break
        cells = [re.sub(r"\*\*|`", "", c).strip() for c in line.strip().strip("|").split("|")]
        out.append(cells)
    return out


g72 = md_table(strat, "| Datum | Gate | grün → | sonst → |")
rows = [[g[0], g[1], g[2], g[3], None, None, None] for g in g72]
ws = sheet("Gates", "Gates · harte Prüfpunkte mit Datum",
           "Aus der Strategie (7.2). Am Tag des Gates: Ergebnis wählen, Entscheidung in einem Satz, nichts schieben ohne Eintrag.",
           ["Datum", "Gate", "grün →", "sonst →", "Ergebnis", "Entscheidung", "Notiz"], [16, 48, 34, 60, 11, 40, 40], rows)
dropdown(ws, "E", ["grün", "gelb", "rot"])
status_colors(ws, f"E4:E{3 + len(rows)}", ["grün"], ["gelb"], ["rot"])
INDEX.append(("Gates", "Alle harten Gates mit Regel; Ergebnis und Entscheidung je Termin."))

# ---------- Warteliste ----------
ws = sheet("Warteliste", "Warteliste · bestätigte Anmeldungen",
           "Nur „E-Mail-Marketing: abonniert“ zählt. Quellen: utm_source = Kanal (instagram, tiktok, qr, email) · ref = Person/Abend/Creator (netz, papier, stick, mess1–mess3, mess2b, c-[name], p-[medium], h-[kürzel], code).",
           ["Datum", "Bestätigt gesamt", "Neu seit letzter Zeile", "Anmeldequote Seite %", "Top-Quelle", "Notiz"], [11, 15, 18, 18, 22, 50])
for r in range(5, 120):
    ws[f"C{r}"] = f'=IF(OR(B{r}="",B{r-1}=""),"",B{r}-B{r-1})'
INDEX.append(("Warteliste", "Stand der bestätigten Liste mit Zuwachs und Quelle."))

# ---------- Content ----------
rows = []
for v in sorted(lib["videos"], key=lambda x: (x.get("date") or "9999", x["id"])):
    for plat in ("TikTok", "Instagram"):
        rows.append([v["id"], d(v["date"]) if v.get("date") else "Reserve", plat, v.get("slot", "")])
for v in lib["countdown"]:
    for plat in ("TikTok", "Instagram"):
        rows.append([v["id"], d(v["date"]) if v.get("date") else "", plat, "COUNTDOWN"])
ws = sheet("Content", "Content · eine Zeile pro Video und Plattform",
           "Sonntags 15 Minuten. Hook und Briefing stehen im Docket (Suche nach der ID). Views nach 48 h und nach 7 Tagen. Varianten-Regel: ≥ 2 × Median nach 48 h und Shares über Median → 5 Varianten in 14 Tagen.",
           ["ID", "Datum", "Plattform", "Slot", "Hook-Variante", "Views 48 h", "Views 7 T", "Ø Wiedergabe s", "% ganz", "Shares", "Saves",
            "Kommentare", "Profilaufrufe", "Neue Follower", "Link-Klicks", "Neue Anmeldungen", "Notiz"],
           [7, 10, 10, 11, 9, 10, 10, 10, 8, 8, 8, 10, 10, 10, 10, 11, 40], rows)
for r in range(4, 4 + len(rows)):
    if isinstance(ws[f"B{r}"].value, dt.date):
        ws[f"B{r}"].number_format = "DD.MM.YY"
dropdown(ws, "E", ["A", "B"], last=4 + len(rows))
ws.freeze_panes = "E4"
INDEX.append(("Content", f"{len(rows)} Zeilen: alle Videos der Bibliothek und der Countdown, je TikTok und Instagram."))

# ---------- Die ersten 35 ----------
ws = sheet("Die ersten 35", "Die ersten 35 · Zusagen und Vielleicht",
           "Jedes Gate zählt nur „Zusage“: Name, Größe und der Satz „ich bestelle am 14.01.“. „Vielleicht“ zählt nie.",
           ["Nr", "Zusage: Name", "Größe", "Satz gesagt?", "Datum", "Quelle", "", "Vielleicht: Name", "Größe", "Was noch fehlt", "Nachfassen am"],
           [5, 24, 8, 12, 11, 16, 3, 24, 8, 34, 13], [[i] for i in range(1, 51)])
ws["G3"].fill = PatternFill(None)
dropdown(ws, "C", ["W30", "W32", "W34", "W36", "W38", "kleiner", "größer"], last=53)
dropdown(ws, "I", ["W30", "W32", "W34", "W36", "W38", "kleiner", "größer"], last=53)
dropdown(ws, "D", ["ja", "nein"], last=53)
ws["M3"] = "Zusagen gezählt"
ws["M3"].font = Font(bold=True, color="FFFFFF")
ws["M3"].fill = HEAD
ws["M4"] = '=COUNTIFS(B4:B53,"<>",D4:D53,"ja")'
ws["M4"].font = Font(bold=True, size=14)
ws.column_dimensions["M"].width = 16
INDEX.append(("Die ersten 35", "Zusagen-Liste für die Schwellen; der Zähler oben rechts zählt nur echte Zusagen."))

# ---------- Netz ----------
ws = sheet("Netz", "Netz · warmes Netz und Novalife-Bestand",
           "Freunde, Familie, Bleach-Käufer. Keine Herkunft in diesem Blatt.",
           ["Name / Kürzel", "Woher kenne ich sie/ihn", "Kanal", "N1 gesendet", "Antwort", "Auf der Liste?", "N2 gesendet", "Zusage / Vielleicht", "Notiz"],
           [24, 24, 12, 12, 30, 12, 12, 16, 40])
dropdown(ws, "C", ["WhatsApp", "Instagram", "TikTok", "persönlich", "E-Mail"])
dropdown(ws, "F", ["ja", "nein"])
dropdown(ws, "H", ["Zusage", "Vielleicht", "nein"])
INDEX.append(("Netz", "Wen du persönlich anschreibst und was daraus wird."))

# ---------- Gespräche / Schnelltest ----------
sheet("Gespräche", "Gespräche · Zielgruppen-Interviews",
      "Nur Codes (G1, G2 …) mit Segment, nie Namen neben der Herkunft.",
      ["Datum", "Code", "Segment", "F1", "F2", "F3", "F4", "F5", "F6", "Preis-Antwort", "Auffällige Zitate"],
      [11, 7, 18, 22, 22, 22, 22, 22, 22, 20, 50])
sheet("Schnelltest", "Schnelltest · Papiertest 3 (08.10.)",
      "Codes P1–P10 mit Segment. Die Serp-Regel ist erledigt, der Serp ist seit 11.10. gestrichen. Die Antworten zählen weiter für Zielgruppe und Preis.",
      ["Code", "Segment", "Version gezeigt", "F1 erste drei Wörter", "F2 erinnert an / Version", "F3 erinnert an / hochwertiger", "F4 Detail zuerst", "F5 tragen 1–5", "149 € vorbestellen?", "Sowjet/Wappen genannt?"],
      [7, 18, 12, 26, 26, 26, 22, 10, 14, 14], [[f"P{i}"] for i in range(1, 11)])
ws = wb["Schnelltest"]
dropdown(ws, "I", ["ja", "vielleicht", "nein"], last=13)
dropdown(ws, "J", ["ja", "nein"], last=13)
ws["L3"] = "Sowjet/Wappen gezählt"
ws["L3"].font = Font(bold=True, color="FFFFFF")
ws["L3"].fill = HEAD
ws["L4"] = '=COUNTIF(J4:J13,"ja")'
ws["L4"].font = Font(bold=True, size=14)
ws.column_dimensions["L"].width = 20
INDEX.append(("Gespräche", "Interviews mit Codes, ohne Namen neben der Herkunft."))
INDEX.append(("Schnelltest", "Papiertest-3-Antworten P1–P10 (Serp seit 11.10. gestrichen)."))

# ---------- Fabriken ----------
ws = sheet("Fabriken", "Fabriken · Anfragen und Vergleich",
           "Nur offizielle Websites. Kontaktweg genau so, wie er auf der Website steht. Punkte nach dem Raster im Docket (Referenz „Fabriken und Lieferanten“ 1.6).",
           ["Name", "Land", "Website", "Kontaktweg", "Quelle", "geprüft am", "Eigene Fabrik", "Punkte", "MOQ ≤ 75", "gesendet", "Antwort", "Stickerei im Haus",
            "Panel-Stickerei", "MOQ", "Preis Basis €", "Preis / 1.000 Stiche €", "Sample-Preis €", "Zahlung", "Lieferzeit", "DAP/DDP", "Notizen"],
           [24, 8, 26, 26, 22, 11, 12, 8, 9, 11, 22, 12, 12, 8, 11, 12, 11, 10, 12, 9, 40])
dropdown(ws, "B", ["TR", "PT", "andere"])
dropdown(ws, "G", ["ja", "Vermittler", "unklar"])
dropdown(ws, "I", ["ja", "nein"])
dropdown(ws, "L", ["ja", "nein", "unklar"])
dropdown(ws, "M", ["ja", "nein", "unklar"])
dropdown(ws, "T", ["DAP", "DDP"])
INDEX.append(("Fabriken", "Die 8 Anfragen: Prüfung, Antworten, Preise, Konditionen."))

# ---------- Sticker / Patches ----------
ws = sheet("Sticker", "Berliner Sticker · Zipper und Polo (MOQ 1)", "Pflichtfragen: Fleece 330–350 g/m² mit Topping? Piqué? Externe DST/EMB? Preis bei 1 / 10 / 50?",
           ["Name", "Website", "Bezirk", "Kontaktweg (URL)", "Fotos auf Fleece", "Piqué", "ab 1 Stück", "Preis 1 / 10 / 50", "Lieferzeit", "Musterteil", "Notiz"],
           [22, 26, 14, 26, 12, 9, 10, 18, 12, 12, 40])
for col in "EFG":
    dropdown(ws, col, ["ja", "nein", "unklar"])
ws = sheet("Patches", "Patches · Label-Patch D und Chenille", "Budget: Muster 80 €, Serie ~330 € (Schätzung). Chenille-Muster 120 € nur, falls am 19.12. gewählt. Waschtest 3× 60 °C.",
           ["Anbieter", "Art", "Website", "Kontaktweg", "angefragt am", "MOQ", "Preis Muster €", "Preis Serie €", "Waschtest", "Notiz"],
           [22, 12, 26, 26, 12, 8, 12, 12, 12, 40])
dropdown(ws, "B", ["Stickpatch D", "Chenille"])
dropdown(ws, "I", ["bestanden", "durchgefallen", "offen"])
INDEX.append(("Sticker", "Berliner Sticker für Zipper und Polo."))
INDEX.append(("Patches", "Label-Patch D und Chenille: Anbieter, Muster, Waschtest."))

# ---------- Creator / Presse / Orte / Berlin / Abende / Shoot ----------
ws = sheet("Creator", "Creator · Longlist, Shortlist, Abmachung", "Kriterien: Berlin oder deutschsprachig, 5.000–80.000 Follower, eigene Jeans-Outfits, keine Politik. Geschenktes Paar = als Anzeige kennzeichnen.",
           ["Handle", "Plattform", "Ort", "Follower ca.", "Stil in 3 Wörtern", "Größe (falls sichtbar)", "Brand-Safety ok", "Liste", "DM C2 am", "Antwort", "Zusage", "Ref-Code", "Clip bis 15.01.", "Story 19.–23.06.", "Anmeldungen", "Notiz"],
           [18, 10, 12, 11, 22, 12, 11, 11, 11, 20, 9, 14, 11, 11, 11, 30])
dropdown(ws, "B", ["TikTok", "Instagram", "YouTube"])
dropdown(ws, "G", ["ja", "nein"])
dropdown(ws, "H", ["Longlist", "Shortlist", "Top 8", "Nano"])
for col in "KMN":
    dropdown(ws, col, ["ja", "nein"])
ws = sheet("Presse", "Presse · Medien und Wellen", "Kontakt nur aus Impressum oder offizieller Seite. Einmal nachfassen, nie öfter.",
           ["Medium", "Ressort", "Autor", "Kontakt (URL der Quelle)", "3 Artikel (Links)", "Aufhänger in einem Satz", "Welle", "gesendet", "nachgefasst", "Antwort", "Artikel", "Notiz"],
           [20, 14, 18, 28, 30, 34, 8, 11, 11, 20, 24, 30])
dropdown(ws, "G", ["1", "2", "3", "Event-Tipp"])
ws = sheet("Orte", "Orte · Läden und Räume für Abende", "Schriftliche Voranfrage, dann mit Proto fest anfragen.",
           ["Ort", "Adresse", "Kanal", "gesendet am", "Antwort", "Termin", "Konditionen", "Nachfassen am", "Notiz"], [22, 28, 16, 11, 26, 14, 26, 12, 30])
ws = sheet("Berlin", "Berlin · Feedback aus Läden und Märkten", "Wer, was gesagt, was du änderst.",
           ["Datum", "Wo", "Wer (Rolle)", "Was gesagt", "Was ich ändere", "Folge-Termin"], [11, 22, 18, 50, 40, 14])
ws = sheet("Abende", "Abende · Papiertest, Stick, Mess-Abende, Drop", "Ein Abend ist ein Erfolg, wenn Gäste auf die Liste kommen und Zusagen entstehen.",
           ["Abend", "Datum", "Ort", "Gast", "eingeladen", "zugesagt", "gekommen", "auf der Liste", "Größe gemessen", "Zusage", "bestellt", "Notiz"],
           [16, 11, 18, 20, 10, 9, 9, 10, 10, 9, 9, 30])
dropdown(ws, "A", ["Papiertest 24.10.", "Stick 27.11.", "Creator-Preview 12.01.", "Mess 1 16.01.", "Mess 2 30.01.", "Mess 2b 03.02.", "Mess 3 15.05.", "Drop-Abend 26.06."])
for col in "EFGHJK":
    dropdown(ws, col, ["ja", "nein"])
dropdown(ws, "I", ["W30", "W32", "W34", "W36", "W38", "kleiner", "größer"])
ws = sheet("Shoot", "Shoot · Sa 06.03.", "Fotograf mit schriftlichen Nutzungsrechten (Shop, Werbung, Presse).",
           ["Name", "Rolle", "Kontaktweg", "angefragt am", "Zusage", "Nutzungsrechte schriftlich", "Kosten €", "Notiz"], [20, 14, 26, 12, 9, 14, 10, 30])
for t, w_ in (("Creator", "Creator von Longlist bis Story im April."), ("Presse", "Medien, Wellen, Antworten."), ("Orte", "Läden und Räume für die Abende."),
              ("Berlin", "Feedback aus Läden und von Märkten."), ("Abende", "Gäste je Abend bis zur Bestellung."), ("Shoot", "Team und Rechte für den Shoot.")):
    INDEX.append((t, w_))

# ---------- Proto / QC ----------
mp = [("Bund, flach (½)", 40.6, 0.3), ("Hüfte, 20 cm unter Bund (½)", 50.0, 0.5), ("Vordere Leibhöhe", 28.0, 0.3), ("Hintere Leibhöhe", 40.0, 0.3),
      ("Oberschenkel, 2,5 cm unter Schritt (½)", 30.0, 0.5), ("Knie, 33 cm unter Schritt (½)", 24.0, 0.5), ("Beinöffnung (½)", 22.0, 0.5),
      ("Innenbeinlänge, fertig", 80.5, 0.5), ("Außenlänge", 106.0, 0.5), ("Bundbreite", 4.0, 0.2)]
rows = [[i, m, s, t, None, None, None, None] for i, (m, s, t) in enumerate(mp, 1)]
ws = sheet("Proto", "Proto · W32 messen (10 Messpunkte)", "Soll und Toleranz aus der Spec Rev. 13 (W32, cm). Flach messen, nicht ziehen, zweimal messen.",
           ["#", "Messpunkt", "Soll W32 cm", "Toleranz ±", "Ist cm", "Abweichung", "ok?", "Notiz / Foto-Nr."], [5, 38, 11, 10, 10, 11, 8, 40], rows)
for r in range(4, 14):
    ws[f"F{r}"] = f'=IF(E{r}="","",E{r}-C{r})'
    ws[f"G{r}"] = f'=IF(E{r}="","",IF(ABS(E{r}-C{r})<=D{r},"ok","raus"))'
    ws[f"E{r}"].fill = YELLOW
    ws[f"F{r}"].number_format = "+0.0;-0.0;0.0"
status_colors(ws, "G4:G13", ["ok"], [], ["raus"])
ws = sheet("QC", "QC · Wareneingang (15 % Stichprobe)", "Karton, Größe, Messwert gegen Soll; dazu Schnittkante, Weizenfäden, Patch-Sitz, Position aller fünf Elemente.",
           ["Karton", "Größe", "Prüfpunkt", "Soll", "Ist", "ok?", "Foto-Nr.", "Notiz"], [9, 8, 34, 10, 10, 8, 10, 40])
dropdown(ws, "F", ["ok", "raus"])
status_colors(ws, "F4:F400", ["ok"], [], ["raus"])
INDEX.append(("Proto", "10 Messpunkte W32 mit Soll, Toleranz und automatischem ok/raus."))
INDEX.append(("QC", "Wareneingang: Stichprobe je Karton."))

# ---------- Pre-Order / Nummern / Bestand / Retouren / Kaufgrund / Drop ----------
ws = sheet("Pre-Order", "Vorbestellungen · ab Do 14.01.", "Nummern nach Bestelldatum ohne Lücke: 001–035 zu 149 €, ab 036 Stufe 2 zu 169 €. Für die Schwellen zählt nur ausgezahltes Geld.",
           ["Bestellnr.", "Datum", "Kürzel", "Größe", "Nummer", "Stufe", "Betrag €", "ausgezahlt am", "Quelle (ref/utm)", "Status", "Notiz"],
           [12, 11, 14, 8, 8, 12, 10, 12, 18, 12, 30])
dropdown(ws, "D", ["W30", "W32", "W34", "W36", "W38"])
dropdown(ws, "F", ["149 €", "Stufe 2 169 €"])
dropdown(ws, "J", ["bezahlt", "ausgezahlt", "storniert", "erstattet"])
ws["M3"] = "Bezahlt gesamt"
ws["M4"] = '=COUNTIFS(A4:A400,"<>",J4:J400,"<>storniert",J4:J400,"<>erstattet")'
ws["N3"] = "Davon ausgezahlt"
ws["N4"] = '=COUNTIF(H4:H400,"<>")'
for c in ("M3", "N3"):
    ws[c].font = Font(bold=True, color="FFFFFF")
    ws[c].fill = HEAD
for c in ("M4", "N4"):
    ws[c].font = Font(bold=True, size=14)
ws.column_dimensions["M"].width = 15
ws.column_dimensions["N"].width = 16
rows = []
for i in range(1, 101):
    plan_ = "Vorbestellung 149 €" if i <= 35 else "Stufe 2" if i <= 60 else "Creator" if i <= 65 else "Reserve" if i <= 67 else "Drop"
    rows.append([f"{i:03d}", plan_, None, None, None, None])
ws = sheet("Nummern", "Nummern 001–100", "Plan bei vollem Verkauf. Füllt sich Stufe 2 nicht, rücken Creator, Reserve und Drop ohne Lücke nach.",
           ["Nummer", "Plan", "Status", "Bestellnr.", "Größe", "Notiz"], [9, 20, 14, 12, 8, 30], rows)
dropdown(ws, "C", ["frei", "vorbestellt", "Stufe 2", "Creator", "Reserve", "Drop verkauft", "retour, frei"], last=103)
ws = sheet("Bestand", "Bestand je Größe", "Drop-Bestand = geliefert − Vorbestellungen − Creator − Reserve. Plan-Verteilung aus der Spec (wird im Januar durch echte Zahlen ersetzt).",
           ["Größe", "Plan Stück", "geliefert", "Vorbestellungen", "Creator", "Reserve", "Drop-Bestand", "im Drop verkauft", "Rest"],
           [9, 10, 10, 14, 9, 9, 13, 14, 9], [["W30", 14], ["W32", 30], ["W34", 30], ["W36", 18], ["W38", 8]])
for r in range(4, 9):
    ws[f"G{r}"] = f'=IF(C{r}="","",C{r}-N(D{r})-N(E{r})-N(F{r}))'
    ws[f"I{r}"] = f'=IF(G{r}="","",G{r}-N(H{r}))'
ws["A9"] = "Summe"
for col in "BCDEFGHI":
    ws[f"{col}9"] = f"=SUM({col}4:{col}8)"
for col in "ABCDEFGHI":
    ws[f"{col}9"].font = Font(bold=True)
    ws[f"{col}9"].fill = SOFT
ws = sheet("Retouren", "Retouren", "Grund erfassen: Größe ist laut Recherche der häufigste Retourengrund.",
           ["Bestellnr.", "Nummer der Jeans", "Datum", "Grund", "Umtausch / Erstattung", "erledigt am", "Notiz"], [12, 14, 11, 20, 18, 12, 30])
dropdown(ws, "D", ["zu klein", "zu groß", "Länge", "Qualität", "gefällt nicht", "anderes"])
dropdown(ws, "E", ["Umtausch", "Erstattung"])
ws = sheet("Kaufgrund", "Kaufgrund · eine Frage nach dem Kauf", "Datum, Antwort im Wortlaut, Quellen-Tag.",
           ["Datum", "Antwort", "Quellen-Tag", "Notiz"], [11, 60, 18, 30])
ws = sheet("Drop", "Drop · 24.–27.06.", "Prüfpunkte: Do 21:00 ≥ 15 · Fr 19:00 ≥ 26 · So ≥ 29 netto.",
           ["Zeitpunkt", "Soll", "Ist", "ok?", "Maßnahme"], [18, 8, 8, 8, 60],
           [["Do 24.06. 21:00", 15], ["Fr 25.06. 19:00", 26], ["So 27.06. netto", 29]])
for r in range(4, 7):
    ws[f"D{r}"] = f'=IF(C{r}="","",IF(C{r}>=B{r},"ok","darunter"))'
    ws[f"C{r}"].fill = YELLOW
status_colors(ws, "D4:D6", ["ok"], [], ["darunter"])
for t, w_ in (("Pre-Order", "Jede Vorbestellung mit Nummer, Stufe und Auszahlung; Zähler oben rechts."),
              ("Nummern", "001–100 mit Plan und Status."), ("Bestand", "Bestand je Größe bis zum Drop-Rest."),
              ("Retouren", "Jede Retoure mit Grund."), ("Kaufgrund", "Warum Leute gekauft haben."), ("Drop", "Prüfpunkte am Drop-Wochenende.")):
    INDEX.append((t, w_))

# ---------- Website / Tools / Recht / Entscheidungen ----------
sheet("Website", "Website · Bauschritte der Scroll-Story", "Ein Schritt pro Zeile, Bauplan im Docket (Referenz „Website“).",
      ["Schritt", "Datum geplant", "erledigt am", "Test bestanden", "Problem", "Notiz"], [34, 13, 12, 13, 34, 30])
sheet("Tools", "Tools · Konten, Abos, Markenrecherche", "Keine Passwörter in dieses Blatt.",
      ["Tool", "Wofür", "Konto angelegt", "Kosten / Monat €", "Kündigen bis", "Notiz"], [20, 30, 13, 14, 12, 40])
sheet("Recht", "Recht und Steuer", "Steuerberater, Rechtstexte, LUCID, Gewerbe, EORI, GPSR: Stand und Belege.",
      ["Thema", "Stand", "erledigt am", "Beleg / Link", "Nächster Schritt", "Notiz"], [26, 22, 12, 30, 30, 30],
      [["Gewerbe (Herstellung + Online-Handel)"], ["Steuerberater: Kleinunternehmer, EUSt"], ["LUCID Verpackungsregister"], ["Impressum + Datenschutz"],
       ["AGB, Widerruf, Versand (Rechtstexte-Service)"], ["Shopify Payments + Auszahlung"], ["EORI (falls Türkei)"], ["Pflegeetikett + GPSR-Herstellerangabe"],
       ["Creator-Kennzeichnung"], ["Markenrecherche „Novalife“"]])
sheet("Entscheidungen", "Entscheidungen · was du wann festlegst", "Aus dem Urteil im Docket. Eintragen, was du entschieden hast.",
      ["Bis", "Frage", "Mein Rat", "Entschieden", "am", "Notiz"], [12, 50, 40, 30, 11, 30],
      md_table(strat, "| Bis | Frage | Mein Rat |"))
for t, w_ in (("Website", "Bauschritte der Scroll-Story mit Test."), ("Tools", "Konten und Abos."),
              ("Recht", "Recht und Steuer mit Belegen."), ("Entscheidungen", "Deine Entscheidungen mit Datum.")):
    INDEX.append((t, w_))

# Index auf dem Start-Blatt
ws = wb["Start"]
for i, (n_, w_) in enumerate(INDEX, 8):
    ws[f"A{i}"] = n_
    ws[f"B{i}"] = w_
    ws[f"A{i}"].font = Font(bold=True)
    ws[f"A{i}"].hyperlink = f"#'{n_}'!A1"
ws.freeze_panes = "A8"

# Tab-Farben
for name, color in (("Start", INK), ("Wochen", BRASS), ("Kasse", BRASS), ("Budget", BRASS), ("Gates", "9C3827"), ("Die ersten 35", "7A2E4A"),
                    ("Warteliste", "7A2E4A"), ("Content", INDIGO)):
    wb[name].sheet_properties.tabColor = color

wb.save(OUT)
print("Blätter:", len(wb.sheetnames), wb.sheetnames)
print("Bytes:", OUT.stat().st_size)
