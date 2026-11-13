#!/usr/bin/env node
// 行迹地点工具，规则见 docs/atlas-trajectory-guide.md。
//   node scripts/atlas-places.mjs lookup 安喜 中山 --year 184   试查询名
//   node scripts/atlas-places.mjs check [id ...]               检查 M3、M4（默认检查所有标了地点的人物）
// 依赖本机的江山时序项目：默认 ~/ai/github/jiangshan-map，可用 JIANGSHAN_DIR 指定。
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { createRequire } from 'node:module';
import { stripNote, trajectoryStops } from '../src/lib/atlas.mjs';

const dir = process.env.JIANGSHAN_DIR ?? path.join(os.homedir(), 'ai/github/jiangshan-map');
const serverPath = path.join(dir, 'scripts/mcp_server.js');
if (!fs.existsSync(serverPath)) {
  console.error(`找不到江山时序项目：${serverPath}\n请用 JIANGSHAN_DIR 指定 jiangshan-map 的目录。`);
  process.exit(2);
}
const mcp = createRequire(import.meta.url)(serverPath);
const runtime = mcp.createMcpRuntime();

/** 解析一个地名；识别不了时返回 null。 */
function resolve(place, year) {
  try {
    const r = mcp.executeMcpTool(runtime, 'inspect_place', { year, place });
    return { name: r.resolvedName, modern: r.modern || '', province: r.modernProvince || '', coord: r.coord, polity: r.polity };
  } catch {
    return null;
  }
}

const [command, ...rest] = process.argv.slice(2);

if (command === 'lookup') {
  const yearAt = rest.indexOf('--year');
  const year = yearAt >= 0 ? Number(rest[yearAt + 1]) : 200;
  const names = rest.filter((_, i) => i !== yearAt && i !== yearAt + 1);
  if (!names.length) { console.error('用法：lookup <地名...> [--year 年份]'); process.exit(2); }
  for (const n of names) {
    const r = resolve(n, year);
    console.log(r ? `${n} → ${r.name}｜今 ${r.modern || '—'}｜${r.province || '省份未知'}｜[${r.coord}]｜时属 ${r.polity ?? '—'}` : `${n} → 未识别`);
  }
} else if (command === 'check') {
  const { people } = JSON.parse(fs.readFileSync('src/data/cards.json', 'utf8'));
  const targets = rest.length ? people.filter(p => rest.includes(p.id)) : people.filter(p => p.milestones.some(m => m.place));
  if (rest.length && targets.length !== rest.length) { console.error(`未知人物 id：${rest.filter(id => !people.some(p => p.id === id)).join(', ')}`); process.exit(2); }
  const errors = [];
  for (const p of targets) {
    const rows = p.milestones.filter(m => m.place);
    if (!rows.length) { errors.push(`${p.id}: 没有标注地点`); continue; }
    console.log(`\n${p.name}（${p.id}）：年表 ${p.milestones.length} 行，标地点 ${rows.length} 行，合并后 ${trajectoryStops(p.milestones).length} 站`);
    for (const m of rows) {
      const pl = m.place;
      const r = resolve(pl.query, pl.mapYear);
      const at = `${p.id}/${m.id}`;
      let flag = '';
      if (!r) { errors.push(`${at}: 未识别 ${pl.query}`); flag = '✗ 未识别'; }
      else {
        if (!(r.province.startsWith(pl.province) || r.modern.includes(pl.province))) { errors.push(`${at}: province mismatch ${pl.query} → ${r.name}（${r.province || r.modern || '省份未知'}），应为 ${pl.province}`); flag += ' ✗ 省份不符'; }
        const shouldApprox = stripNote(r.name) !== pl.name;
        if (shouldApprox !== Boolean(pl.approx)) { errors.push(`${at}: approx should be ${shouldApprox ? 'True' : 'False'}（${pl.name} → ${r.name}）`); flag += ' ✗ approx'; }
        else if (shouldApprox) flag += ' 近似，需在浏览器中确认';
      }
      console.log(`  ${m.id.padEnd(14)} ${String(pl.mapYear).padEnd(5)} ${pl.name} ⇢ ${pl.query} → ${r ? `${r.name}（${r.modern || r.province}）` : '—'}${flag}`);
    }
  }
  if (errors.length) { console.error(`\n${errors.length} 个错误：\n${errors.map(e => '  ' + e).join('\n')}`); process.exit(1); }
  console.log('\natlas places ok');
} else {
  console.error('用法：node scripts/atlas-places.mjs lookup <地名...> [--year 年份] | check [id ...]');
  process.exit(2);
}
