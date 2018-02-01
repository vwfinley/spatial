"""
Module defines an 2D affine identity matrix.
"""
import numpy

class Identity:
    """ 
        Trivial class that defines a 2D affine (3x3) identity matrix as follows:
        [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0]
        ]   
    """

    def __init__(self):
        """Constructs Identity matrix"""       
        self.m = numpy.identity(3)
