"""New biographies connect existing event participants without duplicating names."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from profile_v3 import create_new


class NewProfileEvents(unittest.TestCase):
    def seed(self, name, roles):
        return dict(tier='C', new=dict(name=name, faction='汉末', period='汉末'),
                    role='人物', lead='简介', facts=[dict(key='lifespan')], reading=['029'],
                    eventRoles=roles)

    def test_promotes_named_participant_in_place(self):
        events = [dict(id='battle', participants=[dict(name='乐进', role='城中守备')], tags=[])]
        create_new([], events, {'yue-jin': self.seed('乐进', [('battle', '守备')])})
        self.assertEqual(events[0]['participants'], [dict(personId='yue-jin', role='城中守备')])
        self.assertEqual(events[0]['tags'], ['乐进'])

    def test_preserves_other_participants_in_group(self):
        events = [dict(id='battle', participants=[dict(name='丁奉、留赞、吕据、唐咨', role='吴军前部将领')], tags=[])]
        create_new([], events, {'ding-feng': self.seed('丁奉', [('battle', '率先登堤')])})
        self.assertEqual(events[0]['participants'], [
            dict(personId='ding-feng', role='率先登堤'), dict(name='留赞、吕据、唐咨', role='吴军前部将领')
        ])

    def test_hua_tuo_needs_no_invented_event(self):
        people = []
        create_new(people, [], {'hua-tuo': self.seed('华佗', [])})
        self.assertEqual([p['id'] for p in people], ['hua-tuo'])
        with self.assertRaisesRegex(ValueError, 'eventRoles'):
            create_new([], [], {'other': self.seed('其他', [])})
