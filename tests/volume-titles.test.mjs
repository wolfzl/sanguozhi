import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';

const book = JSON.parse(fs.readFileSync('src/data/book.json', 'utf8'));
const titles = JSON.parse(fs.readFileSync('src/data/volume-titles.json', 'utf8'));

test('every volume has a display title in the 「魏书 · 卷名」 format', () => {
  assert.equal(Object.keys(titles).length, book.volumes.length);
  for (const volume of book.volumes) {
    const title = titles[volume.id];
    assert.ok(title, `${volume.id} has a display title`);
    if (volume.id === 'appendix') { assert.equal(title, '上三国志注表'); continue; }
    assert.match(title, /^(魏|蜀|吴)书 · [^\s·《》（）()第]+$/, `${volume.id}: ${title}`);
    const number = Number(volume.id);
    const expected = number <= 30 ? '魏书' : number <= 45 ? '蜀书' : '吴书';
    assert.ok(title.startsWith(`${expected} · `), `${volume.id} belongs to ${expected}`);
    assert.doesNotMatch(title, /[呉歩傳書紀]/, `${volume.id} uses simplified characters`);
  }
});

test('previously inconsistent volume titles are normalised', () => {
  assert.equal(titles['030'], '魏书 · 乌丸鲜卑东夷传');
  assert.equal(titles['048'], '吴书 · 三嗣主传');
  assert.equal(titles['050'], '吴书 · 妃嫔传');
  assert.equal(titles['052'], '吴书 · 张顾诸葛步传');
  assert.equal(titles['055'], '吴书 · 程黄韩蒋周陈董甘凌徐潘丁传');
  assert.equal(titles['059'], '吴书 · 吴主五子传');
});
