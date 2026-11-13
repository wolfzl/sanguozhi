#!/usr/bin/env node
// 行迹地图工具，规则见 docs/atlas-trajectory-guide.md。
//   node scripts/atlas-places.mjs person liubei                 列出江山时序人物路线和站号（从 0 数）
//   node scripts/atlas-places.mjs lookup 安喜 中山 --year 184   试查询名（模式二）
//   node scripts/atlas-places.mjs check [id ...]               检查站号年份（模式一）或地名解析（模式二）
// 依赖本机的江山时序项目：默认 ~/ai/github/jiangshan-map，可用 JIANGSHAN_DIR 指定。
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { createRequire } from 'node:module';
import { stripNote } from '../src/lib/atlas.mjs';

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

/** 江山时序人物路线的各站；没有这个人物时返回 null。 */
function personRoute(key) {
  try {
    return mcp.executeMcpTool(runtime, 'inspect_person', { person: key }).person.events;
  } catch {
    return null;
  }
}

const [command, ...rest] = process.argv.slice(2);

if (command === 'person') {
  if (!rest.length) { console.error('用法：person <江山时序人物 key...>'); process.exit(2); }
  for (const key of rest) {
    const route = personRoute(key);
    if (!route) { console.log(`${key}：江山时序中没有这个人物`); continue; }
    console.log(`${key}：共 ${route.length} 站（站号从 0 数）`);
    for (const e of route) console.log(`  ${String(e.index).padStart(2)}  ${e.year}  ${e.site}｜${e.text}`);
  }
} else if (command === 'lookup') {
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
  const targets = rest.length ? people.filter(p => rest.includes(p.id)) : people.filter(p => p.dossier?.trajectory);
  if (rest.length && targets.length !== rest.length) { console.error(`未知人物 id：${rest.filter(id => !people.some(p => p.id === id)).join(', ')}`); process.exit(2); }
  const errors = [];
  for (const p of targets) {
    const t = p.dossier?.trajectory;
    if (!t) { errors.push(`${p.id}: 没有 trajectory`); continue; }
    if (t.atlasPerson) {
      const route = personRoute(t.atlasPerson);
      if (!route) { errors.push(`${p.id}: 江山时序中没有人物 ${t.atlasPerson}`); continue; }
      const used = new Set(t.phases.flatMap(ph => ph.atlasStops));
      console.log(`\n${p.name}（${p.id}）：模式一，江山时序 ${t.atlasPerson} 共 ${route.length} 站，挂上 ${used.size} 站，${t.phases.length} 个时期`);
      for (const [i, ph] of t.phases.entries()) {
        const parts = ph.atlasStops.map(n => {
          const e = route[n];
          if (!e) { errors.push(`${p.id}/${ph.id}: 站号 ${n} 不存在`); return `${n}✗`; }
          if (e.year < ph.span[0] || e.year > ph.span[1]) errors.push(`${p.id}/${ph.id}: atlas stop year outside span，站 ${n}（${e.year} ${e.site}）不在 ${ph.span.join('—')}`);
          return `${n} ${e.year} ${e.site}`;
        });
        console.log(`  ${i + 1}. ${ph.title}（${ph.when}，${ph.careers.length} 行）→ ${parts.join('；') || '未挂站'}`);
      }
      const unused = route.filter(e => !used.has(e.index));
      if (unused.length) console.log(`  未挂的站：${unused.map(e => `${e.index} ${e.year} ${e.site}`).join('；')}`);
    } else {
      console.log(`\n${p.name}（${p.id}）：模式二，${t.phases.length} 个时期`);
      for (const [i, ph] of t.phases.entries()) {
        const pl = ph.place;
        const r = resolve(pl.query, pl.mapYear);
        const at = `${p.id}/${ph.id}`;
        let flag = '';
        if (!r) { errors.push(`${at}: 未识别 ${pl.query}`); flag = ' ✗ 未识别'; }
        else {
          if (!(r.province.startsWith(pl.province) || r.modern.includes(pl.province))) { errors.push(`${at}: province mismatch ${pl.query} → ${r.name}（${r.province || r.modern || '省份未知'}），应为 ${pl.province}`); flag += ' ✗ 省份不符'; }
          const shouldApprox = stripNote(r.name) !== pl.name;
          if (shouldApprox !== Boolean(pl.approx)) { errors.push(`${at}: approx should be ${shouldApprox ? 'True' : 'False'}（${pl.name} → ${r.name}）`); flag += ' ✗ approx'; }
          else if (shouldApprox) flag += ' 近似，需在浏览器中确认';
        }
        console.log(`  ${i + 1}. ${ph.title}（${ph.when}）${pl.mapYear} ${pl.name} ⇢ ${pl.query} → ${r ? `${r.name}（${r.modern || r.province}）` : '—'}${flag}`);
      }
    }
  }
  if (errors.length) { console.error(`\n${errors.length} 个错误：\n${errors.map(e => '  ' + e).join('\n')}`); process.exit(1); }
  console.log('\natlas trajectory ok');
} else {
  console.error('用法：node scripts/atlas-places.mjs person <key...> | lookup <地名...> [--year 年份] | check [id ...]');
  process.exit(2);
}
