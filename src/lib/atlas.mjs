// 人物行迹地图：把人物卡的 trajectory（按时期分组）转成江山时序（jiangshan-map）的深链。
// 规则见 docs/guides/atlas-trajectory-guide.md。本文件同时被页面和 Node 脚本使用，保持纯 JS。
//   模式一：trajectory.atlasPerson 存在，地图用江山时序自己的人物路线（?person=…&stop=…）。
//   模式二：已知时期的代表地点 place 连成本站路线；地点未详的时期不标点。

export const DEFAULT_ATLAS_BASE = 'http://127.0.0.1:8000/';

/** Refresh the atlas HTML as well as its hashed assets after a site deployment. */
export function versionedAtlasBase(base, revision) {
  const url = new URL(base);
  url.searchParams.set('sgz_rev', revision);
  return url.toString();
}

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
  if (trajectory.atlasPerson) return phase.atlasStops?.length
    ? build(base, { person: trajectory.atlasPerson, stop: stopParam(phase.atlasStops) }) : '';
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

// 三大战役推演：江山时序（atlas_campaigns.js）里的分阶段战役回放，按本站事件 id 对应。
// key、年份范围与阶段数须与江山时序的 CAMPAIGNS 条目一致（?campaign=<key>&cphase=<从 1 开始>）。
export const CAMPAIGNS = {
  guandu: { key: 'guandu', title: '官渡之战', from: 199, to: 200, phases: 7, sides: '曹操 vs 袁绍', hook: '声西击东解白马，两军相持官渡；许攸来奔，曹操夜袭乌巢，袁绍败北。' },
  chibi: { key: 'chibi', title: '赤壁之战', from: 208, to: 208, phases: 6, sides: '曹操 vs 孙刘联军', hook: '孙刘合兵沿江迎击；黄盖诈降，火船延烧曹军营落，曹操北归。' },
  yiling: { key: 'yiling', title: '夷陵之战', from: 221, to: 222, phases: 6, sides: '刘备 vs 孙权', hook: '刘备东征驻营猇亭，陆逊持军不出；纵火并破连营，刘备退至白帝。' },
};

/** 战役推演地址。embed=true 时生成嵌入地址，并把时间轴限定在战役年份范围内。 */
export function campaignUrl(base, campaign, { embed = false, phase = 1 } = {}) {
  if (!campaign) return '';
  return build(base, {
    ...(embed ? { embed: 1, from: campaign.from, to: campaign.to } : { year: campaign.from }),
    campaign: campaign.key,
    cphase: phase,
  });
}
