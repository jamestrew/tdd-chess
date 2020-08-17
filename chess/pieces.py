""" Pieces Module (entities) """
from chess.constants import *
from itertools import permutations


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
        """ returns True if capture is possible """
        piece = game[(new_r, new_c)]
        if not isinstance(piece, Null):
            return piece.is_white != self.is_white


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

            if self._check_capture(row + fwd, col + side, game):
                moves.append((row + fwd, col + side))

        return moves


class Rook(Piece):
    pass


class Bishop(Piece):

    def get_moves(self, game):
        moves = []

        def _check_move(new_r, new_c):
            """ [Helper function] may be moved to superclass in the future
                Add move. Returns False if a capture is possible.
                Return False causes a break.
            """
            if isinstance(game[(new_r, new_c)], Null):
                moves.append((new_r, new_c))
                return True
            elif self._check_capture(new_r, new_c, game):
                moves.append((new_r, new_c))
                return False
            return False

        def append(dx, dy):
            multi = 1
            while True:
                new_r = self.row + multi * dx
                new_c = self.col + multi * dy

                if new_r < 0 or new_r >= DIM or new_c < 0 or new_c >= DIM:
                    break
                if not _check_move(new_r, new_c):
                    break
                multi += 1

        for dx in (-1, 1):
            for dy in (-1, 1):
                append(dx, dy)
        return moves


class Night(Piece):
    """ Night used in place of Knight """

    def get_moves(self, game):
        moves = []

        for dx, dy in permutations([1, 2, -1, -2], 2):
            if abs(dx) == abs(dy):
                continue

            new_r = self.row + dx
            new_c = self.col + dy
            if new_r < 0 or new_r >= DIM or new_c < 0 or new_c >= DIM:
                continue
            if isinstance(game[(new_r, new_c)], Null):
                moves.append((new_r, new_c))
            if self._check_capture(new_r, new_c, game):
                moves.append((new_r, new_c))
        return moves


class King(Piece):
    pass


class Queen(Piece):
    pass


class Null:
    """ Represents empty spaces on the chess board """

    def __init__(self):
        self.name = '--'
