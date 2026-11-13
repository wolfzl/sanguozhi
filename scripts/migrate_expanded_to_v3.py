"""把旧 expanded 人物（profiles_*_expanded.py）转成 v3 种子草稿，供人工修订。

用法（仓库根目录）：
  python3 scripts/migrate_expanded_to_v3.py profiles_shu_expanded zhuge-liang > /tmp/draft.py

草稿只搬运 intro / careers / records / scholarship / assessment / readingNotes / glossary，
引文原样保留。以下部分必须人工完成（刘备样例 scripts/profile_v3_liubei.py 即按此修订）：
  - facts：按 docs/person-template-v3.md §5.2 逐项写 value/text/refs（草稿只给出旧值）；
  - careers 的 id：草稿为 c01、c02…，改成有意义的英文 slug，并同步 records 的 careerRef；
  - relations：补 category、personId、text（草稿中为 TODO）；
  - sourceScope：删去“附录收录……”之类的说法，改为指向阅读器；
  - 头部的 tier / reading / role（role 不超过 15 字）。
"""
import importlib
import sys

sys.path.insert(0, 'scripts')


def q(source):
    if isinstance(source, str):
        return f'Q({source!r}, "TODO：旧数据只有段落 ID，需补逐句引文")'
    return 'Q(' + ', '.join(repr(x) for x in source) + ')'


def refs(sources, indent=18):
    return '[' + (',\n' + ' ' * indent).join(q(s) for s in sources) + ']'


def main(module_name, pid):
    d = importlib.import_module(module_name).PROFILES[pid]
    slugs = [f'c{i:02d}' for i in range(1, len(d['careers']) + 1)]
    out = [f'"""{pid}：v3 种子草稿（由 {module_name} 迁移，待人工修订）。"""', 'from profile_v3 import Q', '', 'PROFILE = dict(',
           f'    id={pid!r},', "    tier='TODO',", "    reading=['TODO'],", f"    lead={d['lead']!r},", f"    role={d['role']!r},", '',
           f"    # 旧档案值，供改写 facts 参考：{d['facts']!r}", '    facts=[],', '']
    w = out.append
    w('    intro=[')
    for r in d['intro']:
        extra = f", eventLinks={r['eventLinks']!r}" if r.get('eventLinks') else ''
        w(f"        dict(title={r['title']!r},\n             text={r['text']!r},\n             refs={refs(r['sources'])}{extra}),")
    w('    ],\n')
    w('    careers=[')
    for slug, r in zip(slugs, d['careers']):
        ev = f", eventIds={r['eventIds']!r}" if r.get('eventIds') else ''
        w(f"        dict(id={slug!r}, when={r['when']!r}, title={r['title']!r}, office={r['office']!r}{ev},\n             text={r['text']!r},\n             refs={refs(r['sources'])}),")
    w('    ],\n')
    w('    records=[')
    for key, section in [('civil', 'civil'), ('military', 'military'), ('setbacks', 'setback')]:
        w(f'        # {section}')
        for r in d[key]:
            ref = next((f', careerRef={s!r}' for s, c in zip(slugs, d['careers'])
                        if set(r.get('eventIds') or []) & set(c.get('eventIds') or [])), '')
            ev = f", eventIds={r['eventIds']!r}" if r.get('eventIds') else ''
            group = f", group={r['group']!r}" if r.get('group') else ''
            w(f"        dict(section={section!r}{group}, when={r['when']!r}, title={r['title']!r}, category={r['category']!r}{ref}{ev},\n             text={r['text']!r},\n             refs={refs(r['sources'])}),")
    w('    ],\n')
    for key in ['scholarship', 'assessment', 'readingNotes']:
        w(f'    {key}=[')
        for r in d.get(key, []):
            w(f"        dict(title={r['title']!r},\n             text={r['text']!r},\n             refs={refs(r['sources'])}),")
        w('    ],\n')
    w('    relations=[')
    for r in d.get('relations', []):
        w(f"        dict(category='TODO', name={r['name']!r}, label={r['label']!r},\n             text='TODO',\n             refs={refs(r['sources'])}),")
    w('    ],\n')
    w(f"    glossary={d['glossary']!r},\n")
    w(f"    # 旧 sourceScope：{d['sourceScope']!r}")
    w("    sourceScope='TODO',")
    w(')')
    print('\n'.join(out))


if __name__ == '__main__':
    main(*sys.argv[1:3])
