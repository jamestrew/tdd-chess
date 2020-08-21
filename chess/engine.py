""" Engine module (Use Cases) """
from chess.pieces import *
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
        self._config_en_passant()

        self.game.moves.append(self._get_rank_file())
        self.game.white_to_move = not self.game.white_to_move

    def _get_rank_file(self):
        """ Convert array row/col to chess grid notation """
        return str(self.game.files[self.pos_2[1]]
                   + str(self.game.ranks[self.pos_2[0]]))  # noqa

    def _config_en_passant(self):
        if not isinstance(self.from_piece, Pawn):
            return
        if self.from_piece.first_move and abs(self.pos_1[0] - self.pos_2[0]) == 2:
            self.from_piece.enpassantable = True
        else:
            self.from_piece.enpassantable = False
        self.from_piece.first_move = False


def get_all_moves(game, for_white):
    """ Get a list of all possible moves.
    Facilitates controller.Select
    """

    all_moves = []
    for i in range(DIM):
        for j in range(DIM):
            piece = game[(i, j)]
            if isinstance(piece, Null) or piece.is_white != for_white:
                continue
            if (move := piece.get_moves(game)):
                all_moves.extend(move)
    return set(all_moves)


def get_location(game, turn_white=None, find_king=False):
    """ Get a list of location of all pieces either color.
        By default, returns the color of the current turn.
    """
    turn_white = game.white_to_move if turn_white is None else turn_white

    location = []
    for i in range(DIM):
        for j in range(DIM):
            piece = game[(i, j)]
            if isinstance(piece, Null) or piece.is_white != turn_white:
                continue
            if find_king:
                if not isinstance(piece, King):
                    continue
            location.append((piece.row, piece.col))
    return location.pop() if len(location) == 1 else set(location)


def king_checked(game, turn_white):
    """ returns True if king is in check """
    opp_moves = get_all_moves(game, for_white=(not turn_white))
    king_pos = get_location(game, turn_white=turn_white, find_king=True)

    return king_pos in opp_moves


def move_allows_check(game, piece, turn_white=None):
    """ Checks whether moving selected piece will result in
        own king being checked.

        CURRENTLY RELEGATED.
    """
    piece_loc = piece.row, piece.col
    piece_moves = piece.get_moves(game)

    for move in piece_moves:
        # move peek
        game[piece_loc] = Null()
        game[move] = piece
        invalid = king_checked(game, piece.is_white)
        game[move] = Null()
        if invalid:
            break
    else:
        invalid = False

    # revert peek
    game[piece_loc] = piece
    return invalid


def get_valid_moves(game, piece):
    """ Returns all valid moves (disregards moves which will result in
        own king being checked.)
    """
    all_moves = piece.get_moves(game)
    piece_loc = piece.row, piece.col

    valid_moves = []
    for move in all_moves:
        game[piece_loc] = Null()
        capt_piece = game[move]
        game[move] = piece
        if not king_checked(game, turn_white=piece.is_white):
            valid_moves.append(move)
        game[move] = capt_piece
    game[piece_loc] = piece

    return valid_moves
