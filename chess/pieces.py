""" Pieces Module"""


class Piece:
    """ Parent class for all chess pieces """

    def __init__(self, row, col, white):
        self.row = row
        self.col = col
        self.white = white

        unit_name = self.__class__.__name__
        # Unit is simply the first letter of the piece type
        # eg. Pawn = 'p', Knight = 'n' (the one except commonly used)
        self.unit = unit_name[0].lower()

        if self.white is True:
            self.name = 'w' + self.unit
        else:
            self.name = 'b' + self.unit

    def __repr__(self):
        return self.__class__.__name__ + \
            f"({self.row}, {self.col}, white={self.white})"


class Pawn(Piece):
    """docstring for Pawn"""

    def __init__(self, row, col, white, first_move=True):
        super().__init__(row, col, white)
        self.first_move = first_move


class Rook(Piece):
    pass


class Bishop(Piece):
    pass


class Night(Piece):
    """ Night used in place of Knight """
    pass


class King(Piece):
    pass


class Queen(Piece):
    pass
