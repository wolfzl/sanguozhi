import { test } from 'node:test';
import assert from 'node:assert/strict';
import { validateReferences } from '../scripts/content-validation.mjs';
const book = { volumes: [{ id: '001', blocks: [{ id: 'v001-b0001', mainText: '正文甲乙。', notes: [{ id: 'v001-b0001-n01', text: '注文丙丁。' }] }] }] };
test('rejects dangling source anchors before generating a card page', () => {
  assert.equal(validateReferences(book, [{ volume: '001', blockId: 'missing', kind: 'body', quote: '甲乙' }]).length, 1);
});
test('rejects an invented quotation and annotation presented as main text', () => {
  assert.equal(validateReferences(book, [{ volume: '001', blockId: 'v001-b0001', kind: 'body', quote: '从未出现' }]).length, 1);
  assert.equal(validateReferences(book, [{ volume: '001', blockId: 'v001-b0001-n01', kind: 'body', quote: '注文丙丁' }]).length, 1);
});
test('accepts matching main text and separately identified annotation quotes', () => {
  assert.deepEqual(validateReferences(book, [
    { volume: '001', blockId: 'v001-b0001', kind: 'body', quote: '甲乙' },
    { volume: '001', blockId: 'v001-b0001-n01', kind: 'peizhu', quote: '丙丁', sourceBook: '测试文献' },
  ]), []);
});
