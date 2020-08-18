""" Engine module (Use Cases) """
from chess.pieces import Null
from chess.constants import *

class Move:

    def __init__(self, p1, p2, game):
        self.from_row, self.from_col = p1
        self.dest_row, self.dest_col = p2
        self.game = game

        self.from_piece = game[(self.from_row, self.from_col)]
        self.dest_piece = game[(self.dest_row, self.dest_col)]

    def execute(self):
        self.game[(self.from_row, self.from_col)] = Null()
        self.game[(self.dest_row, self.dest_col)] = self.from_piece

        self.game.moves.append(self._get_rank_file())
        self.game.white_to_move = not self.game.white_to_move

        self.from_piece.first_move = False

    def _get_rank_file(self):
        """ Convert array row/col to chess grid notation """
        return str(self.game.files[self.dest_col]
                   + str(self.game.ranks[self.dest_row]))  # noqa


class GetMoves:
    """ Get a list of all possible moves.
        Facilitates controller.Select
    """

    def get_all_moves(self, game):
        self.all_moves = []
        for i in range(DIM):
            for j in range(DIM):
                piece = game[(i, j)]
                if isinstance(piece, Null):
                    continue
                if (move := piece.get_moves(game)):
                    self.all_moves.extend(move)
        return set(self.all_moves)
