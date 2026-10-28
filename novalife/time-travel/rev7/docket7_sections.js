/* ---- Content-Plan ---- */
(function(){
  var host = document.getElementById("cplanList");
  if (!host) return;
  var h = "", lastW = -1;
  CPLAN.forEach(function(s){
    var v = VIDS[s.id] || {}, e = DAYMAP[s.post[0]], wn = e ? e.w.n : 0;
    if (wn !== lastW){
      var ws = e ? e.w._start : null, we = ws ? addDays(ws, 6) : null;
      h += '<div class="cpw">W' + wn + (ws ? ' · ' + ws.getDate() + '. ' + MON[ws.getMonth()] + ' – ' + we.getDate() + '. ' + MON[we.getMonth()] : '') + (e && PH[e.w.phase] ? ' · ' + esc(PH[e.w.phase][0]) : '') + '</div>';
      lastW = wn;
    }
    var kind = briefKind(v);
    var cls = s.kind + (s.plus ? " plus" : "") + (s.auto ? " auto" : "") + (kind === "Countdown" ? " cd" : "");
    var film = s.kind === "story" ? "Story" : (s.film ? (s.film[1] > 0 ? "Dreh " + fmtShort(parseISO(s.film[0])) : "aus dem Material") : "Dreh am Posttag");
    var q = [s.id, v.titel, v.saeule, v.hook_en, v.hook_de, kind].join(" ").toLowerCase();
    h += '<details class="cpi" data-k="' + cls + '" data-q="' + esc(q) + '"><summary>' +
      '<span class="cpd mono">' + fmtShort(parseISO(s.post[0])) + ' · ' + esc(s.post[1]) + '</span>' +
      '<span class="cpid mono">' + esc(s.id) + '</span><span class="cpt">' + esc(v.titel || "") + '</span>' +
      '<span class="cps">' + esc((v.saeule || kind) + ' · ' + film + (s.plus ? ' · Grind+' : '') + (s.auto ? ' · Autopilot' : '')) + '</span></summary>' +
      '<div class="lazy" data-vr="' + esc(s.id) + '" data-pid="cp_' + esc(s.id) + '"></div></details>';
  });
  host.innerHTML = h;
  var box = document.getElementById("cpq"), sel = document.getElementById("cpk"), hits = document.getElementById("cphits");
  function apply(){
    var q = (box.value || "").trim().toLowerCase(), k = sel.value, n = 0;
    var items = host.querySelectorAll(".cpi");
    for (var i = 0; i < items.length; i++){
      var it = items[i], cls = " " + it.getAttribute("data-k") + " ";
      var ok = (!q || (it.getAttribute("data-q") || "").indexOf(q) >= 0) && (!k || cls.indexOf(" " + k + " ") >= 0);
      it.classList.toggle("miss", !ok);
      if (ok) n++;
    }
    hits.textContent = (q || k) ? n + " Treffer" : "";
  }
  box.addEventListener("input", apply);
  sel.addEventListener("change", apply);
})();

/* ---- E-Mails ---- */
(function(){
  var host = document.getElementById("mailList");
  if (!host) return;
  var h = "";
  Object.keys(MAILS).sort().forEach(function(k){
    var m = MAILS[k];
    h += '<details class="ref mref"><summary><span class="chev"></span><span class="mid">' + esc(k) + '</span><span class="msub">' + esc(m.betreff) + '</span><span class="mwann">' + esc(m.wann) + '</span></summary>' +
      '<div class="inner"><div class="lazy" data-mail="' + esc(k) + '" data-pid="ml_' + esc(k) + '"></div></div></details>';
  });
  host.innerHTML = h;
})();
