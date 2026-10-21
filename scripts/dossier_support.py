"""Resolve curated dossier source specifications with the generator's exact-quote check."""
from portrait_support import refs_for


def record(when, title, category, text, sources, event_ids=()):
    return dict(when=when, title=title, category=category, text=text,
                sources=sources, eventIds=list(event_ids))


def career(when, title, text, office, sources, event_ids=()):
    return dict(when=when, title=title, text=text, office=office,
                sources=sources, eventIds=list(event_ids))


def set_dossier(people, R, pid, *, tier, hometown, highestOffice, highestTitle,
                posthumous, deeds, facts, civil=(), military=(), setbacks=(),
                civilNote='', militaryNote='', setbacksNote='', careers=None,
                glossary=(), lead=None):
    person = next(p for p in people if p['id'] == pid)

    def resolve(item):
        item = dict(item)
        item['refs'] = refs_for(R, item.pop('sources'))
        if '年' not in item['when']:
            item['when'] += '，确年未载'
        return item

    person['dossier'] = dict(
        tier=tier, hometown=hometown, highestOffice=highestOffice,
        highestTitle=highestTitle, posthumous=posthumous, deeds=list(deeds),
        refs=refs_for(R, facts), civil=[resolve(x) for x in civil],
        military=[resolve(x) for x in military], setbacks=[resolve(x) for x in setbacks],
        civilNote=civilNote, militaryNote=militaryNote, setbacksNote=setbacksNote,
        extraRelations=[], glossary=[dict(item) if isinstance(item, dict)
                                    else dict(term=item[0], text=item[1]) for item in glossary])
    if careers is not None:
        person['milestones'] = [resolve(x) for x in careers]
    else:
        for milestone in person['milestones']:
            milestone.setdefault('office', '—')
    if lead is not None:
        person['lead'] = lead
