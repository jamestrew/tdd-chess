""" Engine module (Use Cases) """
from chess.pieces import *
from chess.constants import *


class Move:
    """
        To-do:
            - enable promotion
            - move rook during castling
    """

    def __init__(self, pos_1, pos_2, game):
        self.pos_1 = pos_1
        self.pos_2 = pos_2
        self.game = game

        self.from_piece = game[pos_1]
        self.dest_piece = game[pos_2]

    def execute(self):
        self._castle()
        self._enpassant()
        self.game[self.pos_1] = Null()
        self.game[self.pos_2] = self.from_piece

        self.game.moves.append(self._get_rank_file())
        self.game.white_to_move = not self.game.white_to_move
        self._enpassant_config()

    def _get_rank_file(self):
        """ Convert array row/col to chess grid notation """
        return str(self.game.files[self.pos_2[1]]
                   + str(self.game.ranks[self.pos_2[0]]))  # noqa

    def _enpassant(self):
        """ Helper function to execute en passant capture """
        if not isinstance(self.from_piece, Pawn):
            return
        piece_loc = (self.pos_1[0], self.pos_2[1])
        piece = self.game[piece_loc]
        ep_true = piece.enpassantable if isinstance(piece, Pawn) else False
        if self.pos_1[1] == self.pos_2[1] and not ep_true:
            return

        self.game[piece_loc] = Null()

    def _enpassant_config(self):
        """ Helper function to config pawn according to en passant rules """
        if not isinstance(self.from_piece, Pawn):
            return
        if self.from_piece.first_move and abs(self.pos_1[0] - self.pos_2[0]) == 2:
            self.from_piece.enpassantable = True
        else:
            self.from_piece.enpassantable = False
        self.from_piece.first_move = False

    def _castle(self):
        if not isinstance(self.from_piece, King):
            return

        move = get_castling(self.game, self.from_piece)
        # breakpoint()
        if self.pos_2 not in move.get(King):
            return

        index = move.get(King).index(self.pos_2)
        rook_dest = move.get(Rook)[index]
        rook_col = 0 if index else 7
        rook_row = self.pos_2[0]

        # move rook
        rook = self.game[(rook_row, rook_col)]
        self.game[(rook_row, rook_col)] = Null()
        self.game[rook_dest] = rook

        # config pieces
        rook.first_move = False
        self.from_piece.first_move = False


def get_all_moves(game, for_white):
    """ Get a list of all possible moves.
    Facilitates controller.Select
    """
    all_moves = []
    for row in game.board:
        for piece in row:
            if isinstance(piece, Null) or piece.is_white != for_white:
                continue
            if (move := piece.get_moves(game)):
                all_moves.extend(move)
    return set(all_moves)


def get_location(game, turn_white=None, find_piece=None):
    """ Get a list of location of all pieces either color.
        By default, returns the color of the current turn.
    """
    turn_white = game.white_to_move if turn_white is None else turn_white

    location = []
    for row in game.board:
        for piece in row:
            if isinstance(piece, Null) or piece.is_white != turn_white:
                continue
            if find_piece is not None:
                if not isinstance(piece, find_piece):
                    continue
            location.append((piece.row, piece.col))

    if not location:
        return location
    elif len(location) == 1:
        return location.pop()
    else:
        return set(location)


def king_checked(game, turn_white):
    """ returns True if king is in check """
    opp_moves = get_all_moves(game, for_white=(not turn_white))
    king_pos = get_location(game, turn_white=turn_white, find_piece=King)

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

    if isinstance(piece, King) and piece.first_move:
        valid_moves.extend(get_castling(game, piece).get(King))
    return valid_moves


def get_castling(game, king):
    """ Returns valid castling moves if possible. """

    """
        To-do:
            - check king is not currently in check
            - check king doesn't pass through sqr currently attacked
            - check king doesn't end up in check

    """
    moves = {King: [(), ()], Rook: [(), ()]}
    white = king.is_white
    rook_locs = get_location(game, turn_white=white, find_piece=Rook)
    rooks = [game[loc] for loc in rook_locs if game[loc].first_move]

    if not rooks:
        return moves

    row = rooks[0].row
    for rook in rooks:
        king_side = rook.col > king.col
        mult = 1

        if king_side:
            start, end = king.col + 1, rook.col
        else:
            start, end = rook.col + 1, king.col

        for col in range(start, end):
            if not isinstance(game[(row, col)], Null):
                break
        else:
            if king_side:
                moves[King][0] = (row, king.col + mult * 2)
                moves[Rook][0] = (row, rook.col - mult * 2)
            else:
                moves[King][1] = (row, king.col - mult * 2)
                moves[Rook][1] = (row, rook.col + mult * 3)
    return moves
