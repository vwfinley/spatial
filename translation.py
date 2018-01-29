
from transform import Transform

class Translation(Transform):
    def __init__(self, tx, ty):
        Transform.__init__(self) 
        self.m[0][0] = 1
        self.m[0][2] = tx
        self.m[1][1] = 1
        self.m[1][2] = ty
        self.m[2][2] = 1
