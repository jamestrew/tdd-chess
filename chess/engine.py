""" Engine module (Use Cases) """
from chess.pieces import Null
from chess.constants import *

class Move:

    def __init__(self, pos_1, pos_2, game):
        self.pos_1 = pos_1
        self.pos_2 = pos_2
        self.game = game

        self.from_piece = game[pos_1]
        self.dest_piece = game[pos_2]

    def execute(self):
        self.game[self.pos_1] = Null()
        self.game[self.pos_2] = self.from_piece
        self.from_piece.row, self.from_piece.col = self.pos_2

        self.game.moves.append(self._get_rank_file())
        self.game.white_to_move = not self.game.white_to_move

        self.from_piece.first_move = False

    def _get_rank_file(self):
        """ Convert array row/col to chess grid notation """
        return str(self.game.files[self.pos_2[1]]
                   + str(self.game.ranks[self.pos_2[0]]))  # noqa


def get_all_moves(game):
    """ Get a list of all possible moves.
    Facilitates controller.Select
    """
    all_moves = []
    for i in range(DIM):
        for j in range(DIM):
            piece = game[(i, j)]
            if isinstance(piece, Null):
                continue
            if (move := piece.get_moves(game)):
                all_moves.extend(move)
    return set(all_moves)


def get_location(game):
    """ Get a list of location of all pieces for the correct turn """
    turn_white = game.white_to_move

    location = []
    for i in range(DIM):
        for j in range(DIM):
            piece = game[(i, j)]
            if isinstance(piece, Null) or piece.is_white != turn_white:
                continue
            location.append((piece.row, piece.col))
    return location
