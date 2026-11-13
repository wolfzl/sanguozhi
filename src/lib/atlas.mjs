// 人物行迹地图：把生平履历中的 place 字段转成江山时序（jiangshan-map）的深链。
// 规则见 docs/atlas-trajectory-guide.md。本文件同时被页面和 Node 脚本使用，保持纯 JS。

export const DEFAULT_ATLAS_BASE = 'http://127.0.0.1:8000/';

/** 去掉地图解析名里的括号注释，例如“下邳（睢宁）”→“下邳”。 */
export const stripNote = (name = '') => name.replace(/[（(][^）)]*[）)]/g, '').trim();

/** 生平履历中有地点的行，按顺序合并相邻的同一查询地点。 */
export function trajectoryStops(milestones = []) {
  const stops = [];
  for (const row of milestones) {
    const place = row.place;
    if (!place) continue;
    const last = stops.at(-1);
    if (last && last.query === place.query) { last.rows.push(row); continue; }
    stops.push({ query: place.query, name: place.name, year: place.mapYear, approx: Boolean(place.approx), rows: [row] });
  }
  return stops.map((stop, i) => ({ ...stop, index: i + 1 }));
}

const join = (base, params) => {
  const url = new URL(base);
  for (const [k, v] of Object.entries(params)) if (v !== undefined && v !== null && v !== '') url.searchParams.set(k, String(v));
  return url.toString();
};

/** 单个地点：打开那一年、那个地方。 */
export const placeUrl = (base, place) => join(base, { year: place.mapYear, place: place.query });

/** 全程路线。embed=true 时生成嵌入用地址，并把时间轴限定在首末站之间。 */
export function routeUrl(base, stops, { embed = false } = {}) {
  if (!stops.length) return '';
  const years = stops.map(s => s.year);
  return join(base, {
    ...(embed ? { embed: 1 } : {}),
    year: years.join(','),
    place: stops.map(s => s.query).join(','),
    ...(embed ? { from: Math.min(...years), to: Math.max(...years) } : {}),
  });
}

/** 从 when 文字中取出年份区间；没有年份时返回 null。 */
export function whenRange(when = '') {
  const years = (when.match(/\d{2,4}(?=\s*[年—–-])/g) ?? []).map(Number);
  return years.length ? [Math.min(...years), Math.max(...years)] : null;
}
