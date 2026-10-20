import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import { matchesEvent, parseTimelineState } from '../src/lib/timeline.mjs';
const cards=JSON.parse(fs.readFileSync(new URL('../src/data/cards.json',import.meta.url)));
test('Han grouping includes both Yuans and requested lords with reciprocal event entries',()=>{
 for(const name of ['袁绍','袁术','公孙瓒','吕布','马腾']) {
  const person=cards.people.find(p=>p.name===name);
  assert.ok(person,name);
  assert.equal(person.faction,'汉末');
  assert.ok(person.eventIds.length,`${name} must be reachable through events`);
  for(const id of person.eventIds) assert.ok(cards.events.find(e=>e.id===id).participants.some(p=>p.personId===person.id));
 }
 assert.equal(cards.people.some(p=>p.faction==='袁氏'),false);
});
test('lords reading includes common background and reaches the later Han independent forces',()=>{
 const state={...parseTimelineState(),lane:'lords'};
 const selected=cards.events.filter(e=>matchesEvent(e,state));
 assert.ok(selected.some(e=>e.id==='yellow-turbans'));
 assert.ok(selected.some(e=>e.id==='tongguan'));
 assert.ok(selected.some(e=>e.id==='zhanglu-surrender'));
 assert.equal(new Set(selected.map(e=>e.id)).size,selected.length);
 assert.ok(cards.events.every(e=>matchesEvent(e,parseTimelineState())));
 assert.ok(cards.events.filter(e=>matchesEvent(e,parseTimelineState('?importance=key'))).every(e=>e.importance==='key'));
});
test('Jingzhou surrender precedes Red Cliffs within 208',()=>{
 const events=cards.events.filter(e=>e.year===208).sort((a,b)=>a.order-b.order);
 assert.ok(events.findIndex(e=>e.id==='jingzhou-surrender')<events.findIndex(e=>e.id==='chibi'));
});
