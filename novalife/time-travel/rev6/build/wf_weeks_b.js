export const meta = {
  name: 'tt-docket-rev6-weeks-b',
  description: 'Schreibt die Wochen 8–32 des Time Travel Drop Docket mit festem Lesebudget und Selbstprüfung (Format + Skelett-Deckung)',
  phases: [{ title: 'Schreiben', detail: '11 Autoren, je 2–3 Wochen, chronologisch' }],
}

const T = '/home/user/email-bot/novalife/time-travel'
const R = T + '/rev6'
// chronologisch: die nahen Wochen zuerst, falls das Nutzungslimit vorher greift
const ALL = [[8, 9], [10, 11], [12, 13], [14, 15, 16], [17, 18], [19, 20, 21], [22, 23, 24], [25, 26], [27, 28], [29, 30], [31, 32]]
const GROUPS = (args && args.groups) ? args.groups : ALL

const WS = { type: 'object', properties: { wochen: { type: 'array', items: { type: 'object', properties: { n: { type: 'integer' }, aufgaben: { type: 'integer' }, videos: { type: 'integer' }, fehler: { type: 'integer' }, deckung_offen: { type: 'integer' } }, required: ['n', 'aufgaben', 'fehler'] } } }, required: ['wochen'] }

const prompt = g => `Arbeitsverzeichnis: ${T}. Du schreibst die Wochen ${g.join(', ')} des Tagesplans „Time Travel Drop Docket“ (Rev. 6) für Ernest (Novalife, Denim, Berlin). Vorbild für Detailgrad und Ton: ${R}/weeks/w5.json (lies daraus nur die ersten 150 Zeilen).

FESTES BUDGET, höchstens ~25 Werkzeugaufrufe:
1. Lies ${R}/briefs/rules.md vollständig und ${g.map(n => `${R}/briefs/w${n}.md`).join(' und ')} vollständig. Dort steht alles: Skelett je Tag (verbindlich), alte Rev.-5.3-Aufgaben (Schritte und Prompts übernehmen und verbessern), Video-Konzepte dieser Wochen.
2. Orte, Adressen, Websites: nur per grep -i in ${R}/briefs/links.md (mehrere Begriffe in einem grep mit -e).
3. strategie.md und die Recherche-Dateien NICHT komplett lesen. Höchstens 3 gezielte Abschnitte (grep -n, dann Read mit offset/limit, je max. 80 Zeilen), nur wenn ein Stichpunkt ausdrücklich darauf verweist und die Aufgabe ohne ihn nicht konkret wird.
4. Schreibe jede Woche mit einem Write-Aufruf nach ${R}/weeks/w{n}.json (Format in rules.md).
5. Prüfe jede Woche: python3 ${R}/build/check_week.py N (muss 0 Fehler melden) und python3 ${R}/build/coverage6.py N (jede gemeldete Skelett-Zeile ergänzen; Fehlalarme nur, wenn der Stichpunkt sichtbar anders formuliert umgesetzt ist). Korrigiere mit Edit, nicht durch Neuschreiben.

Inhalt: Jeder Stichpunkt des Skeletts wird eine ausgearbeitete Aufgabe mit konkreten Schritten (Klickpfad, Adresse, was sagen, was mitnehmen), Orten und Links in "o", vollständigem Video-Briefing in "v" an Dreh- und Posttagen (Korrekturen aus rules.md 9.3: Wortliste, CTA der Phase, Bildregeln, Sperrtermine), Prompt an Claude wo Claude hilft, prüfbarem „Fertig, wenn“. Sonntags: Wochenreview mit Gates, Cockpit-Zahlen (Warteliste bestätigt, Follower gesamt, Zusagen, bezahlte Jeans) und die Zeile an Claude. Keine erfundenen URLs, Adressen, Preise. Nichts über Claudes Netzwerk oder Sandbox. Gib je Woche Aufgaben, Videos, Fehler und offene Deckungs-Meldungen zurück.`

const res = await parallel(GROUPS.map(g => () => agent(prompt(g), { label: 'schreiben:W' + g.join('-'), phase: 'Schreiben', schema: WS })))
return { gruppen: GROUPS.map((g, i) => ({ g, ok: !!res[i], r: res[i] })) }
