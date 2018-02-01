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
    if x == 0.0 and y == 0.0:
        return [0, 0]

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
    if r < 0.0:
        raise ValueError("argument r must be >= 0")
        
    x = r * cos(theta)
    y = r * sin(theta)
    return [x, y]
