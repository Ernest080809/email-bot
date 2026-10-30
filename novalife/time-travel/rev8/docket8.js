(function(){
"use strict";
var TAGNAME = {B:"FABRIK", G:"DESIGN", D:"ENTSCHEIDUNG", A:"ADMIN", R:"RECHT", W:"SHOP", V:"VERKAUF", C:"CONTENT", S:"STUNT"};
var WDN = ["So","Mo","Di","Mi","Do","Fr","Sa"], MON = ["Jan","Feb","Mär","Apr","Mai","Jun","Jul","Aug","Sep","Okt","Nov","Dez"];
function esc(s){ return String(s == null ? "" : s).replace(/[&<>"']/g, function(c){ return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]; }); }
function parseISO(s){ var p = s.split("-"); return new Date(+p[0], +p[1]-1, +p[2]); }
function iso(d){ return d.getFullYear() + "-" + ("0"+(d.getMonth()+1)).slice(-2) + "-" + ("0"+d.getDate()).slice(-2); }
function addDays(d, n){ var x = new Date(d); x.setDate(x.getDate()+n); return x; }
function fmtShort(d){ return WDN[d.getDay()] + " " + ("0"+d.getDate()).slice(-2) + "." + ("0"+(d.getMonth()+1)).slice(-2) + "."; }
function minTxt(m){ return m >= 60 ? (Math.floor(m/60) + " h" + (m%60 ? " " + (m%60) + " Min." : "")) : m + " Min."; }

var done = Object.create(null), kv = Object.create(null), db = null;
var writing = false, pending = false, kwriting = false, kpending = false;
var noteEl = document.getElementById("saveNote");
function note(t){ if (noteEl) noteEl.textContent = t; }
var TODAY = iso(new Date());

/* ---------- Briefings und Mails ---------- */
function lst(a){ return '<ol>' + a.map(function(x){ return '<li>' + esc(x) + '</li>'; }).join("") + '</ol>'; }
function drow(lbl, val){
  if (val == null || val === "" || val === "—" || (Array.isArray(val) && !val.length)) return "";
  return '<dt>' + lbl + '</dt><dd>' + (Array.isArray(val) ? lst(val) : esc(val)) + '</dd>';
}
function copyBox(label, txt, cid){
  return '<div class="prompt"><div class="ph"><span class="eyebrow">' + label + '</span><button type="button" data-copy="' + cid + '">Kopieren</button></div><pre class="code" id="' + cid + '">' + esc(txt) + '</pre></div>';
}
function briefKind(v){
  if (v.trick) return "Stunt";
  if (/COUNTDOWN/.test(v.saeule || "")) return "Countdown";
  return "Video";
}
function briefBlock(v, pid){
  if (!v) return "";
  var h = '<div class="vb"><div class="vbh"><span class="eyebrow">' + briefKind(v) + ' ' + esc(v.id) + (v.saeule ? ' · ' + esc(v.saeule) : '') + '</span>';
  var meta = [v.slot, v.dauer, v.plattform].filter(function(x){ return !!x; });
  if (meta.length) h += '<span class="vt">' + esc(meta.join(" · ")) + '</span>';
  h += '</div>';
  if (v.titel) h += '<div class="brt">' + esc(v.titel) + '</div>';
  if (v.ziel) h += '<p class="bz"><b>Ziel:</b> ' + esc(v.ziel) + '</p>';
  if (v.hook_en) h += '<div class="hook">„' + esc(v.hook_en) + '“</div>';
  if (v.hook_de) h += '<div class="hookde">' + esc(v.hook_de) + '</div>';
  if (v.hook_alt && v.hook_alt.length) h += '<div class="halt"><b>Andere Hooks:</b> ' + v.hook_alt.map(function(x){ return '„' + esc(x) + '“'; }).join(" · ") + '</div>';
  if (v.beats && v.beats.length){
    h += '<div class="beats"><table><thead><tr><th>Zeit</th><th>Bild</th><th>Text im Bild</th><th>Ton und Stimme</th></tr></thead><tbody>';
    v.beats.forEach(function(b){ h += '<tr><td class="mono">' + esc(b[0]) + '</td><td>' + esc(b[1]) + '</td><td>' + esc(b[2]) + '</td><td>' + esc(b[3]) + '</td></tr>'; });
    h += '</tbody></table></div>';
  }
  h += '<dl>' + drow("Trick", v.trick) + drow("Idee", v.idee) + drow("Dreh", v.dreh) + drow("Vorbereitung", v.prep) + drow("Ablauf", v.ablauf) +
    drow("Shots", v.shots) + drow("Sicherheit", v.safety) + drow("Ort", v.ort) + drow("Requisiten", v.req) + drow("Kleidung", v.kleid) +
    drow("Licht", v.licht) + drow("Kamera", v.kamera) + drow("Ton", v.ton) + drow("Text im Bild", v.text) + drow("Schnitt", v.schnitt) +
    drow("Cover", v.cover) + drow("Deutsche Zeile", v.de) + drow("Story", v.story) + drow("CTA", v.cta) + '</dl>';
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
  var h = '<div class="vb mb"><div class="vbh"><span class="eyebrow">E-Mail ' + esc(eid) + '</span><span class="vt">' + esc(m.wann) + '</span></div>';
  h += '<dl>' + drow("An", m.an) + drow("Vorschau", m.vorschau) + drow("Andere Betreffs", (m.alt || []).join(" · ")) + '</dl>';
  h += copyBox("Betreff", m.betreff, "bt_" + pid + "_" + eid) + copyBox("Text", m.text, "tx_" + pid + "_" + eid);
  if (m.check) h += '<div class="rc"><b>Vor dem Senden</b>' + esc(m.check) + '</div>';
  return h + '</div>';
}
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

/* ---------- Aufgaben ---------- */
var ALL = [], IDX = Object.create(null);
WEEKS.forEach(function(w){
  w._start = parseISO(w.start);
  w.days.forEach(function(day, di){
    var d = iso(addDays(w._start, di));
    day.forEach(function(t){ t._d = d; t._w = w.n; if (t.c !== "N"){ ALL.push(t); IDX[t.id] = t; } });
  });
});
function whereBlock(o){
  if (!o || !o.length) return "";
  return '<div class="where">' + o.map(function(x){ return '<a href="' + esc(x.u) + '" target="_blank" rel="noopener">' + esc(x.n) + (x.h ? ' <span>· ' + esc(x.h) + '</span>' : '') + '</a>'; }).join("") + '</div>';
}
function taskRow(t, pfx, open){
  if (t.c === "N") return '<li class="tk note">' + esc(t.t) + '</li>';
  var id = (pfx || "") + t.id, vv = t.vr ? VIDS[t.vr] : null, es = t.e ? (Array.isArray(t.e) ? t.e : [t.e]) : [];
  var q = [t.t, (t.s || []).join(" "), t.f || "", vv ? (vv.id + " " + vv.titel + " " + (vv.hook_en || "")) : "", es.join(" ")].join(" ").toLowerCase();
  var h = '<li class="tk' + (t.plus ? " isplus" : "") + (done[t.id] ? " done" : "") + '" data-q="' + esc(q) + '" data-id="' + esc(t.id) + '"><div class="tkrow">' +
    '<input type="checkbox" id="' + esc(id) + '" data-ms="' + esc(t.id) + '"' + (done[t.id] ? " checked" : "") + '>' +
    '<div class="body"><label class="ttl" for="' + esc(id) + '"><span class="tg ' + t.c + '">' + (TAGNAME[t.c] || t.c) + '</span><span class="txt">' + esc(t.t) + '</span></label>';
  var chips = "";
  if (t.m) chips += '<span class="chip">' + minTxt(t.m) + '</span>';
  if (t.plus) chips += '<span class="chip plus">optional</span>';
  if (vv) chips += '<span class="chip ' + (vv.trick ? "stu" : "vid") + '">' + briefKind(vv) + ' ' + esc(vv.id) + '</span>';
  es.forEach(function(e){ chips += '<span class="chip ml">Mail ' + esc(e) + '</span>'; });
  var has = (t.s && t.s.length) || t.f || vv || es.length || (t.o && t.o.length);
  if (has){
    h += '<details class="how"' + (open ? " open" : "") + '><summary>' + chips + '<span class="sg">So geht’s</span></summary>';
    if (t.s && t.s.length) h += '<ol class="hs">' + t.s.map(function(s){ return '<li>' + esc(s) + '</li>'; }).join("") + '</ol>';
    if (vv) h += '<div class="lazy" data-vr="' + esc(t.vr) + '" data-pid="' + esc(id) + '"></div>';
    es.forEach(function(e){ h += '<div class="lazy" data-mail="' + esc(e) + '" data-pid="' + esc(id) + '"></div>'; });
    h += whereBlock(t.o);
    if (t.f) h += '<div class="fw"><b>Fertig, wenn</b>' + esc(t.f) + '</div>';
    h += '</details>';
  } else if (chips) h += '<div class="how">' + chips + '</div>';
  return h + '</div></div></li>';
}

/* Wochen */
function curWeek(){
  var now = parseISO(TODAY), n = Math.floor((now - WEEKS[0]._start) / 604800000) + 1;
  return Math.max(1, Math.min(WEEKS.length, n));
}
function renderWeeks(){
  var host = document.getElementById("weekList"), cw = curWeek(), last = "", h = "";
  WEEKS.forEach(function(w){
    if (w.phase !== last){ h += '<div class="phase">' + esc(PH[w.phase][0]) + ' <span>' + esc(PH[w.phase][1]) + '</span></div>'; last = w.phase; }
    var tasks = [], mins = 0, n = 0, dn = 0;
    w.days.forEach(function(d){ d.forEach(function(t){ if (t.c !== "N"){ n++; if (done[t.id]) dn++; if (!t.plus) mins += t.m || 0; } }); });
    var we = addDays(w._start, 6);
    h += '<details class="wk' + (w.n === cw ? " cur" : (w.n < cw ? " past" : "")) + '" data-w="' + w.n + '"' + (w.n === cw ? " open" : "") + '><summary>' +
      '<span class="wkn">W' + w.n + '</span><span class="wkd">' + w._start.getDate() + '. ' + MON[w._start.getMonth()] + ' – ' + we.getDate() + '. ' + MON[we.getMonth()] + '</span>' +
      '<span class="wkg">' + esc(w.goal) + '</span><span class="wkm" data-wc="' + w.n + '">' + dn + '/' + n + ' · ' + minTxt(mins) + '</span></summary><div class="wkbody">';
    w.days.forEach(function(day, di){
      if (!day.length) return;
      var d = addDays(w._start, di), di_ = iso(d);
      h += '<div class="day' + (di_ === TODAY ? " is-today" : "") + '"><div class="dh">' + fmtShort(d) + (di_ === TODAY ? " · heute" : "") + '</div><ul class="tasks">' +
        day.map(function(t){ return taskRow(t, "w_"); }).join("") + '</ul></div>';
    });
    h += '</div></details>';
  });
  host.innerHTML = h;
}
function renderToday(){
  var host = document.getElementById("todayList"), cw = curWeek(), w = WEEKS[cw - 1], h = "";
  var upcoming = ALL.filter(function(t){ return t._d >= TODAY; }).sort(function(a, b){ return a._d < b._d ? -1 : a._d > b._d ? 1 : 0; });
  var days = [], seen = {};
  upcoming.forEach(function(t){ if (!seen[t._d] && days.length < 3){ seen[t._d] = 1; days.push(t._d); } });
  if (TODAY < WEEKS[0].start) days = [WEEKS[0].start];
  days.forEach(function(d){
    var ts = ALL.filter(function(t){ return t._d === d; });
    var notes = [];
    WEEKS.forEach(function(w){ w.days.forEach(function(day){ day.forEach(function(t){ if (t.c === "N" && t._d === d) notes.push(t); }); }); });
    h += '<div class="dayh">' + fmtShort(parseISO(d)) + (d === TODAY ? " · heute" : "") + '</div><ul class="tasks">' + notes.concat(ts).map(function(t){ return taskRow(t, "t_"); }).join("") + '</ul>';
  });
  if (!h) h = '<p>Alles erledigt. Der Drop war am 24.06.</p>';
  host.innerHTML = h;
}

/* ---------- Stunts, Content, Mails ---------- */
function renderStunts(){
  var host = document.getElementById("stuntList"), h = "";
  CPLAN.forEach(function(c){
    if (c.id.charAt(0) !== "R") return;
    var v = VIDS[c.id] || {};
    var film = c.film && c.film[0] !== "BATCH" ? (c.id.slice(-1) === "M" ? "Schnitt " : "Dreh ") + fmtShort(parseISO(c.film[0])) : "";
    h += '<details class="st" data-q="' + esc((c.id + " " + v.titel + " " + (v.idee || "")).toLowerCase()) + '"><summary><span class="eyebrow">' + esc(v.trick || "Making-of") + '</span>' +
      '<span class="stn">' + esc(v.titel) + '</span><span class="stm">Post ' + esc(v.slot) + (film ? ' · ' + film : '') + (c.auto ? ' · Autopilot' : '') + '</span>' +
      (v.idee ? '<span class="sti">' + esc(v.idee) + '</span>' : '') + '</summary><div class="lazy" data-vr="' + esc(c.id) + '" data-pid="st_' + esc(c.id) + '"></div></details>';
  });
  host.innerHTML = h;
}
function renderContent(){
  var host = document.getElementById("cplanList"), h = "", lastM = "";
  CPLAN.forEach(function(c){
    var v = VIDS[c.id] || {}, d = parseISO(c.post[0]), m = MON[d.getMonth()] + " " + d.getFullYear();
    if (m !== lastM){ h += '<div class="cpw">' + m + '</div>'; lastM = m; }
    var film = c.film ? (c.film[0] === "BATCH" ? "Countdown-Dreh" : (c.schnitt ? "Schnitt " : "Dreh ") + fmtShort(parseISO(c.film[0]))) : "Dreh am Posttag";
    var k = c.kind + (c.auto ? " auto" : "") + (c.cd ? " cd" : "");
    h += '<details class="cpi' + (c.kind === "rewind" ? " isst" : "") + '" data-k="' + k + '" data-q="' + esc([c.id, v.titel, v.saeule, v.hook_en, v.hook_de].join(" ").toLowerCase()) + '"><summary>' +
      '<span class="cpd mono">' + fmtShort(d) + ' ' + esc(c.post[1]) + '</span><span class="cpid mono">' + esc(c.id) + '</span><span class="cpt">' + esc(v.titel || "") + '</span>' +
      '<span class="cps">' + esc((v.saeule || "") + ' · ' + (v.dauer || "") + ' · ' + film + (c.auto ? ' · Autopilot' : '')) + '</span></summary>' +
      '<div class="lazy" data-vr="' + esc(c.id) + '" data-pid="cp_' + esc(c.id) + '"></div></details>';
  });
  host.innerHTML = h;
  var box = document.getElementById("cpq"), sel = document.getElementById("cpk"), hits = document.getElementById("cphits");
  function apply(){
    var q = (box.value || "").trim().toLowerCase(), k = sel.value, n = 0, items = host.querySelectorAll(".cpi");
    for (var i = 0; i < items.length; i++){
      var it = items[i], cls = " " + it.getAttribute("data-k") + " ";
      var ok = (!q || it.getAttribute("data-q").indexOf(q) >= 0) && (!k || cls.indexOf(" " + k + " ") >= 0);
      it.classList.toggle("miss", !ok); if (ok) n++;
    }
    hits.textContent = (q || k) ? n + " Treffer" : "";
  }
  box.addEventListener("input", apply); sel.addEventListener("change", apply);
}
function renderMails(){
  var host = document.getElementById("mailList"), h = "";
  Object.keys(MAILS).sort().forEach(function(k){
    var m = MAILS[k];
    h += '<details class="ml"><summary><span class="mid">' + esc(k) + '</span><span class="msub">' + esc(m.betreff) + '</span><span class="mwann">' + esc(m.wann) + '</span></summary>' +
      '<div class="lazy" data-mail="' + esc(k) + '" data-pid="ml_' + esc(k) + '"></div></details>';
  });
  host.innerHTML = h;
}

/* ---------- Zahlen ---------- */
function stat(val, goal, alarm){
  if (val === "" || val == null || goal == null) return "";
  var v = +val;
  if (isNaN(v)) return "";
  return v >= goal ? "st-g" : (v >= alarm ? "st-y" : "st-r");
}
function renderCockpit(){
  var body = document.getElementById("kpiBody"), h = "";
  KPI.forEach(function(k){
    var r = kv[k.d] || {};
    function cell(f){
      if (k[f] == null) return '<td class="tgt">—</td>';
      var v = r[f] == null ? "" : r[f];
      return '<td class="tgt"><input class="kin ' + stat(v, k[f], k[f + "_a"]) + '" inputmode="numeric" data-kd="' + k.d + '" data-kf="' + f + '" value="' + esc(v) + '" aria-label="' + f + ' ' + k.d + '"><br><small>Ziel ' + k[f] + ' · Alarm ' + k[f + "_a"] + '</small></td>';
    }
    h += '<tr><td class="mono">' + fmtShort(parseISO(k.d)) + '<br><small>' + k.d.slice(0, 4) + '</small></td>' + cell("fo") + cell("wl") + cell("pre") + '<td class="gate">' + esc(k.gate || "") + '</td></tr>';
  });
  body.innerHTML = h;
}
document.addEventListener("change", function(e){
  var t = e.target;
  if (!t || !t.getAttribute || !t.getAttribute("data-kd")) return;
  var d = t.getAttribute("data-kd"), f = t.getAttribute("data-kf"), val = t.value.trim();
  if (!kv[d]) kv[d] = {};
  if (val === "") delete kv[d][f]; else kv[d][f] = val;
  renderCockpit(); ksave();
});
function ksave(){
  if (!db){ note("Nur in diesem Tab · Speicher nicht verfügbar"); return; }
  if (kwriting){ kpending = true; return; }
  kwriting = true;
  var snap = {};
  Object.keys(kv).forEach(function(d){ var o = {}, n = 0; Object.keys(kv[d]).forEach(function(f){ o[f] = kv[d][f]; n++; }); if (n) snap[d] = o; });
  db.doc("progress/kpi").set({ vals: snap, updatedAt: new Date().toISOString() })
    .then(function(){ note("Zahlen gespeichert · " + new Date().toLocaleTimeString("de-DE")); })
    .catch(function(err){ note("Zahlen nicht gespeichert (" + (err && err.code ? err.code : "Fehler") + ")"); })
    .then(function(){ kwriting = false; if (kpending){ kpending = false; ksave(); } });
}

/* ---------- Erledigt ---------- */
function renderDone(){
  var host = document.getElementById("oldDone"), keys = Object.keys(OLDDONE), h = "";
  keys.sort(function(a, b){ return OLDDONE[a][1] < OLDDONE[b][1] ? -1 : 1; });
  h = keys.map(function(k){
    var o = OLDDONE[k];
    return '<li class="tk' + (done[k] ? " done" : "") + '"><div class="tkrow"><input type="checkbox" id="od_' + esc(k) + '" data-ms="' + esc(k) + '"' + (done[k] ? " checked" : "") + '>' +
      '<div class="body"><label class="ttl" for="od_' + esc(k) + '"><span class="tg A">' + fmtShort(parseISO(o[1])) + '</span><span class="txt">' + esc(o[2]) + '</span></label></div></div></li>';
  }).join("");
  host.innerHTML = h;
}

/* ---------- Fortschritt ---------- */
function progress(){
  var n = 0, dn = 0;
  ALL.forEach(function(t){ if (!t.plus){ n++; if (done[t.id]) dn++; } });
  var p = n ? Math.round(dn * 100 / n) : 0;
  document.getElementById("megaBar").style.width = p + "%";
  document.getElementById("megaPct").textContent = p + " %";
  document.getElementById("megaCount").textContent = dn + " von " + n + " Aufgaben";
  WEEKS.forEach(function(w){
    var el = document.querySelector('[data-wc="' + w.n + '"]'); if (!el) return;
    var c = 0, d = 0, m = 0;
    w.days.forEach(function(day){ day.forEach(function(t){ if (t.c !== "N"){ c++; if (done[t.id]) d++; if (!t.plus) m += t.m || 0; } }); });
    el.textContent = d + "/" + c + " · " + minTxt(m);
  });
}
function syncBoxes(){
  var boxes = document.querySelectorAll("input[data-ms]");
  for (var i = 0; i < boxes.length; i++){
    var b = boxes[i], k = b.getAttribute("data-ms"), on = !!done[k];
    if (b.checked !== on) b.checked = on;
    var li = b.closest("li"); if (li) li.classList.toggle("done", on);
  }
  progress();
}
document.addEventListener("change", function(e){
  var t = e.target;
  if (!t || !t.getAttribute || !t.getAttribute("data-ms")) return;
  var k = t.getAttribute("data-ms");
  if (t.checked) done[k] = true; else delete done[k];
  syncBoxes(); save();
});
function save(){
  if (!db){ note("Nur in diesem Tab · Speicher nicht verfügbar"); return; }
  if (writing){ pending = true; return; }
  writing = true;
  var snap = {};
  Object.keys(done).forEach(function(k){ snap[k] = true; });
  db.doc("progress/tasks").set({ done: snap, updatedAt: new Date().toISOString() })
    .then(function(){ note("Gespeichert · " + new Date().toLocaleTimeString("de-DE")); })
    .catch(function(err){ note("Nicht gespeichert (" + (err && err.code ? err.code : "Fehler") + ")"); })
    .then(function(){ writing = false; if (pending){ pending = false; save(); } });
}

/* ---------- Suche in den Wochen ---------- */
(function(){
  var box = document.getElementById("wq"), only = document.getElementById("wopen"), hits = document.getElementById("whits");
  function apply(){
    var q = (box.value || "").trim().toLowerCase(), oo = only.checked, n = 0;
    var weeks = document.querySelectorAll("#weekList details.wk");
    for (var i = 0; i < weeks.length; i++){
      var wk = weeks[i], items = wk.querySelectorAll("li.tk"), any = false;
      for (var j = 0; j < items.length; j++){
        var li = items[j], isNote = li.classList.contains("note");
        var ok = (!q || (!isNote && (li.getAttribute("data-q") || "").indexOf(q) >= 0)) && (!oo || isNote || !li.classList.contains("done"));
        if (q && isNote) ok = false;
        li.classList.toggle("miss", !ok);
        if (ok && !isNote){ any = true; n++; }
      }
      var ds = wk.querySelectorAll(".day");
      for (var k = 0; k < ds.length; k++){ ds[k].classList.toggle("miss", !ds[k].querySelector("li.tk:not(.miss)")); }
      wk.classList.toggle("miss", (q || oo) && !any);
      if (q && any) wk.open = true;
    }
    hits.textContent = (q || oo) ? n + " Aufgaben" : "";
  }
  box.addEventListener("input", apply); only.addEventListener("change", apply);
})();

/* ---------- Countdown ---------- */
var dEl = document.getElementById("cdDays"), wEl = document.getElementById("weekOf");
function tick(){
  var ms = DROPTS - Date.now();
  dEl.textContent = ms > 0 ? Math.ceil(ms / 86400000) : "0";
  wEl.textContent = "Woche " + curWeek() + " von " + WEEKS.length;
}
tick(); setInterval(tick, 60000);

/* ---------- Kopieren ---------- */
document.addEventListener("click", function(e){
  var b = e.target && e.target.closest ? e.target.closest("[data-copy]") : null;
  if (!b) return;
  e.preventDefault();
  var pre = document.getElementById(b.getAttribute("data-copy")); if (!pre) return;
  var txt = pre.innerText;
  function ok(){ b.textContent = "Kopiert"; setTimeout(function(){ b.textContent = "Kopieren"; }, 1600); }
  function fallback(){
    try { var r = document.createRange(); r.selectNodeContents(pre); var s = window.getSelection(); s.removeAllRanges(); s.addRange(r);
      if (document.execCommand && document.execCommand("copy")) ok(); else b.textContent = "Markiert"; } catch(err){ b.textContent = "Markiert"; }
  }
  try { if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(txt).then(ok, fallback); else fallback(); } catch(err){ fallback(); }
});

/* ---------- Start ---------- */
function renderAll(){ renderToday(); renderWeeks(); renderDone(); syncBoxes(); }
renderAll(); renderStunts(); renderContent(); renderMails(); renderCockpit();
var cur = document.querySelector("#weekList details.wk.cur"); if (cur) fillLazy(cur);

if (window.claude && window.claude.use){
  window.claude.use("db").then(function(d){
    if (!d){ note("Nur in diesem Tab · Speicher nicht verfügbar"); return; }
    db = d; note("Fortschritt wird gespeichert");
    db.doc("progress/tasks").onSnapshot(function(snap){
      if (!snap.exists) return;
      var rec = (snap.data() || {}).done || {};
      done = Object.create(null);
      Object.keys(rec).forEach(function(k){ if (rec[k]) done[k] = true; });
      syncBoxes();
      if (!snap.metadata.hasPendingWrites) note("Gespeichert");
    }, function(err){ note("Speicher unterbrochen (" + (err && err.code ? err.code : "Fehler") + ")"); });
    db.doc("progress/kpi").onSnapshot(function(snap){
      if (!snap.exists) return;
      var act = document.activeElement;
      if (act && act.getAttribute && act.getAttribute("data-kd")) return;
      var rec = (snap.data() || {}).vals || {};
      kv = Object.create(null);
      Object.keys(rec).forEach(function(d){ kv[d] = {}; Object.keys(rec[d] || {}).forEach(function(f){ kv[d][f] = rec[d][f]; }); });
      renderCockpit();
    }, function(){});
  }).catch(function(){ note("Nur in diesem Tab · Speicher nicht verfügbar"); });
} else note("Nur in diesem Tab · Speicher nicht verfügbar");
})();
