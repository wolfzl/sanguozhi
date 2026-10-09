"""Lossless text extraction with separate, addressable Pei annotations."""
import argparse
import hashlib
import html
import json
import posixpath
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from zipfile import ZipFile

NS = {'o': 'http://www.idpf.org/2007/opf', 'h': 'http://www.w3.org/1999/xhtml'}
DEFAULT_SOURCE = '/Users/zhangliang/ai/readbook/inbox/三国志-陈寿撰裴松之注-维基文库-20260923.epub'
ALLOWED = {'p', 'span', 'a', 'small', 'blockquote', 'h1', 'h2', 'h3', 'h4', 'div', 'section', 'em', 'strong', 'b', 'i', 'sup', 'sub', 'br', 'ul', 'ol', 'li', 'dl', 'dt', 'dd', 'table', 'tbody', 'tr', 'th', 'td'}

def tag(node):
    return node.tag.split('}')[-1]

def clean(text):
    return re.sub(r'\s+', ' ', text).strip()

def is_note(node):
    return 'peizhu' in node.get('class', '').split()

def main_text(node):
    if is_note(node) or tag(node) in {'script', 'style'}:
        return ''
    parts = [node.text or '']
    for child in node:
        parts.extend([main_text(child), child.tail or ''])
    return ''.join(parts)

def serialize(node, block_id, notes, root=False):
    name = tag(node)
    if name in {'script', 'style'}:
        return ''
    attrs = ''
    if is_note(node):
        note_id = block_id if root else f'{block_id}-n{len(notes) + 1:02d}'
        text = clean(''.join(node.itertext()))
        notes.append({'id': note_id, 'text': text, 'books': list(dict.fromkeys(re.findall(r'《([^》]+)》', text)))})
        name = 'aside' if root else 'span'
        attrs = f' id="{note_id}" class="peizhu"'
    elif root:
        attrs = f' id="{block_id}"'
    elif node.get('id'):
        attrs = f' id="{html.escape(node.get("id"), quote=True)}"'
    if name == 'a':
        href = node.get('href', '')
        if href.startswith(('https://', 'http://', '#')):
            attrs += f' href="{html.escape(href, quote=True)}"'
        else:
            name = 'span'
    content = html.escape(node.text or '')
    for child in node:
        content += serialize(child, block_id, notes) + html.escape(child.tail or '')
    if name not in ALLOWED and name != 'aside':
        name = 'div' if root else 'span'
    if name == 'br':
        return '<br>'
    return f'<{name}{attrs}>{content}</{name}>'

def extract_book(path):
    path = Path(path)
    with ZipFile(path) as z:
        container = ET.fromstring(z.read('META-INF/container.xml'))
        opf_path = next(n.get('full-path') for n in container.iter() if tag(n) == 'rootfile')
        opf = ET.fromstring(z.read(opf_path))
        base = posixpath.dirname(opf_path)
        manifest = {n.get('id'): n.get('href') for n in opf.find('o:manifest', NS)}
        metadata = {tag(n): n.text or '' for n in opf.find('o:metadata', NS)}
        volumes = []
        for ref in opf.find('o:spine', NS):
            href = manifest[ref.get('idref')]
            if posixpath.basename(href) in {'intro.xhtml', 'nav.xhtml'}:
                continue
            epub_path = posixpath.normpath(posixpath.join(base, href))
            tree = ET.fromstring(z.read(epub_path))
            body = tree.find('h:body', NS)
            if body is None:
                continue
            number = re.search(r'c(\d+)', href)
            volume_id = f'{int(number.group(1)):03d}' if number else 'appendix'
            heading = body.find('h:h1', NS)
            title_node = heading if heading is not None else tree.find('h:head/h:title', NS)
            title = clean(''.join(title_node.itertext())) if title_node is not None else href
            source_url = ''; revision = ''; blocks = []
            for node in body:
                if node is heading:
                    continue
                if node.get('class') == 'source':
                    links = list(node.iter('{http://www.w3.org/1999/xhtml}a'))
                    source_url = links[0].get('href', '') if links else ''
                    match = re.search(r'修订号\s*(\d+)', ''.join(node.itertext()))
                    revision = match.group(1) if match else ''
                    continue
                if tag(node) in {'script', 'style'} or not clean(''.join(node.itertext())):
                    continue
                block_id = f'v{volume_id}-b{len(blocks) + 1:04d}'
                notes = []
                rendered = serialize(node, block_id, notes, root=True)
                blocks.append({'id': block_id, 'tag': tag(node), 'kind': 'peizhu' if is_note(node) else 'body', 'text': clean(''.join(node.itertext())), 'mainText': clean(main_text(node)), 'notes': notes, 'html': rendered})
            if volume_id == 'appendix':
                source_url = 'https://zh.wikisource.org/wiki/上三國志註表'
                cached_revision = re.search(r'revision id (\d+)', z.read(epub_path).decode('utf-8'))
                revision = cached_revision.group(1) if cached_revision else ''
            volumes.append({'id': volume_id, 'title': title, 'epubPath': epub_path, 'sourceUrl': source_url, 'revision': revision, 'permalink': f'https://zh.wikisource.org/w/index.php?oldid={revision}' if revision else source_url, 'blocks': blocks})
        return {'title': metadata.get('title', '三國志'), 'creator': metadata.get('creator', '陳壽；裴松之'), 'rights': metadata.get('rights', ''), 'sourceUrl': metadata.get('source', ''), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'sourceFile': path.name, 'volumes': volumes}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('source', nargs='?', default=DEFAULT_SOURCE)
    parser.add_argument('--output', default='src/data/book.json')
    args = parser.parse_args()
    result = extract_book(args.source)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'Extracted {len(result["volumes"])} volumes, {sum(len(v["blocks"]) for v in result["volumes"])} blocks, {sum(len(b["notes"]) for v in result["volumes"] for b in v["blocks"])} annotations → {output}')
