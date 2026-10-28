/* ---- Rev. 7: Briefings, Mails, verzögertes Rendern ---- */
function lst(a){
  if (!a || !a.length) return "";
  return '<ol>' + a.map(function(x){ return '<li>' + esc(x) + '</li>'; }).join("") + '</ol>';
}
function drow(lbl, val){
  if (val == null || val === "" || val === "—" || (Array.isArray(val) && !val.length)) return "";
  return '<dt>' + lbl + '</dt><dd>' + (Array.isArray(val) ? lst(val) : esc(val)) + '</dd>';
}
function copyBox(label, txt, cid){
  return '<div class="prompt"><div class="ph"><span class="eyebrow">' + label + '</span>' +
    '<button type="button" data-copy="' + cid + '">Kopieren</button></div>' +
    '<pre class="code" id="' + cid + '">' + esc(txt) + '</pre></div>';
}
function briefKind(v){
  if (v.frames) return "Story";
  if (v.trick) return "REWIND";
  if (/COUNTDOWN/.test(v.saeule || "")) return "Countdown";
  if (/Vorlage/.test(v.saeule || "")) return "Vorlage";
  return "Video";
}
function briefBlock(v, pid){
  if (!v) return "";
  var h = '<div class="vb br"><div class="vbh"><span class="eyebrow">' + briefKind(v) + ' ' + esc(v.id) + (v.saeule ? ' · ' + esc(v.saeule) : '') + '</span>';
  var meta = [v.slot, v.dauer, v.plattform].filter(function(x){ return !!x; });
  if (meta.length) h += '<span class="vt">' + esc(meta.join(" · ")) + '</span>';
  h += '</div>';
  if (v.titel) h += '<div class="brt">' + esc(v.titel) + '</div>';
  if (v.ziel) h += '<p class="bz"><b>Ziel:</b> ' + esc(v.ziel) + '</p>';
  if (v.hook_en) h += '<div class="hook">„' + esc(v.hook_en) + '“</div>';
  if (v.hook_de) h += '<div class="hookde">' + esc(v.hook_de) + '</div>';
  if (v.hook_alt && v.hook_alt.length) h += '<div class="halt"><b>Andere Hooks zum Testen:</b> ' + v.hook_alt.map(function(x){ return '„' + esc(x) + '“'; }).join(" · ") + '</div>';
  if (v.beats && v.beats.length){
    h += '<div class="beats"><table><thead><tr><th>Zeit</th><th>Bild</th><th>Text im Bild</th><th>Ton und Stimme</th></tr></thead><tbody>';
    v.beats.forEach(function(b){ h += '<tr><td class="mono">' + esc(b[0]) + '</td><td>' + esc(b[1]) + '</td><td>' + esc(b[2]) + '</td><td>' + esc(b[3]) + '</td></tr>'; });
    h += '</tbody></table></div>';
  }
  if (v.frames && v.frames.length){
    h += '<div class="beats"><table><thead><tr><th>Bild</th><th>Was zu sehen ist</th><th>Text</th><th>Sticker</th></tr></thead><tbody>';
    v.frames.forEach(function(f, i){ h += '<tr><td class="mono">' + (i + 1) + '</td><td>' + esc(f[0]) + '</td><td>' + esc(f[1]) + '</td><td>' + esc(f[2]) + '</td></tr>'; });
    h += '</tbody></table></div>';
  }
  h += '<dl>' + drow("Trick", v.trick) + drow("Idee", v.idee) + drow("Dreh", v.dreh) + drow("Vorbereitung", v.prep) + drow("Ablauf", v.ablauf) +
    drow("Shots", v.shots) + drow("Sicherheit", v.safety) + drow("Ort", v.ort) + drow("Requisiten", v.req) + drow("Kleidung", v.kleid) +
    drow("Licht", v.licht) + drow("Kamera", v.kamera) + drow("Ton", v.ton) + drow("Text im Bild", v.text) + drow("Schnitt", v.schnitt) +
    drow("Cover", v.cover) + drow("Deutsche Zeile", v.de) + drow("Story", v.story) + drow("Danach", v.folge) + drow("CTA", v.cta) + '</dl>';
  if (v.caption) h += copyBox("Caption", v.caption, "cap_" + pid);
  if (v.kommentar && v.kommentar !== "—") h += copyBox("Erster Kommentar, anpinnen", v.kommentar, "kom_" + pid);
  var pm = drow("Posten", v.posten) + drow("Messen", v.messen) + drow("Varianten", v.varianten);
  if (pm) h += '<details class="pmv"><summary>Posten · Messen · Varianten</summary><dl>' + pm + '</dl></details>';
  if (v.check) h += '<div class="rc"><b>Regel-Check</b>' + esc(v.check) + '</div>';
  return h + '</div>';
}
function mailBlock(eid, pid){
  var m = MAILS[eid];
  if (!m) return "";
  var h = '<div class="vb mb"><div class="vbh"><span class="eyebrow">E-Mail ' + esc(m.id) + '</span><span class="vt">' + esc(m.wann) + '</span></div>';
  h += '<dl>' + drow("An", m.an) + drow("Vorschau", m.vorschau) + drow("Andere Betreffs", (m.alt || []).join(" · ")) + '</dl>';
  h += copyBox("Betreff", m.betreff, "bt_" + pid + "_" + eid) + copyBox("Text", m.text, "tx_" + pid + "_" + eid);
  if (m.check) h += '<div class="rc"><b>Vor dem Senden</b>' + esc(m.check) + '</div>';
  return h + '</div>';
}
/* Briefings und Mails erst rendern, wenn ihr Kasten aufgeht */
function fillLazy(root){
  if (!root || !root.querySelectorAll) return;
  var els = root.querySelectorAll(".lazy:not(.filled)");
  for (var i = 0; i < els.length; i++){
    var el = els[i], box = el.parentNode && el.parentNode.closest ? el.parentNode.closest("details") : null;
    if (box && !box.open) continue;
    var pid = el.getAttribute("data-pid") || "x";
    if (el.getAttribute("data-vr")) el.innerHTML = briefBlock(VIDS[el.getAttribute("data-vr")], pid);
    else if (el.getAttribute("data-mail")) el.innerHTML = mailBlock(el.getAttribute("data-mail"), pid);
    el.classList.add("filled");
  }
}
document.addEventListener("toggle", function(e){ var d = e.target; if (d && d.open) fillLazy(d); }, true);

