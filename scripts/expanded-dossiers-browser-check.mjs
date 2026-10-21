import assert from 'node:assert/strict';
import fs from 'node:fs';
import {chromium} from 'playwright';
const base=process.env.SANGUO_URL||'http://127.0.0.1:4324';
const {people}=JSON.parse(fs.readFileSync('src/data/cards.json','utf8'));
const expanded=people.filter(p=>p.dossier.expanded);
const browser=await chromium.launch();
const page=await browser.newPage();
const errors=[];
page.on('pageerror',e=>errors.push(String(e)));
fs.mkdirSync('work/expanded-screens',{recursive:true});
try{
  for(const width of [1440,768,390,320]){
    await page.setViewportSize({width,height:1000});
    for(const p of expanded){
      const response=await page.goto(`${base}/people/${p.id}/`,{waitUntil:'networkidle'});
      assert.equal(response.status(),200,p.id);
      assert.equal(await page.locator('.expanded-dossier').count(),1);
      assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),`overflow ${width}/${p.id}`);
      assert.equal(await page.locator('#milestones tbody tr').count(),p.milestones.length);
      for(const [id,key] of [['civil-achievements','civil'],['military-achievements','military'],['setbacks','setbacks']])
        assert.equal(await page.locator(`#${id} tbody tr`).count(),p.dossier[key].length,`${p.id}/${key}`);
      const broken=await page.locator('a[href^="#"]').evaluateAll(as=>as.map(a=>a.getAttribute('href')).filter(h=>!document.getElementById(h.slice(1))));
      assert.deepEqual(broken,[],`anchors ${p.id}`);
      if(width===1440){
        for(const key of ['scholarship','assessment','readingNotes']) if(p.dossier[key].length) assert.ok(await page.locator(key==='readingNotes'?'#reading-note':`#${key}`).count());
        const search=page.locator('[data-source-query]');
        await search.fill('a-nonexistent-source-query');
        await search.dispatchEvent('input');
        assert.equal(await page.locator('.source-item:visible').count(),0);
        const citation=page.locator('.profile-evidence a').first();
        const hash=await citation.getAttribute('href');
        await citation.click();
        assert.equal(await search.inputValue(),'');
        assert.ok(await page.locator(hash).evaluate(el=>el.open&&!el.hidden));
        // Native fragment navigation briefly resets focus before hashchange runs.
        await page.waitForFunction(hash=>document.querySelector(`${hash} > summary`)===document.activeElement,hash);
        // Repeating a citation must also reveal a target hidden by a new filter.
        await search.fill('a-nonexistent-source-query');
        await citation.click();
        await page.waitForFunction(hash=>document.querySelector(`${hash} > summary`)===document.activeElement,hash);
        assert.equal(await search.inputValue(),'');
        assert.ok(await page.locator(hash).evaluate(el=>el.open&&!el.hidden));
        await page.goto(`${base}/people/${p.id}/${hash}`,{waitUntil:'networkidle'});
        assert.ok(await page.locator(hash).evaluate(el=>el.open));
        await search.fill('裴注');await search.dispatchEvent('input');
        const simplified=await page.locator('.source-item:visible').count();
        await search.fill('裴註');await search.dispatchEvent('input');
        assert.equal(await page.locator('.source-item:visible').count(),simplified);
        assert.ok(simplified>0);
        await search.fill('');await search.dispatchEvent('input');
      }
      if([1440,390].includes(width)){
        await page.evaluate(()=>window.scrollTo(0,0));
        await page.screenshot({path:`work/expanded-screens/${p.id}-${width}.png`});
        await page.locator('#military-achievements').scrollIntoViewIfNeeded();
        await page.screenshot({path:`work/expanded-screens/${p.id}-military-${width}.png`});
      }
    }
  }
  assert.deepEqual(errors,[]);
  console.log(`Verified ${expanded.length} expanded profiles at 1440/768/390/320px; source search, citation reveal/focus, direct hashes, section counts, navigation and no overflow or JS errors.`);
}finally{await browser.close();}
