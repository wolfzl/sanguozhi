import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {validateAtlasPlaces} from '../scripts/content-validation.mjs';
import {trajectoryStops, placeUrl, routeUrl, stripNote, whenRange} from '../src/lib/atlas.mjs';

const {people} = JSON.parse(fs.readFileSync('src/data/cards.json', 'utf8'));
const sample = people.find(p => p.id === 'liubei');
const clone = () => structuredClone(sample);
const row = (p, id) => p.milestones.find(m => m.id === id);
const failsWith = (person, fragment) => assert.ok(validateAtlasPlaces([person]).some(e => e.includes(fragment)), fragment);
const BASE = 'http://127.0.0.1:8000/';

test('Liu Bei is the trajectory sample and passes every place rule', () => {
  assert.deepEqual(validateAtlasPlaces([sample]), []);
  assert.equal(sample.milestones.filter(m => m.place).length, 25);
  assert.equal(trajectoryStops(sample.milestones).length, 23);
});

test('rows that the guide says to skip stay unmarked', () => {
  for (const id of ['youth', 'xuxi', 'longzhong']) assert.equal(row(sample, id).place, undefined, id);
});

test('place name must come from the row itself (M2)', () => {
  const p = clone();
  row(p, 'longzhong').place = {name: '隆中', query: '隆中', province: '湖北', mapYear: 207};
  failsWith(p, 'name not in row');
});

test('mapYear stays inside when and never goes backwards (M5)', () => {
  const p = clone();
  row(p, 'chengdu').place.mapYear = 215;
  failsWith(p, 'outside when');
  const q = clone();
  row(q, 'bowang').place.mapYear = 200;
  failsWith(q, 'goes backwards');
});

test('place fields are complete and closed', () => {
  const p = clone();
  delete row(p, 'chibi').place.province;
  failsWith(p, 'missing province');
  const q = clone();
  row(q, 'chibi').place.note = 'x';
  failsWith(q, 'unknown field');
  const r = clone();
  row(r, 'chibi').place.approx = false;
  failsWith(r, 'approx must be omitted or true');
});

test('places are only allowed on v3 profiles', () => {
  const p = structuredClone(people.find(x => x.id === 'zhuge-liang'));
  p.milestones[1].place = {name: '隆中', query: '隆中', province: '湖北', mapYear: 207};
  failsWith(p, 'only allowed on v3');
});

test('consecutive rows at the same place merge into one stop', () => {
  const stops = trajectoryStops(sample.milestones);
  assert.deepEqual(stops[0].rows.map(r => r.id), ['yellow', 'duyou']);
  assert.equal(stops[0].name, '安喜');
  assert.deepEqual(stops.map(s => s.index), stops.map((_, i) => i + 1));
  const chengdu = stops.find(s => s.rows.some(r => r.id === 'liufeng'));
  assert.deepEqual(chengdu.rows.map(r => r.id), ['liufeng', 'accession']);
});

test('links follow the atlas URL protocol', () => {
  assert.equal(placeUrl(BASE, row(sample, 'yiling').place), `${BASE}?year=222&place=${encodeURIComponent('夷陵')}`);
  const stops = trajectoryStops(sample.milestones);
  const embed = new URL(routeUrl(BASE, stops, {embed: true}));
  assert.equal(embed.searchParams.get('embed'), '1');
  assert.equal(embed.searchParams.get('from'), '184');
  assert.equal(embed.searchParams.get('to'), '223');
  assert.equal(embed.searchParams.get('place').split(',').length, stops.length);
  assert.equal(embed.searchParams.get('year').split(',').length, stops.length);
  assert.equal(new URL(routeUrl(BASE, stops)).searchParams.has('embed'), false);
  assert.equal(routeUrl(BASE, []), '');
});

test('helpers', () => {
  assert.equal(stripNote('下邳（睢宁）'), '下邳');
  assert.deepEqual(whenRange('212—214年'), [212, 214]);
  assert.deepEqual(whenRange('约220年前后，确切月日未载'), [220, 220]);
  assert.equal(whenRange('寄居荆州期间，确年未载'), null);
});
