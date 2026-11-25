// 阅读器人物反向链接：在每个正文段落里，给已建档人物的姓名首次出现处加指向 /people/<id>/ 的低调链接。
//
// 匹配规则（宁缺毋滥）：
// - 只匹配人物卡里的全名（至少两个字）；不处理单字名、「曹公」「太祖」等称谓和字号。
// - 以简体形式匹配：繁体底本先经 OpenCC（与阅读器同一转换）转成简体再找名字，只在逐字对应时才回写位置，
//   因此底本里繁简混用的字形也能命中，而底本文字本身一字不改，只是给命中处套上 <a>。
// - 每个段落每位人物最多链接一次；已在 <a> 内、裴注（行内注文）内、标题和独立注文块中的名字一律跳过。
// - 同名的多张人物卡（目前没有）会被整体跳过；被更长的已建档姓名包含的短名按最长优先处理。
import { Converter } from 'opencc-js/t2cn';
import { people } from './catalog';

const simplify = Converter({ from: 't', to: 'cn' });

interface Entry { id: string; name: string }
// 同时收录人物卡原写法与 OpenCC 转换后的写法（如「孙乾」→「孙干」），白话文本用前者，繁体底本转简体后用后者。
const byName = new Map<string, Entry[]>();
const add = (name: string, id: string) => {
  if (name.length < 2) return;
  const list = byName.get(name) ?? [];
  if (!list.some(entry => entry.id === id)) byName.set(name, [...list, { id, name }]);
};
for (const p of people) { add(p.name, p.id); add(simplify(p.name), p.id); }
// 同名多张人物卡则整体跳过（目前没有）。
const entries: Entry[] = [...byName.values()].filter(list => list.length === 1).map(list => list[0]);
entries.sort((a, b) => b.name.length - a.name.length);
const escape = (s: string) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
const pattern = new RegExp(entries.map(e => escape(e.name)).join('|'), 'g');
const idByName = new Map(entries.map(e => [e.name, e.id]));

// 名字撞上常用词的几个例外：（前文，后文）任一命中即不链接。例如「于禁中」「无法正面抵挡」。
const guards: Record<string, { before?: RegExp; after?: RegExp }> = {
  于禁: { after: /^[中门庭省闼内]/ },
  法正: { before: /[无办想用方做作设没]$/, after: /^[面确当式视常义]/ },
};

export const personLinkTags = new Set(['p', 'blockquote', 'div', 'dl']);

export interface LinkPart { text: string; personId?: string }

/** 在一段纯文本里找出尚未链接过的人物姓名，返回切好的片段；位置以原文字符为准。 */
export function splitPeople(text: string, seen: Set<string>, convert = true): LinkPart[] {
  const simple = convert ? simplify(text) : text;
  // 繁简转换必须逐字对应才可回写位置，否则整段不处理。
  if (simple.length !== text.length) return [{ text }];
  const parts: LinkPart[] = [];
  let last = 0;
  for (const match of simple.matchAll(pattern)) {
    const name = match[0];
    const at = match.index!;
    const id = idByName.get(name);
    if (!id || seen.has(id)) continue;
    const guard = guards[name];
    if (guard && (guard.before?.test(simple.slice(0, at)) || guard.after?.test(simple.slice(at + name.length)))) continue;
    seen.add(id);
    if (at > last) parts.push({ text: text.slice(last, at) });
    parts.push({ text: text.slice(at, at + name.length), personId: id });
    last = at + name.length;
  }
  if (last < text.length) parts.push({ text: text.slice(last) });
  return parts.length ? parts : [{ text }];
}

const link = (part: LinkPart) => part.personId
  ? `<a class="person-link" href="/people/${part.personId}/" title="查看人物页">${part.text}</a>`
  : part.text;

/** 给一个原文块的 HTML 加人物链接。只改文字节点外包的 <a>，不改任何原有标签、id 与文字。 */
export function linkPeopleInHtml(html: string, tag: string, kind: string): string {
  if (kind !== 'body' || !personLinkTags.has(tag)) return html;
  const seen = new Set<string>();
  const tokens = html.split(/(<[^>]*>)/);
  let anchorDepth = 0;
  const spanStack: boolean[] = [];
  return tokens.map(token => {
    if (token.startsWith('<')) {
      if (/^<a[\s>]/i.test(token)) anchorDepth++;
      else if (/^<\/a>/i.test(token)) anchorDepth = Math.max(0, anchorDepth - 1);
      else if (/^<span[\s>]/i.test(token)) spanStack.push((spanStack.at(-1) ?? false) || /class="[^"]*\bpeizhu\b/.test(token));
      else if (/^<\/span>/i.test(token)) spanStack.pop();
      return token;
    }
    if (!token || anchorDepth > 0 || spanStack.at(-1)) return token;
    // 文字里的 HTML 实体（&amp; 等）不含汉字，只在含实体时保守跳过整个节点，避免位置错位。
    if (token.includes('&')) return token;
    return splitPeople(token, seen).map(link).join('');
  }).join('');
}
