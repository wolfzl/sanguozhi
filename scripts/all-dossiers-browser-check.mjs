import assert from 'node:assert/strict';
import fs from 'node:fs';
import {chromium} from 'playwright';
const base=process.env.SANGUO_URL||'http://127.0.0.1:4324';
const {people}=JSON.parse(fs.readFileSync('src/data/cards.json','utf8'));
const browser=await chromium.launch();
const page=await browser.newPage();
const errors=[];
page.on('pageerror',e=>errors.push(String(e)));
fs.mkdirSync('work/dossier-screens',{recursive:true});
try{
  for(const width of [1440,390,320]){
    await page.setViewportSize({width,height:1000});
    for(const p of people){
      const response=await page.goto(`${base}/people/${p.id}/`,{waitUntil:'domcontentloaded'});
      assert.equal(response.status(),200,p.id);
      assert.equal(await page.locator('.person-dossier').count(),1,p.id);
      assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),`overflow ${width}/${p.id}`);
      const rows=await page.locator('.dossier-table tbody tr').evaluateAll(els=>els.map(el=>{const r=el.getBoundingClientRect();return {left:r.left,right:r.right};}));
      assert.ok(rows.every(r=>r.left>=0&&r.right<=width+1),`table bounds ${width}/${p.id}`);
      if(width===1440){
        assert.equal(await page.locator('#milestones tbody tr:not(.phase-row)').count(),p.milestones.length,p.id);
        for(const [section,key] of [['civil-achievements','civil'],['military-achievements','military'],['setbacks','setbacks']]){
          assert.equal(await page.locator(`#${section} tbody tr`).count(),p.dossier[key].length,`${p.id}/${key}`);
          if(!p.dossier[key].length) assert.ok((await page.locator(`#${section} .evidence-note`).innerText()).trim().length>0,`${p.id}/${key} empty note`);
        }
        assert.ok((await page.locator('h1').innerText()).includes(p.courtesy==='本书未详'?'字号未详':p.courtesy),p.id);
        assert.equal(await page.locator('.profile-evidence .citations a').count(),p.dossier.refs.length,p.id);
        const dangling=await page.locator('.detail-sidebar nav a').evaluateAll(as=>as.map(a=>a.getAttribute('href')).filter(h=>!document.querySelector(h)));
        assert.deepEqual(dangling,[],`navigation ${p.id}`);
        const caption=await page.locator('.career-table caption').innerText();
        assert.ok(caption.startsWith(p.name),`caption ${p.id}`);
        const glossary=p.dossier.glossary;
        assert.equal(await page.locator('.glossary').count(),glossary.length?1:0,p.id);
        if(glossary.length)assert.ok((await page.locator('.glossary summary').innerText()).includes(glossary.map(g=>g.term).join(' · ')),p.id);
      }
      if(['caocao','zhuge-liang','zhang-jiao','luxun','sun-qian'].includes(p.id)&&width!==320){
        await page.screenshot({path:`work/dossier-screens/${p.id}-${width}.png`});
        await page.locator('#milestones').scrollIntoViewIfNeeded();
        await page.screenshot({path:`work/dossier-screens/${p.id}-career-${width}.png`});
      }
    }
  }
  assert.deepEqual(errors,[]);
  console.log(`Verified all ${people.length} dossiers at 1440/390/320px: career/achievement rows, empty explanations, profile citations, courtesy names, captions, navigation, glossary and no overflow or JS errors.`);
}finally{await browser.close();}
