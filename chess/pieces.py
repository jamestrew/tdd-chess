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

    def _check_move(new_r, new_c):
        """ [Helper function] - currently unused.
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

    def get_moves(self, game):
        moves = []

        def append(dx, dy):
            multi = 1
            while True:
                new_r = self.row + multi * dx
                new_c = self.col + multi * dy
                sqr = (new_r, new_c)

                if new_r < 0 or new_r >= DIM or new_c < 0 or new_c >= DIM:
                    break
                if isinstance(game[sqr], Null):
                    moves.append(sqr)
                elif self._check_capture(new_r, new_c, game):
                    moves.append(sqr)
                    break
                else:
                    break
                multi += 1

        for dx, dy in permutations([1, -1, 0], 2):
            if abs(dx) != abs(dy):
                append(dx, dy)
        return moves


class Bishop(Piece):

    def get_moves(self, game):
        moves = []

        def append(dx, dy):
            multi = 1
            while True:
                new_r = self.row + multi * dx
                new_c = self.col + multi * dy
                sqr = (new_r, new_c)

                if new_r < 0 or new_r >= DIM or new_c < 0 or new_c >= DIM:
                    break
                if isinstance(game[sqr], Null):
                    moves.append(sqr)
                elif self._check_capture(new_r, new_c, game):
                    moves.append(sqr)
                    break
                else:
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
            sqr = (new_r, new_c)

            if new_r < 0 or new_r >= DIM or new_c < 0 or new_c >= DIM:
                continue
            if isinstance(game[sqr], Null):
                moves.append(sqr)
            elif self._check_capture(new_r, new_c, game):
                moves.append(sqr)
        return moves


class King(Piece):
    pass


class Queen(Piece):
    pass


class Null:
    """ Represents empty spaces on the chess board """

    def __init__(self):
        self.name = '--'
