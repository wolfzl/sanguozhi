import assert from 'node:assert/strict';
import fs from 'node:fs';
import {chromium} from 'playwright';

const base=process.env.SANGUO_URL||'http://127.0.0.1:4324';
// Expected values come from the data so content edits do not make this check stale.
const {people}=JSON.parse(fs.readFileSync('src/data/cards.json','utf8'));
const zf=people.find(p=>p.id==='zhangfei');
const zd=zf.dossier;
const phases=zd.trajectory?.phases??[];
const firstEventMilestone=zf.milestones.find(m=>m.eventIds?.length);
fs.mkdirSync('work',{recursive:true});
const browser=await chromium.launch();
const page=await browser.newPage({viewport:{width:1440,height:1100}});
const errors=[];
page.on('pageerror',error=>errors.push(String(error)));
try {
  const response=await page.goto(`${base}/people/zhangfei/`,{waitUntil:'load'});
  assert.equal(response.status(),200);
  assert.equal(await page.locator('.person-dossier').count(),1);
  assert.equal(await page.getByRole('heading',{name:'生平履历',exact:true}).count(),1);
  assert.equal(await page.getByRole('heading',{name:'关键经历',exact:true}).count(),0);
  // Careers are folded into one <details class="fold-group"> per phase; rows are real milestones only.
  assert.equal(await page.locator('#milestones tbody tr:not(.phase-row)').count(),zf.milestones.length);
  assert.equal(await page.locator('#milestones details.fold-group').count(),phases.length);
  assert.equal(await page.locator('#milestones details.fold-group[open]').count(),1,'only the first period starts open');
  // Later periods start collapsed, so read textContent rather than rendered innerText.
  assert.ok((await page.locator('#milestones tbody tr:not(.phase-row)').last().textContent()).includes(zf.milestones.at(-1).title));
  assert.equal(zd.civil.length,0,'Zhang Fei is expected to have no civil achievements');
  assert.equal(await page.locator('#civil-achievements table').count(),0);
  assert.ok((await page.locator('#civil-achievements .evidence-note').innerText()).includes(zd.civilNote));
  assert.equal(await page.locator('#military-achievements tbody tr').count(),zd.military.length);
  assert.equal(await page.locator('#setbacks tbody tr').count(),zd.setbacks.length);
  // v3 pages group relations into context-relations items.
  assert.equal(await page.locator('#relations .context-relations .narrative-part').count(),zd.contextRelations.length);
  assert.equal(await page.locator('#relations a[href*="undefined"]').count(),0);
  await page.screenshot({path:'work/zhangfei-desktop.png',fullPage:false});
  await page.locator('#milestones').scrollIntoViewIfNeeded();
  await page.screenshot({path:'work/zhangfei-career-desktop.png',fullPage:false});

  // Follow the annotation citation and verify both its work and original passage.
  const firstRef=zd.setbacks[0].refs[0];
  const cite=page.locator('#setbacks tbody tr').first().locator('.citations a').first();
  const target=await cite.getAttribute('href');
  await cite.click();
  // A click now opens an in-place popover with the excerpt; its link jumps to the full evidence item.
  const pop=page.locator('.cite-pop');
  await pop.waitFor({state:'visible'});
  assert.ok((await pop.innerText()).length>10);
  await pop.getByRole('link',{name:/查看页底依据/}).click();
  const source=page.locator(target);
  await source.waitFor({state:'visible'});
  assert.equal(await source.getAttribute('open'),'');
  assert.ok((await source.innerText()).includes(firstRef.blockId));
  assert.ok((await source.innerText()).includes(firstRef.kind==='peizhu'?'裴注':'陈寿正文'));
  await source.getByRole('link',{name:/阅读完整原文/}).click();
  assert.ok(page.url().includes(`/read/${firstRef.volume}/#${firstRef.blockId}`));
  assert.equal(await page.locator(`#${firstRef.blockId}`).count(),1);

  await page.goto(`${base}/people/zhangfei/`,{waitUntil:'load'});
  // Milestone rows link to events; the event page must link back to the person.
  const eventId=firstEventMilestone.eventIds[0];
  await page.evaluate(()=>document.querySelectorAll('#milestones details').forEach(d=>{d.open=true;}));
  await page.locator(`#milestones a[href="/events/${eventId}/"]`).first().click();
  assert.equal(new URL(page.url()).pathname,`/events/${eventId}/`);
  assert.ok(await page.locator('a[href="/people/zhangfei/"]').count()>0);

  for (const width of [390,320]) {
    await page.setViewportSize({width,height:844});
    await page.goto(`${base}/people/zhangfei/`,{waitUntil:'load'});
    assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),`Page overflow at ${width}`);
    const rows=await page.locator('.dossier-table tbody tr').evaluateAll(els=>els.map(el=>{const r=el.getBoundingClientRect();return {left:r.left,right:r.right};}));
    assert.ok(rows.every(r=>r.left>=0&&r.right<=width+1),`Table overflow at ${width}`);
    assert.equal(await page.locator('.career-table tbody td').first().evaluate(el=>getComputedStyle(el).display),'block');
    if(width===390){
      await page.screenshot({path:'work/zhangfei-mobile.png',fullPage:false});
      await page.locator('#military-achievements').scrollIntoViewIfNeeded();
      await page.screenshot({path:'work/zhangfei-military-mobile.png',fullPage:false});
    }
    if(zd.glossary.length){
      await page.locator('.glossary summary').click();
      assert.ok(await page.locator('.glossary dd').first().isVisible());
    }else assert.equal(await page.locator('.glossary').count(),0);
  }
  assert.deepEqual(errors,[]);
  console.log('Verified Zhang Fei unified timeline with phase rows, achievement evidence, grouped relationships, citation/source navigation, reciprocal event links, glossary and 1440/390/320px layouts.');
} finally {await browser.close();}
