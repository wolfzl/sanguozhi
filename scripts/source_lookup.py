"""人物卡取证辅助：在 src/data/book.json 中查原文。

用法（在仓库根目录运行）：
  python3 scripts/source_lookup.py volume 036 --to 7       # 打印卷 036 第 1—7 段正文与全部裴注
  python3 scripts/source_lookup.py find 關羽 雲長           # 全书检索（繁体），列出段落/注释 ID 与上下文
  python3 scripts/source_lookup.py show v036-b0006 v036-b0006-n01   # 打印指定段落或注释全文
  python3 scripts/source_lookup.py check v036-b0006 '禁降羽，羽又斬將軍龐德。'  # 核对引句是否逐字存在
"""
import argparse
import json
import re
from pathlib import Path

BOOK = json.loads(Path('src/data/book.json').read_text())
BLOCKS = {b['id']: b for v in BOOK['volumes'] for b in v['blocks']}
NOTES = {n['id']: n for b in BLOCKS.values() for n in b['notes']}


def text_of(source_id):
    if source_id in NOTES:
        return NOTES[source_id]['text']
    return BLOCKS[source_id]['mainText']


def label(source_id):
    if source_id in NOTES:
        books = NOTES[source_id].get('books') or []
        return f"[{source_id}] 裴注 books={books or '未标注，需从注文开头判断书名'}"
    return f'## {source_id}'


def cmd_volume(args):
    volume = next(v for v in BOOK['volumes'] if v['id'] == args.volume)
    print(volume['title'])
    for i, b in enumerate(volume['blocks'], 1):
        if i < args.start or i > args.to:
            continue
        print(label(b['id']))
        print(b['mainText'])
        for n in b['notes']:
            print('  ' + label(n['id']))
            print('  ' + n['text'])


def cmd_find(args):
    pattern = re.compile('|'.join(map(re.escape, args.terms)))
    hits = 0
    for v in BOOK['volumes']:
        if args.volume and v['id'] not in args.volume:
            continue
        for b in v['blocks']:
            for sid in [b['id']] + [n['id'] for n in b['notes']]:
                t = text_of(sid)
                m = pattern.search(t)
                if m:
                    hits += 1
                    start = max(0, m.start() - args.context)
                    print(f"{sid} | {t[start:m.end() + args.context].replace(chr(10), '')}")
    print(f'共 {hits} 处')


def cmd_show(args):
    for sid in args.ids:
        print(label(sid))
        print(text_of(sid))


def cmd_check(args):
    t = text_of(args.id)
    ok = args.quote in t
    print('OK' if ok else 'NOT FOUND', f'{len(args.quote)} 字')
    if not ok:
        raise SystemExit(1)


parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
sub = parser.add_subparsers(required=True)
p = sub.add_parser('volume'); p.add_argument('volume'); p.add_argument('--start', type=int, default=1); p.add_argument('--to', type=int, default=10**6); p.set_defaults(fn=cmd_volume)
p = sub.add_parser('find'); p.add_argument('terms', nargs='+'); p.add_argument('--volume', nargs='*'); p.add_argument('--context', type=int, default=60); p.set_defaults(fn=cmd_find)
p = sub.add_parser('show'); p.add_argument('ids', nargs='+'); p.set_defaults(fn=cmd_show)
p = sub.add_parser('check'); p.add_argument('id'); p.add_argument('quote'); p.set_defaults(fn=cmd_check)
args = parser.parse_args()
args.fn(args)
