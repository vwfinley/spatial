"""
Module defines a 2D scale rotation.
"""

from identity import identity

class scale(Identity):
    """
    2D affine scale to be used in a matrix multiply operation
    to scale a 2D affine point about the origin.
    """

    def __init__(self, sx, sy):
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
        identity.__init__(self) 
        self.m[0][0] = sx
        self.m[1][1] = sy
