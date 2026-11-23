"""C 级默认不做行迹地图：profile_v3 拒绝非例外 C 级种子带 trajectory。"""
import sys
import unittest
from copy import deepcopy
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import profile_v3
from profile_v3_zhang_jiao import PROFILE as ZHANG_JIAO


class CTierTrajectory(unittest.TestCase):
    def test_exception_list_is_zhang_jiao_only(self):
        self.assertEqual(profile_v3.C_TRAJECTORY_EXCEPTIONS, ['zhang-jiao'])
        self.assertEqual(profile_v3.TIERS['zhang-jiao'], 'C')

    def test_zhang_jiao_keeps_trajectory(self):
        self.assertTrue(ZHANG_JIAO['trajectory'])
        profile_v3.to_expanded(deepcopy(ZHANG_JIAO))

    def test_other_c_tier_seed_with_trajectory_is_rejected(self):
        seed = deepcopy(ZHANG_JIAO)
        seed['id'] = 'dian-wei'
        self.assertEqual(profile_v3.TIERS['dian-wei'], 'C')
        with self.assertRaisesRegex(ValueError, '不做行迹地图'):
            profile_v3.to_expanded(seed)


if __name__ == '__main__':
    unittest.main()
