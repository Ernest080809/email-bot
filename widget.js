/**
 * AI Vintage Stylist — Embeddable Widget for novalife.store
 *
 * Install: paste this ONE line just before </body> in theme.liquid
 *
 *   <script src="https://ai-vintage-stylist.onrender.com/widget.js" data-ai-stylist async></script>
 *
 * This build is pinned to novalife.store — it does not detect or analyse
 * any other domain. Analysis starts the moment the page loads (in the
 * background) so the quiz is usually ready instantly by the time someone
 * clicks the button.
 */
(function () {
  'use strict';

  var me = document.querySelector('script[data-ai-stylist]');
  if (!me) return;

  var SERVER      = new URL(me.src).origin;
  var SHOP_DOMAIN = 'novalife.store';   // ← hardcoded, this build is only for this store

  var cfg      = window.AIStylistConfig || {};
  var BTN_TEXT = cfg.buttonText      || '✨ Find Your Style';
  var BTN_BG   = cfg.buttonColor     || '#111';
  var BTN_FG   = cfg.buttonTextColor || '#fff';

  /* ── state ── */
  var phase = 'idle';   // idle | loading | quiz | results | error
  var sid = null, quiz = null, shopName = '';
  var qIdx = 0, answers = {};
  var pendingOpen = false;   // true if user clicked while the pre-load was still running
  var errMsg = '';

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

  /* ── overlay (100% inline styles, no CSS file dependency, no Shadow DOM) ── */
  var overlayEl = document.createElement('div');
  overlayEl.id = 'ais-overlay';
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

  /* ── dom shortcuts ── */
  function $title() { return document.getElementById('ais-title'); }
  function $body()  { return document.getElementById('ais-body');  }

  /* ── modal open/close ── */
  function openModal() {
    overlayEl.style.display = 'flex';
    document.body.style.overflow = 'hidden';

    if (phase === 'idle' || phase === 'loading') {
      pendingOpen = true;
      renderLoading('Loading your style quiz…', 'Just a moment');
    } else if (phase === 'quiz') {
      renderQuestion();
    } else if (phase === 'error') {
      renderError(errMsg);
    }
    /* results: already rendered, nothing to do */
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
    } catch (e) {
      if (e.name === 'AbortError') throw new Error('Server is waking up — please try again.');
      throw e;
    } finally {
      clearTimeout(t);
    }
  }

  /* ── views ── */
  function setTitle(t) { $title().textContent = t; }

  function renderLoading(title, sub) {
    setTitle('AI Stylist');
    $body().innerHTML = [
      '<div style="text-align:center;padding:40px 0">',
      '<div style="width:38px;height:38px;border-radius:50%;border:3px solid #eee;border-top-color:#b05e30;animation:ais-spin .8s linear infinite;margin:0 auto 16px"></div>',
      '<div style="font-size:16px;font-weight:700;color:#111;margin-bottom:8px">' + esc(title) + '</div>',
      '<div style="font-size:13px;color:#888;line-height:1.5">' + esc(sub) + '</div>',
      '</div>',
    ].join('');
    if (!document.getElementById('ais-spin-kf')) {
      var kf = document.createElement('style');
      kf.id = 'ais-spin-kf';
      kf.textContent = '@keyframes ais-spin{to{transform:rotate(360deg)}}';
      document.head.appendChild(kf);
    }
  }

  function renderError(msg) {
    setTitle('AI Stylist');
    var m = msg || 'Could not load quiz. Please try again.';
    $body().innerHTML = [
      '<div style="text-align:center;padding:36px 10px">',
      '<div style="font-size:34px;margin-bottom:12px">😕</div>',
      '<div style="font-size:17px;font-weight:700;margin-bottom:8px">Something went wrong</div>',
      '<div style="font-size:13px;color:#888;line-height:1.55;margin-bottom:20px">' + esc(m) + '</div>',
      '<button id="ais-retry" style="padding:10px 20px;border:none;border-radius:8px;cursor:pointer;font-size:13px;font-weight:700;background:#111;color:#fff;font-family:inherit">↺ Try Again</button>',
      '</div>',
    ].join('');
    document.getElementById('ais-retry').onclick = function () {
      phase = 'idle';
      pendingOpen = true;
      renderLoading('Loading your style quiz…', 'Just a moment');
      runAnalysis();
    };
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
      'Question ' + (qIdx + 1) + ' of ' + tot + '</div>',
      '<div style="font-size:18px;font-weight:700;color:#111;line-height:1.35;margin-bottom:' + (q.context_hint ? '4px' : '16px') + '">',
      esc(q.question) + '</div>',
      q.context_hint ? '<div style="font-size:12px;color:#aaa;font-style:italic;margin-bottom:16px">' + esc(q.context_hint) + '</div>' : '',
      '<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:20px">',
      q.options.map(function (o) {
        var sty = 'padding:12px 10px;border:1.5px solid ' + (sel === o.id ? '#b05e30' : '#e0e0e0') +
          ';border-radius:10px;background:' + (sel === o.id ? '#fff5f0' : '#fafafa') +
          ';cursor:pointer;text-align:left;font-size:13px;color:#222;display:flex;align-items:center;gap:8px;' +
          'line-height:1.3;width:100%;box-sizing:border-box;font-family:inherit;' +
          (sel === o.id ? 'box-shadow:0 0 0 2px #b05e30;' : '');
        return '<button class="ais-opt" data-id="' + esc(o.id) + '" style="' + sty + '">' +
          (o.emoji ? '<span style="font-size:20px;flex-shrink:0">' + o.emoji + '</span>' : '') +
          '<span>' + esc(o.text) + '</span></button>';
      }).join(''),
      '</div>',
      '<div style="display:flex;align-items:center;justify-content:space-between">',
      '<button id="ais-prev" style="padding:10px 20px;border:1.5px solid #ddd;border-radius:8px;cursor:pointer;font-size:13px;font-weight:700;background:transparent;color:#555;font-family:inherit' + (qIdx === 0 ? ';visibility:hidden' : '') + '">← Back</button>',
      '<span style="font-size:12px;color:#bbb">' + (qIdx + 1) + ' / ' + tot + '</span>',
      '<button id="ais-next" style="padding:10px 20px;border:none;border-radius:8px;cursor:pointer;font-size:13px;font-weight:700;background:#111;color:#fff;font-family:inherit' + (sel ? '' : ';opacity:.3;cursor:not-allowed') + '"' + (sel ? '' : ' disabled') + '>' +
        (qIdx === tot - 1 ? 'See my picks →' : 'Next →') + '</button>',
      '</div>',
    ].join('');

    document.querySelectorAll('.ais-opt').forEach(function (btn) {
      btn.onclick = function () {
        answers[q.id] = btn.dataset.id;
        renderQuestion();
      };
    });

    document.getElementById('ais-next').onclick = function () {
      if (qIdx < quiz.questions.length - 1) { qIdx++; renderQuestion(); }
      else runRecommendations();
    };
    var prev = document.getElementById('ais-prev');
    if (prev) prev.onclick = function () { if (qIdx > 0) { qIdx--; renderQuestion(); } };
  }

  function renderResults(data) {
    phase = 'results';
    setTitle('Your Picks ✦');
    var items = data.recommendations || [];

    $body().innerHTML = [
      '<div style="background:#111;color:#fff;border-radius:12px;padding:20px;margin-bottom:18px;text-align:center">',
      '<div style="font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:#c9a84c;margin-bottom:3px">Your style is…</div>',
      '<div style="font-size:22px;font-weight:700;color:#c9a84c;margin-bottom:8px">' + esc(data.style_profile_title || 'Uniquely You') + '</div>',
      '<div style="font-size:13px;color:rgba(255,255,255,.75);line-height:1.6">' + esc(data.style_profile || '') + '</div>',
      '</div>',
      '<div style="font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:#aaa;margin-bottom:10px">Picked for you</div>',
      items.map(function (r) {
        return '<a href="' + esc(r.product_url || '#') + '" target="_blank" rel="noopener" style="display:flex;border:1px solid #eee;border-radius:10px;overflow:hidden;text-decoration:none;color:inherit;margin-bottom:10px;background:#fff">' +
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

    document.getElementById('ais-restart').onclick = function () {
      phase = 'quiz'; qIdx = 0; answers = {};
      renderQuestion();
    };
  }

  /* ── API calls ── */
  async function runAnalysis() {
    phase = 'loading';
    try {
      var data = await post('/api/shop/analyze', { shop_domain: SHOP_DOMAIN });
      sid = data.session_id;
      quiz = data.quiz;
      shopName = data.shop_name || '';
      phase = 'quiz';
      qIdx = 0;
      answers = {};
      if (pendingOpen) { pendingOpen = false; renderQuestion(); }
    } catch (e) {
      phase = 'error';
      errMsg = e.message;
      if (pendingOpen) { pendingOpen = false; renderError(errMsg); }
    }
  }

  async function runRecommendations() {
    phase = 'loading';
    renderLoading('Finding your picks…', 'Matching your style to the collection');
    try {
      var data = await post('/api/shop/recommendations', { session_id: sid, answers: answers });
      renderResults(data);
    } catch (e) {
      phase = 'error';
      errMsg = e.message;
      renderError(errMsg);
    }
  }

  /* ── pre-warm: start analysing novalife.store the instant the page loads ── */
  runAnalysis();

})();
