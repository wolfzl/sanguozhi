import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import crypto from 'node:crypto';

const sourceBytes = fs.readFileSync('src/data/book.json');
const book = JSON.parse(sourceBytes);
const sourceHash = crypto.createHash('sha256').update(sourceBytes).digest('hex');
const directory = 'src/data/translations';

for (const file of fs.readdirSync(directory).filter(file => file.endsWith('.json'))) {
  test(`${file} translates every source block and annotation in order`, () => {
    const translation = JSON.parse(fs.readFileSync(`${directory}/${file}`, 'utf8'));
    const source = book.volumes.find(volume => volume.id === translation.volumeId);
    assert.ok(source, 'source volume exists');
    assert.equal(file, `${source.id}.json`);
    assert.equal(translation.source.sourceSha256, sourceHash, 'translation matches current source edition');
    assert.equal(translation.status, 'draft', 'unreviewed translations remain drafts');
    assert.deepEqual(translation.blocks.map(block => block.id), source.blocks.map(block => block.id));
    for (const [index, block] of translation.blocks.entries()) {
      const original = source.blocks[index];
      assert.equal(Boolean(block.translation.trim()), Boolean(original.mainText.trim()), block.id);
      assert.deepEqual(block.notes.map(note => note.id), original.notes.map(note => note.id), block.id);
      for (const note of block.notes) assert.ok(note.translation.trim(), note.id + ' has a translation');
    }
    const blockIds = new Set(source.blocks.map(block => block.id));
    const sectionIds = translation.sections.map(section => section.startsAt);
    assert.equal(sectionIds.length, new Set(sectionIds).size, 'section starts are unique');
    for (const section of translation.sections) {
      assert.ok(blockIds.has(section.startsAt));
      assert.ok(section.title.trim());
    }
  });
}
