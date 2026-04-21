/**
 * AI Vintage Stylist Widget
 * ─────────────────────────
 * Install in Shopify: Online Store → Themes → Edit code → theme.liquid
 * Paste just before </body>:
 *
 *   <script src="https://ai-vintage-stylist.onrender.com/widget.js"
 *           data-ai-stylist async></script>
 *
 * Optional config (paste ABOVE the script tag):
 *   <script>
 *     window.AIStylistConfig = {
 *       buttonText:  'Find My Style ✨',
 *       buttonColor: '#000000',
 *     };
 *   </script>
 */
(function () {
  'use strict';

  const scriptEl = document.querySelector('script[data-ai-stylist]');
  if (!scriptEl) return;

  const API_BASE = new URL(scriptEl.src).origin;
  const cfg      = window.AIStylistConfig || {};
  const BTN_TEXT = cfg.buttonText  || '✨ Find Your Style';
  const BTN_BG   = cfg.buttonColor || '#1a1a1a';
  const BTN_FG   = cfg.buttonTextColor || '#ffffff';

  /* ── State ── */
  let phase      = 'idle';   // idle | loading | quiz | results | error
  let sessionId  = null;
  let quiz       = null;
  let shopName   = '';
  let currentQ   = 0;
  let answers    = {};
  let shadow     = null;

  /* ── CSS ── */
  const CSS = `
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    .overlay {
      position: fixed; inset: 0; z-index: 2147483646;
      background: rgba(0,0,0,0.6);
      display: flex; align-items: center; justify-content: center;
      padding: 16px;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      opacity: 0; transition: opacity .25s;
      pointer-events: none;
    }
    .overlay.on { opacity: 1; pointer-events: all; }

    .modal {
      background: #fff; border-radius: 16px;
      width: 100%; max-width: 460px; max-height: 90vh;
      overflow-y: auto;
      box-shadow: 0 20px 60px rgba(0,0,0,.35);
      transform: translateY(20px); transition: transform .3s;
    }
    .overlay.on .modal { transform: translateY(0); }

    /* header */
    .hdr {
      padding: 16px 20px;
      border-bottom: 1px solid #eee;
      display: flex; align-items: center; justify-content: space-between;
      position: sticky; top: 0; background: #fff; z-index: 1;
      border-radius: 16px 16px 0 0;
    }
    .hdr-left { display: flex; flex-direction: column; gap: 1px; }
    .hdr-eyebrow { font-size: 11px; letter-spacing: .12em; text-transform: uppercase; color: #b05e30; font-weight: 600; }
    .hdr-title { font-size: 15px; font-weight: 700; color: #111; }
    .hdr-close {
      width: 28px; height: 28px; border: none; background: #f0f0f0;
      border-radius: 50%; cursor: pointer; font-size: 16px;
      display: flex; align-items: center; justify-content: center; color: #555;
      flex-shrink: 0;
    }
    .hdr-close:hover { background: #ddd; }

    /* body */
    .body { padding: 22px 20px; }

    /* loading */
    .loading { text-align: center; padding: 40px 0; }
    .spinner {
      width: 40px; height: 40px; border-radius: 50%;
      border: 3px solid #eee; border-top-color: #b05e30;
      animation: spin .8s linear infinite; margin: 0 auto 18px;
    }
    @keyframes spin { to { transform: rotate(360deg); } }
    .load-title { font-size: 17px; font-weight: 700; color: #111; margin-bottom: 7px; }
    .load-sub { font-size: 13px; color: #888; line-height: 1.5; }

    /* progress bar */
    .progress { height: 3px; background: #eee; border-radius: 2px; margin-bottom: 20px; }
    .progress-fill { height: 100%; background: #b05e30; border-radius: 2px; transition: width .35s; }

    /* quiz */
    .q-step { font-size: 11px; letter-spacing: .1em; text-transform: uppercase; color: #999; margin-bottom: 5px; }
    .q-text { font-size: 18px; font-weight: 700; color: #111; line-height: 1.35; margin-bottom: 5px; }
    .q-hint { font-size: 12px; color: #999; font-style: italic; margin-bottom: 18px; }

    .options { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 20px; }
    .opt {
      padding: 12px 10px; border: 1.5px solid #e0e0e0; border-radius: 10px;
      background: #fafafa; cursor: pointer; text-align: left;
      font-size: 13px; color: #222; display: flex; align-items: center; gap: 8px;
      transition: border-color .15s, background .15s; line-height: 1.3;
    }
    .opt:hover { border-color: #b05e30; background: #fff5f0; }
    .opt.sel { border-color: #b05e30; background: #fff5f0; box-shadow: 0 0 0 2px #b05e30; }
    .opt-emoji { font-size: 20px; flex-shrink: 0; }

    .nav { display: flex; align-items: center; justify-content: space-between; }
    .nav-info { font-size: 12px; color: #aaa; }
    .btn {
      padding: 10px 20px; border: none; border-radius: 8px; cursor: pointer;
      font-size: 13px; font-weight: 700; transition: opacity .15s;
    }
    .btn:disabled { opacity: .35; cursor: not-allowed; }
    .btn-primary { background: #111; color: #fff; }
    .btn-primary:hover:not(:disabled) { background: #b05e30; }
    .btn-ghost { background: transparent; color: #555; border: 1.5px solid #ddd; }
    .btn-ghost:hover { border-color: #aaa; }

    /* results */
    .profile {
      background: #111; color: #fff; border-radius: 12px;
      padding: 20px; margin-bottom: 20px; text-align: center;
    }
    .profile-label { font-size: 11px; letter-spacing: .12em; text-transform: uppercase; color: #c9a84c; margin-bottom: 4px; }
    .profile-name { font-size: 22px; font-weight: 700; color: #c9a84c; margin-bottom: 8px; }
    .profile-desc { font-size: 13px; color: rgba(255,255,255,.75); line-height: 1.6; }

    .section-title { font-size: 11px; letter-spacing: .1em; text-transform: uppercase; color: #999; margin-bottom: 12px; }

    .products { display: flex; flex-direction: column; gap: 10px; margin-bottom: 18px; }
    .prod {
      display: flex; border: 1px solid #eee; border-radius: 10px; overflow: hidden;
      text-decoration: none; color: inherit; transition: box-shadow .2s;
    }
    .prod:hover { box-shadow: 0 4px 14px rgba(0,0,0,.1); }
    .prod-img-wrap { width: 80px; flex-shrink: 0; background: #f5f5f5; }
    .prod-img { width: 100%; height: 100%; object-fit: cover; display: block; }
    .prod-placeholder { width: 100%; min-height: 80px; display: flex; align-items: center; justify-content: center; font-size: 24px; opacity: .3; }
    .prod-info { padding: 11px 13px; flex: 1; }
    .prod-name { font-size: 14px; font-weight: 600; margin-bottom: 2px; color: #111; }
    .prod-price { font-size: 13px; color: #b05e30; font-weight: 600; margin-bottom: 5px; }
    .prod-why { font-size: 12px; color: #777; line-height: 1.5; margin-bottom: 6px; }
    .prod-match { display: inline-block; font-size: 10px; background: #111; color: #c9a84c; padding: 2px 7px; border-radius: 20px; }

    .tip {
      background: #f9f0eb; border-left: 3px solid #b05e30;
      border-radius: 8px; padding: 13px 15px; margin-bottom: 18px;
      font-size: 13px; color: #555; line-height: 1.6;
    }
    .tip strong { color: #b05e30; display: block; margin-bottom: 3px; font-size: 11px; letter-spacing: .08em; text-transform: uppercase; }

    .restart-row { text-align: center; padding-top: 4px; }
    .restart-btn { background: none; border: none; color: #aaa; font-size: 12px; cursor: pointer; text-decoration: underline; }
    .restart-btn:hover { color: #b05e30; }

    /* error */
    .err-box { text-align: center; padding: 36px 10px; }
    .err-icon { font-size: 36px; margin-bottom: 14px; }
    .err-title { font-size: 17px; font-weight: 700; margin-bottom: 8px; color: #111; }
    .err-msg { font-size: 13px; color: #888; line-height: 1.55; margin-bottom: 22px; }

    @media (max-width: 500px) {
      .overlay { align-items: flex-end; padding: 0; }
      .modal { border-radius: 16px 16px 0 0; max-height: 92vh; }
      .options { grid-template-columns: 1fr; }
    }
  `;

  /* ── helpers ── */
  function esc(s) {
    return (s || '').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
  }

  async function apiPost(path, body) {
    const ctrl  = new AbortController();
    const timer = setTimeout(() => ctrl.abort(), 90000); // 90s to survive cold start
    try {
      const r    = await fetch(API_BASE + path, {
        method:  'POST',
        headers: { 'Content-Type': 'application/json' },
        body:    JSON.stringify(body),
        signal:  ctrl.signal,
      });
      const data = await r.json();
      if (!r.ok) throw new Error(data.detail || 'Server error');
      return data;
    } catch (e) {
      if (e.name === 'AbortError') throw new Error('The server is taking too long. Please try again — it should be faster now.');
      throw e;
    } finally {
      clearTimeout(timer);
    }
  }

  /* ── Build DOM ── */
  let overlay, modal, hdrTitle, body;

  function build() {
    /* floating trigger button */
    const trigger = document.createElement('button');
    trigger.id = 'ais-btn';
    Object.assign(trigger.style, {
      position: 'fixed', bottom: '22px', right: '22px',
      zIndex: '2147483645',
      padding: '13px 22px',
      background: BTN_BG, color: BTN_FG,
      border: 'none', borderRadius: '50px',
      fontFamily: 'inherit', fontSize: '14px', fontWeight: '700',
      cursor: 'pointer', letterSpacing: '.01em',
      boxShadow: '0 4px 18px rgba(0,0,0,.3)',
      transition: 'transform .2s, box-shadow .2s',
    });
    trigger.textContent = BTN_TEXT;
    trigger.addEventListener('mouseover', () => { trigger.style.transform = 'translateY(-2px)'; trigger.style.boxShadow = '0 7px 24px rgba(0,0,0,.38)'; });
    trigger.addEventListener('mouseout',  () => { trigger.style.transform = ''; trigger.style.boxShadow = '0 4px 18px rgba(0,0,0,.3)'; });
    trigger.addEventListener('click', open);
    document.body.appendChild(trigger);

    /* shadow host */
    const host = document.createElement('div');
    document.body.appendChild(host);
    shadow = host.attachShadow({ mode: 'open' });

    const styleEl = document.createElement('style');
    styleEl.textContent = CSS;
    shadow.appendChild(styleEl);

    overlay = document.createElement('div');
    overlay.className = 'overlay';
    overlay.addEventListener('click', e => { if (e.target === overlay) close(); });

    modal = document.createElement('div');
    modal.className = 'modal';
    modal.setAttribute('role', 'dialog');

    modal.innerHTML = `
      <div class="hdr">
        <div class="hdr-left">
          <span class="hdr-eyebrow">✦ AI Stylist</span>
          <span class="hdr-title" id="ais-title">Style Quiz</span>
        </div>
        <button class="hdr-close" id="ais-close">✕</button>
      </div>
      <div class="body" id="ais-body"></div>
    `;

    overlay.appendChild(modal);
    shadow.appendChild(overlay);

    hdrTitle = shadow.getElementById('ais-title');
    body     = shadow.getElementById('ais-body');
    shadow.getElementById('ais-close').addEventListener('click', close);
  }

  function open() {
    overlay.classList.add('on');
    document.body.style.overflow = 'hidden';
    if      (phase === 'idle')    startAnalysis();
    else if (phase === 'quiz')    renderQuestion();
    else if (phase === 'results') { /* already rendered */ }
    else if (phase === 'error')   renderError();
  }

  function close() {
    overlay.classList.remove('on');
    document.body.style.overflow = '';
  }

  /* ── Views ── */
  function renderLoading(title, sub) {
    hdrTitle.textContent = 'AI Stylist';
    body.innerHTML = `
      <div class="loading">
        <div class="spinner"></div>
        <div class="load-title">${esc(title)}</div>
        <div class="load-sub">${esc(sub)}</div>
      </div>
    `;
  }

  function renderError(msg) {
    const message = msg || 'Could not load the quiz. Please try again.';
    hdrTitle.textContent = 'AI Stylist';
    body.innerHTML = `
      <div class="err-box">
        <div class="err-icon">😕</div>
        <div class="err-title">Something went wrong</div>
        <div class="err-msg">${esc(message)}</div>
        <button class="btn btn-primary" id="ais-retry">↺ Try Again</button>
      </div>
    `;
    shadow.getElementById('ais-retry').addEventListener('click', () => {
      phase = 'idle';
      startAnalysis();
    });
  }

  function renderQuestion() {
    const q   = quiz.questions[currentQ];
    const tot = quiz.questions.length;
    const pct = Math.round(((currentQ + 1) / tot) * 100);
    const sel = answers[q.id];

    hdrTitle.textContent = shopName ? shopName + ' · Quiz' : 'Style Quiz';

    body.innerHTML = `
      <div class="progress"><div class="progress-fill" style="width:${pct}%"></div></div>
      <div class="q-step">Question ${currentQ + 1} of ${tot}</div>
      <div class="q-text">${esc(q.question)}</div>
      ${q.context_hint ? `<div class="q-hint">${esc(q.context_hint)}</div>` : ''}
      <div class="options">
        ${q.options.map(o => `
          <button class="opt${sel === o.id ? ' sel' : ''}" data-id="${esc(o.id)}">
            ${o.emoji ? `<span class="opt-emoji">${o.emoji}</span>` : ''}
            <span>${esc(o.text)}</span>
          </button>
        `).join('')}
      </div>
      <div class="nav">
        <button class="btn btn-ghost" id="ais-prev" ${currentQ === 0 ? 'style="visibility:hidden"' : ''}>← Back</button>
        <span class="nav-info">${currentQ + 1} / ${tot}</span>
        <button class="btn btn-primary" id="ais-next" ${sel ? '' : 'disabled'}>
          ${currentQ === tot - 1 ? 'See my picks →' : 'Next →'}
        </button>
      </div>
    `;

    shadow.querySelectorAll('.opt').forEach(btn => {
      btn.addEventListener('click', () => {
        answers[q.id] = btn.dataset.id;
        shadow.querySelectorAll('.opt').forEach(b => b.classList.toggle('sel', b === btn));
        shadow.getElementById('ais-next').removeAttribute('disabled');
      });
    });

    shadow.getElementById('ais-next').addEventListener('click', async () => {
      if (currentQ < quiz.questions.length - 1) {
        currentQ++;
        renderQuestion();
      } else {
        await submitAnswers();
      }
    });

    const prev = shadow.getElementById('ais-prev');
    if (prev) prev.addEventListener('click', () => { if (currentQ > 0) { currentQ--; renderQuestion(); } });
  }

  function renderResults(data) {
    phase = 'results';
    hdrTitle.textContent = 'Your Picks ✦';
    const recs = data.recommendations || [];

    const prods = recs.map(r => `
      <a class="prod" href="${esc(r.product_url || '#')}" target="_blank" rel="noopener">
        <div class="prod-img-wrap">
          ${r.product_image
            ? `<img class="prod-img" src="${esc(r.product_image)}" alt="${esc(r.product_name)}" loading="lazy">`
            : `<div class="prod-placeholder">👗</div>`}
        </div>
        <div class="prod-info">
          <div class="prod-name">${esc(r.product_name)}</div>
          ${r.product_price ? `<div class="prod-price">${esc(r.product_price)}</div>` : ''}
          ${r.match_score   ? `<div class="prod-match">${r.match_score}% match</div>` : ''}
          <div class="prod-why">${esc(r.why_for_you)}</div>
        </div>
      </a>
    `).join('');

    body.innerHTML = `
      <div class="profile">
        <div class="profile-label">Your style is…</div>
        <div class="profile-name">${esc(data.style_profile_title || 'Uniquely You')}</div>
        <div class="profile-desc">${esc(data.style_profile || '')}</div>
      </div>
      <div class="section-title">Picked for you from ${esc(shopName || 'the store')}</div>
      <div class="products">${prods}</div>
      ${data.styling_tip ? `
        <div class="tip">
          <strong>Stylist tip</strong>
          ${esc(data.styling_tip)}
        </div>
      ` : ''}
      <div class="restart-row">
        <button class="restart-btn" id="ais-restart">↺ Retake quiz</button>
      </div>
    `;

    shadow.getElementById('ais-restart').addEventListener('click', () => {
      phase     = 'quiz';
      currentQ  = 0;
      answers   = {};
      renderQuestion();
    });
  }

  /* ── API flow ── */
  async function startAnalysis() {
    phase = 'loading';
    renderLoading(
      'Analysing this store…',
      'Reading the collection and building your quiz. First visit takes ~30 seconds.'
    );

    // Update message after 20s so user knows it's still working
    const tip = setTimeout(() => {
      if (phase === 'loading') {
        renderLoading('Still working…', 'The server is waking up. Almost there — hang tight!');
      }
    }, 20000);

    try {
      const data = await apiPost('/api/shop/analyze', {
        shop_domain: window.location.hostname,
      });
      clearTimeout(tip);
      sessionId = data.session_id;
      quiz      = data.quiz;
      shopName  = data.shop_name || '';
      phase     = 'quiz';
      currentQ  = 0;
      answers   = {};
      renderQuestion();
    } catch (e) {
      clearTimeout(tip);
      phase = 'error';
      renderError(e.message);
    }
  }

  async function submitAnswers() {
    phase = 'loading';
    renderLoading('Finding your picks…', 'Matching your style to the collection');
    try {
      const data = await apiPost('/api/shop/recommendations', {
        session_id: sessionId,
        answers:    answers,
      });
      renderResults(data);
    } catch (e) {
      phase = 'error';
      renderError(e.message);
    }
  }

  /* ── Init ── */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', build);
  } else {
    build();
  }
})();
