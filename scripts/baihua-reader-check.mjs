import assert from 'node:assert/strict';
import fs from 'node:fs';
import {chromium} from 'playwright';

const base = process.env.SANGUO_URL || 'http://127.0.0.1:4324';
const browser = await chromium.launch();
const context = await browser.newContext();
const page = await context.newPage();
const errors = [];
page.on('pageerror', error => errors.push(String(error)));
const button = name => page.getByRole('button', {name, exact:true});
const normalize = text => text.replace(/\[([^\]]+)\]\(https?:\/\/[^)]+\)/g, '$1').replace(/\s+/g, '');
try {
  await page.goto(base + '/read/001/', {waitUntil:'networkidle'});
  assert.equal(await button('白话').count(), 1, 'Wudi offers a vernacular reading option');
  const simplified = await page.locator('[data-reader]').innerHTML();
  await button('繁体').click();
  const traditional = await page.locator('[data-reader]').innerHTML();
  await button('白话').click();
  assert.equal(await button('白话').getAttribute('aria-pressed'), 'true');
  assert.match(await page.locator('[data-reader-script-state]').textContent(), /白话.*试译/);
  assert.match(await page.locator('#v001-b0001 [data-baihua-main]').textContent(), /没有人能确切弄清他的亲生家世/);
  assert.equal(await page.locator('[data-reader] .peizhu').count(), 122);
  assert.equal(await page.locator('[data-reader] [data-baihua-main]').count(), 123);
  const data = JSON.parse(fs.readFileSync('src/data/translations/001.json', 'utf8'));
  for (const block of data.blocks) {
    if (block.translation) assert.equal(normalize(await page.locator(`#${block.id} > [data-baihua-main]`).textContent()), normalize(block.translation), block.id + ' complete translation');
    for (const note of block.notes) assert.equal(normalize(await page.locator(`#${note.id} [data-baihua-note]`).textContent()), normalize(note.translation), note.id + ' complete annotation');
  }
  const ids = await page.locator('[id]').evaluateAll(elements => elements.map(el => el.id));
  assert.equal(ids.length, new Set(ids).size, 'Active document has no duplicate source IDs');
  await button('显示裴注').click();
  assert.equal(await page.locator('#v001-b0001-n01').isVisible(), false);
  await page.evaluate(() => {location.hash='v001-b0002-n02';});
  await page.waitForFunction(() => document.querySelector('#v001-b0002-n02')?.checkVisibility());
  await page.evaluate(async () => {
    // Wait for the hash's smooth scroll to settle before changing versions.
    let previous = window.scrollY;
    let stable = 0;
    while (stable < 4) {
      await new Promise(requestAnimationFrame);
      stable = Math.abs(window.scrollY - previous) < 1 ? stable + 1 : 0;
      previous = window.scrollY;
    }
  });
  const targetURL = page.url();
  for (const mode of ['繁体', '白话', '简体', '白话']) {
    const rect = await button(mode).boundingBox();
    await page.mouse.click(rect.x + rect.width/2, rect.y + rect.height/2);
    assert.equal(page.url(), targetURL);
    assert.ok(await page.locator('#v001-b0002-n02').evaluate(el => {const r=el.getBoundingClientRect();return r.bottom>0 && r.top<innerHeight;}), mode + ' retains citation position');
  }
  await page.reload({waitUntil:'networkidle'});
  assert.equal(await button('白话').getAttribute('aria-pressed'), 'true', 'Vernacular preference survives refresh');
  await page.goto(base + '/read/003/', {waitUntil:'networkidle'});
  assert.equal(await button('白话').count(), 0, 'Untranslated volumes do not offer unavailable content');
  assert.equal(await button('简体').getAttribute('aria-pressed'), 'true');
  await page.goto(base + '/read/001/', {waitUntil:'networkidle'});
  assert.equal(await button('白话').getAttribute('aria-pressed'), 'true', 'An untranslated volume does not erase vernacular preference');
  await button('繁体').click();
  assert.equal(await page.locator('[data-reader]').innerHTML(), traditional, 'Traditional source restored exactly');
  await button('简体').click();
  assert.equal(await page.locator('[data-reader]').innerHTML(), simplified, 'Simplified source restored exactly');
  await button('白话').click();
  assert.equal(await page.locator('#v001-b0104-n01 a').getAttribute('href'), 'https://zh.wikisource.org/w/index.php?title=全三國文/卷2&oldid=2325901');
  fs.mkdirSync('work', {recursive:true});
  for (const width of [320,390,768,1440]) {
    await page.setViewportSize({width,height:900});
    await page.goto(base + '/read/001/', {waitUntil:'networkidle'});
    assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth+1), width+'px no overflow');
    const controls=await page.locator('[data-script-controls]').boundingBox();
    const notes=await page.locator('[data-notes]').boundingBox();
    assert.ok(controls.x+controls.width <= notes.x+1 || controls.y+controls.height <= notes.y+1 || notes.y+notes.height <= controls.y+1, width+'px toolbar does not overlap');
    if ([390,1440].includes(width)) await page.screenshot({path:`work/reader-baihua-${width}.png`});
  }
  await page.setViewportSize({width:390,height:600});
  await page.evaluate(() => {
    const note = document.querySelector('#v001-b0086-n03');
    window.scrollTo({top:scrollY + note.getBoundingClientRect().top + 1800, behavior:'instant'});
  });
  for (const mode of ['繁体','白话','简体','白话']) {
    const rect = await button(mode).boundingBox();
    await page.mouse.click(rect.x + rect.width/2, rect.y + rect.height/2);
    assert.ok(await page.locator('#v001-b0086-n03').evaluate(el => {
      const r=el.getBoundingClientRect();
      const toolbar=document.querySelector('.reader-toolbar').getBoundingClientRect();
      return r.bottom>toolbar.bottom && r.top<innerHeight;
    }), mode+' retains position inside a long annotation on mobile');
  }
  const denied = await browser.newContext();
  await denied.addInitScript(() => {
    Storage.prototype.getItem = () => {throw new Error('Storage disabled');};
    Storage.prototype.setItem = () => {throw new Error('Storage disabled');};
  });
  const deniedPage=await denied.newPage();
  await deniedPage.goto(base+'/read/001/', {waitUntil:'networkidle'});
  await deniedPage.getByRole('button',{name:'白话',exact:true}).click();
  assert.match(await deniedPage.locator('#v001-b0001').textContent(), /亲生家世/);
  await deniedPage.getByRole('button',{name:'繁体',exact:true}).click();
  assert.match(await deniedPage.locator('#v001-b0001').textContent(), /沛國譙人/);
  await denied.close();

  // Verify the complete second volume, including its long imperial documents.
  await page.goto(base + '/read/002/', {waitUntil:'networkidle'});
  await button('繁体').click();
  const wendiSource = await page.locator('[data-reader]').innerHTML();
  await button('白话').click();
  const wendi = JSON.parse(fs.readFileSync('src/data/translations/002.json', 'utf8'));
  const book = JSON.parse(fs.readFileSync('src/data/book.json', 'utf8'));
  const source = book.volumes.find(volume => volume.id === '002');
  assert.deepEqual(wendi.blocks.map(block => block.id), source.blocks.map(block => block.id));
  assert.equal(await page.locator('[data-reader] [data-baihua-main]').count(), 39);
  assert.equal(await page.locator('[data-reader] [data-baihua-note]').count(), 47);
  for (const [index, block] of wendi.blocks.entries()) {
    assert.deepEqual(block.notes.map(note => note.id), source.blocks[index].notes.map(note => note.id));
    assert.ok(block.translation.trim(), block.id + ' has a translation');
    assert.equal(normalize(await page.locator(`#${block.id} > [data-baihua-main]`).textContent()), normalize(block.translation));
    for (const note of block.notes) {
      assert.ok(note.translation.trim(), note.id + ' has a translation');
      assert.equal(normalize(await page.locator(`#${note.id} [data-baihua-note]`).textContent()), normalize(note.translation));
    }
  }
  const wendiIds = await page.locator('[id]').evaluateAll(elements => elements.map(element => element.id));
  assert.equal(wendiIds.length, new Set(wendiIds).size, 'Wendi has no duplicate IDs');
  await page.reload({waitUntil:'networkidle'});
  assert.equal(await button('白话').getAttribute('aria-pressed'), 'true');
  await button('繁体').click();
  assert.equal(await page.locator('[data-reader]').innerHTML(), wendiSource, 'Wendi source restored exactly');
  for (const width of [320, 390, 768, 1440]) {
    await page.setViewportSize({width, height:900});
    await button('白话').click();
    assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), width + 'px Wendi no overflow');
    if ([390,1440].includes(width)) await page.screenshot({path:`work/reader-wendi-baihua-${width}.png`});
  }
  assert.deepEqual(errors, []);
  console.log('PASS: Wudi 123 main translations / 122 annotations; Wendi 39 / 47; source restoration, preferences, anchors, notes, 4 viewport sizes, denied storage.');
} finally {
  await browser.close();
}
