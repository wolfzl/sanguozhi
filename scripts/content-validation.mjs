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
    const targets = [];
    for (const paragraph of person.paragraphs) {
      let offset = 0;
      for (const link of paragraph.eventLinks ?? []) {
        const index = link.label ? paragraph.text.indexOf(link.label,offset) : -1;
        if (index < 0) errors.push(`Missing or unordered event label ${person.id}/${link.label}`);
        else offset = index + link.label.length;
        targets.push(link.eventId);
      }
    }
    for (const milestone of person.milestones) targets.push(...(milestone.eventIds ?? []));
    for (const id of targets) {
      if (!byId.has(id)) errors.push(`Missing person event target ${person.id}/${id}`);
      else if (!person.eventIds.includes(id) || !byId.get(id).participants.some(p=>p.personId===person.id))
        errors.push(`Missing reciprocal person event ${person.id}/${id}`);
    }
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
