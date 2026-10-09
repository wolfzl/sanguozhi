import assert from 'node:assert/strict';
import fs from 'node:fs';
import { chromium } from 'playwright';

const base = process.env.SANGUO_URL || 'http://127.0.0.1:4324';
const book = JSON.parse(fs.readFileSync('src/data/book.json', 'utf8'));
const browser = await chromium.launch();
const context = await browser.newContext();
const page = await context.newPage();
const errors = [];
page.on('pageerror', error => errors.push(String(error)));
try {
  await page.goto(base + '/read/001/', {waitUntil: 'networkidle'});
  assert.ok((await page.locator('#v001-b0001').textContent()).startsWith('太祖武皇帝，沛国谯人也，姓曹，讳操'), 'New readers see simplified body text');
  assert.ok((await page.locator('#v001-b0001-n01').textContent()).includes('《曹瞒传》'), 'Embedded Pei notes are simplified too');
  assert.ok((await page.locator('#v001-b0001-n02').textContent()).includes('《续汉书》'), 'Book titles in note links are simplified');
  assert.equal(await page.locator('[data-reader]').getAttribute('lang'), 'zh-Hans');
  await page.getByRole('button', {name: '繁体', exact: true}).click();
  assert.ok((await page.locator('#v001-b0001').textContent()).startsWith('太祖武皇帝，沛國譙人也，姓曹，諱操'));
  await page.reload({waitUntil: 'networkidle'});
  assert.equal(await page.locator('[data-reader]').getAttribute('lang'), 'zh-Hant', 'Preference survives reload');
  await page.locator('.reader-pagination a').last().click();
  await page.waitForLoadState('networkidle');
  assert.equal(new URL(page.url()).pathname, '/read/002/');
  assert.equal(await page.locator('[data-reader]').getAttribute('lang'), 'zh-Hant', 'Preference survives next-volume navigation');
  await page.getByRole('button', {name: '简体', exact: true}).click();

  // Every volume must retain the exact original HTML after switching back.
  const plainContext = await browser.newContext({javaScriptEnabled: false});
  const plainPage = await plainContext.newPage();
  let noteCount = 0;
  for (const volume of book.volumes) {
    const path = '/read/' + volume.id + '/';
    await plainPage.goto(base + path);
    const original = await plainPage.locator('[data-reader]').innerHTML();
    const shape = await plainPage.locator('[data-reader] *').evaluateAll(elements => elements.map(el => [el.tagName, [...el.attributes].map(a => [a.name, a.value])]));
    await page.goto(base + path, {waitUntil: 'networkidle'});
    assert.equal(await page.locator('[data-reader]').getAttribute('lang'), 'zh-Hans', path);
    assert.doesNotMatch(await page.locator('[data-reader]').textContent(), /[國軍漢傳]/, path + ' converts common traditional characters throughout the body and notes');
    assert.deepEqual(await page.locator('[data-reader] *').evaluateAll(elements => elements.map(el => [el.tagName, [...el.attributes].map(a => [a.name, a.value])])), shape, path + ' preserves tags, IDs, classes and hrefs');
    noteCount += await page.locator('[data-reader] .peizhu').count();
    await page.getByRole('button', {name: '繁体', exact: true}).click();
    assert.equal(await page.locator('[data-reader]').innerHTML(), original, path + ' restores the exact source, including ambiguous characters');
    await page.getByRole('button', {name: '简体', exact: true}).click();
  }
  assert.equal(await plainPage.locator('[data-script-controls]').isVisible(), false, 'Unavailable controls are hidden without JavaScript');
  assert.equal(await plainPage.locator('[data-reader]').getAttribute('lang'), 'zh-Hant');
  await plainContext.close();

  await page.goto(base + '/read/001/', {waitUntil: 'networkidle'});
  await page.getByRole('button', {name: '显示裴注', exact: true}).click();
  await page.evaluate(() => { location.hash = 'v001-b0002-n02'; });
  await page.waitForFunction(() => document.querySelector('#v001-b0002-n02')?.checkVisibility());
  await page.waitForFunction(() => {
    const top = document.querySelector('#v001-b0002-n02').getBoundingClientRect().top;
    return top >= 0 && top <= 250;
  });
  const targetURL = page.url();
  for (const script of ['繁体', '简体', '繁体', '简体']) {
    // Locator.click() scrolls Chromium's sticky toolbar before dispatching a
    // pointer event. Click its visible coordinates to test actual user scrolling.
    const button = await page.getByRole('button', {name: script, exact: true}).boundingBox();
    assert.ok(button);
    await page.mouse.click(button.x + button.width / 2, button.y + button.height / 2);
    assert.equal(page.url(), targetURL, 'Switching scripts retains the citation URL');
    assert.equal(await page.locator('#v001-b0002-n02').isVisible(), true);
    assert.equal(await page.locator('#v001-b0002-n02').evaluate(el => el.matches(':target')), true);
    assert.ok(await page.locator('#v001-b0002-n02').evaluate(el => {const r=el.getBoundingClientRect();return r.bottom>0 && r.top<innerHeight;}), 'Citation remains in view after conversion');
  }
  for (const width of [320, 390, 768, 1440]) {
    await page.setViewportSize({width, height: 900});
    await page.goto(base + '/read/001/', {waitUntil: 'networkidle'});
    assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), width + 'px reader has no horizontal overflow');
    const controls = await page.locator('[data-script-controls]').boundingBox();
    const notes = await page.locator('[data-notes]').boundingBox();
    assert.ok(controls && notes && (controls.x + controls.width <= notes.x + 1 || controls.y + controls.height <= notes.y + 1 || notes.y + notes.height <= controls.y + 1), width + 'px controls do not overlap');
  }
  fs.mkdirSync('work', {recursive: true});
  await page.setViewportSize({width:390, height:900});
  await page.goto(base + '/read/001/', {waitUntil:'networkidle'});
  await page.screenshot({path:'work/reader-simplified-mobile.png'});
  await page.setViewportSize({width:1440, height:1000});
  await page.screenshot({path:'work/reader-simplified-desktop.png'});

  // Storage denial must not prevent either conversion or switching back.
  const denied = await browser.newContext();
  await denied.addInitScript(() => {
    Storage.prototype.getItem = () => { throw new Error('Storage disabled'); };
    Storage.prototype.setItem = () => { throw new Error('Storage disabled'); };
  });
  const deniedPage = await denied.newPage();
  await deniedPage.goto(base + '/read/001/', {waitUntil:'networkidle'});
  assert.ok((await deniedPage.locator('#v001-b0001').textContent()).includes('沛国谯人也'));
  await deniedPage.getByRole('button', {name:'繁体', exact:true}).click();
  assert.ok((await deniedPage.locator('#v001-b0001').textContent()).includes('沛國譙人也'));
  await denied.close();
  assert.deepEqual(errors, [], 'No reader JavaScript errors');
  console.log(JSON.stringify({volumes:book.volumes.length, annotations:noteCount, checks:'simplified body and notes, exact restoration, DOM structure, preferences, anchors, mobile, no-JS and denied storage'}, null, 2));
} finally {
  await browser.close();
}
