"""Apply comprehensive, source-checked profiles after the legacy dossiers."""
from copy import deepcopy
from pathlib import Path
import json
import re
import profile_caocao_content as cao


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
        r['refs'] = [resolve(s) for s in r.pop('sources', r.pop('refs', []))]
        return r

    def caocao():
        flatten = lambda groups: [dict(r,group=title) for title, rows in groups for r in rows]
        original = next(p for p in people if p['id']=='caocao')
        links = [('兖州', 'qingzhou-army'),('迎汉献帝迁都许','welcome-emperor'),('官渡','guandu'),('赤壁','chibi'),('汉中','hanzhong')]
        intro = deepcopy(cao.intro)
        for label, eid in links:
            target = next(r for r in intro if label in r['text'])
            target.setdefault('eventLinks', []).append(dict(label=label,eventId=eid))
        for r in intro:
            r['eventLinks'] = sorted(r.get('eventLinks',[]),key=lambda x:r['text'].index(x['label']))
        careers = deepcopy(cao.career)
        # Retain the established event associations on their corresponding year.
        for old in original['milestones']:
            for eid in old.get('eventIds',[]):
                ev = next(e for e in events if e['id']==eid)
                candidates=[]
                for i, row in enumerate(careers):
                    years = [int(y) for y in re.findall(r'\d{3}',row['when'])]
                    if years and min(years)<=ev['year']<=max(years): candidates.append(i)
                if not candidates: raise ValueError(f'No career match: {eid}')
                careers[candidates[-1]].setdefault('eventIds',[]).append(eid)
        return dict(lead=cao.lead,role='汉丞相、魏王，曹魏政权的奠基者',
            facts=dict(hometown='沛国谯县',highestOffice='汉丞相，兼领冀州牧',highestTitle='魏王，216年进封；生前没有称帝',posthumous='220年先谥武王；曹丕称帝后追尊武皇帝，庙号太祖',deeds=['立足兖州','迎帝都许','兴办屯田','官渡破袁','平定河北','北征乌桓','进取关中','建立魏国']),
            factsSources=list(dict.fromkeys(s for _,_,ss in cao.facts for s in ss)),
            factDetails=[dict(label=label,text=text,refs=ss) for label,text,ss in cao.facts],
            intro=intro,careers=careers,civil=flatten(cao.civil),military=flatten(cao.military),setbacks=cao.setbacks,
            scholarship=cao.scholarship,assessment=[cao.assessment],readingNotes=cao.reading,
            contextRelations=[dict(title=r['title'],text=r['text'],category=r['when'],refs=r['refs']) for r in cao.relations],
            glossary=cao.glossary,appendixBlocks=[b['id'] for v in book['volumes'] if v['id']=='001' for b in v['blocks']],
            sourceScope='以卷一《武帝纪》全部正文与122条裴注为基础，按关键问题交叉核查相关本纪、列传。附录保留卷一全部有文字的正文段落与全部注释，以及本文引用的其他卷材料。音训、引典、旁及人物、星占和方术异闻保留在原文中，不逐条列为功绩。本页不声称穷尽全书所有提及曹操之处。')

    profiles = {'caocao':caocao()}
    if include_six:
        for module_name in ['profiles_shu_expanded','profiles_wu_expanded','profiles_other_expanded']:
            module = __import__(module_name)
            profiles.update(module.PROFILES)
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
                else:d['extraRelations'].append(r)
        # Put complete biography material after cited evidence. Empty bodies aren't excerpts.
        d['appendixRefs']=[]
        for bid in data.get('appendixBlocks',[]):
            b=blocks[bid]
            for sid in [bid]+[n['id'] for n in b['notes']]:
                if (notes[sid]['text'] if sid in notes else blocks[sid]['mainText']).strip():
                    d['appendixRefs'].append(full_ref(sid))
