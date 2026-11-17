"""v3 人物卡种子（docs/person-template-v3.md）到现有 expanded 数据结构的适配器。

渲染层尚未迁移，因此这里把 v3 的统一结构转换成 expanded_profiles.apply 已能处理的字段，
再在 apply 之后补写 v3 专属字段（contentTier、careerRef、关系名单等）。
新增人物：写 scripts/profile_v3_<id>.py，定义 PROFILE，并把模块名加入 V3_MODULES。
"""
import importlib
from copy import deepcopy

# 已按 v3 编写的人物种子模块。顺序不影响结果。
V3_MODULES = [
    'profile_v3_guanyu', 'profile_v3_liubei', 'profile_v3_zhang_jiao',
    'profile_v3_zhuge_liang', 'profile_v3_zhouyu', 'profile_v3_sima_yi',
    'profile_v3_luxun', 'profile_v3_sunquan', 'profile_v3_caocao',
    'profile_v3_zhangfei', 'profile_v3_zhaoyun', 'profile_v3_ma_chao',
    'profile_v3_pang_tong', 'profile_v3_fa_zheng', 'profile_v3_liu_shan',
    'profile_v3_jiang_wan', 'profile_v3_fei_yi', 'profile_v3_jiang_wei',
    'profile_v3_sun_jian', 'profile_v3_sun_ce', 'profile_v3_sun_hao',
    'profile_v3_lusu', 'profile_v3_lumeng', 'profile_v3_taishi_ci',
    'profile_v3_zhang_zhao', 'profile_v3_zhu_zhi', 'profile_v3_lv_fan',
    'profile_v3_cao_pi',
    'profile_v3_jia_xu',
    'profile_v3_sima_zhao',
    'profile_v3_sima_shi',
    'profile_v3_cao_shuang',
    'profile_v3_cao_rui',
    'profile_v3_cao_mao',
    'profile_v3_deng_ai',
    'profile_v3_zhong_hui',
    'profile_v3_zhang_liao',
    'profile_v3_xun_yu',
    'profile_v3_xun_you',
    'profile_v3_guo_jia',
    'profile_v3_cheng_yu',
    'profile_v3_yuanshao',
    'profile_v3_yuan_shu',
    'profile_v3_gongsun_zan',
    'profile_v3_han_sui',
    'profile_v3_dong_zhuo',
    'profile_v3_lv_bu',
    'profile_v3_liu_biao',
    'profile_v3_tao_qian',
    'profile_v3_liu_yan',
    'profile_v3_liu_zhang',
    'profile_v3_zhang_lu',
]

# 人物分级（scripts/person_tiers.py 按史料篇幅计算；改动须同时更新该脚本并通过 --check）。
TIERS = {
    # A 级（7 人）
    'caocao': 'A', 'sunquan': 'A', 'liubei': 'A', 'zhuge-liang': 'A', 'luxun': 'A', 'zhouyu': 'A', 'sima-yi': 'A',
    # B 级（44 人）
    'cao-pi': 'B', 'cao-rui': 'B', 'yuanshao': 'B', 'dong-zhuo': 'B', 'sun-hao': 'B', 'cao-mao': 'B', 'sun-ce': 'B', 'xun-yu': 'B',
    'zhong-hui': 'B', 'gongsun-zan': 'B', 'liu-shan': 'B', 'sun-jian': 'B', 'deng-ai': 'B', 'lumeng': 'B', 'jiang-wei': 'B', 'jia-xu': 'B',
    'cao-shuang': 'B', 'lusu': 'B', 'fa-zheng': 'B', 'guo-jia': 'B', 'zhang-zhao': 'B', 'xun-you': 'B', 'cheng-yu': 'B', 'taishi-ci': 'B',
    'pang-tong': 'B', 'tao-qian': 'B', 'ma-chao': 'B', 'zhang-lu': 'B', 'guanyu': 'B', 'zhang-liao': 'B', 'yuan-shu': 'B', 'liu-biao': 'B',
    'liu-yan': 'B', 'zhaoyun': 'B', 'jiang-wan': 'B', 'lv-fan': 'B', 'fei-yi': 'B', 'liu-zhang': 'B', 'zhu-zhi': 'B', 'lv-bu': 'B',
    'zhangfei': 'B', 'han-sui': 'B', 'sima-shi': 'B', 'sima-zhao': 'B',
    # C 级（14 人）
    'huang-gai': 'C', 'han-dang': 'C', 'mi-zhu': 'C', 'zhang-xiu': 'C', 'cheng-pu': 'C', 'huang-zhong': 'C', 'sun-qian': 'C', 'yuan-tan': 'C',
    'yuan-shang': 'C', 'ma-teng': 'C', 'wang-jun': 'C', 'sima-yan': 'C', 'du-yu': 'C', 'zhang-jiao': 'C',
}

SECTIONS = ('civil', 'military', 'setback')
DEFAULT_SECTION_TITLES = {'civil': '文治功绩', 'military': '武功功绩', 'setback': '失误、挫折与争议'}
FACT_FIELDS = {'hometown': 'hometown', 'office': 'highestOffice', 'title': 'highestTitle', 'posthumous': 'posthumous'}


def Q(block_id, quote, work=None):
    """一条逐句引文：段落/注释 ID + 原文中逐字存在的最短支撑句（繁体）+ 注引书名。"""
    return (block_id, quote, work) if work else (block_id, quote)


