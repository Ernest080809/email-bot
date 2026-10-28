const { chromium } = require('playwright');
const fs = require('fs');
const S = '/tmp/claude-0/-home-user-email-bot/54727a9c-5c3e-59b1-82f7-802a7ce6ad79/scratchpad';
const done = JSON.parse(fs.readFileSync(S + '/export/daten/docket/progress/tasks.json', 'utf8')).done;
(async () => {
  const browser = await chromium.launch();
  for (const [name, vp] of [['desk', {width: 1280, height: 900}], ['mobil', {width: 390, height: 844}]]) {
    const page = await browser.newPage({viewport: vp});
    const errs = [];
    page.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
    page.on('pageerror', e => errs.push('PAGEERROR ' + e.message));
    await page.addInitScript(d => {
      const doc = p => ({
        onSnapshot: (cb) => { setTimeout(() => cb({exists: p === 'progress/tasks', data: () => ({done: d}), metadata: {hasPendingWrites: false}}), 50); return () => {}; },
        set: () => Promise.resolve()
      });
      window.claude = {use: () => Promise.resolve({doc})};
    }, done);
    await page.goto('file://' + S + '/docket7/time_travel_docket.html');
    await page.waitForTimeout(800);
    const info = await page.evaluate(() => {
      const wk = document.querySelectorAll('#weeks input[type=checkbox]');
      const chk = [...wk].filter(x => x.checked).map(x => x.getAttribute('data-ms'));
      return {
        tasks: wk.length, checked: chk.length, sample: chk.slice(-3),
        today: document.getElementById('tdTitle').textContent + ' · ' + document.getElementById('tdWeek').textContent,
        todayItems: [...document.querySelectorAll('#todayList > li')].map(li => li.innerText.split('\n')[0]).slice(0, 8),
        mega: document.getElementById('megaCount').textContent,
        cplan: document.querySelectorAll('#cplanList .cpi').length,
        mails: document.querySelectorAll('#mailList details').length,
        inv: document.querySelectorAll('#inventur table.inv tbody tr').length,
        hscroll: document.documentElement.scrollWidth > window.innerWidth + 1,
        phases: [...document.querySelectorAll('.phcell')].map(x => x.querySelector('.nm').textContent + ' ' + x.querySelector('.ct').textContent)
      };
    });
    console.log(name, JSON.stringify(info, null, 1));
    console.log(name, 'Fehler:', errs.length ? errs.slice(0, 5) : 'keine');
    await page.screenshot({path: S + `/rev7/shots/${name}_top.png`});
    // eine Aufgabe mit Briefing im Heute-Bereich öffnen
    await page.evaluate(() => { const w = document.getElementById('wk12'); if (w) { w.open = true; w.scrollIntoView(); } });
    await page.waitForTimeout(200);
    const opened = await page.evaluate(() => {
      const d = [...document.querySelectorAll('#wk12 details.how')].find(x => x.querySelector('.lazy[data-vr]'));
      if (!d) return 'keine';
      d.open = true; d.scrollIntoView();
      return d.closest('li').querySelector('.txt').textContent;
    });
    await page.waitForTimeout(300);
    const filled = await page.evaluate(() => document.querySelectorAll('#wk12 .lazy.filled').length);
    console.log(name, 'geöffnet:', opened, '· gerendert:', filled);
    await page.screenshot({path: S + `/rev7/shots/${name}_brief.png`});
    await page.evaluate(() => { document.getElementById('contentplan').scrollIntoView(); const c = document.querySelector('#cplanList .cpi'); c.open = true; });
    await page.waitForTimeout(300);
    await page.screenshot({path: S + `/rev7/shots/${name}_cplan.png`});
    await page.evaluate(() => { document.getElementById('mails').scrollIntoView(); const c = document.querySelector('#mailList details'); c.open = true; });
    await page.waitForTimeout(300);
    await page.screenshot({path: S + `/rev7/shots/${name}_mails.png`});
    await page.evaluate(() => document.getElementById('inventur').scrollIntoView());
    await page.screenshot({path: S + `/rev7/shots/${name}_inv.png`});
    await page.evaluate(() => document.getElementById('urteil').scrollIntoView());
    await page.screenshot({path: S + `/rev7/shots/${name}_urteil.png`});
    const errs2 = errs.length;
    console.log(name, 'Fehler am Ende:', errs2);
    await page.close();
  }
  await browser.close();
})();
