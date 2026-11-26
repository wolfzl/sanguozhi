"""Independent comparison of shipped text against the actual source EPUB."""
import json
import os
import unittest
import xml.etree.ElementTree as ET
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from zipfile import ZipFile

SITE = Path(__file__).parents[1]
SOURCE = Path(os.environ.get('SANGUO_EPUB') or SITE / 'work' / '三国志-陈寿撰裴松之注-维基文库-20260923.epub')

def normalized(text):
    return ' '.join(text.split())

class TextCollector(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts = []
    def handle_data(self, data):
        self.parts.append(data)

@unittest.skipUnless(SOURCE.exists(), 'Original EPUB is required for full-source comparison')
class FullBookIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.book = json.loads((SITE / 'src/data/book.json').read_text())

    def test_every_nonempty_annotation_is_preserved_including_duplicates(self):
        expected = []
        with ZipFile(SOURCE) as z:
            for volume in self.book['volumes']:
                tree = ET.fromstring(z.read(volume['epubPath']))
                expected.extend(normalized(''.join(n.itertext())) for n in tree.iter() if 'peizhu' in n.get('class', '').split() and normalized(''.join(n.itertext())))
        actual = [n['text'] for v in self.book['volumes'] for b in v['blocks'] for n in b['notes'] if n['text']]
        self.assertEqual(len(expected), 1821)
        self.assertEqual(Counter(expected), Counter(actual))

    def test_all_body_block_text_survives_html_rendering_without_reordering(self):
        with ZipFile(SOURCE) as z:
            for volume in self.book['volumes']:
                tree = ET.fromstring(z.read(volume['epubPath']))
                body = tree.find('{http://www.w3.org/1999/xhtml}body')
                heading = body.find('{http://www.w3.org/1999/xhtml}h1')
                expected = [normalized(''.join(n.itertext())) for n in body if n is not heading and n.tag.split('}')[-1] not in {'script','style'} and n.get('class') != 'source' and normalized(''.join(n.itertext()))]
                actual = []
                for block in volume['blocks']:
                    collector = TextCollector(); collector.feed(block['html'])
                    actual.append(normalized(''.join(collector.parts)))
                self.assertEqual(expected, actual, volume['id'])
