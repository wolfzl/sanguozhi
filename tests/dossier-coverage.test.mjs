import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {validatePersonDossiers} from '../scripts/content-validation.mjs';

const {people}=JSON.parse(fs.readFileSync('src/data/cards.json','utf8'));

// A forgotten editor module must block publication, rather than silently using the old page.
test('every published person has sourced facts and a combined career timeline',()=>{
  assert.deepEqual(people.filter(p=>!p.dossier).map(p=>p.id),[]);
  for(const p of people){
    assert.ok(p.dossier.refs.length,`${p.id}: profile evidence`);
    assert.ok(p.milestones.every(m=>m.office?.trim()),`${p.id}: career office column`);
    for(const group of ['civil','military','setbacks']){
      assert.ok(p.dossier[group].length || p.dossier[`${group}Note`]?.trim(),`${p.id}/${group}: evidence or explanation`);
    }
  }
});

test('publication validation rejects missing dossiers when full coverage is required',()=>{
  assert.ok(validatePersonDossiers([{id:'missing'}],{requireAll:true}).length);
});
