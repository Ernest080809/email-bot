/**
 * AI Vintage Stylist – Embeddable Shopify Widget
 * ───────────────────────────────────────────────
 * How store owners install it (one snippet into Shopify → Online Store
 * → Themes → Edit code → theme.liquid, just before </body>):
 *
 *   <!-- Optional: customise the button -->
 *   <script>
 *     window.AIStylistConfig = {
 *       buttonText:      'Find My Style ✨',   // default shown below
 *       buttonColor:     '#2c2825',
 *       buttonTextColor: '#faf7f2',
 *     };
 *   </script>
 *
 *   <!-- Required: the widget itself -->
 *   <script src="https://YOUR-SERVER.com/widget.js"
 *           data-ai-stylist
 *           data-key="THEIR_API_KEY"
 *           async></script>
 *
 * The widget:
 *  1. Reads window.location.hostname to know which Shopify store it is on.
 *  2. Immediately calls the backend in the background to analyse the store.
 *  3. Shows a floating button bottom-right.
 *  4. On click → opens a modal with the quiz, then personalised picks.
 *  5. Optional photo upload for an AI outfit-image generation.
 *
 * All UI is in a Shadow DOM – zero CSS conflicts with the store's theme.
 */

(function () {
  'use strict';

  /* ─── Locate own script tag ───────────────────────────────── */
  // document.currentScript is null for async scripts, so we use an attribute.
  const scriptEl = document.querySelector('script[data-ai-stylist]');
  if (!scriptEl) return;

  const API_BASE = new URL(scriptEl.src).origin;
  const API_KEY  = scriptEl.getAttribute('data-key') || '';

  const userCfg      = window.AIStylistConfig || {};
  const BTN_TEXT     = userCfg.buttonText      || '\u2728 Find Your Style';
  const BTN_COLOR    = userCfg.buttonColor     || '#2c2825';
  const BTN_TXT_C    = userCfg.buttonTextColor || '#faf7f2';

  /* ─── State ───────────────────────────────────────────────── */
  let sessionId     = null;
  let quiz          = null;
  let shopName      = '';
  let currentQ      = 0;
  let answers       = {};
  let analysisReady = false;
  let pendingOpen   = false;
  let shadow        = null;
  let cardBody      = null;

  /* ─── Shadow DOM styles ───────────────────────────────────── */
  const CSS = `
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Inter:wght@400;500;600&display=swap');

    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    .overlay {
      position: fixed; inset: 0;
      background: rgba(20,17,15,0.65);
      z-index: 2147483646;
      display: flex; align-items: center; justify-content: center;
      padding: 16px;
      opacity: 0; transition: opacity 0.3s ease;
      font-family: 'Inter', sans-serif;
    }
    .overlay.open { opacity: 1; }

    .card {
      background: #faf7f2; border-radius: 20px;
      width: 100%; max-width: 480px; max-height: 88vh;
      overflow-y: auto;
      box-shadow: 0 24px 80px rgba(0,0,0,0.4);
      transform: translateY(24px);
      transition: transform 0.38s cubic-bezier(0.34,1.45,0.64,1);
      color: #2c2825;
    }
    .overlay.open .card { transform: translateY(0); }

    /* Header */
    .card-header {
      padding: 18px 22px 14px;
      border-bottom: 1px solid #e8ddd0;
      display: flex; align-items: center; justify-content: space-between;
      position: sticky; top: 0; background: #faf7f2; z-index: 1;
      border-radius: 20px 20px 0 0;
    }
    .hdr-brand {
      font-size: 0.72rem; letter-spacing: 0.15em;
      text-transform: uppercase; color: #c4714a; font-weight: 600;
      margin-bottom: 2px;
    }
    .hdr-title {
      font-family: 'Playfair Display', serif;
      font-size: 1.05rem; color: #2c2825;
    }
    .close-btn {
      width: 30px; height: 30px; border: none;
      background: #e8ddd0; border-radius: 50%;
      cursor: pointer; display: flex; align-items: center;
      justify-content: center; font-size: 0.9rem;
      color: #2c2825; flex-shrink: 0; transition: background 0.2s;
    }
    .close-btn:hover { background: #c4714a; color: #fff; }

    /* Card body */
    .card-body { padding: 22px; }

    /* Loading */
    .loading {
      display: flex; flex-direction: column;
      align-items: center; gap: 16px;
      padding: 44px 0; text-align: center;
    }
    .spinner {
      width: 42px; height: 42px;
      border: 3px solid #e8ddd0; border-top-color: #c4714a;
      border-radius: 50%; animation: spin 0.85s linear infinite;
    }
    @keyframes spin { to { transform: rotate(360deg); } }
    .loading-title {
      font-family: 'Playfair Display', serif;
      font-size: 1.15rem; color: #2c2825;
    }
    .loading-sub { font-size: 0.83rem; color: #8b6f5e; line-height: 1.5; }

    /* Progress */
    .progress { height: 3px; background: #e8ddd0; border-radius: 2px; margin-bottom: 22px; overflow: hidden; }
    .progress-fill {
      height: 100%; background: #c4714a; border-radius: 2px;
      transition: width 0.4s ease;
    }

    /* Quiz */
    .q-counter { font-size: 0.72rem; letter-spacing: 0.12em; text-transform: uppercase; color: #8b6f5e; margin-bottom: 5px; }
    .q-text { font-family: 'Playfair Display', serif; font-size: 1.18rem; line-height: 1.35; margin-bottom: 6px; }
    .q-hint { font-size: 0.82rem; color: #8b6f5e; font-style: italic; margin-bottom: 18px; }

    .options { display: grid; grid-template-columns: 1fr 1fr; gap: 9px; margin-bottom: 22px; }

    .opt {
      display: flex; align-items: center; gap: 9px;
      padding: 13px 12px; background: #fffef9;
      border: 1.5px solid #e8ddd0; border-radius: 10px;
      cursor: pointer; text-align: left;
      font-family: 'Inter', sans-serif; font-size: 0.865rem;
      color: #2c2825; transition: all 0.18s; line-height: 1.3;
    }
    .opt:hover { border-color: #c4714a; background: #fdf5f0; }
    .opt.selected { border-color: #c4714a; background: #fdf5f0; box-shadow: 0 0 0 2px #c4714a; }
    .opt-emoji { font-size: 1.3rem; flex-shrink: 0; }

    .quiz-nav { display: flex; align-items: center; justify-content: space-between; }
    .q-of { font-size: 0.8rem; color: #8b6f5e; }

    /* Buttons */
    .btn {
      display: inline-flex; align-items: center; gap: 6px;
      padding: 11px 20px; border: none; border-radius: 8px;
      font-family: 'Inter', sans-serif; font-size: 0.88rem; font-weight: 600;
      cursor: pointer; transition: all 0.2s; white-space: nowrap;
    }
    .btn-primary { background: #2c2825; color: #faf7f2; }
    .btn-primary:hover:not(:disabled) { background: #c4714a; }
    .btn-primary:disabled { opacity: 0.38; cursor: not-allowed; }
    .btn-ghost { background: transparent; color: #2c2825; border: 1.5px solid #d4c9bc; }
    .btn-ghost:hover { border-color: #2c2825; }
    .btn-invis { background: none; border: none; color: #8b6f5e; font-size: 0.8rem; font-family: 'Inter', sans-serif; cursor: pointer; text-decoration: underline; padding: 0; }
    .btn-invis:hover { color: #c4714a; }

    /* Results */
    .profile-card {
      background: #2c2825; color: #faf7f2;
      border-radius: 14px; padding: 22px;
      margin-bottom: 22px; text-align: center;
      position: relative; overflow: hidden;
    }
    .profile-card::after {
      content: ''; position: absolute;
      top: -30px; right: -30px;
      width: 120px; height: 120px;
      background: #c4714a; border-radius: 50%; opacity: 0.12;
    }
    .pc-label { font-size: 0.7rem; letter-spacing: 0.16em; text-transform: uppercase; color: #c9a84c; margin-bottom: 5px; }
    .pc-title { font-family: 'Playfair Display', serif; font-size: 1.45rem; color: #c9a84c; margin-bottom: 10px; }
    .pc-desc { font-size: 0.85rem; color: rgba(250,247,242,0.82); line-height: 1.65; }

    .section-label { font-size: 0.7rem; letter-spacing: 0.14em; text-transform: uppercase; color: #8b6f5e; margin-bottom: 12px; }

    .products { display: flex; flex-direction: column; gap: 12px; margin-bottom: 18px; }

    .product {
      display: flex; gap: 0; background: #fffef9;
      border: 1px solid #e8ddd0; border-radius: 12px; overflow: hidden;
      transition: box-shadow 0.2s;
    }
    .product:hover { box-shadow: 0 4px 18px rgba(44,40,37,0.12); }
    .prod-img-wrap { width: 88px; flex-shrink: 0; background: #e8ddd0; }
    .prod-img { width: 100%; height: 100%; object-fit: cover; display: block; }
    .prod-placeholder {
      width: 100%; height: 100%; min-height: 88px;
      display: flex; align-items: center; justify-content: center;
      font-size: 1.8rem; opacity: 0.35;
    }
    .prod-body { padding: 12px 14px; flex: 1; display: flex; flex-direction: column; }
    .prod-name { font-family: 'Playfair Display', serif; font-size: 0.95rem; margin-bottom: 2px; }
    .prod-price { font-size: 0.83rem; color: #c4714a; font-weight: 600; margin-bottom: 6px; }
    .prod-why { font-size: 0.78rem; color: #8b6f5e; line-height: 1.55; margin-bottom: 9px; flex: 1; }
    .prod-match { display: inline-block; font-size: 0.7rem; background: #2c2825; color: #c9a84c; padding: 2px 8px; border-radius: 20px; margin-bottom: 6px; }
    .prod-cta {
      display: inline-block; padding: 7px 14px;
      background: #2c2825; color: #faf7f2;
      border-radius: 6px; font-size: 0.78rem; font-weight: 600;
      text-decoration: none; transition: background 0.2s; width: fit-content;
    }
    .prod-cta:hover { background: #c4714a; }

    .tip {
      background: linear-gradient(135deg, #c49a8c 0%, #8b6f5e 100%);
      border-radius: 12px; padding: 15px 17px; margin-bottom: 18px;
      display: flex; gap: 11px; color: white;
    }
    .tip-icon { font-size: 1.3rem; flex-shrink: 0; margin-top: 1px; }
    .tip-label { font-size: 0.68rem; letter-spacing: 0.12em; text-transform: uppercase; opacity: 0.8; margin-bottom: 3px; }
    .tip-text { font-size: 0.83rem; line-height: 1.6; }

    /* Photo section */
    .photo-section {
      text-align: center; border-top: 1px solid #e8ddd0;
      padding-top: 18px; margin-top: 4px;
    }
    .photo-title { font-family: 'Playfair Display', serif; font-size: 0.97rem; margin-bottom: 4px; }
    .photo-sub { font-size: 0.78rem; color: #8b6f5e; margin-bottom: 12px; }
    .photo-label {
      display: inline-flex; align-items: center; gap: 7px;
      padding: 9px 18px; border: 1.5px dashed #c4714a;
      border-radius: 8px; cursor: pointer; font-size: 0.85rem;
      color: #c4714a; transition: all 0.2s; font-family: 'Inter', sans-serif;
    }
    .photo-label:hover { background: #fdf5f0; }
    .photo-preview {
      width: 76px; height: 76px; border-radius: 50%;
      object-fit: cover; border: 2px solid #c4714a;
      display: none; margin: 10px auto;
    }
    .photo-preview.on { display: block; }
    .generating { font-size: 0.8rem; color: #c4714a; margin-top: 8px; display: none; }
    .generating.on { display: block; }
    .outfit-img { width: 100%; border-radius: 10px; margin-top: 10px; display: none; }
    .outfit-img.on { display: block; }
    .photo-msg { font-size: 0.78rem; color: #8b6f5e; margin-top: 7px; font-style: italic; }

    /* Error */
    .err { background: #fef2f0; border: 1px solid #e8a89a; color: #8b3a2a; padding: 11px 15px; border-radius: 8px; font-size: 0.83rem; margin-top: 14px; display: none; }
    .err.on { display: block; }

    /* Restart row */
    .restart-row { text-align: center; margin-top: 14px; }

    @media (max-width: 520px) {
      .overlay { align-items: flex-end; padding: 0; }
      .card { border-radius: 20px 20px 0 0; max-height: 92vh; }
      .options { grid-template-columns: 1fr; }
    }
  `;

  /* ─── Utility ─────────────────────────────────────────────── */
  function esc(s) {
    return (s || '')
      .replace(/&/g, '&amp;').replace(/</g, '&lt;')
      .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  async function apiPost(path, body) {
    const r = await fetch(API_BASE + path, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'X-API-Key': API_KEY },
      body: JSON.stringify(body),
    });
    const data = await r.json();
    if (!r.ok) throw new Error(data.detail || 'Request failed');
    return data;
  }

  /* ─── DOM setup ───────────────────────────────────────────── */
  let overlay, card, hdrTitle;

  function createTrigger() {
    const btn = document.createElement('button');
    btn.id = 'ais-trigger';
    Object.assign(btn.style, {
      position: 'fixed', bottom: '24px', right: '24px',
      zIndex: '2147483645',
      padding: '14px 22px',
      background: BTN_COLOR, color: BTN_TXT_C,
      border: 'none', borderRadius: '50px',
      fontFamily: "'Inter', sans-serif",
      fontSize: '0.94rem', fontWeight: '600',
      cursor: 'pointer',
      boxShadow: '0 4px 20px rgba(0,0,0,0.28)',
      transition: 'transform 0.2s, box-shadow 0.2s',
      letterSpacing: '0.01em', lineHeight: '1',
    });
    btn.textContent = BTN_TEXT;
    btn.addEventListener('pointerover', () => {
      btn.style.transform = 'translateY(-2px)';
      btn.style.boxShadow = '0 8px 28px rgba(0,0,0,0.35)';
    });
    btn.addEventListener('pointerout', () => {
      btn.style.transform = '';
      btn.style.boxShadow = '0 4px 20px rgba(0,0,0,0.28)';
    });
    btn.addEventListener('click', openModal);
    document.body.appendChild(btn);
  }

  function createModal() {
    const host = document.createElement('div');
    host.id = 'ais-host';
    document.body.appendChild(host);

    shadow = host.attachShadow({ mode: 'open' });

    const styleEl = document.createElement('style');
    styleEl.textContent = CSS;
    shadow.appendChild(styleEl);

    overlay = document.createElement('div');
    overlay.className = 'overlay';
    overlay.addEventListener('click', e => { if (e.target === overlay) closeModal(); });

    card = document.createElement('div');
    card.className = 'card';
    card.setAttribute('role', 'dialog');
    card.setAttribute('aria-modal', 'true');
    card.setAttribute('aria-label', 'AI Style Quiz');

    const header = document.createElement('div');
    header.className = 'card-header';
    header.innerHTML = `
      <div>
        <div class="hdr-brand">&#10022; AI Stylist</div>
        <div class="hdr-title" id="ais-hdr-title">Your Style Quiz</div>
      </div>
      <button class="close-btn" id="ais-close" aria-label="Close">&times;</button>
    `;

    cardBody = document.createElement('div');
    cardBody.className = 'card-body';

    card.appendChild(header);
    card.appendChild(cardBody);
    overlay.appendChild(card);
    shadow.appendChild(overlay);

    hdrTitle = shadow.getElementById('ais-hdr-title');
    shadow.getElementById('ais-close').addEventListener('click', closeModal);
  }

  /* ─── Modal control ───────────────────────────────────────── */
  function openModal() {
    overlay.classList.add('open');
    document.body.style.overflow = 'hidden';
    if (analysisReady) {
      showQuiz();
    } else {
      pendingOpen = true;
      showLoading('Discovering your store\u2019s style\u2026', 'This takes ~15 seconds on first visit');
    }
  }

  function closeModal() {
    overlay.classList.remove('open');
    document.body.style.overflow = '';
  }

  /* ─── Views ───────────────────────────────────────────────── */
  function showLoading(title, sub) {
    hdrTitle.textContent = 'AI Stylist';
    cardBody.innerHTML = `
      <div class="loading">
        <div class="spinner"></div>
        <div class="loading-title">${esc(title)}</div>
        <div class="loading-sub">${esc(sub || '')}</div>
      </div>
    `;
  }

  function showQuiz() {
    currentQ = 0;
    answers = {};
    hdrTitle.textContent = shopName ? shopName + ' \u00b7 Style Quiz' : 'Your Style Quiz';
    renderQuestion();
  }

  function renderQuestion() {
    const q   = quiz.questions[currentQ];
    const tot = quiz.questions.length;
    const pct = (((currentQ + 1) / tot) * 100).toFixed(0);
    const sel = answers[q.id];
    const last = currentQ === tot - 1;

    cardBody.innerHTML = `
      <div class="progress"><div class="progress-fill" style="width:${pct}%"></div></div>
      <div class="q-counter">Question ${currentQ + 1} of ${tot}</div>
      <div class="q-text">${esc(q.question)}</div>
      ${q.context_hint ? `<div class="q-hint">${esc(q.context_hint)}</div>` : ''}
      <div class="options">
        ${q.options.map(o => `
          <button class="opt${sel === o.id ? ' selected' : ''}" data-oid="${esc(o.id)}">
            <span class="opt-emoji">${o.emoji || ''}</span>
            <span>${esc(o.text)}</span>
          </button>
        `).join('')}
      </div>
      <div class="quiz-nav">
        <button class="btn btn-ghost" id="ais-prev" ${currentQ === 0 ? 'style="visibility:hidden"' : ''}>&#8592; Back</button>
        <span class="q-of">${currentQ + 1} / ${tot}</span>
        <button class="btn btn-primary" id="ais-next" ${sel ? '' : 'disabled'}>
          ${last ? 'See my picks \u2746' : 'Next \u2192'}
        </button>
      </div>
      <div class="err" id="ais-err"></div>
    `;

    shadow.querySelectorAll('.opt').forEach(btn => {
      btn.addEventListener('click', () => {
        answers[q.id] = btn.dataset.oid;
        shadow.querySelectorAll('.opt').forEach(b => b.classList.toggle('selected', b === btn));
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

    const prevBtn = shadow.getElementById('ais-prev');
    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        if (currentQ > 0) { currentQ--; renderQuestion(); }
      });
    }
  }

  function showResults(data) {
    hdrTitle.textContent = 'Your Style Picks \u2746';
    const recs = data.recommendations || [];

    const prodsHtml = recs.map(rec => `
      <div class="product">
        <div class="prod-img-wrap">
          ${rec.product_image
            ? `<img class="prod-img" src="${esc(rec.product_image)}" alt="${esc(rec.product_name)}" loading="lazy" />`
            : `<div class="prod-placeholder">\uD83D\uDC57</div>`}
        </div>
        <div class="prod-body">
          <div class="prod-name">${esc(rec.product_name)}</div>
          ${rec.product_price ? `<div class="prod-price">${esc(rec.product_price)}</div>` : ''}
          ${rec.match_score   ? `<div class="prod-match">${rec.match_score}% match</div>` : ''}
          <div class="prod-why">${esc(rec.why_for_you)}</div>
          ${rec.product_url
            ? `<a class="prod-cta" href="${esc(rec.product_url)}" target="_blank" rel="noopener">Shop Now \u2192</a>`
            : ''}
        </div>
      </div>
    `).join('');

    cardBody.innerHTML = `
      <div class="profile-card">
        <div class="pc-label">Your style is\u2026</div>
        <div class="pc-title">${esc(data.style_profile_title || 'Uniquely You')}</div>
        <div class="pc-desc">${esc(data.style_profile || '')}</div>
      </div>

      <div class="section-label">Your curated picks</div>
      <div class="products">${prodsHtml}</div>

      ${data.styling_tip ? `
        <div class="tip">
          <div class="tip-icon">\uD83D\uDCA1</div>
          <div>
            <div class="tip-label">Stylist tip</div>
            <div class="tip-text">${esc(data.styling_tip)}</div>
          </div>
        </div>
      ` : ''}

      <div class="photo-section">
        <div class="photo-title">\uD83D\uDCF7 See yourself in the look</div>
        <div class="photo-sub">Upload a photo for an AI-generated outfit image</div>
        <label class="photo-label" for="ais-photo-inp">\uD83D\uDCF7\u00a0Choose photo</label>
        <input type="file" id="ais-photo-inp" accept="image/*" style="display:none" />
        <img class="photo-preview" id="ais-photo-prev" src="" alt="Your photo" />
        <div class="generating" id="ais-gen">\u2728 Generating your look\u2026</div>
        <img class="outfit-img" id="ais-outfit" src="" alt="AI outfit" />
        <div class="photo-msg" id="ais-photo-msg"></div>
      </div>

      <div class="restart-row">
        <button class="btn-invis" id="ais-restart">\u21BA Retake quiz</button>
      </div>
    `;

    shadow.getElementById('ais-photo-inp').addEventListener('change', handlePhoto);
    shadow.getElementById('ais-restart').addEventListener('click', showQuiz);
  }

  /* ─── Photo / outfit image ────────────────────────────────── */
  async function handlePhoto(e) {
    const file = e.target.files[0];
    if (!file) return;

    // Show preview
    const reader = new FileReader();
    reader.onload = ev => {
      const prev = shadow.getElementById('ais-photo-prev');
      prev.src = ev.target.result;
      prev.classList.add('on');
    };
    reader.readAsDataURL(file);

    shadow.getElementById('ais-gen').classList.add('on');
    shadow.getElementById('ais-outfit').classList.remove('on');
    shadow.getElementById('ais-photo-msg').textContent = '';

    try {
      const fd = new FormData();
      fd.append('session_id', sessionId);
      fd.append('photo', file);

      const r = await fetch(API_BASE + '/api/shop/outfit-image', {
        method: 'POST',
        headers: { 'X-API-Key': API_KEY },
        body: fd,
      });
      const data = await r.json();

      shadow.getElementById('ais-gen').classList.remove('on');
      if (data.success && data.image_url) {
        const img = shadow.getElementById('ais-outfit');
        img.src = data.image_url;
        img.classList.add('on');
        shadow.getElementById('ais-photo-msg').textContent = data.message || '';
      } else {
        shadow.getElementById('ais-photo-msg').textContent =
          data.message || 'Image generation unavailable.';
      }
    } catch {
      shadow.getElementById('ais-gen').classList.remove('on');
      shadow.getElementById('ais-photo-msg').textContent =
        'Image generation failed. Please try again.';
    }
  }

  /* ─── API calls ───────────────────────────────────────────── */
  async function preloadAnalysis() {
    try {
      const data = await apiPost('/api/shop/analyze', {
        shop_domain: window.location.hostname,
      });
      sessionId     = data.session_id;
      quiz          = data.quiz;
      shopName      = data.shop_name || '';
      analysisReady = true;
      if (pendingOpen) { pendingOpen = false; showQuiz(); }
    } catch (err) {
      console.warn('[AI Stylist] Could not load quiz:', err.message);
      if (pendingOpen) {
        pendingOpen = false;
        cardBody.innerHTML = `<div class="err on">Could not load the style quiz. Please refresh and try again.</div>`;
      }
    }
  }

  async function submitAnswers() {
    showLoading('Finding your perfect picks\u2026', 'Matching your style to the collection');
    try {
      const data = await apiPost('/api/shop/recommendations', {
        session_id: sessionId,
        answers: answers,
      });
      showResults(data);
    } catch (err) {
      cardBody.innerHTML = `<div class="err on">${esc(err.message)}</div>`;
    }
  }

  /* ─── Bootstrap ───────────────────────────────────────────── */
  function init() {
    createTrigger();
    createModal();
    preloadAnalysis(); // silent background pre-warm
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
