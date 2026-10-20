import test from 'node:test';
import assert from 'node:assert/strict';
import * as validation from '../scripts/content-validation.mjs';

const ref={volume:'036',blockId:'v036-b0010',kind:'body',quote:'巴土獲安。'};
const dossier={tier:'核心人物',hometown:'涿郡',highestOffice:'车骑将军',highestTitle:'西乡侯',posthumous:'桓侯，260年追谥',deeds:['巴西破张郃'],civil:[],civilNote:'现存记载以军事活动为主。',military:[{when:'215—216年',title:'巴西破张郃',category:'守御',text:'击退张郃。',refs:[ref],eventIds:['baxi']}],setbacks:[],extraRelations:[],glossary:[]};
const person={id:'zhangfei',dossier,paragraphs:[],milestones:[{when:'215—216年',title:'巴西破张郃',text:'击退张郃。',office:'—',refs:[ref]}],eventIds:['baxi']};

// Catches incomplete dossiers being published as if they were sourced records.
test('dossier validation accepts legacy portraits and rejects unsupported achievement records',()=>{
  assert.equal(typeof validation.validatePersonDossiers,'function');
  assert.deepEqual(validation.validatePersonDossiers([{id:'legacy'},person]),[]);
  const invalid={...person,dossier:{...dossier,civilNote:'',military:[{...dossier.military[0],refs:[]}]}};
  assert.ok(validation.validatePersonDossiers([invalid]).length>=2);
});

// Catches links added to new tables without a real reciprocal event association.
test('achievement event links must exist and include their person',()=>{
  assert.deepEqual(validation.validatePersonEventLinks([person],[{id:'baxi',participants:[{personId:'zhangfei'}]}]),[]);
  assert.ok(validation.validatePersonEventLinks([person],[]).length);
  assert.ok(validation.validatePersonEventLinks([person],[{id:'baxi',participants:[]}]).length);
});
