import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {validateTrajectory} from '../scripts/content-validation.mjs';
import {phaseUrl, routeUrl, stripNote, phaseNumeral, stopParam} from '../src/lib/atlas.mjs';

const {people} = JSON.parse(fs.readFileSync('src/data/cards.json', 'utf8'));
const sample = people.find(p => p.id === 'liubei');
const clone = () => structuredClone(sample);
const phase = (p, id) => p.dossier.trajectory.phases.find(x => x.id === id);
const failsWith = (person, fragment) => assert.ok(validateTrajectory([person]).some(e => e.includes(fragment)), fragment);
const BASE = 'http://127.0.0.1:8000/';

test('Liu Bei is the trajectory sample: 7 phases on the atlas route', () => {
  assert.deepEqual(validateTrajectory([sample]), []);
  const t = sample.dossier.trajectory;
  assert.equal(t.atlasPerson, 'liubei');
  assert.equal(t.phases.length, 7);
  assert.ok(sample.milestones.every(m => !('place' in m)));
});

test('phases cover every career row once and in order (M1)', () => {
  const p = clone();
  phase(p, 'xuzhou').careers.pop();
  failsWith(p, 'not covered in order');
  const q = clone();
  phase(q, 'early').careers.reverse();
  failsWith(q, 'not covered in order');
});

test('phase count follows the tier (M2)', () => {
  const p = clone();
  p.dossier.trajectory.phases = p.dossier.trajectory.phases.slice(0, 4);
  failsWith(p, 'phase count out of range');
});

test('spans are valid and never go backwards (M3)', () => {
  const p = clone();
  phase(p, 'chibi').span = [199, 210];
  failsWith(p, 'span goes backwards');
  const q = clone();
  phase(q, 'chibi').span = [210, 208];
  failsWith(q, 'invalid span');
});

test('atlas stops are required in mode one and keep increasing (M4)', () => {
  const p = clone();
  delete phase(p, 'yizhou').atlasStops;
  failsWith(p, 'needs atlasStops');
  const q = clone();
  phase(q, 'yizhou').atlasStops = [4];
  failsWith(q, 'atlasStops must increase');
  const r = clone();
  phase(r, 'emperor').atlasStops = [10, 12];
  failsWith(r, 'must be consecutive');
});

test('mode two needs a place whose name comes from the phase rows (M5)', () => {
  const p = clone();
  delete p.dossier.trajectory.atlasPerson;
  for (const ph of p.dossier.trajectory.phases) delete ph.atlasStops;
  failsWith(p, 'needs place');
  const q = structuredClone(p);
  for (const ph of q.dossier.trajectory.phases) ph.place = {name: '成都', query: '成都', province: '四川', mapYear: ph.span[0]};
  failsWith(q, 'name not in phase');
  const r = structuredClone(q);
  phase(r, 'yizhou').place.mapYear = 230;
  failsWith(r, 'mapYear outside span');
});

test('trajectory is v3 only and per-row places are retired', () => {
  const p = clone();
  p.dossier.schema = 'expanded';
  failsWith(p, 'only allowed on v3');
  const q = clone();
  q.milestones[0].place = {name: '安喜'};
  failsWith(q, 'per-row place is retired');
});

test('mode one links reuse the atlas person route', () => {
  const t = sample.dossier.trajectory;
  assert.equal(phaseUrl(BASE, t, phase(sample, 'chibi')), `${BASE}?person=liubei&stop=3-4`);
  assert.equal(phaseUrl(BASE, t, phase(sample, 'xuzhou')), `${BASE}?person=liubei&stop=1`);
  assert.equal(phaseUrl(BASE, t, phase(sample, 'emperor')), `${BASE}?person=liubei&stop=10-12`);
  const embed = new URL(routeUrl(BASE, t, {embed: true}));
  assert.equal(embed.searchParams.get('embed'), '1');
  assert.equal(embed.searchParams.get('person'), 'liubei');
  assert.equal(embed.searchParams.get('from'), '175');
  assert.equal(embed.searchParams.get('to'), '223');
  assert.equal(routeUrl(BASE, t), `${BASE}?person=liubei`);
});

test('mode two links use the phase places', () => {
  const t = {phases: [
    {id: 'a', span: [191, 199], place: {query: '邺', mapYear: 191}},
    {id: 'b', span: [200, 202], place: {query: '官渡', mapYear: 200}},
  ]};
  assert.equal(phaseUrl(BASE, t, t.phases[1]), `${BASE}?year=200&place=${encodeURIComponent('官渡')}`);
  const url = new URL(routeUrl(BASE, t, {embed: true}));
  assert.equal(url.searchParams.get('place'), '邺,官渡');
  assert.equal(url.searchParams.get('year'), '191,200');
  assert.equal(routeUrl(BASE, {phases: []}), '');
});

