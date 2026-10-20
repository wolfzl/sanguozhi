import test from 'node:test';
import assert from 'node:assert/strict';
import * as validation from '../scripts/content-validation.mjs';
const person={id:'sima-zhao',eventIds:['shouchun'],paragraphs:[{text:'257—258年围攻寿春',eventLinks:[{label:'257—258年围攻寿春',eventId:'shouchun'}]}],milestones:[{eventIds:['shouchun']}]};
const events=[{id:'shouchun',participants:[{personId:'sima-zhao'}]}];
test('person narrative and milestones link to an event that includes the person',()=>{
 assert.equal(typeof validation.validatePersonEventLinks,'function');
 assert.deepEqual(validation.validatePersonEventLinks([person],events),[]);
});
test('rejects missing event targets, absent labels and missing reciprocal participation',()=>{
 assert.equal(typeof validation.validatePersonEventLinks,'function');
 assert.ok(validation.validatePersonEventLinks([person],[]).length);
 assert.ok(validation.validatePersonEventLinks([{...person,paragraphs:[{text:'寿春',eventLinks:[{label:'未出现的文字',eventId:'shouchun'}]}]}],events).length);
 assert.ok(validation.validatePersonEventLinks([person],[{id:'shouchun',participants:[]}]).length);
});
