// 人物行迹地图：把人物卡的 trajectory（按时期分组）转成江山时序（jiangshan-map）的深链。
// 规则见 docs/atlas-trajectory-guide.md。本文件同时被页面和 Node 脚本使用，保持纯 JS。
//   模式一：trajectory.atlasPerson 存在，地图用江山时序自己的人物路线（?person=…&stop=…）。
//   模式二：已知时期的代表地点 place 连成本站路线；地点未详的时期不标点。

export const DEFAULT_ATLAS_BASE = 'http://127.0.0.1:8000/';

/** 去掉地图解析名里的括号注释，例如“下邳（睢宁）”→“下邳”。 */
export const stripNote = (name = '') => name.replace(/[（(][^）)]*[）)]/g, '').trim();

const build = (base, params) => {
  const url = new URL(base);
  for (const [k, v] of Object.entries(params)) if (v !== undefined && v !== null && v !== '') url.searchParams.set(k, String(v));
  return url.toString();
};

const spanOf = phases => [Math.min(...phases.map(p => p.span[0])), Math.max(...phases.map(p => p.span[1]))];

/** 时期对应的站号参数：一站写“3”，多站写区间“3-4”（江山时序会把整段路线高亮为实线）。 */
export function stopParam(stops = []) {
  if (!stops.length) return undefined;
  const first = stops[0], last = stops.at(-1);
  return last > first ? `${first}-${last}` : String(first);
}

/** 打开某个时期：模式一高亮该时期在江山时序路线上的全部站，模式二打开代表地点。 */
export function phaseUrl(base, trajectory, phase) {
  if (trajectory.atlasPerson) return build(base, { person: trajectory.atlasPerson, stop: stopParam(phase.atlasStops) });
  return phase.place ? build(base, { year: phase.place.mapYear, place: phase.place.query }) : '';
}

/** 整条路线。embed=true 时生成嵌入用地址，并把时间轴限定在各时期的起止年之间。 */
export function routeUrl(base, trajectory, { embed = false } = {}) {
  const phases = trajectory?.phases ?? [];
  if (!phases.length) return '';
  const [from, to] = spanOf(phases);
  const range = embed ? { from, to } : {};
  const head = embed ? { embed: 1 } : {};
  if (trajectory.atlasPerson) return build(base, { ...head, person: trajectory.atlasPerson, ...range });
  const placed = phases.filter(p => p.place);
  if (!placed.length) return '';
  return build(base, {
    ...head,
    year: placed.map(p => p.place.mapYear).join(','),
    place: placed.map(p => p.place.query).join(','),
    ...range,
  });
}

/** 时期序号用的中文数字（时期最多 8 个）。 */
export const phaseNumeral = i => '一二三四五六七八九十'[i] ?? String(i + 1);