def _check_sources(pid, where, sources):
    if not sources:
        raise ValueError(f'{pid}: {where} 缺少引文')
    for s in sources:
        if isinstance(s, str):
            raise ValueError(f'{pid}: {where} 只给了段落 ID {s}，v3 要求逐句引文 Q(id, quote)')
        if '-n' in s[0] and len(s) < 3:
            raise ValueError(f'{pid}: {where} 的裴注引文 {s[0]} 缺少注引书名')


def load():
    """返回 {person_id: v3 PROFILE}。"""
    profiles = {}
    for name in V3_MODULES:
        seed = importlib.import_module(name).PROFILE
        profiles[seed['id']] = seed
    return profiles


def to_expanded(seed):
    """把 v3 PROFILE 转为 expanded_profiles.apply 使用的数据字典。"""
    pid = seed['id']
    if seed['tier'] != TIERS.get(pid):
        raise ValueError(f"{pid}: 种子 tier={seed['tier']}，但分级名单为 {TIERS.get(pid)}（见 scripts/person_tiers.py）")
    facts = {f['key']: f for f in seed['facts']}
    for f in seed['facts']:
        _check_sources(pid, f"facts/{f['key']}", f['refs'])
    for key in ['intro', 'careers', 'records', 'relations', 'assessment', 'readingNotes', 'scholarship']:
        for i, r in enumerate(seed.get(key, [])):
            _check_sources(pid, f'{key}[{i}]', r['refs'])

    sections = seed.get('sections', {})
    unknown = [s for s in sections if s not in SECTIONS] + [r['section'] for r in seed['records'] if r['section'] not in SECTIONS]
    if unknown:
        raise ValueError(f'{pid}: 自定义栏目 {sorted(set(unknown))} 需要先完成迁移步骤 1（渲染层支持 sections）')

    def rows(section):
        out = []
        for r in seed['records']:
            if r['section'] != section:
                continue
            row = {k: v for k, v in r.items() if k not in ('section', 'refs')}
            row['sources'] = r['refs']
            out.append(row)
        return out

    def note(section):
        return sections.get(section, {}).get('note') or ''

    return dict(
        lead=seed['lead'],
        role=seed['role'],
        facts=dict(
            # 非必填且未写的档案项，侧栏显示“本书未载”。
            **{target: facts[key]['value'] if key in facts else '本书未载' for key, target in FACT_FIELDS.items()},
            deeds=facts['deeds']['items'] if 'deeds' in facts else [],
        ),
        factsSources=list(dict.fromkeys(s for f in seed['facts'] for s in f['refs'])),
        factDetails=[dict(label=f['label'], text=f['text'], sources=f['refs']) for f in seed['facts']],
        intro=[dict(title=r['title'], text=r['text'], sources=r['refs'], **({'eventLinks': r['eventLinks']} if r.get('eventLinks') else {})) for r in seed['intro']],
        careers=[{**{k: v for k, v in r.items() if k != 'refs'}, 'sources': r['refs']} for r in seed['careers']],
        civil=rows('civil'),
        military=rows('military'),
        setbacks=rows('setback'),
        civilNote=note('civil'),
        militaryNote=note('military'),
        setbacksNote=note('setback'),
        scholarship=[dict(title=r['title'], text=r['text'], sources=r['refs']) for r in seed.get('scholarship', [])],
        assessment=[dict(title=r['title'], text=r['text'], sources=r['refs']) for r in seed.get('assessment', [])],
        readingNotes=[dict(title=r['title'], text=r['text'], sources=r['refs']) for r in seed.get('readingNotes', [])],
        contextRelations=[dict(title=f"{r['name']}｜{r['label']}", text=r['text'], category=r['category'], sources=r['refs']) for r in seed['relations']],
        glossary=seed.get('glossary', []),
        sourceScope=seed['sourceScope'],
        appendixBlocks=[],
        **({'relatedEventNotes': seed['relatedEventNotes']} if seed.get('relatedEventNotes') else {}),
    )


def finish(person, seed, R):
    """apply 之后补写 v3 专属字段。"""
    d = person['dossier']
    d['schema'] = 'v3'
    d['contentTier'] = seed['tier']
    d['sectionTitles'] = {s: seed.get('sections', {}).get(s, {}).get('title') or DEFAULT_SECTION_TITLES[s] for s in SECTIONS}
    if seed.get('appendix'):
        d['appendixVolumes'] = seed['appendix'].get('volumes', [])
    person['reading'] = list(dict.fromkeys(seed.get('reading', person['reading'])))
    # 经核对的年代可显式同步侧栏；未选择同步的既有样例保持原值。
    if seed.get('syncLifespan'):
        life = next(f for f in seed['facts'] if f['key'] == 'lifespan')
        ref = R(*life['refs'][0])
        person['lifespan'] = dict(
            text=life['value'], sourceTitle=f"《三国志》卷{ref['volume']}",
            sourceUrl=f"/read/{ref['volume']}/#{ref['blockId']}",
            quote=ref['quote'], note=life['text'],
        )
    # 行迹时期（docs/atlas-trajectory-guide.md），原样写入；span 转成列表便于 JSON 校验。
    if seed.get('trajectory'):
        t = deepcopy(seed['trajectory'])
        for ph in t['phases']:
            ph['span'] = list(ph['span'])
        d['trajectory'] = t
    # 有页面的人物同时写入 relations，供其他页面和关系检索使用。
    person['relations'] = [
        dict(personId=r['personId'], label=r['label'], refs=[R(*s) for s in r['refs']])
        for r in seed['relations'] if r.get('personId')
    ]
    d['extraRelations'] = []
    for row, r in zip(d['contextRelations'], seed['relations']):
        row['people'] = [dict(name=r['name'], personId=r['personId'])] if r.get('personId') else []
