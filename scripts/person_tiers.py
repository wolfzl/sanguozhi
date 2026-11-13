"""按史料多少给人物卡分级（docs/person-template-v3.md §4）。

用法：python3 scripts/person_tiers.py        # 打印每人的篇幅统计与分级
      python3 scripts/person_tiers.py --check # 核对统计结果与 profile_v3.TIERS 一致

规则：
  A：开创政权或主持一国军政、决定三国格局的人物，且材料足以展开（人工指定，见 A_LIST）。
  B：有独立帝纪/本传/附传，且 正文 ≥ 600 字，或 正文 ≥ 300 字且正文+裴注 ≥ 1500 字；
     没有独立传记、但正文中有 ≥ 20 段散见记载的人物也定为 B（sourceScope 须说明无本传）。
  C：其余人物（本传短，或只散见少量记载）。
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

A_LIST = ['caocao', 'liubei', 'sunquan', 'zhuge-liang', 'zhouyu', 'luxun', 'sima-yi']
B_MAIN, B_MIN_MAIN, B_TOTAL, B_SCATTERED = 600, 300, 1500, 20

# 帝纪按整卷统计；标题与人名不一致或传中夹有小标题的，手工给出段落范围 [start, end)。
SPANS = {
    'caocao': ('001', 0, None), 'liubei': ('032', 0, None), 'sunquan': ('047', 0, None),
    'cao-pi': ('002', 0, None), 'cao-rui': ('003', 0, None), 'liu-shan': ('033', 0, None),
    'cao-mao': ('004', 28, 65),        # 高貴鄉公
    'cao-shuang': ('009', 32, 38),     # 子 爽（附曹真傳）
    'gongsun-zan': ('008', 0, 13),     # 傳中夾有「劉虞」小標題
}
# 没有独立传记的人物：统计正文中提到的段落数。
SCATTERED = {
    'sima-yi': ['司馬懿', '司馬宣王', '宣王'], 'sima-shi': ['司馬師', '景王', '司馬景王'],
    'sima-zhao': ['司馬昭', '司馬文王', '晉文王', '大將軍文王'], 'sima-yan': ['司馬炎', '晉武帝', '晉王炎', '晉太子'],
    'zhang-jiao': ['張角'], 'yuan-tan': ['袁譚'], 'yuan-shang': ['袁尚'], 'wang-jun': ['王濬', '王浚'],
    'ma-teng': ['馬騰'], 'han-sui': ['韓遂'], 'du-yu': ['杜預'],
}

BOOK = json.loads(Path('src/data/book.json').read_text())
VOLUMES = {v['id']: v for v in BOOK['volumes']}
PEOPLE = json.loads(Path('src/data/cards.json').read_text())['people']


def is_heading(text):
    text = text.strip()
    return 0 < len(text) <= 14 and not re.search(r'[，。：；「」、？！]', text)


def span_size(vid, start, end):
    blocks = VOLUMES[vid]['blocks'][start:end]
    return sum(len(b['mainText']) for b in blocks), sum(len(n['text']) for b in blocks for n in b['notes'])


def find_biography(person, trad):
    for vid in person['reading'] + list(VOLUMES):
        blocks = VOLUMES[vid]['blocks']
        for i, b in enumerate(blocks):
            if b['mainText'].strip() in (trad, person['name']):
                j = i + 1
                while j < len(blocks) and not is_heading(blocks[j]['mainText']):
                    j += 1
                return vid, i, j
    return None


def measure(person, trad):
    pid = person['id']
    span = SPANS.get(pid) or find_biography(person, trad)
    if span and pid not in SCATTERED:
        main, notes = span_size(*span)
        return dict(kind=f'传记 卷{span[0]}', main=main, notes=notes, scattered=None)
    terms = SCATTERED.get(pid, [trad])
    hits = sum(1 for v in BOOK['volumes'] for b in v['blocks'] if any(t in b['mainText'] for t in terms))
    return dict(kind='无独立传记', main=0, notes=0, scattered=hits)


def tier_of(pid, m):
    if pid in A_LIST:
        return 'A'
    if m['scattered'] is not None:
        return 'B' if m['scattered'] >= B_SCATTERED else 'C'
    if m['main'] >= B_MAIN or (m['main'] >= B_MIN_MAIN and m['main'] + m['notes'] >= B_TOTAL):
        return 'B'
    return 'C'


def traditional_names():
    """简体人名到繁体：仅覆盖本项目人物，避免依赖 opencc。"""
    table = str.maketrans('刘关张赵吕孙陆鲁诸葛袁绍董术瓒焉璋鲁绣谭荀彧郭贾诩马庞统费祎姜维邓钟会皓濬预辽韩遂陶谦麋竺黄盖当范慈坚策丕叡禅爽髦懿师昭炎蒋琬腾逊飞云肃备权', '劉關張趙呂孫陸魯諸葛袁紹董術瓚焉璋魯繡譚荀彧郭賈詡馬龐統費禕姜維鄧鍾會皓濬預遼韓遂陶謙麋竺黃蓋當範慈堅策丕叡禪爽髦懿師昭炎蔣琬騰遜飛雲肅備權')
    return {p['id']: p['name'].translate(table) for p in PEOPLE}


def compute():
    trad = traditional_names()
    rows = []
    for p in PEOPLE:
        m = measure(p, trad[p['id']])
        rows.append(dict(id=p['id'], name=p['name'], label=p['dossier']['tier'], tier=tier_of(p['id'], m), **m))
    return rows


if __name__ == '__main__':
    rows = compute()
    if '--check' in sys.argv:
        from profile_v3 import TIERS
        diff = {r['id']: (TIERS.get(r['id']), r['tier']) for r in rows if TIERS.get(r['id']) != r['tier']}
        print('一致' if not diff else f'不一致：{diff}')
        sys.exit(1 if diff else 0)
    for t in 'ABC':
        group = [r for r in rows if r['tier'] == t]
        print(f'\n{t} 级（{len(group)} 人）')
        for r in sorted(group, key=lambda r: -(r['main'] + r['notes'] + (r['scattered'] or 0))):
            size = f"散见正文 {r['scattered']} 段" if r['scattered'] is not None else f"正文 {r['main']} 字 / 裴注 {r['notes']} 字"
            print(f"  {r['name']}（{r['id']}）{r['kind']}，{size}；原标签 {r['label']}")