const sparseRoute = () => {
  const p = structuredClone(people.find(p => p.id === 'zhang-jiao'));
  p.dossier.trajectory = {phases: [
    {id: 'taiping', title: '传道与联结信众', when: '起事前，确年未载', span: [178, 184],
      careers: ['taiping', 'organize'], unmappedReason: '只记东方，具体驻地未载。'},
    {id: 'uprising', title: '魏郡起事', when: '184年', span: [184, 184],
      careers: ['uprising'], place: {name: '魏郡', query: '魏郡', province: '河北', mapYear: 184, approx: true}},
    {id: 'suppressed', title: '遭讨击与被诛', when: '起事后，确年未载', span: [184, 184],
      careers: ['suppressed'], unmappedReason: '被诛地点未载。'},
  ]};
  return p;
};

test('mode two accepts unknown locations with an explicit reason', () => {
  assert.deepEqual(validateTrajectory([sparseRoute()]), []);
  const p = sparseRoute();
  p.dossier.trajectory.phases[0].unmappedReason = ' ';
  failsWith(p, 'needs place');
  p.dossier.trajectory.phases[0].unmappedReason = true;
  failsWith(p, 'needs place');
});

test('an unknown-location reason cannot accompany a mapped place', () => {
  const p = sparseRoute();
  p.dossier.trajectory.phases[1].unmappedReason = '地点未载。';
  failsWith(p, 'both place and unmappedReason');
});

test('mode two requires at least one supported location', () => {
  const p = sparseRoute();
  delete p.dossier.trajectory.phases[1].place;
  p.dossier.trajectory.phases[1].unmappedReason = '地点未载。';
  failsWith(p, 'needs at least one mapped place');
});

test('unknown periods keep their careers without adding map stops or links', () => {
  const t = sparseRoute().dossier.trajectory;
  assert.equal(phaseUrl(BASE, t, t.phases[0]), '');
  assert.equal(phaseUrl(BASE, t, t.phases[2]), '');
  const url = new URL(routeUrl(BASE, t, {embed: true}));
  assert.equal(url.searchParams.get('place'), '魏郡');
  assert.equal(url.searchParams.get('year'), '184');
  assert.equal(routeUrl(BASE, {phases: [t.phases[0], t.phases[2]]}), '');
});

test('helpers', () => {
  assert.equal(stripNote('下邳（睢宁）'), '下邳');
  assert.equal(phaseNumeral(0), '一');
  assert.equal(phaseNumeral(6), '七');
  assert.equal(stopParam([3, 4]), '3-4');
  assert.equal(stopParam([8]), '8');
  assert.equal(stopParam([]), undefined);
});

test('a period with no personal location does not link to the entire unrelated itinerary', () => {
  const t = {atlasPerson:'zhaoyun',phases:[{id:'after',span:[229,261],atlasStops:[]}]};
  assert.equal(phaseUrl(BASE,t,t.phases[0]),'');
});

const shuAudit = JSON.parse(fs.readFileSync('docs/shu-trajectory-audit.json','utf8'));
test('all nine corrected Shu routes preserve sourced careers and exact phase stop ranges', () => {
  assert.equal(Object.keys(shuAudit).length,9);
  for (const [id,route] of Object.entries(shuAudit)) {
    const p=people.find(p=>p.id===id), t=p.dossier.trajectory;
    assert.equal(t.atlasPerson,route.atlasPerson);
    assert.deepEqual(t.phases.flatMap(ph=>ph.atlasStops),route.stops.map((_,i)=>i),id);
    for (const [i,stop] of route.stops.entries()) {
      const ph=t.phases.find(ph=>ph.id===stop.phaseId);
      const career=p.milestones.find(m=>m.id===stop.careerId);
      assert.ok(ph.careers.includes(career.id));
      assert.ok(ph.atlasStops.includes(i));
      assert.deepEqual(stop.sourceRefs,career.refs);
      assert.ok(stop.coord.every(Number.isFinite));
      assert.ok(stop.year>=ph.span[0]&&stop.year<=ph.span[1]);
    }
  }
});
test('Shu homonyms do not fall on unrelated provinces or conflate Ji and Shanggui', () => {
  const stops=Object.values(shuAudit).flatMap(r=>r.stops);
  for (const s of stops.filter(s=>s.ancientZh==='江州')) assert.ok(s.coord[0]<108&&s.coord[1]<30);
  for (const s of stops.filter(s=>s.ancientZh==='汉寿')) assert.ok(s.coord[0]<107&&s.coord[1]>32);
  const ji=stops.find(s=>s.ancientZh==='冀城'), shang=stops.find(s=>s.ancientZh==='上邽');
  assert.ok(Math.abs(ji.coord[0]-shang.coord[0])>0.3);
  const ta=stops.find(s=>s.ancientZh==='沓中'); assert.ok(ta.coord[0]<105&&ta.coord[1]>33);
});
