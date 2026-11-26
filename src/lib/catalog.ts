import bookData from "../data/book.json";
import cardData from "../data/cards.json";
import volumeTitleData from "../data/volume-titles.json";
import { Converter } from "opencc-js/t2cn";

export interface SourceRef {
  volume: string;
  blockId: string;
  kind: "body" | "peizhu";
  quote: string;
  sourceBook?: string;
}
export interface Paragraph {
  text: string;
  title?: string;
  refs: SourceRef[];
  eventLinks?: { label: string; eventId: string }[];
}
export interface SourceNote {
  title: string;
  text: string;
  refs: SourceRef[];
}
export interface DossierRecord extends Paragraph {
  when: string;
  title: string;
  category: string;
  group?: string;
  eventIds?: string[];
}
export interface PersonDossier {
  trajectory?: Trajectory;
  expanded?: boolean;
  sourceScope?: string;
  factDetails?: {label: string; text: string; refs: SourceRef[]}[];
  scholarship?: SourceNote[];
  assessment?: SourceNote[];
  readingNotes?: SourceNote[];
  contextRelations?: (SourceNote & {category: string; people: {name: string; personId: string}[]})[];
  appendixRefs?: SourceRef[];
  relatedEventNotes?: {eventId: string; label: string; text: string}[];
  tier: '核心人物' | '拓展人物' | '背景人物';
  hometown: string;
  highestOffice: string;
  highestTitle: string;
  posthumous: string;
  deeds: string[];
  refs: SourceRef[];
  civil: DossierRecord[];
  civilNote: string;
  military: DossierRecord[];
  militaryNote?: string;
  setbacks: DossierRecord[];
  setbacksNote?: string;
  extraRelations: {name: string; label: string; refs: SourceRef[]; people?: {name: string; personId: string}[]}[];
  glossary: {term: string; text: string}[];
}
export interface Person {
  id: string;
  name: string;
  courtesy: string;
  faction: string;
  role: string;
  lead: string;
  period: string;
  lifespan?: { text: string; sourceTitle: string; sourceUrl: string; quote: string; note: string };
  dossier?: PersonDossier;
  aliases: string[];
  tags: string[];
  paragraphs: Paragraph[];
  milestones: (Paragraph & { id?: string; when: string; title: string; office?: string; eventIds?: string[] })[];
  relations: { personId: string; label: string; refs: SourceRef[] }[];
  reading: string[];
  eventIds: string[];
  note: SourceNote | null;
}
/** 行迹时期，见 docs/guides/atlas-trajectory-guide.md。 */
export interface AtlasPlace { name: string; query: string; province: string; mapYear: number; approx?: boolean }
export interface TrajectoryPhase { id: string; title: string; when: string; span: [number, number]; careers: string[]; atlasStops?: number[]; place?: AtlasPlace; unmappedReason?: string }
export interface Trajectory { atlasPerson?: string; phases: TrajectoryPhase[] }
export interface Event {
  id: string;
  title: string;
  time: string;
  year: number;
  lead: string;
  aliases: string[];
  tags: string[];
  endYear: number;
  order: number;
  phase: "formation" | "states" | "unification";
  lanes: ("common" | "wei" | "shu" | "wu" | "lords")[];
  importance: "key" | "standard";
  categories: ("war" | "state" | "succession" | "diplomacy" | "governance")[];
  participants: { personId?: string; name?: string; role: string }[];
  sections: (Paragraph & { heading: string; interpretation: boolean })[];
  note: SourceNote | null;
}
export interface EventRelation {
  id: string;
  from: string;
  to: string;
  type: "context" | "process" | "parallel" | "succession";
  summary: string;
  interpretation: boolean;
  refs: SourceRef[];
}
export interface Volume {
  id: string;
  title: string;
  epubPath: string;
  sourceUrl: string;
  revision: string;
  permalink: string;
  blocks: {
    id: string;
    tag: string;
    kind: string;
    text: string;
    mainText: string;
    html: string;
    notes: { id: string; text: string; books: string[] }[];
  }[];
}
export const book = bookData;
export const volumes = bookData.volumes as Volume[];
export const people = cardData.people as Person[];
export const events = (cardData.events as unknown as Event[]).sort(
  (a, b) => a.year - b.year || a.order - b.order,
);
const simplify = Converter({ from: "tw", to: "cn" });
/**
 * 卷目显示名：统一为「魏书 · 卷名」。显示名由 src/data/volume-titles.json 按卷号给出，
 * 不依赖 EPUB 提取出的原始标题（其中混有繁简、「第十」「卷五十五」等不一致写法），
 * 因此重新提取原书不会让卷名回退。book.json 保持不变以固定来源哈希。
 */
const volumeTitles = volumeTitleData as Record<string, string>;
export function volumeTitle(v: Volume) {
  const fixed = volumeTitles[v.id];
  if (fixed) return fixed;
  return simplify(v.title)
    .replace(/^卷\d+\s*/, "")
    .replace(/[•]/g, "·")
    .replace(/呉/g, "吴")
    .replace(/·/g, " · ")
    .replace(/\s+/g, " ")
    .trim();
}
export function refKey(ref: SourceRef) {
  return `${ref.blockId}:${ref.quote}`;
}
export function referencesFor(record: unknown): SourceRef[] {
  const result: SourceRef[] = [];
  const seen = new Set<string>();
  function walk(value: unknown) {
    if (!value || typeof value !== "object") return;
    if (Array.isArray(value)) return value.forEach(walk);
    const obj = value as Record<string, unknown>;
    if ("blockId" in obj && "quote" in obj) {
      const ref = obj as unknown as SourceRef;
      if (!seen.has(refKey(ref))) {
        seen.add(refKey(ref));
        result.push(ref);
      }
    } else Object.values(obj).forEach(walk);
  }
  walk(record);
  return result;
}
export function refLabel(ref: SourceRef) {
  return `卷${Number(ref.volume)} · ${ref.kind === "peizhu" ? `裴注${/裴松之|评论|按语/.test(ref.sourceBook ?? "") ? " · " : "引 "}${ref.sourceBook ?? "文献"}` : "陈寿正文"}`;
}
export function personById(id: string) {
  return people.find((p) => p.id === id)!;
}
export function eventById(id: string) {
  return events.find((e) => e.id === id)!;
}

export const eventRelations = (cardData as unknown as {eventRelations?: EventRelation[]}).eventRelations ?? [];
export function relationsForEvent(id: string) {
  return eventRelations.filter(r => r.from === id || r.to === id);
}
export function participantName(p: Event["participants"][number]) {
  return p.personId ? personById(p.personId).name : p.name ?? "";
}
