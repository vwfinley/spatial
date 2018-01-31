"""
    Module contains basic conversions.  For example
    between polar and cartesian coords.
"""

from math import sin, cos, hypot, atan2

def cart2pol(x, y):   
    """
        Converts x, y to polar coords.

        x = position along x-axis.
        y = position along y-axis.

        returns [r, theta]
    """
    r = hypot(x, y)
    theta = atan2(y, x)
    return [r, theta]

def pol2cart(r, theta):
    """
        Converts r, theta to cartesian coords.

        r = distance of a point from the origin.
        theta = angle of the point with respect to the x-axis.

        returns [x, y]
    """
    x = r * cos(theta)
    y = r * sin(theta)
    return [x, y]
