/**
 * AI Vintage Stylist — Embeddable Widget
 *
 * Install: paste this ONE line just before </body> in theme.liquid
 *
 *   <script src="https://ai-vintage-stylist.onrender.com/widget.js" data-ai-stylist async></script>
 */
(function () {
  'use strict';

  var me = document.querySelector('script[data-ai-stylist]');
  if (!me) return;

  var SERVER = new URL(me.src).origin;
  var cfg    = window.AIStylistConfig || {};
  var BTN_TEXT = cfg.buttonText  || '✨ Find Your Style';
  var BTN_BG   = cfg.buttonColor || '#111';
  var BTN_FG   = cfg.buttonTextColor || '#fff';

  /* ── state ── */
  var phase = 'idle', sid = null, quiz = null, shopName = '';
  var qIdx = 0, answers = {};

  /* ── inject CSS once into <head> (prefixed so no theme conflicts) ── */
  var styleEl = document.createElement('style');
  styleEl.textContent = [
    '#ais-overlay{display:none;position:fixed;inset:0;z-index:2147483646;',
    'background:rgba(0,0,0,.6);align-items:center;justify-content:center;padding:16px;',
    'font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif!important}',
    '#ais-overlay.ais-open{display:flex!important}',

    '#ais-card{background:#fff!important;border-radius:16px!important;width:100%!important;',
    'max-width:450px!important;max-height:88vh!important;overflow-y:auto!important;',
    'box-shadow:0 20px 60px rgba(0,0,0,.4)!important;color:#111!important}',

    '#ais-hdr{padding:15px 18px!important;border-bottom:1px solid #eee!important;',
    'display:flex!important;align-items:center!important;justify-content:space-between!important;',
    'position:sticky!important;top:0!important;background:#fff!important;z-index:1!important;',
    'border-radius:16px 16px 0 0!important}',

    '#ais-hdr-left{display:flex!important;flex-direction:column!important;gap:2px!important}',
    '#ais-tag{font-size:10px!important;letter-spacing:.12em!important;text-transform:uppercase!important;',
    'color:#b05e30!important;font-weight:700!important;margin:0!important}',
    '#ais-title{font-size:15px!important;font-weight:700!important;color:#111!important;margin:0!important}',

    '#ais-close{width:28px!important;height:28px!important;border:none!important;',
    'background:#f0f0f0!important;border-radius:50%!important;cursor:pointer!important;',
    'font-size:16px!important;color:#555!important;display:flex!important;',
    'align-items:center!important;justify-content:center!important;flex-shrink:0!important;',
    'line-height:1!important;padding:0!important}',
    '#ais-close:hover{background:#ddd!important}',

    '#ais-body{padding:22px 20px!important}',

    '.ais-spin{width:38px;height:38px;border-radius:50%;border:3px solid #eee;',
    'border-top-color:#b05e30;animation:ais-spin .8s linear infinite;margin:0 auto 16px}',
    '@keyframes ais-spin{to{transform:rotate(360deg)}}',

    '.ais-opt{padding:12px 10px!important;border:1.5px solid #e0e0e0!important;',
    'border-radius:10px!important;background:#fafafa!important;cursor:pointer!important;',
    'text-align:left!important;font-size:13px!important;color:#222!important;',
    'display:flex!important;align-items:center!important;gap:8px!important;',
    'line-height:1.3!important;width:100%!important;box-sizing:border-box!important;',
    'font-family:inherit!important;transition:border-color .15s,background .15s!important}',
    '.ais-opt:hover{border-color:#b05e30!important;background:#fff5f0!important}',
    '.ais-opt.ais-sel{border-color:#b05e30!important;background:#fff5f0!important;',
    'box-shadow:0 0 0 2px #b05e30!important}',

    '.ais-btn-p{padding:10px 20px!important;border:none!important;border-radius:8px!important;',
    'cursor:pointer!important;font-size:13px!important;font-weight:700!important;',
    'background:#111!important;color:#fff!important;font-family:inherit!important}',
    '.ais-btn-p:hover:not(:disabled){background:#b05e30!important}',
    '.ais-btn-p:disabled{opacity:.3!important;cursor:not-allowed!important}',
    '.ais-btn-g{padding:10px 20px!important;border:1.5px solid #ddd!important;',
    'border-radius:8px!important;cursor:pointer!important;font-size:13px!important;',
    'font-weight:700!important;background:transparent!important;color:#555!important;',
    'font-family:inherit!important}',
    '.ais-btn-g:hover{border-color:#aaa!important}',

    '.ais-prod{display:flex!important;border:1px solid #eee!important;border-radius:10px!important;',
    'overflow:hidden!important;text-decoration:none!important;color:inherit!important;',
    'margin-bottom:10px!important;background:#fff!important}',
    '.ais-prod:hover{box-shadow:0 4px 14px rgba(0,0,0,.1)!important}',

    '@media(max-width:500px){',
    '#ais-overlay{align-items:flex-end!important;padding:0!important}',
    '#ais-card{border-radius:16px 16px 0 0!important;max-height:92vh!important}',
    '.ais-opts-grid{grid-template-columns:1fr!important}}',
  ].join('');
  document.head.appendChild(styleEl);

  /* ── overlay HTML ── */
  var overlayEl = document.createElement('div');
  overlayEl.id = 'ais-overlay';
  /* Set critical layout via inline style — does NOT depend on the injected CSS */
  overlayEl.style.cssText = [
    'display:none', 'position:fixed', 'top:0', 'left:0', 'right:0', 'bottom:0',
    'z-index:2147483646', 'background:rgba(0,0,0,.6)',
    'align-items:center', 'justify-content:center', 'padding:16px',
    'font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif',
  ].join(';');
  overlayEl.innerHTML = [
    '<div id="ais-card" style="background:#fff;border-radius:16px;width:100%;max-width:450px;max-height:88vh;overflow-y:auto;box-shadow:0 20px 60px rgba(0,0,0,.4);color:#111">',
    '  <div id="ais-hdr" style="padding:15px 18px;border-bottom:1px solid #eee;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;background:#fff;z-index:1;border-radius:16px 16px 0 0">',
    '    <div style="display:flex;flex-direction:column;gap:2px">',
    '      <span style="font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:#b05e30;font-weight:700">✦ AI Stylist</span>',
    '      <span id="ais-title" style="font-size:15px;font-weight:700;color:#111">Style Quiz</span>',
    '    </div>',
    '    <button id="ais-close" style="width:28px;height:28px;border:none;background:#f0f0f0;border-radius:50%;cursor:pointer;font-size:16px;color:#555;display:flex;align-items:center;justify-content:center;flex-shrink:0;padding:0;line-height:1">✕</button>',
    '  </div>',
    '  <div id="ais-body" style="padding:22px 20px"></div>',
    '</div>',
  ].join('');
  document.body.appendChild(overlayEl);

  overlayEl.addEventListener('click', function (e) { if (e.target === overlayEl) closeModal(); });
  document.getElementById('ais-close').addEventListener('click', closeModal);

  /* ── floating button ── */
  var triggerBtn = document.createElement('button');
  triggerBtn.id = 'ais-trigger';
  triggerBtn.textContent = BTN_TEXT;
  triggerBtn.style.cssText = [
    'position:fixed', 'bottom:22px', 'right:22px',
    'z-index:2147483645', 'padding:13px 22px',
    'background:' + BTN_BG, 'color:' + BTN_FG,
    'border:none', 'border-radius:50px',
    'font-family:inherit', 'font-size:14px', 'font-weight:700',
    'cursor:pointer', 'letter-spacing:.01em',
    'box-shadow:0 4px 18px rgba(0,0,0,.3)',
    'transition:transform .2s,box-shadow .2s',
  ].join(';');
  triggerBtn.addEventListener('mouseover', function () { triggerBtn.style.transform = 'translateY(-2px)'; });
  triggerBtn.addEventListener('mouseout',  function () { triggerBtn.style.transform = ''; });
  triggerBtn.addEventListener('click', openModal);
  document.body.appendChild(triggerBtn);

  /* ── dom shortcuts ── */
  function $title() { return document.getElementById('ais-title'); }
  function $body()  { return document.getElementById('ais-body');  }

  /* ── modal ── */
  function openModal() {
    overlayEl.style.display = 'flex';
    document.body.style.overflow = 'hidden';
    if (phase === 'idle')    runAnalysis();
    else if (phase === 'quiz')    renderQuestion();
    else if (phase === 'error')   renderError();
    /* loading / results already displayed */
  }

  function closeModal() {
    overlayEl.style.display = 'none';
    document.body.style.overflow = '';
  }

  /* ── helpers ── */
  function esc(s) {
    return (s || '').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
  }

  async function post(path, body) {
    var ac = new AbortController();
    var t  = setTimeout(function(){ ac.abort(); }, 120000);
    try {
      var r    = await fetch(SERVER + path, {
        method:  'POST',
        headers: {'Content-Type':'application/json'},
        body:    JSON.stringify(body),
        signal:  ac.signal,
      });
      var data = await r.json();
      if (!r.ok) throw new Error(data.detail || 'Server error');
      return data;
    } catch(e) {
      if (e.name === 'AbortError') throw new Error('Server is waking up — please try again.');
      throw e;
    } finally { clearTimeout(t); }
  }

  /* ── views ── */
  function setTitle(t) { $title().textContent = t; }

  function renderLoading(title, sub) {
    setTitle('AI Stylist');
    $body().innerHTML = [
      '<div style="text-align:center;padding:40px 0">',
      '<div class="ais-spin"></div>',
      '<div style="font-size:16px;font-weight:700;color:#111;margin-bottom:8px">' + esc(title) + '</div>',
      '<div style="font-size:13px;color:#888;line-height:1.5">' + esc(sub) + '</div>',
      '</div>',
    ].join('');
  }

  function renderError(msg) {
    setTitle('AI Stylist');
    var m = msg || 'Could not load quiz. Please try again.';
    $body().innerHTML = [
      '<div style="text-align:center;padding:36px 10px">',
      '<div style="font-size:34px;margin-bottom:12px">😕</div>',
      '<div style="font-size:17px;font-weight:700;margin-bottom:8px">Something went wrong</div>',
      '<div style="font-size:13px;color:#888;line-height:1.55;margin-bottom:20px">' + esc(m) + '</div>',
      '<button class="ais-btn-p" id="ais-retry">↺ Try Again</button>',
      '</div>',
    ].join('');
    document.getElementById('ais-retry').onclick = function(){ phase='idle'; runAnalysis(); };
  }

  function renderQuestion() {
    var q   = quiz.questions[qIdx];
    var tot = quiz.questions.length;
    var pct = Math.round(((qIdx + 1) / tot) * 100);
    var sel = answers[q.id];
    setTitle(shopName ? shopName + ' · Quiz' : 'Style Quiz');

    $body().innerHTML = [
      '<div style="height:3px;background:#eee;border-radius:2px;margin-bottom:18px">',
      '<div style="height:100%;width:' + pct + '%;background:#b05e30;border-radius:2px;transition:width .3s"></div></div>',
      '<div style="font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:#aaa;margin-bottom:4px">',
      'Question ' + (qIdx+1) + ' of ' + tot + '</div>',
      '<div style="font-size:18px;font-weight:700;color:#111;line-height:1.35;margin-bottom:' + (q.context_hint ? '4px' : '16px') + '">',
      esc(q.question) + '</div>',
      q.context_hint ? '<div style="font-size:12px;color:#aaa;font-style:italic;margin-bottom:16px">' + esc(q.context_hint) + '</div>' : '',
      '<div class="ais-opts-grid" style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:20px">',
      q.options.map(function(o){
        return '<button class="ais-opt' + (sel===o.id?' ais-sel':'') + '" data-id="' + esc(o.id) + '">' +
          (o.emoji ? '<span style="font-size:20px;flex-shrink:0">' + o.emoji + '</span>' : '') +
          '<span>' + esc(o.text) + '</span></button>';
      }).join(''),
      '</div>',
      '<div style="display:flex;align-items:center;justify-content:space-between">',
      '<button class="ais-btn-g" id="ais-prev"' + (qIdx===0?' style="visibility:hidden"':'') + '>← Back</button>',
      '<span style="font-size:12px;color:#bbb">' + (qIdx+1) + ' / ' + tot + '</span>',
      '<button class="ais-btn-p" id="ais-next"' + (sel?'':' disabled') + '>' +
        (qIdx===tot-1 ? 'See my picks →' : 'Next →') + '</button>',
      '</div>',
    ].join('');

    document.querySelectorAll('.ais-opt').forEach(function(btn){
      btn.onclick = function(){
        answers[q.id] = btn.dataset.id;
        document.querySelectorAll('.ais-opt').forEach(function(b){ b.classList.toggle('ais-sel', b===btn); });
        document.getElementById('ais-next').disabled = false;
      };
    });

    document.getElementById('ais-next').onclick = function(){
      if (qIdx < quiz.questions.length-1){ qIdx++; renderQuestion(); }
      else runRecommendations();
    };
    var prev = document.getElementById('ais-prev');
    if (prev) prev.onclick = function(){ if(qIdx>0){ qIdx--; renderQuestion(); } };
  }

  function renderResults(data) {
    phase = 'results';
    setTitle('Your Picks ✦');
    var items = data.recommendations || [];

    $body().innerHTML = [
      '<div style="background:#111;color:#fff;border-radius:12px;padding:20px;margin-bottom:18px;text-align:center">',
      '<div style="font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:#c9a84c;margin-bottom:3px">Your style is…</div>',
      '<div style="font-size:22px;font-weight:700;color:#c9a84c;margin-bottom:8px">' + esc(data.style_profile_title||'Uniquely You') + '</div>',
      '<div style="font-size:13px;color:rgba(255,255,255,.75);line-height:1.6">' + esc(data.style_profile||'') + '</div>',
      '</div>',
      '<div style="font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:#aaa;margin-bottom:10px">Picked for you</div>',
      items.map(function(r){
        return '<a class="ais-prod" href="' + esc(r.product_url||'#') + '" target="_blank" rel="noopener">' +
          '<div style="width:90px;min-height:90px;flex-shrink:0;background:#f5f5f5;overflow:hidden">' +
          (r.product_image
            ? '<img src="' + esc(r.product_image) + '" alt="' + esc(r.product_name) + '" style="width:90px;height:90px;object-fit:cover;display:block" onerror="this.style.display=\'none\'">'
            : '<div style="width:90px;height:90px;display:flex;align-items:center;justify-content:center;font-size:24px;opacity:.3">👗</div>') +
          '</div>' +
          '<div style="padding:10px 12px;flex:1">' +
          '<div style="font-size:14px;font-weight:600;color:#111;margin-bottom:2px">' + esc(r.product_name) + '</div>' +
          (r.product_price ? '<div style="font-size:13px;color:#b05e30;font-weight:600;margin-bottom:4px">' + esc(r.product_price) + '</div>' : '') +
          (r.match_score   ? '<span style="font-size:10px;background:#111;color:#c9a84c;padding:2px 7px;border-radius:20px;display:inline-block;margin-bottom:4px">' + r.match_score + '% match</span>' : '') +
          '<div style="font-size:12px;color:#777;line-height:1.5">' + esc(r.why_for_you) + '</div>' +
          '</div></a>';
      }).join(''),
      data.styling_tip ? [
        '<div style="background:#fff5f0;border-left:3px solid #b05e30;border-radius:8px;padding:12px 14px;margin-top:4px;margin-bottom:16px">',
        '<div style="font-size:10px;letter-spacing:.08em;text-transform:uppercase;color:#b05e30;margin-bottom:3px;font-weight:700">Stylist Tip</div>',
        '<div style="font-size:13px;color:#555;line-height:1.6">' + esc(data.styling_tip) + '</div>',
        '</div>',
      ].join('') : '',
      '<div style="text-align:center;padding-top:4px">',
      '<button id="ais-restart" style="background:none;border:none;color:#aaa;font-size:12px;cursor:pointer;text-decoration:underline;font-family:inherit">↺ Retake quiz</button>',
      '</div>',
    ].join('');

    document.getElementById('ais-restart').onclick = function(){
      phase='quiz'; qIdx=0; answers={}; renderQuestion();
    };
  }

  /* ── API calls ── */
  async function runAnalysis() {
    phase = 'loading';
    renderLoading('Analysing this store…', 'Building your quiz. First visit takes ~30 seconds.');

    var tip = setTimeout(function(){
      if (phase==='loading') renderLoading('Almost there…', 'Server is waking up — nearly done!');
    }, 25000);

    try {
      var data = await post('/api/shop/analyze', { shop_domain: window.location.hostname });
      clearTimeout(tip);
      sid=data.session_id; quiz=data.quiz; shopName=data.shop_name||'';
      phase='quiz'; qIdx=0; answers={};
      renderQuestion();
    } catch(e) {
      clearTimeout(tip);
      phase='error';
      renderError(e.message);
    }
  }

  async function runRecommendations() {
    phase='loading';
    renderLoading('Finding your picks…', 'Matching your style to the collection');
    try {
      var data = await post('/api/shop/recommendations', { session_id:sid, answers:answers });
      renderResults(data);
    } catch(e) {
      phase='error';
      renderError(e.message);
    }
  }

  /* ── init (wait for DOM) ── */
  if (document.readyState==='loading') {
    document.addEventListener('DOMContentLoaded', function(){});
  }

})();
