"""Shared schema for event pages added while rewriting person portraits."""
from portrait_support import refs_for


def add_event(events, relations, R, *, id, title, year, time, lead, participants, sections,
              lanes, related, end_year=None, categories=('war',), order=50):
    assert not any(e['id']==id for e in events)
    events.append(dict(id=id,title=title,time=time,lead=lead,aliases=[],
        tags=[title],participants=[p if isinstance(p,dict) else dict(personId=p[0],role=p[1]) for p in participants],
        sections=[dict(heading=h,text=t,refs=refs_for(R,s),interpretation=False) for h,t,s in sections],
        note=None,year=year,endYear=end_year or year,order=order,
        phase='formation' if year<211 else 'states' if year<239 else 'unification',lanes=list(lanes),categories=list(categories),importance='standard'))
    # related = (earlier event id, relationship summary, primary source specs).
    before, summary, sources = related
    relations.append(dict(id=f'{before}--{id}',**{'from':before,'to':id},type='context',
                          summary=summary,interpretation=True,refs=refs_for(R,sources)))
