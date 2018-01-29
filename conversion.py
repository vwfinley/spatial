from math import sin, cos, hypot, atan2

def cart2pol(x, y):
    r = hypot(x, y)
    theta = atan2(y, x)
    return [r, theta]

def pol2cart(r, theta):
    x = r * cos(theta)
    y = r * sin(theta)
    return [x, y]
