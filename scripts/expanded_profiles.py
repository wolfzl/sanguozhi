"""Apply comprehensive, source-checked profiles after the legacy dossiers."""
from copy import deepcopy
from pathlib import Path
import json
import re


def apply(people, events, R, include_six=True):
    book = json.loads(Path('src/data/book.json').read_text())
    blocks = {b['id']: b for v in book['volumes'] for b in v['blocks']}
    notes = {n['id']: n for b in blocks.values() for n in b['notes']}

    def full_ref(source_id):
        source = notes.get(source_id) or blocks[source_id]
        text = source['text'] if source_id in notes else source['mainText']
        work = None
        if source_id in notes:
            works = list(dict.fromkeys(source.get('books', []) + re.findall(r'《([^》]+)》', text)))
            work = '、'.join('《'+w+'》' for w in works) or '裴松之注'
            if '臣松之' in text: work += '；裴松之案'
        return R(source_id, text, work)

    def resolve(source):
        return full_ref(source) if isinstance(source, str) else R(*source)

    def entry(record):
        r = deepcopy(record)
        sources = r.pop('sources', None)
        if sources is None: sources = r.pop('refs', [])
        r['refs'] = [resolve(s) for s in sources]
        return r

    profiles = {}
    if include_six:
        for module_name in ['profiles_shu_expanded','profiles_wu_expanded','profiles_other_expanded']:
            module = __import__(module_name)
            profiles.update(module.PROFILES)
    import profile_v3
    v3 = profile_v3.load()
    profiles.update({pid: profile_v3.to_expanded(seed) for pid, seed in v3.items()})
    name_to_id = {p['name']:p['id'] for p in people}
    for pid, data in profiles.items():
        p=next(p for p in people if p['id']==pid)
        p['lead']=data['lead']
        p['role']=data['role']
        p['paragraphs']=[entry(r) for r in data['intro']]
        p['milestones']=[entry(r) for r in data['careers']]
        for row in p['milestones']:
            if '年' not in row['when']: row['when'] += '，确年未载'
        d=p['dossier']
        d.update(data['facts'])
        d.update(expanded=True,sourceScope=data['sourceScope'],refs=[resolve(s) for s in data['factsSources']])
        for key in ['civil','military','setbacks','scholarship','assessment','readingNotes']:
            d[key]=[entry(r) for r in data.get(key,[])]
        for key in ['civilNote','militaryNote','setbacksNote']:
            d[key]=data.get(key,'本书现有记载不足以单列此类事迹；请结合生平、史料辨析与原文阅读。')
        d['glossary']=[dict(term=r[0],text=r[1]) if isinstance(r,(list,tuple)) else r for r in data['glossary']]
        if 'relatedEventNotes' in data: d['relatedEventNotes']=deepcopy(data['relatedEventNotes'])
        if 'factDetails' in data: d['factDetails']=[entry(r) for r in data['factDetails']]
        if 'contextRelations' in data:
            d['contextRelations']=[entry(r) for r in data['contextRelations']]
            # Link only the names of people with existing pages.
            for r in d['contextRelations']:
                r['people']=[dict(name=name,personId=oid) for name,oid in name_to_id.items() if name in r['title'] and oid!=pid]
        else:
            p['relations']=[]
            d['extraRelations']=[]
            for r in data['relations']:
                r=entry(r)
                if r['name'] in name_to_id and name_to_id[r['name']]!=pid:
                    p['relations'].append(dict(personId=name_to_id[r['name']],label=r['label'],refs=r['refs']))
                else:
                    r['people']=[dict(name=name,personId=oid) for name,oid in name_to_id.items() if name in r['name'] and oid!=pid]
                    d['extraRelations'].append(r)
        # Put complete biography material after cited evidence. Empty bodies aren't excerpts.
        d['appendixRefs']=[]
        for bid in data.get('appendixBlocks',[]):
            b=blocks[bid]
            for sid in dict.fromkeys([bid]+[n['id'] for n in b['notes']]):
                if (notes[sid]['text'] if sid in notes else blocks[sid]['mainText']).strip():
                    d['appendixRefs'].append(full_ref(sid))
        if pid in v3:
            profile_v3.finish(p, v3[pid], R)
