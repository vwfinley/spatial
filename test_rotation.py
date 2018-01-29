"""
    Tests for `rotation.py`.
"""

import unittest
import math
from rotation import Rotation

class RotationTests(unittest.TestCase):
    """Tests for 'rotation.py'."""

    def check_matrix(self, theta, m):
        """ Checks the elements of a 2D 3x3 affine rotation matrix """
        s = math.sin(theta)
        c = math.cos(theta)

        self.assertTrue(m[0][0] == c)
        self.assertTrue(m[0][1] == -s)
        self.assertTrue(m[0][2] == 0.0)

        self.assertTrue(m[1][0] == s)
        self.assertTrue(m[1][1] == c)
        self.assertTrue(m[1][2] == 0.0)

        self.assertTrue(m[2][0] == 0.0)
        self.assertTrue(m[2][1] == 0.0)
        self.assertTrue(m[2][2] == 1.0)

    def check(self, theta):
        """tests if rotation matrix is correctly initialized some angle theta"""
        rot = Rotation(theta)
        print(rot.m)
        self.check_matrix(theta, rot.m)

    def test_matrix_0_pi(self):
        """tests if rotation matrix is correctly initialized for 45 degs"""
        self.check(0)

    def test_matrix_pi_4(self):
        """tests if rotation matrix is correctly initialized for 45 degs"""
        self.check(math.pi / 4)

    def test_matrix_pi_2(self):
        """tests if rotation matrix is correctly initialized for 90 degs"""
        self.check(math.pi / 2)

if __name__ == '__main__':
    unittest.main()
