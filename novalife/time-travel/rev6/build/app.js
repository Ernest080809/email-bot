(function(){
"use strict";

var PH = {"P0": ["Design fertig", "14. Sep – 11. Okt 2026"], "P1": ["Fabrik finden", "12. Okt – 8. Nov 2026"], "P2": ["Sample", "9. Nov – 20. Dez 2026"], "P3": ["Vorbestellung", "21. Dez 2026 – 7. Feb 2027"], "P4": ["Produktion & Kampagne", "8. Feb – 28. Mär 2027"], "P5": ["Countdown & Drop", "29. Mär – 25. Apr 2027"]};
var DROP = new Date("2027-04-22T19:00:00+02:00").getTime();
var NW = WEEKS.length;

var DNAMES = ["Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samstag","Sonntag"];
var DSHORT = ["Mo","Di","Mi","Do","Fr","Sa","So"];
var MON = ["Jan","Feb","Mär","Apr","Mai","Jun","Jul","Aug","Sep","Okt","Nov","Dez"];
var TAGNAME = {B:"BUILD", C:"CONTENT", D:"ENTSCHEIDUNG", A:"ADMIN", S:"SPIEL", V:"VERKAUF"};

function parseISO(s){ var p = s.split("-"); return new Date(+p[0], +p[1]-1, +p[2]); }
function addDays(d, n){ var x = new Date(d.getTime()); x.setDate(x.getDate()+n); return x; }
function iso(d){
  var m = d.getMonth()+1, dd = d.getDate();
  return d.getFullYear() + "-" + (m<10?"0":"") + m + "-" + (dd<10?"0":"") + dd;
}
function fmt(d){ return DSHORT[(d.getDay()+6)%7] + ", " + d.getDate() + ". " + MON[d.getMonth()] + " " + d.getFullYear(); }
function fmtShort(d){ return DSHORT[(d.getDay()+6)%7] + " " + d.getDate() + ". " + MON[d.getMonth()]; }
function esc(s){ return String(s == null ? "" : s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;"); }
function isTask(t){ return t.c !== "N"; }
function minTxt(m){ if (m >= 60){ var h = Math.floor(m/60), r = m%60; return h + " Std." + (r ? " " + r + " Min." : ""); } return m + " Min."; }
function host(u){ try { return new URL(u).hostname.replace(/^www\./, ""); } catch(e){ return u; } }
function safeUrl(u){ return /^https?:\/\//i.test(u || "") ? u : ""; }

var TOTAL = 0, DAYMAP = {};
WEEKS.forEach(function(w){
  w._start = parseISO(w.start);
  w.days.forEach(function(day, di){
    day.forEach(function(t){ if (isTask(t)) TOTAL++; });
    DAYMAP[iso(addDays(w._start, di))] = {w:w, di:di};
  });
});

var done = Object.create(null);
var kv = Object.create(null);
var db = null, writing = false, pending = false, kwriting = false, kpending = false;
var noteEl = document.getElementById("saveNote");
function note(s){ noteEl.textContent = s; }

/* ---- task rendering ---- */
function whereBlock(o){
  if (!o || !o.length) return "";
  var h = '<div class="where"><div class="wh">Wohin · Links · Orte</div><ul>';
  o.forEach(function(x){
    var u = safeUrl(x.u);
    h += '<li><b>' + esc(x.n) + '</b>';
    if (u) h += ' · <a href="' + esc(u) + '" target="_blank" rel="noopener">' + esc(host(u)) + '</a>';
    if (x.a) h += '<br><span class="ad">' + esc(x.a) + '</span>';
    if (x.h) h += '<br>' + esc(x.h);
    h += '</li>';
  });
  return h + '</ul></div>';
}

function videoBlock(v, id){
  if (!v) return "";
  var h = '<div class="vb"><div class="vbh"><span class="eyebrow">Video' + (v.id ? " " + esc(v.id) : "") + '</span>';
  var meta = [];
  if (v.slot) meta.push(v.slot);
  if (v.dauer) meta.push(v.dauer);
  if (v.plattform) meta.push(v.plattform);
  if (meta.length) h += '<span class="vt">' + esc(meta.join(" · ")) + '</span>';
  h += '</div>';
  if (v.hook_en) h += '<div class="hook">„' + esc(v.hook_en) + '“</div>';
  if (v.hook_de) h += '<div class="hookde">' + esc(v.hook_de) + '</div>';
  h += '<dl>';
  if (v.shots && v.shots.length){
    h += '<dt>Shots</dt><dd><ol>';
    v.shots.forEach(function(s){ h += '<li>' + esc(s) + '</li>'; });
    h += '</ol></dd>';
  }
  if (v.ort) h += '<dt>Drehort</dt><dd>' + esc(v.ort) + '</dd>';
  if (v.ton) h += '<dt>Ton</dt><dd>' + esc(v.ton) + '</dd>';
  if (v.text) h += '<dt>Text im Bild</dt><dd>' + esc(v.text) + '</dd>';
  if (v.cta) h += '<dt>CTA</dt><dd>' + esc(v.cta) + '</dd>';
  if (v.check) h += '<dt>Regel-Check</dt><dd>' + esc(v.check) + '</dd>';
  h += '</dl>';
  if (v.caption){
    var cid = "c_" + id;
    h += '<div class="prompt"><div class="ph"><span class="eyebrow">Caption</span>' +
      '<button type="button" data-copy="' + cid + '">Kopieren</button></div>' +
      '<pre class="code" id="' + cid + '">' + esc(v.caption) + '</pre></div>';
  }
  return h + '</div>';
}

function taskRow(wn, di, ti, t, pfx, open){
  var key = "w" + wn + "d" + di + "t" + ti;
  var id = (pfx || "") + key;
  if (t.c === "N"){
    return '<li class="tk note" data-q="' + esc((t.t || "").toLowerCase()) + '"><span class="ntxt"><span class="ok"></span><span>' + esc(t.t) + '</span></span></li>';
  }
  var mins = t.m || 0, steps = t.s || [], fertig = t.f || "", prompt = t.p || "";
  var q = [t.t, steps.join(" "), fertig, (t.o || []).map(function(x){ return x.n + " " + (x.a || ""); }).join(" "), t.v ? (t.v.id + " " + (t.v.hook_en || "") + " " + (t.v.hook_de || "")) : ""].join(" ").toLowerCase();
  var h = '<li class="tk' + (t.plus ? " isplus" : "") + '" data-q="' + esc(q) + '"><div class="tkrow">' +
    '<input type="checkbox" id="' + id + '" data-ms="' + key + '">' +
    '<div class="body"><label class="ttl" for="' + id + '"><span class="tg ' + t.c + '">' + TAGNAME[t.c] + '</span>' +
    '<span class="txt">' + esc(t.t) + '</span></label>';
  var chips = "";
  if (mins) chips += '<span class="chip">' + minTxt(mins) + '</span>';
  if (t.plus) chips += '<span class="chip plus">Grind+ · optional</span>';
  if (t.v) chips += '<span class="chip vid">Video' + (t.v.id ? " " + esc(t.v.id) : "") + '</span>';
  if (t.o && t.o.length) chips += '<span class="chip">' + t.o.length + (t.o.length === 1 ? " Link/Ort" : " Links/Orte") + '</span>';
  if (prompt) chips += '<span class="chip cl">mit Claude</span>';
  if (t.x === "s") chips += '<span class="chip sp">nur bei „Spiel bauen“</span>';
  if (steps.length || fertig || prompt || t.v || (t.o && t.o.length)){
    h += '<details class="how"' + (open ? ' open' : '') + '><summary>' + chips + '<span class="sg">So geht’s</span></summary>';
    if (steps.length){
      h += '<ol class="hs">';
      steps.forEach(function(s){ h += '<li>' + esc(s) + '</li>'; });
      h += '</ol>';
    }
    h += videoBlock(t.v, id);
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

function dayMins(day){
  var m = 0, p = 0, s = 0;
  day.forEach(function(t){
    if (!isTask(t)) return;
    if (t.c === "S" || t.x === "s") s += t.m || 0;
    else if (t.plus) p += t.m || 0;
    else m += t.m || 0;
  });
  return [m, p, s];
}
function minsLabel(mm){
  var mt = mm[0] ? "≈ " + minTxt(mm[0]) : "";
  if (mm[1]) mt += (mt ? " · " : "") + "+" + minTxt(mm[1]) + " Grind+";
  if (mm[2]) mt += (mt ? " · " : "") + "+" + minTxt(mm[2]) + " Spiel";
  return mt;
}

/* ---- phase bar ---- */
(function(){
  var el = document.getElementById("phbar"), h = "";
  Object.keys(PH).forEach(function(k){
    h += '<div class="phcell" data-ph="' + k + '"><span class="id">' + k + '</span>' +
      '<div class="nm">' + PH[k][0] + '</div><div class="dt">' + PH[k][1] + '</div>' +
      '<div class="bar"><i data-phbar="' + k + '"></i></div>' +
      '<div class="ct" data-phct="' + k + '">0/0</div></div>';
  });
  el.innerHTML = h;
})();

/* ---- weeks ---- */
(function(){
  var el = document.getElementById("weeks"), h = "";
  WEEKS.forEach(function(w){
    var s = w._start, e = addDays(s, 6);
    var n = 0;
    w.days.forEach(function(d){ d.forEach(function(t){ if (isTask(t)) n++; }); });
    var range = s.getDate() + ". " + MON[s.getMonth()] + " – " + e.getDate() + ". " + MON[e.getMonth()] + " " + e.getFullYear();
    h += '<details class="wk" id="wk' + w.n + '" data-wk="' + w.n + '" data-ph="' + w.phase + '">' +
      '<summary class="wkhead"><span class="wktag">W' + w.n + " · " + w.phase + '</span>' +
      '<span class="wkti"><span class="g">' + esc(w.goal) + '</span><span class="d">' + range + '</span></span>' +
      '<span class="wkri"><span class="wkct" data-wct="' + w.n + '">0/' + n + '</span>' +
      '<span class="wkbar"><i data-wbar="' + w.n + '"></i></span><span class="chev"></span></span></summary>';
    if (w.kpi && w.kpi.length){
      h += '<div class="weekkpi"><span class="lbl">Ziel bis Sonntag</span>';
      w.kpi.forEach(function(k){ h += '<span>' + esc(k.k) + ': <b>' + esc(k.ziel) + '</b></span>'; });
      h += '</div>';
    }
    w.days.forEach(function(day, di){
      var d = addDays(s, di), mt = minsLabel(dayMins(day));
      h += '<div class="day" data-date="' + iso(d) + '"><div class="dayhd">' +
        '<span class="dn">' + DNAMES[di] + '</span><span class="dd">' + d.getDate() + ". " + MON[d.getMonth()] + '</span>' +
        '<span class="tdy" hidden>Heute</span><span class="dm sp">' + mt + '</span></div><ul>';
      day.forEach(function(t, ti){ h += taskRow(w.n, di, ti, t, "", false); });
      if (!day.length) h += '<li class="tk note"><span class="ntxt" style="color:var(--ink3)">Frei.</span></li>';
      h += '</ul></div>';
    });
    h += '</details>';
  });
  el.innerHTML = h;
})();

/* ---- today ---- */
var TODAY_TARGET = null;
(function(){
  var now = new Date();
  var t = iso(now), todayISO = null;
  var first = WEEKS[0]._start, last = addDays(WEEKS[NW-1]._start, 6);
  var target = t, entry = DAYMAP[t];
  if (!entry){
    if (now < first){ target = iso(first); entry = DAYMAP[target]; }
    else { target = iso(last); entry = DAYMAP[target]; }
  } else { todayISO = t; }
  TODAY_TARGET = target;

  var d = parseISO(target);
  var w = entry.w, di = entry.di, day = w.days[di];
  document.getElementById("tdTitle").textContent = (todayISO ? "Heute · " : "Plan-Tag · ") + DNAMES[di];
  document.getElementById("tdDate").textContent = fmt(d);
  document.getElementById("tdWeek").textContent = "Woche " + w.n + " von " + NW + " · " + w.phase + " " + PH[w.phase][0];
  var goal = "<b>Wochenziel:</b> " + esc(w.goal);
  if (w.kpi && w.kpi.length) goal += "<br><b>Zahlen bis Sonntag:</b> " + w.kpi.map(function(k){ return esc(k.k) + " " + esc(k.ziel); }).join(" · ");
  document.getElementById("tdGoal").innerHTML = goal;
  var mm = dayMins(day), meta = "";
  meta += '<span>Heute: <b>' + (mm[0] ? "≈ " + minTxt(mm[0]) : "frei") + '</b>' + (mm[1] ? " · +" + minTxt(mm[1]) + " Grind+" : "") + (mm[2] ? " · +" + minTxt(mm[2]) + " nur bei Spiel" : "") + '</span>';
  var nd = addDays(d, 1), ne = DAYMAP[iso(nd)];
  if (ne){
    var nt = ne.w.days[ne.di].filter(isTask);
    meta += '<span>Morgen: <b>' + (nt.length ? esc(nt[0].t) + (nt.length > 1 ? " + " + (nt.length-1) + " weitere" : "") : "frei") + '</b></span>';
  }
  if (KPI.some(function(k){ return k.d === target; })) meta += '<span><a class="lnk" href="#cockpit">Heute Zahlen ins Cockpit eintragen</a></span>';
  document.getElementById("tdMeta").innerHTML = meta;
  var ul = document.getElementById("todayList"), h = "";
  day.forEach(function(t, ti){ h += taskRow(w.n, di, ti, t, "td_", true); });
  if (!h) h = '<li class="tk note"><span class="ntxt" style="color:var(--ink3)">Heute ist nichts geplant.</span></li>';
  ul.innerHTML = h;

  var wk = document.getElementById("wk" + w.n);
  if (wk){ wk.open = true; wk.classList.add("cur"); }
  var dayEl = document.querySelector('.day[data-date="' + target + '"] .tdy');
  if (dayEl && todayISO) dayEl.hidden = false;
})();

/* ---- die nächsten 7 Tage ---- */
(function(){
  var host = document.getElementById("nextDays"), h = "";
  var base = parseISO(TODAY_TARGET);
  for (var k = 1; k <= 7; k++){
    var d = addDays(base, k), e = DAYMAP[iso(d)];
    if (!e) break;
    var day = e.w.days[e.di], tasks = day.filter(isTask);
    var mt = minsLabel(dayMins(day));
    var first = tasks.length ? tasks[0].t : "frei";
    h += '<details class="nxday"' + (k === 1 ? " open" : "") + '><summary>' +
      '<span class="dn">' + (k === 1 ? "Morgen · " : "") + DNAMES[e.di] + '</span><span class="dd">' + d.getDate() + ". " + MON[d.getMonth()] + '</span>' +
      '<span class="cnt">' + tasks.length + (tasks.length === 1 ? " Aufgabe" : " Aufgaben") + '</span>' +
      '<span class="first">' + esc(first) + '</span><span class="dm">' + mt + '</span></summary><ul>';
    day.forEach(function(t, ti){ h += taskRow(e.w.n, e.di, ti, t, "nx_", false); });
    if (!day.length) h += '<li class="tk note"><span class="ntxt" style="color:var(--ink3)">Frei.</span></li>';
    h += '</ul></details>';
  }
  host.innerHTML = h || '<p class="intro" style="padding:12px 18px;margin:0">Der Plan endet hier.</p>';
  // aktuelle und nächste Woche im großen Plan offen
  var e0 = DAYMAP[TODAY_TARGET];
  if (e0){
    var nw = document.getElementById("wk" + (e0.w.n + 1));
    if (nw) nw.open = true;
  }
  var btn = document.getElementById("openAll"), allOpen = false;
  btn.addEventListener("click", function(){
    allOpen = !allOpen;
    var wks = document.querySelectorAll("#weeks .wk");
    for (var i = 0; i < wks.length; i++) wks[i].open = allOpen;
    btn.textContent = allOpen ? "Alle Wochen zuklappen" : "Alle Wochen aufklappen";
  });
})();

/* ---- plan filter ---- */
(function(){
  var box = document.getElementById("planq"), plus = document.getElementById("planplus"), hits = document.getElementById("planhits");
  function apply(){
    var q = (box.value || "").trim().toLowerCase();
    var rows = document.querySelectorAll("#weeks .tk"), n = 0;
    for (var i = 0; i < rows.length; i++){
      var m = !q || (rows[i].getAttribute("data-q") || "").indexOf(q) >= 0;
      rows[i].classList.toggle("miss", !m);
      if (m && q) n++;
    }
    if (q){
      var wks = document.querySelectorAll("#weeks .wk");
      for (var j = 0; j < wks.length; j++) wks[j].open = !!wks[j].querySelector(".tk:not(.miss)");
      hits.textContent = n + " Treffer";
    } else hits.textContent = "";
  }
  box.addEventListener("input", apply);
  plus.addEventListener("change", function(){ document.body.classList.toggle("hideplus", !plus.checked); });
})();

/* ---- cockpit ---- */
/* Kennzahlen: [Feld, Name, Feld für den Alarmwert]. Follower: Ernest trägt die Gesamtzahl ein, gezählt wird ab dem Startwert. */
var KF = [["wl","Warteliste bestätigt","wl_a"],["fo","Follower neu seit 12.10.",null],["zu","Zusagen „Die ersten 35“","zu_a"],["pre","Jeans bestellt und bezahlt","pre_a"]];
function kNum(x){ if (x == null) return null; var n = parseFloat(String(x).replace(/\./g,"").replace(",", ".")); return isFinite(n) ? n : null; }
function kIst(f, val){
  if (!val) return null;
  var ist = kNum(val[f]);
  if (ist == null) return null;
  if (f === "fo"){
    var st = kv.start ? kNum(kv.start.fo) : null;
    return st == null ? null : Math.max(0, ist - st);
  }
  return ist;
}
function kOne(row, f, ist){
  var z = row[f[0]], a = f[2] ? row[f[2]] : null;
  if (z == null || ist == null) return null;
  if (ist >= z) return 2;
  if (a != null) return ist >= a ? 1 : 0;
  return ist >= 0.75 * z ? 1 : 0;
}
function kStatus(row, val){
  var worst = null;
  KF.forEach(function(f){
    var r = kOne(row, f, kIst(f[0], val));
    if (r != null && (worst === null || r < worst)) worst = r;
  });
  if (worst === null) return ["n", "offen"];
  return [["r","unter Alarm"],["y","unter Soll"],["g","im Plan"]][worst];
}
function renderCockpit(){
  var todayISO = iso(new Date());
  var cur = null;
  for (var i = 0; i < KPI.length; i++){ if (KPI[i].d >= todayISO){ cur = KPI[i]; break; } }
  if (!cur) cur = KPI[KPI.length-1];
  var lastIst = null;
  KPI.forEach(function(k){ var v = kv[k.d]; if (v && KF.some(function(f){ return kNum(v[f[0]]) != null; })) lastIst = {k:k, v:v}; });

  var head = "";
  KF.forEach(function(f){
    var z = cur[f[0]], ist = lastIst ? kIst(f[0], lastIst.v) : null;
    var pct = (z && ist != null) ? Math.min(100, ist / z * 100) : 0;
    var hint = lastIst ? "zuletzt eingetragen " + fmtShort(parseISO(lastIst.k.d)) : "noch nichts eingetragen";
    if (f[0] === "fo" && !(kv.start && kNum(kv.start.fo) != null)) hint = "erst Startwert eintragen";
    head += '<div class="cpc"><span class="k">' + f[1] + '</span><div class="v">' + (ist != null ? ist.toLocaleString("de-DE") : "—") + '</div>' +
      '<div class="s">Ziel bis ' + fmtShort(parseISO(cur.d)) + ': <b>' + (z != null ? z.toLocaleString("de-DE") : "—") + '</b>' + (f[2] && cur[f[2]] != null ? ' · Alarm ' + cur[f[2]].toLocaleString("de-DE") : '') + ' · ' + hint + '</div>' +
      '<div class="cpbar"><i style="width:' + pct + '%"></i></div></div>';
  });
  document.getElementById("cphead").innerHTML = head;
  var sv = kv.start && kv.start.fo != null ? kv.start.fo : "";
  document.getElementById("cpstart").innerHTML = '<label for="k_fo_start">Startwert Follower (TikTok + Instagram zusammen, gezählt am Sa 10.10.)</label> ' +
    '<input class="kin" id="k_fo_start" inputmode="numeric" data-kd="start" data-kf="fo" value="' + esc(sv) + '" placeholder="Zahl">';

  var rows = "";
  KPI.forEach(function(k){
    var v = kv[k.d] || {}, st = kStatus(k, kv[k.d]);
    rows += '<tr' + (k === cur ? ' class="kcur"' : '') + '><td class="mono">' + fmtShort(parseISO(k.d)) + '</td>';
    KF.forEach(function(f){
      var fid = "k_" + f[0] + "_" + k.d;
      var z = k[f[0]] != null ? k[f[0]].toLocaleString("de-DE") + (f[2] && k[f[2]] != null ? ' <span class="mono" style="color:var(--ink3)">(' + k[f[2]].toLocaleString("de-DE") + ')</span>' : '') : "—";
      var ph = f[0] === "fo" ? "gesamt" : "Ist";
      rows += '<td class="num">' + z + '</td>' +
        '<td><input class="kin" id="' + fid + '" aria-label="' + f[1] + ' Ist ' + k.d + '" inputmode="numeric" data-kd="' + k.d + '" data-kf="' + f[0] + '" value="' + esc(v[f[0]] != null ? v[f[0]] : "") + '" placeholder="' + ph + '"></td>';
    });
    rows += '<td><span class="stat ' + st[0] + '">' + st[1] + '</span></td></tr>';
  });
  document.getElementById("cprows").innerHTML = rows;

  var gh = "";
  var show = lastIst ? lastIst.k : null;
  if (show){
    var st2 = kStatus(show, kv[show.d]);
    if ((st2[0] === "y" || st2[0] === "r") && show.mass && show.mass.length){
      gh += '<div class="risk' + (st2[0] === "y" ? " med" : "") + '"><div class="rh"><span class="rt">Gegenmaßnahmen ab ' + fmtShort(parseISO(show.d)) + '</span><span class="stat ' + st2[0] + '">' + st2[1] + '</span></div>';
      if (show.gate) gh += '<p>' + esc(show.gate) + '</p>';
      gh += '<ul>' + show.mass.map(function(m){ return '<li>' + esc(m) + '</li>'; }).join("") + '</ul></div>';
    } else if (st2[0] === "g"){
      gh += '<div class="callout plain"><span class="eyebrow">Stand ' + fmtShort(parseISO(show.d)) + '</span><p>Im Plan. Weiter nach Tagesplan, nichts zusätzlich.</p></div>';
    }
  }
  if (cur.gate && cur !== show) gh += '<div class="callout plain"><span class="eyebrow">Nächster Check · ' + fmtShort(parseISO(cur.d)) + '</span><p>' + esc(cur.gate) + '</p></div>';
  document.getElementById("cpgate").innerHTML = gh;
}
document.addEventListener("change", function(e){
  var t = e.target;
  if (!t || !t.getAttribute || !t.getAttribute("data-kd")) return;
  var d = t.getAttribute("data-kd"), f = t.getAttribute("data-kf");
  var val = t.value.trim();
  if (!kv[d]) kv[d] = {};
  if (val === "") delete kv[d][f]; else kv[d][f] = val;
  renderCockpit();
  ksave();
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
renderCockpit();

/* ---- render state ---- */
var megaBar = document.getElementById("megaBar");
var megaPct = document.getElementById("megaPct");
var megaCount = document.getElementById("megaCount");

function render(){
  var total = 0, phAgg = {};
  Object.keys(PH).forEach(function(k){ phAgg[k] = [0,0]; });
  WEEKS.forEach(function(w){
    var n = 0, cap = 0;
    w.days.forEach(function(day, di){
      day.forEach(function(t, ti){
        if (!isTask(t)) return;
        cap++;
        if (done["w" + w.n + "d" + di + "t" + ti]) n++;
      });
    });
    total += n;
    phAgg[w.phase][0] += n;
    phAgg[w.phase][1] += cap;
    var c = document.querySelector('[data-wct="' + w.n + '"]');
    var b = document.querySelector('[data-wbar="' + w.n + '"]');
    if (c) c.textContent = n + "/" + cap;
    if (b) b.style.width = (cap ? n/cap*100 : 0) + "%";
    var el = document.getElementById("wk" + w.n);
    if (el) el.classList.toggle("done", cap > 0 && n === cap);
  });
  Object.keys(PH).forEach(function(k){
    var a = phAgg[k];
    var b = document.querySelector('[data-phbar="' + k + '"]');
    var c = document.querySelector('[data-phct="' + k + '"]');
    if (b) b.style.width = (a[1] ? a[0]/a[1]*100 : 0) + "%";
    if (c) c.textContent = a[0] + "/" + a[1];
  });
  var boxes = document.querySelectorAll("[data-ms]");
  for (var i = 0; i < boxes.length; i++){
    boxes[i].checked = !!done[boxes[i].getAttribute("data-ms")];
  }
  megaPct.textContent = Math.round(total / TOTAL * 100);
  megaCount.textContent = total + "/" + TOTAL;
  megaBar.style.width = (total / TOTAL * 100) + "%";
}

document.addEventListener("change", function(e){
  var t = e.target;
  if (!t || !t.getAttribute || !t.getAttribute("data-ms")) return;
  var id = t.getAttribute("data-ms");
  if (t.checked) done[id] = true; else delete done[id];
  render();
  save();
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

render();

/* ---- countdown ---- */
var dEl = document.getElementById("cdDays");
var cEl = document.getElementById("cdClock");
var wEl = document.getElementById("weekOf");
var STARTMS = WEEKS[0]._start.getTime();
function tick(){
  var now = Date.now(), ms = DROP - now;
  if (ms <= 0){
    dEl.textContent = "0"; cEl.textContent = "DROP IST LIVE"; wEl.textContent = "Woche " + NW + " von " + NW; return;
  }
  var s = Math.floor(ms/1000), d = Math.floor(s/86400), h = Math.floor(s%86400/3600), m = Math.floor(s%3600/60), sec = s%60;
  function p(n){ return n < 10 ? "0"+n : ""+n; }
  dEl.textContent = d;
  cEl.textContent = p(h) + ":" + p(m) + ":" + p(sec) + " verbleibend";
  var wk = Math.floor((now - STARTMS)/604800000) + 1;
  wEl.textContent = "Woche " + Math.max(1, Math.min(NW, wk)) + " von " + NW;
}
tick();
setInterval(tick, 1000);

/* ---- copy buttons ---- */
document.addEventListener("click", function(e){
  var b = e.target && e.target.closest ? e.target.closest("[data-copy]") : null;
  if (!b) return;
  e.preventDefault();
  var pre = document.getElementById(b.getAttribute("data-copy"));
  if (!pre) return;
  var txt = pre.innerText;
  function ok(){ b.textContent = "Kopiert"; setTimeout(function(){ b.textContent = "Kopieren"; }, 1600); }
  function fallback(){
    try {
      var r = document.createRange(); r.selectNodeContents(pre);
      var s = window.getSelection(); s.removeAllRanges(); s.addRange(r);
      if (document.execCommand && document.execCommand("copy")) ok(); else b.textContent = "Markiert";
    } catch(err){ b.textContent = "Markiert"; }
  }
  try {
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(txt).then(ok, fallback);
    else fallback();
  } catch(err){ fallback(); }
});

/* ---- db ---- */
if (window.claude && window.claude.use){
  window.claude.use("db").then(function(d){
    if (!d){ note("Nur in diesem Tab · Speicher nicht verfügbar"); return; }
    db = d;
    note("Fortschritt wird gespeichert");
    db.doc("progress/tasks").onSnapshot(function(snap){
      if (!snap.exists){ note("Fortschritt wird gespeichert"); return; }
      var data = snap.data() || {}, rec = data.done || {};
      done = Object.create(null);
      Object.keys(rec).forEach(function(k){ if (rec[k]) done[k] = true; });
      render();
      if (!snap.metadata.hasPendingWrites) note("Gespeichert");
    }, function(err){
      note("Speicher unterbrochen (" + (err && err.code ? err.code : "Fehler") + ")");
    });
    db.doc("progress/kpi").onSnapshot(function(snap){
      if (!snap.exists) return;
      var data = snap.data() || {}, rec = data.vals || {};
      var act = document.activeElement;
      if (act && act.getAttribute && act.getAttribute("data-kd")) return;
      kv = Object.create(null);
      Object.keys(rec).forEach(function(d){ kv[d] = {}; Object.keys(rec[d] || {}).forEach(function(f){ kv[d][f] = rec[d][f]; }); });
      renderCockpit();
    }, function(){});
  }).catch(function(){ note("Nur in diesem Tab · Speicher nicht verfügbar"); });
} else {
  note("Nur in diesem Tab · Speicher nicht verfügbar");
}
})();
