"""
    Tests for `translation.py`.
"""
import sys
import unittest

from numpy.matlib import matrix

sys.path.insert(0, "..")
from spatial import translation

class TranslationTests(unittest.TestCase):
    """Tests for 'translation.py'."""

    def __check_matrix(self, t, m):
        """ Checks the elements of a 2D 3x3 affine rotation matrix """
        self.assertAlmostEqual(t[0, 0], m[0, 0])
        self.assertAlmostEqual(t[0, 1], m[0, 1])
        self.assertAlmostEqual(t[0, 2], m[0, 2])

        self.assertAlmostEqual(t[1, 0], m[1, 0])
        self.assertAlmostEqual(t[1, 1], m[1, 1])
        self.assertAlmostEqual(t[1, 2], m[1, 2])

        self.assertAlmostEqual(t[2, 0], m[2, 0])
        self.assertAlmostEqual(t[2, 1], m[2, 1])
        self.assertAlmostEqual(t[2, 2], m[2, 2])

    def __check(self, x, y, m):
        """tests if translation matrix is correctly to some x, y offset."""
        t = translation(x, y)
        self.__check_matrix(t, m)

    def test_matrix_x0_y0(self):
        """tests if rotation matrix is correctly initialized offset (0, 0)"""
        m = matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.__check(0, 0, m)

    def test_matrix_x10_5_y0(self):
        """tests if rotation matrix is correctly initialized offset (10.5, 0)"""
        m = matrix([[1, 0, 10.5], [0, 1, 0], [0, 0, 1]])
        self.__check(10.5, 0, m)

    def test_matrix_negx10_5_y0(self):
        """tests if rotation matrix is correctly initialized offset (-10.5, 0)"""
        m = matrix([[1, 0, -10.5], [0, 1, 0], [0, 0, 1]])
        self.__check(-10.5, 0, m)

    def test_matrix_x_y10_5(self):
        """tests if rotation matrix is correctly initialized offset (0, 10.5)"""
        m = matrix([[1, 0, 0], [0, 1, 10.5], [0, 0, 1]])
        self.__check(0, 10.5, m)

    def test_matrix_x_negy10_5(self):
        """tests if rotation matrix is correctly initialized offset (0, -10.5)"""
        m = matrix([[1, 0, 0], [0, 1, -10.5], [0, 0, 1]])
        self.__check(0, -10.5, m)

    def test_matrix_x10_5_y10_5(self):
        """tests if rotation matrix is correctly initialized offset (10.5, 10.5)"""
        m = matrix([[1, 0, 10.5], [0, 1, 10.5], [0, 0, 1]])
        self.__check(10.5, 10.5, m)

    def test_matrix_negx10_5_negy10_5(self):
        """tests if rotation matrix is correctly initialized offset (-10.5, -10.5)"""
        m = matrix([[1, 0, -10.5], [0, 1, -10.5], [0, 0, 1]])
        self.__check(-10.5, -10.5, m)

if __name__ == '__main__':
    unittest.main()
