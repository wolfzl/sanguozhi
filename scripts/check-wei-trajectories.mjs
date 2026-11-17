// Run from the site root with JIANGSHAN_DIR pointing to the matching atlas checkout.
// The audit retains the local book evidence and the career/phase owning each stop.
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { createRequire } from 'node:module';
import { phaseUrl, routeUrl } from '../src/lib/atlas.mjs';

const read = file => JSON.parse(fs.readFileSync(file, 'utf8'));
const audit = read('docs/wei-trajectory-audit.json');
const people = new Map(read('src/data/cards.json').people.map(p => [p.id, p]));
const sources = new Map();
for (const volume of read('src/data/book.json').volumes) {
  for (const block of volume.blocks) {
    sources.set(block.id, block.mainText);
    for (const note of block.notes) sources.set(note.id, note.text);
  }
}
const targets = ['cao-pi', 'cao-rui', 'cao-mao', 'cao-shuang', 'sima-shi', 'sima-zhao', 'deng-ai', 'zhong-hui', 'zhang-liao', 'xun-yu', 'xun-you', 'guo-jia', 'cheng-yu', 'jia-xu'];
assert.deepEqual(Object.keys(audit).sort(), targets.sort(), 'audit must cover exactly the fourteen Wei B-tier people');
const atlasDir = process.env.JIANGSHAN_DIR ?? path.join(os.homedir(), 'ai/github/jiangshan-map');
const mcp = createRequire(import.meta.url)(path.join(atlasDir, 'scripts/mcp_server.js'));
const runtime = mcp.createMcpRuntime();
let count = 0, phaseCount = 0;
for (const [id, expected] of Object.entries(audit)) {
  const person = people.get(id);
  const trajectory = person.dossier.trajectory;
  assert.equal(trajectory.atlasPerson, expected.atlasPerson, `${id}: atlas identity`);
  const profile = runtime.sandbox.ATLAS_LORE_DATA.PERSON_PROFILES.find(p => p.key === expected.atlasPerson);
  assert.ok(profile?.curatedOnly, `${id}: public events must not enter the personal itinerary`);
  assert.deepEqual(JSON.parse(JSON.stringify(profile.stops)), expected.stops, `${id}: atlas and site audit differ`);
  const route = mcp.executeMcpTool(runtime, 'inspect_person', { person: expected.atlasPerson }).person.events;
  assert.equal(route.length, expected.stops.length, `${id}: extra or missing route stops`);
  const phases = new Map(trajectory.phases.map(p => [p.id, p]));
  const careers = new Map(person.milestones.map(c => [c.id, c]));
  const assigned = new Set();
  for (const phase of trajectory.phases) {
    phaseCount++;
    const url = phaseUrl('http://localhost/', trajectory, phase);
    if (!phase.atlasStops.length) {
      assert.equal(url, '', `${id}/${phase.id}: no map link for an unlocated phase`);
      continue;
    }
    const first = phase.atlasStops[0], last = phase.atlasStops.at(-1);
    assert.equal(new URL(url).searchParams.get('stop'), first === last ? String(first) : `${first}-${last}`);
    for (const index of phase.atlasStops) {
      assert.ok(!assigned.has(index), `${id}: stop ${index} assigned twice`);
      assigned.add(index);
      assert.equal(expected.stops[index]?.phaseId, phase.id, `${id}: stop ${index} belongs to a different phase`);
    }
  }
  assert.equal(assigned.size, expected.stops.length, `${id}: orphaned map stops`);
  const overview = new URL(routeUrl('http://localhost/', trajectory));
  assert.equal(overview.searchParams.get('person'), expected.atlasPerson);
  assert.equal(overview.searchParams.get('stop'), null, `${id}: overview should not focus one phase`);
  for (const [i, stop] of expected.stops.entries()) {
    count++;
    assert.ok(Number.isInteger(stop.year), `${id}/${i}: integer sorting year`);
    assert.ok(i === 0 || stop.year >= expected.stops[i - 1].year, `${id}/${i}: chronological order`);
    assert.ok(stop.coord.length === 2 && stop.coord.every(Number.isFinite), `${id}/${i}: coordinates`);
    assert.ok(stop.coord[0] > 70 && stop.coord[0] < 140 && stop.coord[1] > 15 && stop.coord[1] < 55, `${id}/${i}: regional bounds`);
    assert.equal(route[i].site, stop.ancientZh, `${id}/${i}: rendered site name`);
    assert.deepEqual(Array.from(route[i].coord), stop.coord, `${id}/${i}: rendered coordinates`);
    const phase = phases.get(stop.phaseId);
    assert.ok(phase && stop.year >= phase.span[0] && stop.year <= phase.span[1], `${id}/${i}: phase year`);
    for (const careerId of stop.careerIds ?? [stop.careerId]) {
      assert.ok(careers.has(careerId), `${id}/${i}: missing career ${careerId}`);
      assert.ok(phase.careers.includes(careerId), `${id}/${i}: career outside phase`);
    }
    for (const location of stop.mergedLocations ?? []) {
      assert.ok(location.ancientZh && location.coord?.length === 2 && location.coord.every(Number.isFinite), `${id}/${i}: merged location`);
      assert.ok(location.year >= phase.span[0] && location.year <= phase.span[1], `${id}/${i}: merged location outside phase`);
      assert.ok(phase.careers.includes(location.careerId), `${id}/${i}: merged location career outside phase`);
    }
    assert.ok(stop.descZh && stop.quoteZh && stop.sourceRefs?.length, `${id}/${i}: evidence required`);
    for (const ref of stop.sourceRefs) {
      assert.ok(ref.quote.length > 0 && ref.quote.length <= 120, `${id}/${i}: short quotation`);
      assert.ok(sources.get(ref.blockId)?.includes(ref.quote), `${id}/${i}: quotation not in book ${ref.blockId}`);
      assert.equal(ref.volume, ref.blockId.slice(1, 4), `${id}/${i}: source volume`);
      assert.equal(ref.kind, ref.blockId.includes('-n') ? 'peizhu' : 'body', `${id}/${i}: source layer`);
      if (ref.kind === 'peizhu') assert.ok(ref.sourceBook, `${id}/${i}: annotation work required`);
    }
  }
  console.log(`${person.name}: ${trajectory.phases.length} phases / ${expected.stops.length} sourced stops`);
}
console.log(`Verified ${targets.length} Wei people, ${phaseCount} phases and ${count} stops against book, careers and atlas runtime.`);
