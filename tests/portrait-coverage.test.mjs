import test from 'node:test';
import assert from 'node:assert/strict';
import {validatePortraits} from '../scripts/content-validation.mjs';
const book={volumes:[{id:'001',blocks:[{id:'v001-b0001',mainText:'年六十六',notes:[]}]}]};
const person={id:'test',courtesy:'本书未详',lifespan:{text:'约155—220年',sourceTitle:'《三国志》',sourceUrl:'/read/001/#v001-b0001',quote:'年六十六',note:'生年按享年推算'},paragraphs:[{eventLinks:[{label:'官渡',eventId:'guandu'}]}],milestones:[{when:'200年',eventIds:['guandu']}],relations:[]};
test('portrait standard requires dates, source evidence and dated event navigation',()=>{
 assert.deepEqual(validatePortraits([person],book),[]);
 assert.ok(validatePortraits([{...person,lifespan:undefined}],book).length);
 assert.ok(validatePortraits([{...person,lifespan:{...person.lifespan,quote:'不存在'}}],book).length);
 assert.ok(validatePortraits([{...person,paragraphs:[],milestones:[{when:'早年'}]}],book).length);
});
test('portrait standard rejects empty courtesy names and duplicate relations',()=>{
 assert.ok(validatePortraits([{...person,courtesy:''}],book).length);
 assert.ok(validatePortraits([{...person,relations:[{personId:'other'},{personId:'other'}]}],book).length);
});

test('only the sourced C-tier Hua Tuo profile can omit event navigation',()=>{
 const noEvents={...person,id:'hua-tuo',dossier:{schema:'v3',contentTier:'C'},eventIds:[],paragraphs:[{}],milestones:[{when:'确年未载'}]};
 assert.deepEqual(validatePortraits([noEvents],book),[]);
 assert.equal(validatePortraits([{...noEvents,id:'other'}],book).length,2);
 assert.equal(validatePortraits([{...noEvents,eventIds:['guandu']}],book).length,2);
});
