
from math import sin, cos 

from transform import Transform

# Rotation about z-axis.
class Rotation(Transform):
    # theta is angle in radians.
    def __init__(self, theta):
        Transform.__init__(self) 
        s = sin(theta)
        c = cos(theta)
        self.m[0][0] = c
        self.m[0][1] = -s
        self.m[1][0] = s
        self.m[1][1] = c
        self.m[2][2] = 1
