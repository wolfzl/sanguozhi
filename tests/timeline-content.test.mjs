import test from 'node:test';
import assert from 'node:assert/strict';
import * as api from '../scripts/content-validation.mjs';
const event = (id,year) => ({id,year,endYear:year,order:0,phase:year<211?'formation':year<239?'states':'unification',importance:'key',lanes:['shu'],categories:['war'],participants:[]});
const edge = {id:'a-b',from:'a',to:'b',type:'process',summary:'同一进程中的后续行动。',interpretation:true,refs:[{blockId:'source'}]};
test('rejects an event relationship with a missing target or an unconnected event',()=>{
 assert.equal(typeof api.validateTimeline,'function');
 const errors=api.validateTimeline([event('a',220),event('b',221)],[{...edge,to:'missing'}]);
 assert.ok(errors.some(e=>e.includes('missing')));
 assert.ok(errors.some(e=>e.includes('Unconnected event b')));
});
test('rejects time range reversal and events extending an ended polity',()=>{
 assert.equal(typeof api.validateTimeline,'function');
 const errors=api.validateTimeline([{...event('a',264),endYear:263},event('b',265)],[edge]);
 assert.ok(errors.some(e=>e.includes('time range')));
 assert.ok(errors.some(e=>e.includes('Shu after 263')));
});
test('accepts an explicitly sourced parallel comparison without turning it into chronological causality',()=>{
 assert.equal(typeof api.validateTimeline,'function');
 assert.deepEqual(api.validateTimeline([event('a',221),event('b',220)],[{...edge,type:'parallel',interpretation:false}]),[]);
});

test('accepts independent lords in the formation and later consolidation periods',()=>{
 assert.deepEqual(api.validateTimeline([{...event('a',199),lanes:['lords']},{...event('b',211),lanes:['wei','lords']}],[edge]),[]);
});

test('rejects stage labels that would move later events ahead of earlier years',()=>{
 const errors=api.validateTimeline([{...event('a',241),phase:'states',lanes:['wu']},{...event('b',249),phase:'unification',lanes:['wei']}],[edge]);
 assert.ok(errors.some(e=>e.includes('phase year a')));
});
