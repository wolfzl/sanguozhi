import test from 'node:test';
import assert from 'node:assert/strict';
import {validatePersonDossiers} from '../scripts/content-validation.mjs';
const ref={volume:'001',blockId:'v001-b0128',kind:'body',quote:'超世之傑矣。'};
const record={when:'220年',title:'评价',category:'评价',text:'陈寿的评价。',refs:[ref]};
const dossier={tier:'核心人物',hometown:'谯县',highestOffice:'丞相',highestTitle:'魏王',posthumous:'武王',deeds:['官渡'],refs:[ref],civil:[],civilNote:'暂无',military:[],setbacks:[],extraRelations:[],glossary:[],expanded:true,sourceScope:'卷一正文与裴注，并核查相关列传。',scholarship:[record],assessment:[record],readingNotes:[record]};
const p={id:'caocao',dossier,paragraphs:[record],milestones:[{...record,office:'—'}]};
test('expanded dossier requires source scope and sourced supplementary records',()=>{
  assert.deepEqual(validatePersonDossiers([p]),[]);
  assert.ok(validatePersonDossiers([{...p,dossier:{...dossier,sourceScope:''}}]).some(x=>x.includes('scope')));
  for(const key of ['scholarship','assessment','readingNotes']){
    const errors=validatePersonDossiers([{...p,dossier:{...dossier,[key]:[{title:'无证',text:'未引证',refs:[]}]}}]);
    assert.ok(errors.some(x=>x.includes(key)),key);
  }
});
test('expanded introduction and timeline require titled sourced entries',()=>{
  const errors=validatePersonDossiers([{...p,paragraphs:[{text:'无证',refs:[]}],milestones:[{when:'220年',text:'无证',office:'—',refs:[]}]}]);
  assert.ok(errors.some(x=>x.includes('introduction')));
  assert.ok(errors.some(x=>x.includes('career')));
});

test('expanded career event links cannot send an early battle to a later same-place battle',async()=>{
  const {validatePersonEventLinks}=await import('../scripts/content-validation.mjs');
  const person={id:'sunquan',dossier:{expanded:true},paragraphs:[],milestones:[{when:'208—209年',eventIds:['hefei']}],eventIds:['hefei']};
  const event={id:'hefei',year:215,endYear:215,participants:[{personId:'sunquan'}]};
  assert.ok(validatePersonEventLinks([person],[event]).some(x=>x.includes('date')));
  assert.deepEqual(validatePersonEventLinks([{...person,milestones:[{when:'215年',eventIds:['hefei']}]}],[event]),[]);
});
