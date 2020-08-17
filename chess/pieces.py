""" Pieces Module (entities) """
from chess.constants import *


class Piece:
    """ Parent class for all chess pieces """

    unit_dict = {
        'Pawn': 'p',
        'Rook': 'r',
        'Night': 'n',
        'Bishop': 'b',
        'Queen': 'q',
        'King': 'k',
        'Piece': 'x'
    }

    def __init__(self, row, col, is_white):
        self.row = row
        self.col = col
        self.is_white = is_white  # bool

        self.unit = self.unit_dict[self.__class__.__name__]

        if self.is_white:
            self.name = 'w' + self.unit
        else:
            self.name = 'b' + self.unit

    def __repr__(self):
        return self.__class__.__name__ + \
            f"({self.row}, {self.col}, is_white={self.is_white})"

    def get_moves(self, game):
        raise NotImplementedError

    def _check_capture(self, new_r, new_c, game):
        piece = game[(new_r, new_c)]
        if not isinstance(piece, Null):
            if piece.is_white != self.is_white:
                return (new_r, new_c)


class Pawn(Piece):
    """Ruleset for pawns"""

    def __init__(self, row, col, is_white, first_move=True):
        super().__init__(row, col, is_white)
        self.first_move = first_move

    def get_moves(self, game):
        row = self.row
        col = self.col
        moves = []
        fwd = -1 if self.is_white is True else 1

        # basic move
        if isinstance(game[(row + fwd, col)], Null):
            moves.append((row + fwd, col))
            if self.first_move:
                moves.append((row + 2 * fwd, col))

        # basic capture
        for side in [-1, 1]:
            if col + side in (-1, DIM):
                continue

            if self._check_capture(row + fwd, col + side, game) is not None:
                moves.append((row + fwd, col + side))

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
