"""
Module defines a 2D scale translation.
"""

from identity import identity

class translation(identity):
    """
    2D affine translation to be used in a matrix multiply operation
    to translate a 2D affine point about the origin.
    """    

    def __init__(self, tx, ty):
        """
        2D affine translation to be used in a matrix multiply operation
        to translate a 2D affine point about the origin.

        tx = translation along x axis.
        ty = translation along y axis.
        """
        identity.__init__(self)
        self.m[0][2] = tx
        self.m[1][2] = ty
