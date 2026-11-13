export function validateReferences(book, refs) {
  const errors = [];
  for (const ref of refs) {
    const volume = book.volumes.find((v) => v.id === ref.volume);
    const block = volume?.blocks.find((b) => b.id === ref.blockId);
    const note = volume?.blocks
      .flatMap((b) => b.notes)
      .find((n) => n.id === ref.blockId);
    const text = ref.kind === "peizhu" ? note?.text : block?.mainText;
    if (!text || !ref.quote || !text.includes(ref.quote))
      errors.push(`Invalid ${ref.kind} quote at ${ref.volume}/${ref.blockId}`);
    else if (ref.kind === "peizhu" && !ref.sourceBook)
      errors.push(`Missing cited work at ${ref.blockId}`);
  }
  return errors;
}
export function collectReferences(value) {
  if (!value || typeof value !== "object") return [];
  if (Array.isArray(value)) return value.flatMap(collectReferences);
  if ("blockId" in value && "quote" in value) return [value];
  return Object.values(value).flatMap(collectReferences);
}

export function validatePortraits(people, book) {
  const errors = [];
  for (const p of people) {
    const life = p.lifespan;
    if (!life || ['text','sourceTitle','sourceUrl','quote','note'].some(key=>!life[key]?.trim())) {
      errors.push(`Missing lifespan evidence ${p.id}`);
    } else if (life.sourceUrl.startsWith('/')) {
      const match = life.sourceUrl.match(/^\/read\/(\d{3})\/#(v\d{3}-b\d{4}(?:-n\d{2})?)$/);
      const volume = book.volumes.find(v=>v.id===match?.[1]);
      const sources = volume?.blocks.flatMap(b=>[{id:b.id,text:b.mainText},...b.notes]) ?? [];
      if (!sources.find(s=>s.id===match?.[2])?.text.includes(life.quote)) errors.push(`Invalid lifespan quote ${p.id}`);
    } else if (!life.sourceUrl.startsWith('https://')) errors.push(`Invalid lifespan URL ${p.id}`);
    if (!p.courtesy?.trim()) errors.push(`Empty courtesy name ${p.id}`);
    if (!p.paragraphs.some(part=>part.eventLinks?.length)) errors.push(`Portrait without narrative events ${p.id}`);
    if (!p.milestones.some(part=>part.eventIds?.length)) errors.push(`Portrait without milestone events ${p.id}`);
    if (p.milestones.some(part=>!part.when?.includes('年'))) errors.push(`Undated milestone ${p.id}`);
    const ids = p.relations.map(r=>r.personId);
    if (ids.includes(p.id) || new Set(ids).size!==ids.length) errors.push(`Duplicate or self relation ${p.id}`);
  }
  return errors;
}

export function validatePersonEventLinks(people, events) {
  const errors = [];
  const byId = new Map(events.map(event=>[event.id,event]));
  for (const person of people) {
    const targets = (person.dossier?.relatedEventNotes ?? []).map(note=>note.eventId);
    for (const paragraph of person.paragraphs) {
      let offset = 0;
      for (const link of paragraph.eventLinks ?? []) {
        const index = link.label ? paragraph.text.indexOf(link.label,offset) : -1;
        if (index < 0) errors.push(`Missing or unordered event label ${person.id}/${link.label}`);
        else offset = index + link.label.length;
        targets.push(link.eventId);
      }
    }
    for (const milestone of person.milestones) {
      targets.push(...(milestone.eventIds ?? []));
      if (person.dossier?.expanded) {
        const years=(milestone.when?.match(/(?<!\d)\d{3}(?!\d)/g) ?? []).map(Number);
        for (const id of milestone.eventIds ?? []) {
          const event=byId.get(id);
          if (years.length && event && (Math.min(...years)>event.endYear || Math.max(...years)<event.year))
            errors.push(`Expanded career event date mismatch ${person.id}/${id}`);
        }
      }
    }
    for (const group of ['civil','military','setbacks']) {
      for (const record of person.dossier?.[group] ?? []) targets.push(...(record.eventIds ?? []));
    }
    for (const id of targets) {
      if (!byId.has(id)) errors.push(`Missing person event target ${person.id}/${id}`);
      else if (!person.eventIds.includes(id) || !byId.get(id).participants.some(p=>p.personId===person.id))
        errors.push(`Missing reciprocal person event ${person.id}/${id}`);
    }
  }
  return errors;
}

export function validatePersonDossiers(people, {requireAll=false} = {}) {
  const errors = [];
  for (const person of people) {
    const d = person.dossier;
    if (!d) {
      if (requireAll) errors.push(`Missing dossier ${person.id}`);
      continue;
    }
    if (d.expanded) {
      if (!d.sourceScope?.trim()) errors.push(`Missing expanded source scope ${person.id}`);
      for (const key of ['scholarship','assessment','readingNotes']) {
        if (!Array.isArray(d[key])) errors.push(`Missing expanded section ${person.id}/${key}`);
        for (const item of d[key] ?? []) if (!item.title?.trim() || !item.text?.trim() || !item.refs?.length)
          errors.push(`Unsupported expanded record ${person.id}/${key}`);
      }
      for (const item of person.paragraphs ?? []) if (!item.title?.trim() || !item.text?.trim() || !item.refs?.length)
        errors.push(`Unsupported expanded introduction ${person.id}`);
      for (const item of person.milestones ?? []) if (!item.title?.trim() || !item.text?.trim() || !item.office?.trim() || !item.refs?.length)
        errors.push(`Unsupported expanded career ${person.id}`);
      for (const item of d.contextRelations ?? []) if (!item.title?.trim() || !item.text?.trim() || !item.refs?.length)
        errors.push(`Unsupported expanded relationship ${person.id}`);
      for (const item of d.factDetails ?? []) if (!item.label?.trim() || !item.text?.trim() || !item.refs?.length)
        errors.push(`Unsupported expanded fact ${person.id}`);
    }
    if (requireAll) {
      if (!d.refs?.length) errors.push(`Missing profile evidence ${person.id}`);
      for (const m of person.milestones ?? []) if (!m.office?.trim()) errors.push(`Missing career office ${person.id}`);
      for (const group of ['civil','military','setbacks']) {
        if (!d[group]?.length && !d[`${group}Note`]?.trim()) errors.push(`Missing evidence explanation ${person.id}/${group}`);
      }
    }
    if (!['核心人物','拓展人物','背景人物'].includes(d.tier)) errors.push(`Invalid reading tier ${person.id}`);
    for (const key of ['hometown','highestOffice','highestTitle','posthumous']) {
      if (!d[key]?.trim()) errors.push(`Missing dossier fact ${person.id}/${key}`);
    }
    if (!d.deeds?.length) errors.push(`Missing representative deeds ${person.id}`);
    for (const group of ['civil','military','setbacks']) {
      if (!Array.isArray(d[group])) { errors.push(`Missing dossier section ${person.id}/${group}`); continue; }
      for (const record of d[group]) {
        if (['when','title','category','text'].some(key=>!record[key]?.trim()) || !record.refs?.length)
          errors.push(`Unsupported dossier record ${person.id}/${group}`);
      }
    }
    if (!d.civil?.length && !d.civilNote?.trim()) errors.push(`Missing civil evidence explanation ${person.id}`);
    for (const item of d.extraRelations ?? []) {
      if (!item.name?.trim() || !item.label?.trim() || !item.refs?.length) errors.push(`Unsupported named relation ${person.id}`);
    }
  }
  return errors;
}

// v3 人物卡规则（docs/person-template-v3.md §4、§7）。只检查 dossier.schema === 'v3' 的人物。
export const V3_LIMITS = {
  A: {introCount:[6,9], introChars:[800,1300], careers:[15,30], records:[5,15], relations:[10,18], readingNotes:[5,12], facts:['lifespan','hometown','identity','office','title','posthumous','names','deeds']},
  B: {introCount:[3,5], introChars:[400,700], careers:[8,15], records:[2,6], relations:[4,10], readingNotes:[2,5], facts:['hometown','identity','office','posthumous','deeds']},
  C: {introCount:[1,2], introChars:[300,450], careers:[3,6], records:[1,6], relations:[2,4], readingNotes:[0,2], facts:['hometown','identity','office','posthumous']},
};
export const V3_MAX_QUOTE = 120;
export const GENERIC_SECTION_NOTE = '本书现有记载不足以单列此类事迹；请结合生平、史料辨析与原文阅读。';
const FACT_LABELS = {lifespan:'生卒年',hometown:'籍贯',identity:'主要身份',office:'最高官职',title:'最高爵位',posthumous:'身后称号',names:'常见称谓',deeds:'代表事迹'};
export function validateV3Profiles(people) {
  const errors = [];
  for (const person of people) {
    const d = person.dossier;
    if (d?.schema !== 'v3') continue;
    const id = person.id;
    const limit = V3_LIMITS[d.contentTier];
    if (!limit) { errors.push(`Invalid v3 content tier ${id}/${d.contentTier}`); continue; }
    const within = (name, value, [min, max]) => { if (value < min || value > max) errors.push(`v3 ${name} out of range ${id}: ${value} not in ${min}-${max}`); };
    for (const ref of collectReferences(person)) {
      if (ref.quote.length > V3_MAX_QUOTE) errors.push(`v3 quote too long ${id}/${ref.blockId}: ${ref.quote.length}`);
    }
    const labels = new Set((d.factDetails ?? []).map(f => f.label));
    for (const key of limit.facts) if (!labels.has(FACT_LABELS[key])) errors.push(`v3 missing fact ${id}/${key}`);
    for (const f of d.factDetails ?? []) if (!f.refs?.length) errors.push(`v3 fact without evidence ${id}/${f.label}`);
    within('introduction count', person.paragraphs.length, limit.introCount);
    within('introduction chars', person.paragraphs.reduce((n, p) => n + p.text.length, 0), limit.introChars);
    within('career count', person.milestones.length, limit.careers);
    const careerIds = person.milestones.map(m => m.id);
    if (careerIds.some(x => !x) || new Set(careerIds).size !== careerIds.length) errors.push(`v3 career ids missing or duplicated ${id}`);
    for (const group of ['civil', 'military', 'setbacks']) {
      const rows = d[group] ?? [];
      if (rows.length) within(`${group} records`, rows.length, limit.records);
      const note = d[`${group}Note`]?.trim();
      if (!rows.length && (!note || note === GENERIC_SECTION_NOTE)) errors.push(`v3 empty section needs a person-specific note ${id}/${group}`);
      for (const r of rows) if (r.careerRef && !careerIds.includes(r.careerRef)) errors.push(`v3 unknown careerRef ${id}/${r.careerRef}`);
    }
    if (!(d.setbacks?.length) && !d.setbacksNote?.trim()) errors.push(`v3 setbacks required ${id}`);
    within('relation count', d.contextRelations?.length ?? 0, limit.relations);
    for (const r of d.contextRelations ?? []) if (!r.category?.trim()) errors.push(`v3 relation without category ${id}/${r.title}`);
    if (d.contentTier !== 'C' && !d.assessment?.length) errors.push(`v3 assessment required ${id}`);
    within('reading note count', d.readingNotes?.length ?? 0, limit.readingNotes);
    if (d.appendixRefs?.length) errors.push(`v3 profiles link to the reader instead of embedding appendix excerpts ${id}`);
  }
  return errors;
}

export function validateTimeline(events, relations) {
  const errors = [];
  const ids = new Set(events.map(e => e.id));
  const connected = new Set();
  const edgeKeys = new Set();
  for (const event of events) {
    if (!Number.isInteger(event.year) || !Number.isInteger(event.endYear) || event.endYear < event.year) errors.push(`Invalid time range ${event.id}`);
    if (!Number.isInteger(event.order)) errors.push(`Missing same-year order ${event.id}`);
    const expectedPhase = event.year < 211 ? 'formation' : event.year < 239 ? 'states' : 'unification';
    if (event.phase !== expectedPhase) errors.push(`Invalid phase year ${event.id}`);
    if (!['formation','states','unification'].includes(event.phase)) errors.push(`Invalid phase ${event.id}`);
    if (!['key','standard'].includes(event.importance)) errors.push(`Invalid importance ${event.id}`);
    if (!Array.isArray(event.lanes) || event.lanes.length === 0 || event.lanes.some(l => !['common','wei','shu','wu','lords'].includes(l)) || new Set(event.lanes).size !== event.lanes.length) errors.push(`Invalid lanes ${event.id}`);
    if (event.lanes?.includes('common') && event.lanes.length !== 1) errors.push(`Common background combined with polity ${event.id}`);
    if (event.lanes?.includes('shu') && event.year > 263) errors.push(`Shu after 263: ${event.id}`);
    if (event.lanes?.includes('wu') && event.year > 280) errors.push(`Wu after 280: ${event.id}`);
    if (!event.categories?.length || event.categories.some(c => !['war','state','succession','diplomacy','governance'].includes(c))) errors.push(`Invalid categories ${event.id}`);
    for (const p of event.participants ?? []) if(Boolean(p.personId) === Boolean(p.name) || !p.role) errors.push(`Ambiguous participant ${event.id}`);
  }
  for (const relation of relations) {
    if (!ids.has(relation.from)) errors.push(`Missing relation source ${relation.from}`);
    if (!ids.has(relation.to)) errors.push(`Missing relation target ${relation.to}`);
    if (relation.from === relation.to) errors.push(`Self relation ${relation.id}`);
    if (!['context','process','parallel','succession'].includes(relation.type)) errors.push(`Invalid relation type ${relation.id}`);
    if (!relation.summary || !relation.refs?.length || typeof relation.interpretation !== 'boolean') errors.push(`Unsupported relation ${relation.id}`);
    const ends = relation.type === 'parallel' ? [relation.from,relation.to].sort() : [relation.from,relation.to];
    const key = `${relation.type}:${ends.join(':')}`;
    if (edgeKeys.has(key)) errors.push(`Duplicate relation ${relation.id}`);
    edgeKeys.add(key);
    if (ids.has(relation.from) && ids.has(relation.to)) {
      connected.add(relation.from); connected.add(relation.to);
      if (relation.type !== 'parallel' && events.find(e=>e.id===relation.from).year > events.find(e=>e.id===relation.to).year) errors.push(`Backward chronological relation ${relation.id}`);
    }
  }
  for (const id of ids) if(!connected.has(id)) errors.push(`Unconnected event ${id}`);
  return errors;
}

// 人物行迹地点（docs/atlas-trajectory-guide.md 的 M2、M5 与字段格式）。
// M3、M4 需要江山时序的地名库，由 scripts/atlas-places.mjs check 检查。
export function validateAtlasPlaces(people) {
  const errors = [];
  const yearsIn = when => {
    const years = (when.match(/\d{2,4}(?=\s*[年—–-])/g) ?? []).map(Number);
    return years.length ? [Math.min(...years), Math.max(...years)] : null;
  };
  for (const person of people) {
    let previous = -Infinity;
    for (const row of person.milestones ?? []) {
      const place = row.place;
      if (!place) continue;
      const at = `${person.id}/${row.id ?? row.title}`;
      if (person.dossier?.schema !== 'v3') { errors.push(`atlas place only allowed on v3 profiles ${at}`); continue; }
      for (const key of ['name', 'query', 'province']) if (typeof place[key] !== 'string' || !place[key].trim()) errors.push(`atlas place missing ${key} ${at}`);
      if (!Number.isInteger(place.mapYear)) { errors.push(`atlas mapYear must be an integer ${at}`); continue; }
      if ('approx' in place && place.approx !== true) errors.push(`atlas approx must be omitted or true ${at}`);
      const extra = Object.keys(place).filter(k => !['name', 'query', 'province', 'mapYear', 'approx'].includes(k));
      if (extra.length) errors.push(`atlas place unknown field ${at}: ${extra.join(',')}`);
      if (place.name && ![row.when, row.title, row.text].some(s => s?.includes(place.name))) errors.push(`atlas place name not in row ${at}: ${place.name}`);
      const range = yearsIn(row.when ?? '');
      if (range && (place.mapYear < range[0] || place.mapYear > range[1])) errors.push(`atlas mapYear outside when ${at}: ${place.mapYear} not in ${range.join('-')}`);
      if (place.mapYear < previous) errors.push(`atlas mapYear goes backwards ${at}: ${place.mapYear} < ${previous}`);
      previous = place.mapYear;
    }
  }
  return errors;
}
