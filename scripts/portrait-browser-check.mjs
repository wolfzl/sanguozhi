import assert from 'node:assert/strict';
import fs from 'node:fs';
import {chromium} from 'playwright';
const base=process.env.SANGUO_URL||'http://127.0.0.1:4324';
const {people}=JSON.parse(fs.readFileSync('src/data/cards.json','utf8'));
const browser=await chromium.launch();
const page=await browser.newPage({viewport:{width:1440,height:1000}});
const errors=[];
page.on('pageerror',e=>errors.push(String(e)));
try {
  for(const person of people){
    const response=await page.goto(`${base}/people/${person.id}/`,{waitUntil:'domcontentloaded'});
    assert.equal(response.status(),200,person.id);
    assert.ok((await page.locator('.detail-sidebar dl dd').first().innerText()).includes(person.lifespan.text),`Lifespan ${person.id}`);
    const biographyLinks=person.paragraphs.flatMap(p=>p.eventLinks??[]);
    assert.equal(await page.locator('#life a[href^="/events/"]').count(),biographyLinks.length,`Narrative links ${person.id}`);
    const renderedLinks=await page.locator('#life a[href^="/events/"]').evaluateAll(els=>els.map(a=>({label:a.textContent,eventId:a.getAttribute('href').split('/')[2]})));
    assert.deepEqual(renderedLinks,biographyLinks,`Linked labels ${person.id}`);
    assert.equal(await page.locator('#milestones .milestone-date').count(),person.milestones.length);
    assert.equal(await page.locator('#milestones a[href^="/events/"]').count(),person.milestones.reduce((n,m)=>n+(m.eventIds?.length??0),0),`Milestone event visibility ${person.id}`);
    // v3 pages group relations into .context-relations items (one link per related person inside .record-events); older pages keep the flat .relation>a list.
    const relationSelector=person.dossier.contextRelations?'#relations .context-relations .record-events a':'#relations .relation>a';
    const relationIds=await page.locator(relationSelector).evaluateAll(els=>[...new Set(els.map(a=>a.getAttribute('href').split('/')[2]))].sort());
    assert.deepEqual(relationIds,[...new Set(person.relations.map(r=>r.personId))].sort(),`Relations ${person.id}`);
  }
  for(const width of [390,320]){
    await page.setViewportSize({width,height:844});
    for(const id of ['liubei','sun-jian','yuan-tan','sima-yi','jiang-wei']){
      await page.goto(`${base}/people/${id}/`,{waitUntil:'domcontentloaded'});
      assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),`Mobile overflow ${width}/${id}`);
    }
  }
  fs.mkdirSync('work',{recursive:true});
  await page.screenshot({path:'work/portrait-mobile.png',fullPage:true});
  assert.deepEqual(errors,[]);
  console.log(`Verified ${people.length} person pages: lifespan evidence, inline event labels, all milestone links and relations; 390/320px layout samples valid.`);
} finally {await browser.close();}
