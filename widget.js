/**
 * AI Vintage Stylist — Embeddable Widget
 *
 * HOW TO INSTALL (send this to your client):
 * ──────────────────────────────────────────
 * In Shopify admin → Online Store → Themes → Edit code → theme.liquid
 * Paste this ONE line just before </body>:
 *
 *   <script src="https://ai-vintage-stylist.onrender.com/widget.js" data-ai-stylist async></script>
 *
 * That's it. The widget reads the shop URL automatically.
 */
(function () {
  'use strict';

  var me = document.querySelector('script[data-ai-stylist]');
  if (!me) return;

  var SERVER = new URL(me.src).origin;
  var cfg    = window.AIStylistConfig || {};
  var BTN_TEXT  = cfg.buttonText      || '✨ Find Your Style';
  var BTN_BG    = cfg.buttonColor     || '#111111';
  var BTN_FG    = cfg.buttonTextColor || '#ffffff';

  /* ─── state ─── */
  var phase    = 'idle';   // idle | loading | quiz | results | error
  var sid      = null;
  var quiz     = null;
  var shopName = '';
  var qIndex   = 0;
  var answers  = {};
  var recs     = null;
  var errMsg   = '';

  /* ─── shadow DOM refs ─── */
  var shadow, $title, $body;

  /* ─── CSS (inside shadow, no theme conflicts) ─── */
  var CSS = [
    '*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}',

    /* overlay */
    '.ov{position:fixed;inset:0;z-index:2147483646;background:rgba(0,0,0,.55);',
    'display:flex;align-items:center;justify-content:center;padding:16px;',
    'font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;',
    'opacity:0;transition:opacity .22s;pointer-events:none}',
    '.ov.open{opacity:1;pointer-events:all}',

    /* modal card */
    '.card{background:#fff;border-radius:18px;width:100%;max-width:450px;max-height:88vh;',
    'overflow-y:auto;box-shadow:0 20px 60px rgba(0,0,0,.35);',
    'transform:translateY(18px);transition:transform .28s}',
    '.ov.open .card{transform:translateY(0)}',

    /* header */
    '.hdr{padding:15px 18px;border-bottom:1px solid #eee;display:flex;',
    'align-items:center;justify-content:space-between;',
    'position:sticky;top:0;background:#fff;z-index:1;border-radius:18px 18px 0 0}',
    '.hdr-l{display:flex;flex-direction:column;gap:2px}',
    '.hdr-tag{font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:#b05e30;font-weight:700}',
    '.hdr-t{font-size:15px;font-weight:700;color:#111}',
    '.x-btn{width:28px;height:28px;border:none;background:#f0f0f0;border-radius:50%;',
    'cursor:pointer;font-size:15px;color:#555;display:flex;align-items:center;justify-content:center;flex-shrink:0}',
    '.x-btn:hover{background:#ddd}',

    /* body */
    '.bd{padding:22px 20px}',

    /* loading */
    '.load{text-align:center;padding:40px 0}',
    '.spin{width:38px;height:38px;border-radius:50%;border:3px solid #eee;border-top-color:#b05e30;',
    'animation:sp .8s linear infinite;margin:0 auto 16px}',
    '@keyframes sp{to{transform:rotate(360deg)}}',
    '.lt{font-size:16px;font-weight:700;color:#111;margin-bottom:6px}',
    '.ls{font-size:13px;color:#888;line-height:1.5}',

    /* progress */
    '.prog{height:3px;background:#eee;border-radius:2px;margin-bottom:18px}',
    '.prog-f{height:100%;background:#b05e30;border-radius:2px;transition:width .3s}',

    /* question */
    '.qstep{font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:#aaa;margin-bottom:4px}',
    '.qtxt{font-size:18px;font-weight:700;color:#111;line-height:1.35;margin-bottom:4px}',
    '.qhint{font-size:12px;color:#aaa;font-style:italic;margin-bottom:16px}',

    /* options */
    '.opts{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:20px}',
    '.opt{padding:12px 10px;border:1.5px solid #e0e0e0;border-radius:10px;background:#fafafa;',
    'cursor:pointer;text-align:left;font-size:13px;color:#222;',
    'display:flex;align-items:center;gap:8px;line-height:1.3;',
    'transition:border-color .15s,background .15s}',
    '.opt:hover{border-color:#b05e30;background:#fff5f0}',
    '.opt.on{border-color:#b05e30;background:#fff5f0;box-shadow:0 0 0 2px #b05e30}',
    '.em{font-size:20px;flex-shrink:0}',

    /* nav */
    '.nav{display:flex;align-items:center;justify-content:space-between}',
    '.nav-n{font-size:12px;color:#bbb}',
    '.btn{padding:10px 20px;border:none;border-radius:8px;cursor:pointer;',
    'font-size:13px;font-weight:700;transition:opacity .15s}',
    '.btn:disabled{opacity:.3;cursor:not-allowed}',
    '.btn-p{background:#111;color:#fff}.btn-p:hover:not(:disabled){background:#b05e30}',
    '.btn-g{background:transparent;color:#555;border:1.5px solid #ddd}.btn-g:hover{border-color:#aaa}',

    /* profile */
    '.prof{background:#111;color:#fff;border-radius:12px;padding:20px;margin-bottom:18px;text-align:center}',
    '.prof-tag{font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:#c9a84c;margin-bottom:3px}',
    '.prof-name{font-size:22px;font-weight:700;color:#c9a84c;margin-bottom:8px}',
    '.prof-desc{font-size:13px;color:rgba(255,255,255,.75);line-height:1.6}',

    /* products */
    '.sec{font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:#aaa;margin-bottom:10px}',
    '.prods{display:flex;flex-direction:column;gap:10px;margin-bottom:16px}',
    '.prod{display:flex;border:1px solid #eee;border-radius:10px;overflow:hidden;',
    'text-decoration:none;color:inherit;transition:box-shadow .2s}',
    '.prod:hover{box-shadow:0 4px 14px rgba(0,0,0,.1)}',
    '.pi{width:78px;flex-shrink:0;background:#f5f5f5}',
    '.pi img{width:100%;height:100%;object-fit:cover;display:block}',
    '.ph{width:100%;min-height:78px;display:flex;align-items:center;justify-content:center;font-size:22px;opacity:.3}',
    '.pinfo{padding:10px 12px;flex:1}',
    '.pname{font-size:14px;font-weight:600;color:#111;margin-bottom:2px}',
    '.pprice{font-size:13px;color:#b05e30;font-weight:600;margin-bottom:4px}',
    '.pwhy{font-size:12px;color:#777;line-height:1.5;margin-bottom:5px}',
    '.pmatch{font-size:10px;background:#111;color:#c9a84c;padding:2px 7px;border-radius:20px;display:inline-block}',

    /* tip */
    '.tip{background:#fff5f0;border-left:3px solid #b05e30;border-radius:8px;padding:12px 14px;',
    'margin-bottom:16px;font-size:13px;color:#555;line-height:1.6}',
    '.tip b{color:#b05e30;display:block;font-size:10px;letter-spacing:.08em;text-transform:uppercase;margin-bottom:3px}',

    /* restart */
    '.restart{text-align:center;padding-top:2px}',
    '.rbtn{background:none;border:none;color:#bbb;font-size:12px;cursor:pointer;text-decoration:underline}',
    '.rbtn:hover{color:#b05e30}',

    /* error */
    '.err-box{text-align:center;padding:36px 10px}',
    '.err-i{font-size:34px;margin-bottom:12px}',
    '.err-t{font-size:17px;font-weight:700;color:#111;margin-bottom:7px}',
    '.err-m{font-size:13px;color:#888;line-height:1.55;margin-bottom:20px}',

    '@media(max-width:500px){',
    '.ov{align-items:flex-end;padding:0}',
    '.card{border-radius:18px 18px 0 0;max-height:92vh}',
    '.opts{grid-template-columns:1fr}}',
  ].join('');

  /* ─── helpers ─── */
  function e(s) {
    return (s || '')
      .replace(/&/g, '&amp;').replace(/</g, '&lt;')
      .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  async function post(path, body) {
    var ac = new AbortController();
    var t  = setTimeout(function () { ac.abort(); }, 120000);
    try {
      var r = await fetch(SERVER + path, {
        method:  'POST',
        headers: { 'Content-Type': 'application/json' },
        body:    JSON.stringify(body),
        signal:  ac.signal,
      });
      var data = await r.json();
      if (!r.ok) throw new Error(data.detail || 'Server error');
      return data;
    } catch (err) {
      if (err.name === 'AbortError') throw new Error('The server is waking up — please try again in a moment.');
      throw err;
    } finally {
      clearTimeout(t);
    }
  }

  /* ─── render ─── */
  function setTitle(t) { $title.textContent = t; }

  function showLoading(title, sub) {
    $body.innerHTML =
      '<div class="load">' +
      '<div class="spin"></div>' +
      '<div class="lt">' + e(title) + '</div>' +
      '<div class="ls">' + e(sub)   + '</div>' +
      '</div>';
  }

  function showError(msg) {
    setTitle('AI Stylist');
    $body.innerHTML =
      '<div class="err-box">' +
      '<div class="err-i">😕</div>' +
      '<div class="err-t">Something went wrong</div>' +
      '<div class="err-m">' + e(msg) + '</div>' +
      '<button class="btn btn-p" id="w-retry">↺ Try Again</button>' +
      '</div>';
    shadow.getElementById('w-retry').onclick = function () { runAnalysis(); };
  }

  function showQuestion() {
    var q   = quiz.questions[qIndex];
    var tot = quiz.questions.length;
    var pct = Math.round(((qIndex + 1) / tot) * 100);
    var sel = answers[q.id];
    var last = qIndex === tot - 1;

    setTitle(shopName ? shopName + ' · Quiz' : 'Style Quiz');

    $body.innerHTML =
      '<div class="prog"><div class="prog-f" style="width:' + pct + '%"></div></div>' +
      '<div class="qstep">Question ' + (qIndex + 1) + ' of ' + tot + '</div>' +
      '<div class="qtxt">' + e(q.question) + '</div>' +
      (q.context_hint ? '<div class="qhint">' + e(q.context_hint) + '</div>' : '') +
      '<div class="opts">' +
      q.options.map(function (o) {
        return '<button class="opt' + (sel === o.id ? ' on' : '') + '" data-id="' + e(o.id) + '">' +
          (o.emoji ? '<span class="em">' + o.emoji + '</span>' : '') +
          '<span>' + e(o.text) + '</span></button>';
      }).join('') +
      '</div>' +
      '<div class="nav">' +
      '<button class="btn btn-g" id="w-prev"' + (qIndex === 0 ? ' style="visibility:hidden"' : '') + '>← Back</button>' +
      '<span class="nav-n">' + (qIndex + 1) + ' / ' + tot + '</span>' +
      '<button class="btn btn-p" id="w-next"' + (sel ? '' : ' disabled') + '>' + (last ? 'See my picks →' : 'Next →') + '</button>' +
      '</div>';

    shadow.querySelectorAll('.opt').forEach(function (btn) {
      btn.onclick = function () {
        answers[q.id] = btn.dataset.id;
        shadow.querySelectorAll('.opt').forEach(function (b) { b.classList.toggle('on', b === btn); });
        shadow.getElementById('w-next').removeAttribute('disabled');
      };
    });

    shadow.getElementById('w-next').onclick = function () {
      if (qIndex < quiz.questions.length - 1) { qIndex++; showQuestion(); }
      else runRecommendations();
    };
    var prev = shadow.getElementById('w-prev');
    if (prev) prev.onclick = function () { if (qIndex > 0) { qIndex--; showQuestion(); } };
  }

  function showResults(data) {
    phase = 'results';
    recs  = data;
    setTitle('Your Picks ✦');
    var items = (data.recommendations || []);

    $body.innerHTML =
      '<div class="prof">' +
      '<div class="prof-tag">Your style is…</div>' +
      '<div class="prof-name">' + e(data.style_profile_title || 'Uniquely You') + '</div>' +
      '<div class="prof-desc">' + e(data.style_profile || '') + '</div>' +
      '</div>' +
      '<div class="sec">Picked for you</div>' +
      '<div class="prods">' +
      items.map(function (r) {
        return '<a class="prod" href="' + e(r.product_url || '#') + '" target="_blank" rel="noopener">' +
          '<div class="pi">' +
          (r.product_image ? '<img src="' + e(r.product_image) + '" alt="' + e(r.product_name) + '" loading="lazy">' : '<div class="ph">👗</div>') +
          '</div>' +
          '<div class="pinfo">' +
          '<div class="pname">' + e(r.product_name) + '</div>' +
          (r.product_price ? '<div class="pprice">' + e(r.product_price) + '</div>' : '') +
          (r.match_score   ? '<span class="pmatch">' + r.match_score + '% match</span>' : '') +
          '<div class="pwhy">' + e(r.why_for_you) + '</div>' +
          '</div></a>';
      }).join('') +
      '</div>' +
      (data.styling_tip ? '<div class="tip"><b>Stylist Tip</b>' + e(data.styling_tip) + '</div>' : '') +
      '<div class="restart"><button class="rbtn" id="w-restart">↺ Retake quiz</button></div>';

    shadow.getElementById('w-restart').onclick = function () {
      phase  = 'quiz'; qIndex = 0; answers = {};
      showQuestion();
    };
  }

  /* ─── API calls ─── */
  async function runAnalysis() {
    phase = 'loading';
    setTitle('AI Stylist');
    showLoading('Analysing this store…', 'Building your personalised quiz. Takes ~30 s on first visit.');

    var tip = setTimeout(function () {
      if (phase === 'loading') showLoading('Almost there…', 'Server is waking up — hang tight!');
    }, 25000);

    try {
      var data = await post('/api/shop/analyze', { shop_domain: window.location.hostname });
      clearTimeout(tip);
      sid      = data.session_id;
      quiz     = data.quiz;
      shopName = data.shop_name || '';
      phase    = 'quiz';
      qIndex   = 0;
      answers  = {};
      showQuestion();
    } catch (err) {
      clearTimeout(tip);
      phase = 'error';
      showError(err.message);
    }
  }

  async function runRecommendations() {
    phase = 'loading';
    setTitle('AI Stylist');
    showLoading('Finding your picks…', 'Matching your taste to the collection');
    try {
      var data = await post('/api/shop/recommendations', { session_id: sid, answers: answers });
      showResults(data);
    } catch (err) {
      phase = 'error';
      showError(err.message);
    }
  }

  /* ─── build DOM ─── */
  function buildDOM() {
    /* floating button */
    var btn = document.createElement('button');
    Object.assign(btn.style, {
      position: 'fixed', bottom: '22px', right: '22px', zIndex: '2147483645',
      padding: '13px 22px', background: BTN_BG, color: BTN_FG,
      border: 'none', borderRadius: '50px',
      fontFamily: 'inherit', fontSize: '14px', fontWeight: '700',
      cursor: 'pointer', boxShadow: '0 4px 18px rgba(0,0,0,.3)',
      transition: 'transform .2s, box-shadow .2s', letterSpacing: '.01em',
    });
    btn.textContent = BTN_TEXT;
    btn.addEventListener('mouseover', function () { btn.style.transform = 'translateY(-2px)'; btn.style.boxShadow = '0 7px 24px rgba(0,0,0,.38)'; });
    btn.addEventListener('mouseout',  function () { btn.style.transform = ''; btn.style.boxShadow = '0 4px 18px rgba(0,0,0,.3)'; });
    btn.addEventListener('click', openModal);
    document.body.appendChild(btn);

    /* shadow host */
    var host = document.createElement('div');
    document.body.appendChild(host);
    shadow = host.attachShadow({ mode: 'open' });

    var style = document.createElement('style');
    style.textContent = CSS;
    shadow.appendChild(style);

    /* overlay + card */
    var ov = document.createElement('div');
    ov.className = 'ov';
    ov.id = 'w-ov';
    ov.addEventListener('click', function (ev) { if (ev.target === ov) closeModal(); });

    var card = document.createElement('div');
    card.className = 'card';

    card.innerHTML =
      '<div class="hdr">' +
      '<div class="hdr-l"><span class="hdr-tag">✦ AI Stylist</span><span class="hdr-t" id="w-title">Style Quiz</span></div>' +
      '<button class="x-btn" id="w-close">✕</button>' +
      '</div>' +
      '<div class="bd" id="w-body"></div>';

    ov.appendChild(card);
    shadow.appendChild(ov);

    $title = shadow.getElementById('w-title');
    $body  = shadow.getElementById('w-body');
    shadow.getElementById('w-close').onclick = closeModal;
  }

  function openModal() {
    shadow.getElementById('w-ov').classList.add('open');
    document.body.style.overflow = 'hidden';

    if      (phase === 'idle')    runAnalysis();
    else if (phase === 'quiz')    showQuestion();
    else if (phase === 'results') { /* already rendered */ }
    else if (phase === 'error')   showError(errMsg);
    /* if loading: modal is already showing the spinner */
  }

  function closeModal() {
    shadow.getElementById('w-ov').classList.remove('open');
    document.body.style.overflow = '';
  }

  /* ─── start ─── */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', buildDOM);
  } else {
    buildDOM();
  }

})();
