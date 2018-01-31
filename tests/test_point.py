"""
    Tests for `point.py`.
"""
import sys
import unittest
from math import atan2
from numpy import hypot

sys.path.insert(0, "..")
from point import Point

class PointTests(unittest.TestCase):
    """Tests for 'point.py'."""

    def __check_vector(self, name, x, y):
        """ Checks the elements of a 2D 1x3 affine point vector """
        p = Point(name, x, y)
        self.assertEqual(p.name, name)
        self.assertAlmostEqual(p.m[0], x)
        self.assertAlmostEqual(p.m[1], y)
        self.assertAlmostEqual(p.m[2], 1)

    def __check_affine(self, name, x, y):
        """ Checks the elements of a 2D 1x3 affine point vector """
        p = Point(name, x, y)
        a = p.affine
        self.assertEqual(p.name, name)
        self.assertAlmostEqual(a[0], x)
        self.assertAlmostEqual(a[1], y)
        self.assertAlmostEqual(a[2], 1)

    def __check_r_theta(self, name, x, y):
        """tests point p (r, theta) coords."""
        p = Point(name, x, y)
        self.assertEqual(p.name, name)
        self.assertAlmostEqual(p.r, hypot(x, y))
        self.assertAlmostEqual(p.theta, atan2(y, x))

    def __check_polar(self, name, x, y):
        """tests point p polar coords."""
        p = Point(name, x, y)
        pol = p.polar
        self.assertEqual(p.name, name)
        self.assertAlmostEqual(pol[0], hypot(x, y))
        self.assertAlmostEqual(pol[1], atan2(y, x))

    def __check_x_y(self, name, x, y):
        """tests point p (x, y) coords."""
        p = Point(name, x, y)
        self.assertEqual(p.name, name)
        self.assertAlmostEqual(p.x, x)
        self.assertAlmostEqual(p.y, y)

    def __check_cart(self, name, x, y):
        """tests point p (x, y) coords."""
        p = Point(name, x, y)
        cart = p.cart
        self.assertEqual(p.name, name)
        self.assertAlmostEqual(cart[0], x)
        self.assertAlmostEqual(cart[1], y)
        
    def test_all(self):
        """tests if rotation matrix is correctly initialized offset (10.5, 0)"""

        data = [["Foo", -3.2, 99],
                ["bArrr", 3.2, -99],
                ["ba43Z", -5555.2, 5555.322],
                ["my_Point", -55.1, -32.2],
                ["yo23ur_Point", -20.1, -0.0005]]

        for d in data:
            self.__check_vector(d[0], d[1], d[2])
            self.__check_affine(d[0], d[1], d[2])
            self.__check_r_theta(d[0], d[1], d[2])
            self.__check_polar(d[0], d[1], d[2])
            self.__check_x_y(d[0], d[1], d[2])
            self.__check_cart(d[0], d[1], d[2])

if __name__ == '__main__':
    unittest.main()
