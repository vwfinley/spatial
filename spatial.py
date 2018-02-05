"""
    Module defines a 2D affine transforms.

    Contains 2D affine spatial transforms that can be
    used to transform points in space.  For example:

    p = point(1, 0)
    r = rotation(radians(45))
    pout = r * p

    Methods:
    Classes:
"""
from math import sin, cos, tan, hypot, atan2
from numpy.matlib import identity, ones
from numpy import radians, degrees

def point(x, y):   
    """
        2D affine point vector used in 2D spatial transformations. To use,
        call the matrix '*' operator.
    """
    m = ones((3, 1))
    m[0] = x
    m[1] = y

    return m

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
    return r, theta

def pol2cart(r, theta):
    """
        Converts r, theta to cartesian coords.

        r = distance of a point from the origin.
        theta = angle of the point with respect to the x-axis.

        returns x, y
    """       
    x = r * cos(theta)
    y = r * sin(theta)
    return x, y

def translation(tx, ty):
    """
    2D affine translation to be used in a matrix multiply operation
    to translate a 2D affine point about the origin.

    tx = translation along x axis.
    ty = translation along y axis.
    """
    m = identity(3)

    m[0, 2] = tx
    m[1, 2] = ty

    return m

def rotation(theta):
    """
    2D affine rotation to be used in a matrix multiply operation
    to rotate a 2D affine point about the origin.
    """
    m = identity(3)
    
    s = sin(theta)
    c = cos(theta)

    m[0, 0] = c
    m[0, 1] = -s
    m[1, 0] = s
    m[1, 1] = c

    return m

def scale(sx, sy):
    """
    2D affine scale transform to be used in a matrix multiply operation
    to scale a 2D affine point about the origin.

    sx = scale in x direction.
        sx < 0.0 reflect about origin
        sx = 1.0 (no scale),
        0.0 < sx < 1.0 (reduce),
        sx > 1.0 (increase),
        sx = 0.0 (exception, undefined),

    sy = scale in y direction.
        sy < 0.0 reflect about origin
        sy = 1.0 (no scale),
        0.0 < sy < 1.0 (reduce),
        sy > 1.0 (increase),
        sy = 0 (exception, undefined)
    """
    m = identity(3)

    m[0, 0] = sx
    m[1, 1] = sy

    return m

def shear(hx, hy):
    """
    2D affine shear to be used in a matrix multiply operation
    to shear a 2D affine point about the origin.

    hx = x axis shear angle, in radians clockwise from y axis,
    hy = y axis shear angle, in radians counter-clockwise from x axis.
    """
    m = identity(3)

    m[0, 1] = tan(hx)
    m[1, 0] = tan(hy)
    
    return m

if __name__ == '__main__':

    p = point(1, 0)
    t = translation(1.5, -2.5)
    r = rotation(radians(-45))
    pout = r * p

    print(cart2pol(p[0], p[1]))

    print(p)
    print(t)
    print(r)
    print(pout)    

    print("r, theta")
    r, theta = cart2pol(pout[0], pout[1])
    print(r, degrees(theta))
