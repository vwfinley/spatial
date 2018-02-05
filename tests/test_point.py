"""
    Tests for `point.py`.
"""
import sys
import unittest
from math import atan2
from numpy import hypot

sys.path.insert(0, "..")
from spatial import point

class PointTests(unittest.TestCase):
    """Tests for 'point.py'."""

    def __check_vector(self, x, y):
        """ Checks the elements of a 2D 1x3 affine point vector """
        p = point(x, y)
        self.assertAlmostEqual(p[0], x)
        self.assertAlmostEqual(p[1], y)
        self.assertAlmostEqual(p[2], 1)
        
    def test_all(self):
        """tests if rotation matrix is correctly initialized offset (10.5, 0)"""

        data = [[-3.2, 99],
                [3.2, -99],
                [-5555.2, 5555.322],
                [-55.1, -32.2],
                [-20.1, -0.0005]]

        for d in data:
            self.__check_vector(d[0], d[1])

if __name__ == '__main__':
    unittest.main()
