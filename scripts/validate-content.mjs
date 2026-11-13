import fs from "node:fs";
import assert from "node:assert/strict";
import {
  validateReferences,
  collectReferences,
  validateTimeline,
  validatePersonEventLinks,
  validatePortraits,
  validatePersonDossiers,
  validateV3Profiles,
  validateTrajectory,
} from "./content-validation.mjs";
const book = JSON.parse(fs.readFileSync("src/data/book.json", "utf8"));
const edition = JSON.parse(fs.readFileSync("src/data/edition.json", "utf8"));
const { people, events, eventRelations = [] } = JSON.parse(
  fs.readFileSync("src/data/cards.json", "utf8"),
);
assert.equal(book.volumes.length, 66);
assert.deepEqual(
  book.volumes.slice(0, 65).map((v) => Number(v.id)),
  Array.from({ length: 65 }, (_, i) => i + 1),
);
assert.equal(book.volumes.at(-1).title, "上三國志註表");
assert.equal(people.length, edition.people);
assert.equal(events.length, edition.events);
assert.equal(events.filter(e=>e.importance==='key').length,edition.keyEvents);
assert.equal(Math.min(...events.map(e=>e.year)),edition.startYear);
assert.equal(Math.max(...events.map(e=>e.endYear)),edition.endYear);
assert.deepEqual(validateTimeline(events,eventRelations),[]);
assert.deepEqual(validatePersonEventLinks(people,events),[]);
assert.deepEqual(validatePortraits(people,book),[]);
assert.deepEqual(validatePersonDossiers(people,{requireAll:true}),[]);
assert.deepEqual(validateV3Profiles(people),[]);
assert.deepEqual(validateTrajectory(people),[]);
for (const records of [people, events, eventRelations, book.volumes])
  assert.equal(
    new Set(records.map((r) => r.id)).size,
    records.length,
    "Duplicate ID",
  );
const allRefs = collectReferences({ people, events, eventRelations });
assert.deepEqual(validateReferences(book, allRefs), []);
for (const v of book.volumes) {
  assert.ok(
    v.blocks.length > 0 && v.sourceUrl && v.revision,
    `Empty or untraceable volume ${v.id}`,
  );
  const ids = v.blocks.flatMap((b) => [
    b.id,
    ...b.notes.filter((n) => n.id !== b.id).map((n) => n.id),
  ]);
  assert.equal(new Set(ids).size, ids.length, `Duplicate anchor ${v.id}`);
  assert.ok(
    !v.blocks.some((b) => b.text.includes("\ufffd")),
    `Replacement character ${v.id}`,
  );
}
for (const p of people) {
  const length = p.paragraphs.reduce((sum, x) => sum + x.text.length, 0);
  assert.ok(
    length >= 300 && length <= (p.dossier?.expanded ? 6000 : p.dossier ? 800 : 500),
    `${p.name}: biography length ${length}`,
  );
  assert.ok(p.milestones.length >= 3 && p.milestones.length <= (p.dossier?.expanded ? 80 : p.dossier ? 12 : 8));
  for (const part of [...p.paragraphs, ...p.milestones, ...p.relations])
    assert.ok(part.refs.length);
  for (const r of p.relations)
    assert.ok(
      people.some((x) => x.id === r.personId),
      `Unknown relation ${r.personId}`,
    );
  for (const id of p.eventIds)
    assert.ok(
      events
        .find((e) => e.id === id)
        ?.participants.some((x) => x.personId === p.id),
    );
  for (const id of p.reading) assert.ok(book.volumes.some((v) => v.id === id));
}
for (const e of events) {
  const length = e.sections.reduce((sum, x) => sum + x.text.length, 0);
  assert.ok(length >= 400 && length <= 700, `${e.title}: length ${length}`);
  assert.ok(Number.isInteger(e.year));
  for (const s of e.sections) assert.ok(s.refs.length);
  for (const p of e.participants) {
    if(p.personId) assert.ok(people.find((x) => x.id === p.personId)?.eventIds.includes(e.id), `Broken reciprocal participant ${e.id}/${p.personId}`);
    else assert.ok(p.name, `Unnamed participant ${e.id}`);
  }
}
console.log(
  `Validated 66 volumes, ${people.length} people, ${events.length} events, ${eventRelations.length} relationships, ${allRefs.length} references; quotations, layers and reciprocal links valid.`,
);
