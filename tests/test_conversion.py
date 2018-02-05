"""
    Tests spatial.py conversions.
"""
import sys
import unittest

sys.path.insert(0, "..")
from spatial import cart2pol, pol2cart

class ConversionTests(unittest.TestCase):
    """Tests for 'conversion.py'."""

    def __check_cart2pol(self, item):       
        """tests conversion of (x, y) to polar coords."""
        polar = cart2pol(item[0], item[1])
        self.assertAlmostEqual(polar[0], item[2])
        self.assertAlmostEqual(polar[1], item[3])

    def __check_pol2cart(self, item):
        """tests conversion of (r, theta) to cartesian coords."""
        cart = pol2cart(item[2], item[3])
        self.assertAlmostEqual(cart[0], item[0])
        self.assertAlmostEqual(cart[1], item[1])

    def test_all(self):
        """ tests conversion of (x, y) to (r, theta) and back."""

        # data is [x, y, r, theta_rads, theta_degs]
        data = [
            [0,	0, 0, 0, 0],
            [1, 1, 1.414213562, 0.785398163, 45],
            [1,	-1, 1.414213562, -0.785398163, -45],
            [-1, 1, 1.414213562, 2.35619449, 135],
            [1,	1, 1.414213562, 0.785398163, 45],
            [0,	1, 1, 1.570796327, 90],
            [0,	-1,	1, -1.570796327, -90],
            [1,	0, 1, 0, 0],
            [-1, 0,	1, 3.141592654, 180],
            [2.3, 10.1, 10.35857133, 1.346891827, 77.17121713],
            [5.3, -3.7, 6.463745044, -0.609458538, -34.91940201],
            [-6.4, 8.8, 10.88117641, 2.199592613, 126.0273734],
            [-3.7, -5.5, 6.628725368, -2.162983006, -123.9297974],
        ]

        for item in data:
            self.__check_cart2pol(item)
            self.__check_pol2cart(item)

if __name__ == '__main__':
    unittest.main()
