
from transform import Transform

class Shear(Transform):
    def __init__(self, hx, hy):
        Transform.__init__(self) 
        self.m[0][0] = 1
        self.m[0][1] = hx
        self.m[1][0] = hy
        self.m[1][1] = 1
        self.m[2][2] = 1
