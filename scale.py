
from transform import Transform

class Scale(Transform):
    def __init__(self, sx, sy):
        Transform.__init__(self) 
        self.m[0][0] = sx
        self.m[1][1] = sy
        self.m[2][2] = 1
