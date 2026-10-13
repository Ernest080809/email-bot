"""Prüft, ob jede Skelett-Zeile in den ausgearbeiteten Wochen vorkommt.

Aufruf: python3 rev6/build/coverage6.py [n …]   (ohne Argument: alle vorhandenen Wochen)
Meldet je Tag die Skelett-Zeilen, deren Video-IDs, Uhrzeiten oder Schlüsselwörter in den Aufgaben des Tages fehlen.
"""
import json
import pathlib
import re
import sys

R6 = pathlib.Path(__file__).resolve().parents[1]
STOP = set("""aber alle allem als also auch auf aus bei beim bis dann dass dein deine deinen deiner dem den der des die dies diese
diesem dieser doch dort durch eine einem einen einer eines erst etwa für gegen hast hier ihre immer jede jeden jeder kein keine
mehr mit nach nicht noch nur oder ohne schon sich sind sonst über und unter vom von vor was weil wenn wie wird wo zum zur zwei drei
heute morgen woche wochen claude ernest docket minuten stunde stunden prüfen machen schreiben senden bitte neue neuen neues""".split())


def words(s):
    s = s.lower()
    return {w for w in re.findall(r"[a-zäöüß0-9][a-zäöüß0-9\-]{4,}", s) if w not in STOP}


def check(n, skel):
    f = R6 / "weeks" / f"w{n}.json"
    if not f.exists():
        return None
    data = json.loads(f.read_text(encoding="utf-8"))
    out = []
    for d, lines in skel["tage"].items():
        tasks = data.get("days", {}).get(d, [])
        text = json.dumps(tasks, ensure_ascii=False).lower()
        for line in lines:
            if line.strip().lower() in ("frei", ""):
                continue
            body = re.sub(r"^(grind\+\s*)?(ausnahme\s*)?\d+\s*[′']\s*·\s*|^(info|gate)\s*·\s*", "", line, flags=re.I)
            miss = []
            for vid in re.findall(r"\b(?:V\d{3}|CD-T\d{2})\b", line):
                if vid.lower() not in text:
                    miss.append(vid)
            for tm in re.findall(r"\b\d{1,2}:\d{2}\b", body[:120]):
                if tm not in text:
                    miss.append(tm)
            kw = list(words(body[:160]))
            hit = [w for w in kw if w in text]
            ratio = len(hit) / len(kw) if kw else 1
            if miss or ratio < 0.4:
                out.append((d, round(ratio, 2), miss, line[:150]))
    return out


def main():
    skel = {w["n"]: w for w in json.loads((R6 / "skeleton.json").read_text(encoding="utf-8"))}
    ns = [int(a) for a in sys.argv[1:]] or sorted(skel)
    total = 0
    for n in ns:
        res = check(n, skel[n])
        if res is None:
            continue
        print(f"== W{n}: {len(res)} verdächtige Skelett-Zeilen")
        for d, r, miss, line in res:
            print(f"  {d} · Deckung {r} · fehlt {miss} · {line}")
        total += len(res)
    print("Summe:", total)


if __name__ == "__main__":
    main()