function taskRow(wn, di, ti, t, pfx, open){
  var key = t.id || ("w" + wn + "d" + di + "t" + ti);
  var id = (pfx || "") + key;
  if (t.c === "N"){
    return '<li class="tk note" data-q="' + esc((t.t || "").toLowerCase()) + '"><span class="ntxt"><span class="ok"></span><span>' + esc(t.t) + '</span></span></li>';
  }
  var mins = t.m || 0, steps = t.s || [], fertig = t.f || "", prompt = t.p || "";
  var vv = t.vr ? VIDS[t.vr] : null;
  var es = t.e ? (Array.isArray(t.e) ? t.e : [t.e]) : [];
  var q = [t.t, steps.join(" "), fertig, (t.o || []).map(function(x){ return x.n + " " + (x.a || ""); }).join(" "),
    t.v ? (t.v.id + " " + (t.v.hook_en || "") + " " + (t.v.hook_de || "")) : "",
    vv ? (vv.id + " " + (vv.titel || "") + " " + (vv.hook_en || "") + " " + (vv.hook_de || "")) : "",
    es.map(function(e){ return e + " " + (MAILS[e] ? MAILS[e].betreff : ""); }).join(" ")].join(" ").toLowerCase();
  var h = '<li class="tk' + (t.plus ? " isplus" : "") + '" data-q="' + esc(q) + '"><div class="tkrow">' +
    '<input type="checkbox" id="' + id + '" data-ms="' + key + '">' +
    '<div class="body"><label class="ttl" for="' + id + '"><span class="tg ' + t.c + '">' + (TAGNAME[t.c] || t.c) + '</span>' +
    '<span class="txt">' + esc(t.t) + '</span></label>';
  var chips = "";
  if (mins) chips += '<span class="chip">' + minTxt(mins) + '</span>';
  if (t.plus) chips += '<span class="chip plus">Grind+ · optional</span>';
  if (t.v) chips += '<span class="chip vid">Video' + (t.v.id ? " " + esc(t.v.id) : "") + '</span>';
  if (vv) chips += '<span class="chip vid">' + briefKind(vv) + ' ' + esc(vv.id) + '</span>';
  es.forEach(function(e){ chips += '<span class="chip ml">Mail ' + esc(e) + '</span>'; });
  if (t.o && t.o.length) chips += '<span class="chip">' + t.o.length + (t.o.length === 1 ? " Link/Ort" : " Links/Orte") + '</span>';
  if (prompt) chips += '<span class="chip cl">mit Claude</span>';
  if (t.x === "s") chips += '<span class="chip sp">nur bei „Spiel bauen“</span>';
  if (steps.length || fertig || prompt || t.v || vv || es.length || (t.o && t.o.length)){
    h += '<details class="how"' + (open ? ' open' : '') + '><summary>' + chips + '<span class="sg">So geht’s</span></summary>';
    if (steps.length){
      h += '<ol class="hs">';
      steps.forEach(function(s){ h += '<li>' + esc(s) + '</li>'; });
      h += '</ol>';
    }
    h += videoBlock(t.v, id);
    if (vv) h += '<div class="lazy" data-vr="' + esc(t.vr) + '" data-pid="' + esc(id) + '"></div>';
    es.forEach(function(e){ h += '<div class="lazy" data-mail="' + esc(e) + '" data-pid="' + esc(id) + '"></div>'; });
    h += whereBlock(t.o);
    if (fertig) h += '<div class="fw"><b>Fertig, wenn</b>' + esc(fertig) + '</div>';
    if (prompt){
      var pid = "p_" + id;
      h += '<div class="prompt"><div class="ph"><span class="eyebrow">Prompt an Claude</span>' +
        '<button type="button" data-copy="' + pid + '">Kopieren</button></div>' +
        '<pre class="code" id="' + pid + '">' + esc(prompt) + '</pre></div>';
    }
    h += '</details>';
  } else if (chips){
    h += '<div class="chips">' + chips + '</div>';
  }
  return h + '</div></div></li>';
}
