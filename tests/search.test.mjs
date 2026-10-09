import { test } from 'node:test';
import assert from 'node:assert/strict';
import { normalizeSearch, matchesCard } from '../src/lib/search.mjs';

const liubei = { name: '刘备', aliases: ['刘玄德', '先主'], courtesy: '玄德', faction: '蜀汉', tags: ['入蜀'] };
test('finds a simplified-name card using traditional characters and spaces', () => {
  assert.equal(normalizeSearch(' 劉 備 '), '刘备');
  assert.equal(matchesCard(liubei, '劉備'), true);
});
test('matches courtesy names and aliases but rejects unrelated queries', () => {
  assert.equal(matchesCard(liubei, '玄德'), true);
  assert.equal(matchesCard(liubei, '先主'), true);
  assert.equal(matchesCard(liubei, '不存在的人'), false);
});
test('combines faction and query rather than treating filters as alternatives', () => {
  assert.equal(matchesCard(liubei, '', '蜀汉'), true);
  assert.equal(matchesCard(liubei, '刘备', '孙吴'), false);
});
test('supports traditional event titles and resets on an empty query', () => {
  const event = { title: '诸葛亮首次北伐', aliases: ['祁山之战', '街亭'], tags: [] };
  assert.equal(matchesCard(event, '諸葛亮'), true);
  assert.equal(matchesCard(event, '街亭'), true);
  assert.equal(matchesCard(event, ''), true);
  assert.equal(matchesCard(event, '官渡'), false);
});
