""" Pieces Module (entities) """


class Piece:
    """ Parent class for all chess pieces """

    def __init__(self, row, col, is_white):
        self.row = row
        self.col = col
        self.is_white = is_white  # bool

        unit_name = self.__class__.__name__
        # Unit is simply the first letter of the piece type
        # eg. Pawn = 'p', Knight = 'n' (the one except commonly used)
        self.unit = unit_name[0].lower()

        if self.is_white is True:
            self.name = 'w' + self.unit
        else:
            self.name = 'b' + self.unit

    def __repr__(self):
        return self.__class__.__name__ + \
            f"({self.row}, {self.col}, is_white={self.is_white})"

    def get_moves(self):
        raise NotImplementedError


class Pawn(Piece):
    """docstring for Pawn"""

    def __init__(self, row, col, is_white, first_move=True):
        super().__init__(row, col, is_white)
        self.first_move = first_move

    def get_moves(self, board):
        moves = []
        fwd = -1 if self.is_white is True else 1

        if board[self.row + fwd][self.col] == '--':
            moves.append((self.row + fwd, self.col))
            if self.first_move:
                moves.append((self.row + 2 * fwd, self.col))
        return moves


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


class Null:
    """ Represents empty spaces on the chess board """

    def __init__(self):
        self.name = '--'
