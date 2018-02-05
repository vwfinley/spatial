"""
    Tests for `spatial.py`.
"""
import sys
import unittest

from numpy.matlib import matrix

sys.path.insert(0, "..")
from spatial import translation, rotation, point, cart2pol 

class SpatialTests(unittest.TestCase):
    """Tests for 'translation.py'."""

    def __check_translation(self, px, py, tx, ty, pox, poy):
        p = point(px, py)
        t = translation(tx, ty)
        po = t * p
        self.assertAlmostEqual(po[0], pox)
        self.assertAlmostEqual(po[1], poy)


    def test_translation(self):
        self.__check_translation(0, 1 ,-2.5, -1.5, -2.5, -0.5)

if __name__ == '__main__':
    unittest.main()

