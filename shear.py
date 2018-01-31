"""
Module defines a 2D shear rotation.
"""

from math import tan
from identity import Identity

class Shear(Identity):
    """
    2D affine shear to be used in a matrix multiply operation
    to shear a 2D affine point about the origin.
    """

    def __init__(self, hx, hy):
        """
        2D affine shear to be used in a matrix multiply operation
        to shear a 2D affine point about the origin.

        hx = x axis shear angle, in radians clockwise from y axis,
        hy = y axis shear angle, in radians counter-clockwise from x axis.
        """

        Identity.__init__(self)
        self.m[0][1] = tan(hx)
        self.m[1][0] = tan(hy)
