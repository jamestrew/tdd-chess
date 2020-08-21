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

    def _append(self, dx, dy, game, short=False):
        """ Appends move to moves for pieces.
            Use 'short=False' for (Rook, Bishop, Queen).
            Use 'short=True' for (King, Night).
        """
        multi = 1
        while True:
            new_r = self.row + multi * dx
            new_c = self.col + multi * dy
            sqr = (new_r, new_c)

            if new_r < 0 or new_r >= DIM or new_c < 0 or new_c >= DIM:
                break
            if isinstance(game[sqr], Null):
                self.moves.append(sqr)
                if short:
                    return
            elif self._check_capture(new_r, new_c, game):
                self.moves.append(sqr)
                if short:
                    return
                break
            else:
                break
            multi += 1


class Pawn(Piece):
    """Ruleset for pawns"""

    def __init__(self, row, col, is_white, first_move=True):
        super().__init__(row, col, is_white)
        self.first_move = first_move
        self.enpassantable = False

    def get_moves(self, game):
        row = self.row
        col = self.col
        moves = []
        fwd = -1 if self.is_white is True else 1

        # move
        if isinstance(game[(row + fwd, col)], Null):
            moves.append((row + fwd, col))
            if self.first_move and isinstance(game[(row + 2 * fwd, col)], Null):
                moves.append((row + 2 * fwd, col))

        # capture
        for side in [-1, 1]:
            new_c = col + side
            if new_c < 0 or new_c >= DIM:  # off the board
                continue
            # basic capture
            if self._check_capture(row + fwd, col + side, game):
                moves.append((row + fwd, col + side))
            # en passant
            if self._check_capture(row, new_c, game) and \
                    isinstance(game[(row, new_c)], Pawn) and \
                    game[(row, new_c)].enpassantable:
                moves.append((row + fwd, new_c))
        # breakpoint()
        return moves


class Rook(Piece):

    def __init__(self, row, col, is_white, first_move=True):
        super().__init__(row, col, is_white)
        self.first_move = first_move

    def get_moves(self, game):
        """
            To-do:
                - enable castling
        """
        self.moves = []

        for dx, dy in permutations([1, -1, 0], 2):
            if abs(dx) != abs(dy):
                self._append(dx, dy, game)
        return self.moves

    def __repr__(self):
        return self.__class__.__name__ + \
            f"({self.row}, {self.col}, white={self.is_white}, first={self.first_move})"


class Bishop(Piece):

    def get_moves(self, game):
        self.moves = []

        for dx in (-1, 1):
            for dy in (-1, 1):
                self._append(dx, dy, game)
        return self.moves


class Night(Piece):
    """ Night used in place of Knight """

    def get_moves(self, game):
        self.moves = []

        for dx, dy in permutations([1, 2, -1, -2], 2):
            if abs(dx) != abs(dy):
                self._append(dx, dy, game, short=True)
        return self.moves


class King(Piece):

    def __init__(self, row, col, is_white, first_move=True):
        super().__init__(row, col, is_white)
        self.first_move = first_move

    def get_moves(self, game):
        """
        To-do:
            - incorporate castling
        """
        self.moves = []

        for dx in (-1, 1):
            for dy in (-1, 1):
                self._append(dx, dy, game, short=True)
        for dx, dy in permutations([1, -1, 0], 2):
            if abs(dx) != abs(dy):
                self._append(dx, dy, game, short=True)
        return self.moves


class Queen(Piece):

    def get_moves(self, game):
        self.moves = []

        for dx in (-1, 1):
            for dy in (-1, 1):
                self._append(dx, dy, game)
        for dx, dy in permutations([1, -1, 0], 2):
            if abs(dx) != abs(dy):
                self._append(dx, dy, game)
        return self.moves


class Null:
    """ Represents empty spaces on the chess board """

    def __init__(self):
        self.name = '--'
