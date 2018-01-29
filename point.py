
from numpy import ones

from conversion import cart2pol

class Point:
    def __init__(self, name, x, y):
        self._name = name
        self.p = ones((1, 3))
        self.p[0][0] = x
        self.p[0][1] = y

    @property
    def name(self):
        return self._name

    @property
    def x(self):
        return self.p[0][0]

    @property
    def y(self):
        return self.p[0][1]

    @property        
    def r(self):
        pol = cart2pol(self.x, self.y)
        return pol[0][0]

    @property
    def theta(self):
        pol = cart2pol(self.x, self.y)
        return pol[0][1]
    
    @property
    def polar(self):
        return cart2pol(self.x, self.y)
    
    @property
    def cart(self):
        return [self.x, self.y]

    @property
    def affine(self):
        return self.p
