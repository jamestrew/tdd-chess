""" Controller module (adapter for UIs) """
from chess import engine
from chess.pieces import *
from chess.constants import *


class Select:
    """ Select piece, shows suggestions and prepares piece for move """

    def __init__(self):
        self.pos_1 = None
        self.moves = []

    def make_selection(self, select, game):
        if select in engine.get_location(game):
            self.pos_1 = select
            self.moves = engine.get_valid_moves(game, game[select])

            if game.player_white:
                suggestions = self.moves
            else:
                suggestions = [converter(coord) for coord in self.moves]
            return suggestions

        if self.pos_1 and select in self.moves:
            move = engine.Move(self.pos_1, select, game)
            if isinstance(game[self.pos_1], Pawn) and select[0] in (0, 7):
                move.promote = Queen  # temporary
            move.execute()
            self._reset()

        self._reset()

    def _reset(self):
        self.pos_1 = None
        self.moves = []


def gui_coord(player, coord):
    y, x = coord

    if BORD < x < B_WIDTH + BORD and BORD < y < B_HEIGHT + BORD:
        row, col = (x // SQ_SIZE, y // SQ_SIZE)
        if player:
            return row, col
        else:
            return converter((row, col))

    return False


def converter(coord):
    conv = {0: 7, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1, 7: 0}
    return conv[coord[0]], conv[coord[1]]
