import importlib.util
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

SPEC = importlib.util.spec_from_file_location('extract_epub', Path(__file__).parents[1] / 'scripts/extract_epub.py')
extractor = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(extractor)

class ExtractionTests(unittest.TestCase):
    def extract_fixture(self):
        self.assertTrue(callable(getattr(extractor, 'extract_book', None)), 'EPUB extraction is not implemented')
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'fixture.epub'
            with ZipFile(path, 'w') as z:
                z.writestr('META-INF/container.xml', '<container xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="OEBPS/content.opf"/></rootfiles></container>')
                z.writestr('OEBPS/content.opf', '<package xmlns="http://www.idpf.org/2007/opf"><metadata xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:title>三國志</dc:title></metadata><manifest><item id="a" href="c002.xhtml"/><item id="b" href="c001.xhtml"/></manifest><spine><itemref idref="a"/><itemref idref="b"/></spine></package>')
                z.writestr('OEBPS/c002.xhtml', '<html xmlns="http://www.w3.org/1999/xhtml"><body><h1>第二卷</h1><p class="source">来源：<a href="https://example.org/v2">维基文库</a>；修订号 123。</p><p>正文甲<small class="peizhu">《魏書》曰：注甲。</small>正文乙。</p><small class="peizhu">《典略》曰：独立注。</small><blockquote><p>引文。</p></blockquote><script>bad()</script></body></html>')
                z.writestr('OEBPS/c001.xhtml', '<html xmlns="http://www.w3.org/1999/xhtml"><head><title>第一卷</title></head><body><p>末卷内容。</p></body></html>')
            return extractor.extract_book(path)

    def test_reads_spine_order_instead_of_filename_order(self):
        book = self.extract_fixture()
        self.assertEqual([v['epubPath'] for v in book['volumes']], ['OEBPS/c002.xhtml', 'OEBPS/c001.xhtml'])

    def test_preserves_inline_note_and_surrounding_main_text(self):
        block = self.extract_fixture()['volumes'][0]['blocks'][0]
        self.assertEqual(block['mainText'], '正文甲正文乙。')
        self.assertEqual(block['notes'][0]['text'], '《魏書》曰：注甲。')
        self.assertEqual(block['notes'][0]['books'], ['魏書'])
        self.assertIn('正文乙。', block['html'])
        self.assertIn('id="v002-b0001-n01"', block['html'])

    def test_keeps_standalone_notes_quotes_and_source_revision(self):
        vol = self.extract_fixture()['volumes'][0]
        self.assertEqual(vol['revision'], '123')
        self.assertEqual(vol['blocks'][1]['kind'], 'peizhu')
        self.assertEqual(vol['blocks'][2]['tag'], 'blockquote')
        self.assertEqual(vol['blocks'][2]['mainText'], '引文。')
        self.assertNotIn('bad()', ''.join(b['html'] for b in vol['blocks']))

    def test_uses_document_title_when_appendix_has_no_h1(self):
        self.assertEqual(self.extract_fixture()['volumes'][1]['title'], '第一卷')

if __name__ == '__main__':
    unittest.main()
