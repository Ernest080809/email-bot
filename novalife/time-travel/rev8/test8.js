const { chromium } = require('playwright');
const fs = require('fs');
const ticks = JSON.parse(fs.readFileSync(__dirname + '/db/progress/tasks.json')).done;
const kpi = JSON.parse(fs.readFileSync(__dirname + '/db/progress/kpi.json')).vals;
(async () => {
  const b = await chromium.launch();
  for (const [name, vp, scheme] of [['mobil', {width: 390, height: 844}, 'light'], ['desktop', {width: 1280, height: 900}, 'dark']]) {
    const p = await b.newPage({viewport: vp, colorScheme: scheme});
    const errs = [];
    p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
    await p.addInitScript(([ticks, kpi]) => {
      const mk = (data) => ({ onSnapshot(cb){ setTimeout(() => cb({exists: true, data: () => data, metadata: {hasPendingWrites: false}}), 50); }, set(){ return Promise.resolve(); } });
      window.claude = { use: () => Promise.resolve({ doc: (path) => path === 'progress/tasks' ? mk({done: ticks}) : mk({vals: kpi}) }) };
    }, [ticks, kpi]);
    await p.goto('file://' + __dirname + '/time_travel_docket_rev8.html', {waitUntil: 'networkidle'});
    await p.waitForTimeout(400);
    const info = await p.evaluate(() => ({
      today: document.querySelectorAll('#todayList li.tk').length,
      weeks: document.querySelectorAll('#weekList details.wk').length,
      cur: (document.querySelector('#weekList details.wk.cur .wkn') || {}).textContent,
      stunts: document.querySelectorAll('#stuntList details.st').length,
      content: document.querySelectorAll('#cplanList details.cpi').length,
      mails: document.querySelectorAll('#mailList details.ml').length,
      olddone: document.querySelectorAll('#oldDone input:checked').length,
      count: document.getElementById('megaCount').textContent,
      days: document.getElementById('cdDays').textContent,
      overflow: document.documentElement.scrollWidth - window.innerWidth,
      note: document.getElementById('saveNote').textContent,
    }));
    console.log(name, JSON.stringify(info), 'errors:', errs);
    await p.screenshot({path: `${__dirname}/shot_${name}_top.png`});
    // eine Aufgabe mit Briefing öffnen
    await p.evaluate(() => { const d = document.querySelector('#stuntList details.st'); d.open = true; d.scrollIntoView(); });
    await p.waitForTimeout(200);
    await p.screenshot({path: `${__dirname}/shot_${name}_stunt.png`});
    await p.evaluate(() => document.getElementById('zahlen').scrollIntoView());
    await p.screenshot({path: `${__dirname}/shot_${name}_zahlen.png`});
    await p.evaluate(() => document.getElementById('wochen').scrollIntoView());
    await p.screenshot({path: `${__dirname}/shot_${name}_wochen.png`});
    await p.close();
  }
  await b.close();
})();
