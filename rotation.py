"""
Module defines a 2D affine rotation.
"""

from math import sin, cos
from transform import Transform

class Rotation(Transform):
    """
    2D affine rotation to be used in a matrix multiply operation
    to rotate a 2D affine point about the origin.
    """

    def __init__(self, theta):
        """
        Constructor for Rotation class.

        Parameters:
           theta (float): The rotation angle about the origin in radians.
        """

        Transform.__init__(self)
        s = sin(theta)
        c = cos(theta)
        self.m[0][0] = c
        self.m[0][1] = -s
        self.m[1][0] = s
        self.m[1][1] = c
        self.m[2][2] = 1
