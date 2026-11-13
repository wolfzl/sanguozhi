import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {validateV3Profiles, GENERIC_SECTION_NOTE} from '../scripts/content-validation.mjs';

const {people} = JSON.parse(fs.readFileSync('src/data/cards.json', 'utf8'));
const sample = people.find(p => p.id === 'guanyu');
const clone = () => structuredClone(sample);
const failsWith = (person, fragment) => assert.ok(validateV3Profiles([person]).some(e => e.includes(fragment)), fragment);

test('Guan Yu is the published v3 B-tier sample and passes every v3 rule', () => {
  assert.equal(sample.dossier.schema, 'v3');
  assert.equal(sample.dossier.contentTier, 'B');
  assert.deepEqual(validateV3Profiles([sample]), []);
});

test('v3 rejects whole-passage quotations', () => {
  const p = clone();
  p.milestones[0].refs[0].quote = '字'.repeat(121);
  failsWith(p, 'quote too long');
});

test('v3 requires every profile fact to carry its own evidence', () => {
  const p = clone();
  p.dossier.factDetails[1].refs = [];
  failsWith(p, 'fact without evidence');
  const q = clone();
  q.dossier.factDetails = q.dossier.factDetails.filter(f => f.label !== '籍贯');
  failsWith(q, 'missing fact');
});

test('v3 enforces tier sizes', () => {
  const p = clone();
  p.milestones = p.milestones.slice(0, 5);
  failsWith(p, 'career count');
  const q = clone();
  q.paragraphs = q.paragraphs.slice(0, 1);
  failsWith(q, 'introduction count');
});

test('v3 empty sections need a person-specific note', () => {
  const p = clone();
  p.dossier.civil = [];
  p.dossier.civilNote = GENERIC_SECTION_NOTE;
  failsWith(p, 'person-specific note');
});

test('v3 record careerRef must point at an existing career row', () => {
  const p = clone();
  p.dossier.military[0].careerRef = 'missing-row';
  failsWith(p, 'unknown careerRef');
});

test('v3 relations need categories and profiles may not embed appendix excerpts', () => {
  const p = clone();
  p.dossier.contextRelations[0].category = '';
  failsWith(p, 'without category');
  const q = clone();
  q.dossier.appendixRefs = [q.milestones[0].refs[0]];
  failsWith(q, 'appendix');
});

test('each tier has a published v3 sample that passes every rule', () => {
  const samples = {liubei: 'A', guanyu: 'B', 'zhang-jiao': 'C'};
  for (const [id, tier] of Object.entries(samples)) {
    const p = people.find(x => x.id === id);
    assert.equal(p.dossier.schema, 'v3', id);
    assert.equal(p.dossier.contentTier, tier, id);
    assert.deepEqual(validateV3Profiles([p]), [], id);
    assert.equal(p.dossier.appendixRefs?.length ?? 0, 0, id);
  }
});

test('C tier allows an explained empty section and omitted optional facts', () => {
  const p = people.find(x => x.id === 'zhang-jiao');
  assert.equal(p.dossier.civil.length, 0);
  assert.notEqual(p.dossier.civilNote, GENERIC_SECTION_NOTE);
  assert.equal(p.dossier.highestTitle, '本书未载');
});
