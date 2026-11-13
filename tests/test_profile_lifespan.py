"""Opt-in v3 lifespan corrections must reach the visible sidebar."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from profile_v3 import finish

class ProfileLifespanTests(unittest.TestCase):
    def seed(self, sync=True):
        return dict(tier='A', relations=[], syncLifespan=sync, facts=[dict(
            key='lifespan', value='生年未详—251年', text='本书未详生年；251年卒。',
            refs=[('v004-b0021', '戊寅，太傅司馬宣王薨')])])

    def test_corrected_fact_replaces_external_sidebar_evidence(self):
        person = dict(dossier=dict(contextRelations=[]), reading=[], lifespan=dict(text='约179—251年'))
        finish(person, self.seed(), lambda sid, quote: dict(volume='004', blockId=sid, quote=quote))
        self.assertEqual(person['lifespan']['text'], '生年未详—251年')
        self.assertEqual(person['lifespan']['sourceUrl'], '/read/004/#v004-b0021')
        self.assertEqual(person['lifespan']['quote'], '戊寅，太傅司馬宣王薨')
        self.assertEqual(person['lifespan']['note'], '本书未详生年；251年卒。')

    def test_existing_samples_are_unchanged_without_opt_in(self):
        old = dict(text='已有年代', sourceUrl='https://example.com')
        person = dict(dossier=dict(contextRelations=[]), reading=[], lifespan=old.copy())
        finish(person, self.seed(False), lambda *args: self.fail('should not resolve a lifespan'))
        self.assertEqual(person['lifespan'], old)
