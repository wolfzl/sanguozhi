import assert from 'node:assert/strict';
import fs from 'node:fs';
import {chromium} from 'playwright';

const base=process.env.SANGUO_URL||'http://127.0.0.1:4324';
fs.mkdirSync('work',{recursive:true});
const browser=await chromium.launch();
const page=await browser.newPage({viewport:{width:1440,height:1100}});
const errors=[];
page.on('pageerror',error=>errors.push(String(error)));
try {
  const response=await page.goto(`${base}/people/zhangfei/`,{waitUntil:'networkidle'});
  assert.equal(response.status(),200);
  assert.equal(await page.locator('.person-dossier').count(),1);
  assert.equal(await page.getByRole('heading',{name:'生平履历',exact:true}).count(),1);
  assert.equal(await page.getByRole('heading',{name:'关键经历',exact:true}).count(),0);
  assert.equal(await page.locator('#milestones tbody tr').count(),11);
  assert.ok((await page.locator('#milestones tbody tr').last().innerText()).includes('追谥桓侯'));
  assert.equal(await page.locator('#civil-achievements table').count(),0);
  assert.ok((await page.locator('#civil-achievements').innerText()).includes('尚缺少可明确列出的代表性文治功绩'));
  assert.equal(await page.locator('#military-achievements tbody tr').count(),3);
  assert.equal(await page.locator('#setbacks tbody tr').count(),3);
  assert.equal(await page.locator('#relations .relation').count(),7);
  assert.equal(await page.locator('#relations a[href*="undefined"]').count(),0);
  await page.screenshot({path:'work/zhangfei-desktop.png',fullPage:false});
  await page.locator('#milestones').scrollIntoViewIfNeeded();
  await page.screenshot({path:'work/zhangfei-career-desktop.png',fullPage:false});

  // Follow the annotation citation and verify both its work and original passage.
  const cite=page.locator('#setbacks tbody tr').first().locator('.citations a').first();
  const target=await cite.getAttribute('href');
  await cite.click();
  const source=page.locator(target);
  await source.waitFor({state:'visible'});
  assert.equal(await source.getAttribute('open'),'');
  assert.ok((await source.innerText()).includes('英雄记'));
  await source.getByRole('link',{name:/阅读完整原文/}).click();
  assert.ok(page.url().includes('/read/032/#v032-b0005-n02'));
  assert.equal(await page.locator('#v032-b0005-n02').count(),1);

  await page.goto(`${base}/people/zhangfei/`,{waitUntil:'networkidle'});
  await page.locator('#military-achievements a[href="/events/enter-shu/"]').click();
  assert.equal(new URL(page.url()).pathname,'/events/enter-shu/');
  assert.ok(await page.locator('a[href="/people/zhangfei/"]').count()>0);

  for (const width of [390,320]) {
    await page.setViewportSize({width,height:844});
    await page.goto(`${base}/people/zhangfei/`,{waitUntil:'networkidle'});
    assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),`Page overflow at ${width}`);
    const rows=await page.locator('.dossier-table tbody tr').evaluateAll(els=>els.map(el=>{const r=el.getBoundingClientRect();return {left:r.left,right:r.right};}));
    assert.ok(rows.every(r=>r.left>=0&&r.right<=width+1),`Table overflow at ${width}`);
    assert.equal(await page.locator('.career-table tbody td').first().evaluate(el=>getComputedStyle(el).display),'block');
    if(width===390){
      await page.screenshot({path:'work/zhangfei-mobile.png',fullPage:false});
      await page.locator('#military-achievements').scrollIntoViewIfNeeded();
      await page.screenshot({path:'work/zhangfei-military-mobile.png',fullPage:false});
    }
    await page.locator('.glossary summary').click();
    assert.ok(await page.locator('.glossary dd').first().isVisible());
  }
  assert.deepEqual(errors,[]);
  console.log('Verified Zhang Fei unified timeline, achievement evidence, 7 relationships, annotation/source navigation, reciprocal event links, glossary and 1440/390/320px layouts.');
} finally {await browser.close();}
