"""
    Tests for `rotation.py`.
"""
import sys
import unittest
import numpy

sys.path.insert(0, "..")
from rotation import Rotation

class RotationTests(unittest.TestCase):
    """Tests for 'rotation.py'."""

    def __check_matrix(self, r, m):
        """ Checks the elements of a 2D 3x3 affine rotation matrix """
        self.assertAlmostEqual(r.m[0][0], m[0][0])
        self.assertAlmostEqual(r.m[0][1], m[0][1])
        self.assertAlmostEqual(r.m[0][2], m[0][2])

        self.assertAlmostEqual(r.m[1][0], m[1][0])
        self.assertAlmostEqual(r.m[1][1], m[1][1])
        self.assertAlmostEqual(r.m[1][2], m[1][2])

        self.assertAlmostEqual(r.m[2][0], m[2][0])
        self.assertAlmostEqual(r.m[2][1], m[2][1])
        self.assertAlmostEqual(r.m[2][2], m[2][2])

    def __check(self, theta_deg, m):
        """tests if rotation matrix is correctly initialized some angle theta"""
        theta = numpy.deg2rad(theta_deg)
        r = Rotation(theta)
        self.__check_matrix(r, m)

    def test_matrix_30(self):
        """tests if rotation matrix is correctly initialized for 30 degs"""
        m = [[0.866025403784439, -0.5, 0], [0.5, 0.866025403784439, 0], [0, 0, 1]]
        self.__check(30, m)

    def test_matrix_neg30(self):
        """tests if rotation matrix is correctly initialized for -30 degs"""
        m = [[0.866025403784439, 0.5, 0], [-0.5, 0.866025403784439, 0], [0, 0, 1]]
        self.__check(-30, m)

    def test_matrix_45(self):
        """tests if rotation matrix is correctly initialized for 45 degs"""
        m=[[0.707106781186548, -0.707106781186547, 0], [0.707106781186547, 0.707106781186548, 0], [0, 0, 1]]
        self.__check(45, m)

    def test_matrix_neg45(self):
        """tests if rotation matrix is correctly initialized for -45 degs"""
        m=[[0.707106781186548, 0.707106781186547, 0], [-0.707106781186547, 0.707106781186548, 0], [0, 0, 1]]
        self.__check(-45, m)

    def test_matrix_90(self):
        """tests if rotation matrix is correctly initialized for 90 degs"""
        m=[[6.12303176911189E-17, -1, 0], [1, 6.12303176911189E-17, 0], [0, 0, 1]]
        self.__check(90, m)

    def test_matrix_neg90(self):
        """tests if rotation matrix is correctly initialized for -90 degs"""
        m=[[6.12303176911189E-17, 1, 0], [-1, 6.12303176911189E-17, 0], [0, 0, 1]]
        self.__check(-90, m)

    def test_matrix_135(self):
        """tests if rotation matrix is correctly initialized for 135 degs"""
        m=[[-0.707106781186547, -0.707106781186548, 0], [0.707106781186548, -0.707106781186547, 0], [0, 0, 1]]
        self.__check(135, m)

    def test_matrix_neg135(self):
        """tests if rotation matrix is correctly initialized for -135 degs"""
        m=[[-0.707106781186547, 0.707106781186548, 0], [-0.707106781186548, -0.707106781186547, 0], [0, 0, 1]]
        self.__check(-135, m)

    def test_matrix_180(self):
        """tests if rotation matrix is correctly initialized for 180 degs"""
        m=[[-1, -1.22460635382238E-16, 0], [1.22460635382238E-16, -1, 0], [0, 0, 1]]
        self.__check(180, m)

    def test_matrix_neg180(self):
        """tests if rotation matrix is correctly initialized for -180 degs"""
        m=[[-1, 1.22460635382238E-16, 0], [-1.22460635382238E-16, -1, 0], [0, 0, 1]]
        self.__check(-180, m)

    def test_matrix_270(self):
        """tests if rotation matrix is correctly initialized for 270 degs"""
        m=[[-1.83690953073357E-16, 1, 0], [-1, -1.83690953073357E-16, 0], [0, 0, 1]]
        self.__check(270, m)

    def test_matrix_neg270(self):
        """tests if rotation matrix is correctly initialized for -270 degs"""
        m=[[-1.83690953073357E-16, -1, 0], [1, -1.83690953073357E-16, 0], [0, 0, 1]]
        self.__check(-270, m)

    def test_matrix_360(self):
        """tests if rotation matrix is correctly initialized for 360 degs"""
        m=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        self.__check(360, m)

    def test_matrix_neg360(self):
        """tests if rotation matrix is correctly initialized for -360 degs"""
        m=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        self.__check(-360, m)

    def test_matrix_370(self):
        """tests if rotation matrix is correctly initialized for 370 degs"""
        m=[[0.984807753012208, -0.17364817766693, 0], [0.17364817766693, 0.984807753012208, 0], [0, 0, 1]]
        self.__check(370, m)

    def test_matrix_neg370(self):
        """tests if rotation matrix is correctly initialized for -370 degs"""
        m=[[0.984807753012208, 0.17364817766693, 0], [-0.17364817766693, 0.984807753012208, 0], [0, 0, 1]]
        self.__check(-370, m)

if __name__ == '__main__':
    unittest.main()
