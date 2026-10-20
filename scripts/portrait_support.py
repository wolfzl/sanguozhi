"""Editorial helpers for the concise, dated person portraits."""
def refs_for(R, sources):
    return [R(source) if isinstance(source, str) else R(*source) for source in sources]

def set_portrait(people, events, R, pid, *, paragraphs, lifespan, milestones=None,
                 relations=(), participations=(), courtesy=None, role=None, lead=None):
    person = next(p for p in people if p['id'] == pid)
    # Each paragraph is (text, source specs, [(exact linked text, event ID)]).
    person['paragraphs'] = [dict(text=text, refs=refs_for(R,sources),
        eventLinks=[dict(label=label,eventId=eid) for label,eid in links])
        for text,sources,links in paragraphs]
    person['lifespan'] = lifespan
    if milestones is not None:
        person['milestones'] = [dict(when=when,title=title,text=text,
            refs=refs_for(R,sources),eventIds=list(ids))
            for when,title,text,sources,ids in milestones]
    if courtesy: person['courtesy'] = courtesy
    if role: person['role'] = role
    if lead: person['lead'] = lead
    for other,label,sources in relations:
        relation = dict(personId=other,label=label,refs=refs_for(R,sources))
        prior = next((i for i,r in enumerate(person['relations']) if r['personId']==other),None)
        if prior is None: person['relations'].append(relation)
        else: person['relations'][prior] = relation
    for eid,participation in participations:
        event = next(e for e in events if e['id'] == eid)
        if not any(p.get('personId') == pid for p in event['participants']):
            # Replace a former plain-name entry when one exists.
            plain = next((i for i,p in enumerate(event['participants']) if p.get('name') == person['name']),None)
            entry = dict(personId=pid,role=participation)
            if plain is None: event['participants'].append(entry)
            else: event['participants'][plain] = entry
        event['tags'] = list(dict.fromkeys(event['tags']+[person['name']]))
