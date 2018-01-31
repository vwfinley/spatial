"""
    Module defines a Point class to be used in 2D spatial transformations.
"""

from numpy import ones
from conversion import cart2pol

class Point:
    """
        2D Point class to be used in 2D spatial transformations.  To use, get the vector
        returned by the affine property and matrix multiply it with a transformation matrix.
    """

    def __init__(self, name, x, y):
        """
            Constructor for Point class.

            name = name of the point, example: "Point5"
            x = x position of point
            y = y position of point
        """
        self._name = name
        self.m = ones((3, 1))
        self.m[0] = x
        self.m[1] = y

    @property
    def name(self):
        """
            Gets name of point.
        """
        return self._name

    @property
    def x(self):
        """
            Gets x position of point.
        """
        return self.m[0]

    @property
    def y(self):
        """
            Gets y position of point.
        """
        return self.m[1]

    @property        
    def r(self):
        """
            Gets the distance (radius) of point from origin.
        """
        pol = cart2pol(self.x, self.y)
        return pol[0]

    @property
    def theta(self):
        """
            Gets the point's angle, theta, with respect to the x-axis.
        """       
        pol = cart2pol(self.x, self.y)
        return pol[1]
    
    @property
    def polar(self):
        """
            Gets the point's location in polar coords. The array [r, theta] is returned.
        """
        return cart2pol(self.x, self.y)
    
    @property
    def cart(self):
        """
            Gets the point's location in cartesian coords. The array [x, y] is returned.
        """       
        return [self.x, self.y]

    @property   
    def affine(self):
        """
            Gets the point's 2D affine vector representation.
            The vector [ x,
                         y,
                         z, ] 
            is returned.
        """              
        return self.m
