"""
    Tests for `rotation.py`.
"""
import sys
import unittest
import math

sys.path.insert(0, "..")
from rotation import Rotation

class RotationTests(unittest.TestCase):
    """Tests for 'rotation.py'."""

    def __check_matrix(self, theta, m):
        """ Checks the elements of a 2D 3x3 affine rotation matrix """
        s = math.sin(theta)
        c = math.cos(theta)

        self.assertEqual(m[0][0], c)
        self.assertEqual(m[0][1], -s)
        self.assertEqual(m[0][2], 0.0)

        self.assertEqual(m[1][0], s)
        self.assertEqual(m[1][1], c)
        self.assertEqual(m[1][2], 0.0)

        self.assertEqual(m[2][0], 0.0)
        self.assertEqual(m[2][1], 0.0)
        self.assertEqual(m[2][2], 1.0)

    def __check(self, theta):
        """tests if rotation matrix is correctly initialized some angle theta"""
        rot = Rotation(theta)
#        print(rot.m)
        self.__check_matrix(theta, rot.m)

    def test_matrix_0_pi(self):
        """tests if rotation matrix is correctly initialized for 0 degs"""
        self.__check(0)

    def test_matrix_pi_4(self):
        """tests if rotation matrix is correctly initialized for 45 degs"""
        self.__check(math.pi / 4)

    def test_matrix_pi_2(self):
        """tests if rotation matrix is correctly initialized for 90 degs"""
        self.__check(math.pi / 2)

if __name__ == '__main__':
    unittest.main()
