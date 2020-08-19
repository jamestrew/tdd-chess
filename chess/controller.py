""" Controller module (adapter for UIs) """
from chess.constants import *
from chess.pieces import Null
from chess import engine


class Select:
    """ Select piece, shows suggestions and prepares piece for move """

    def __init__(self):
        self.pos_1 = None
        self.piece = None
        self.moves = []

    def make_selection(self, select, game):
        if select in engine.get_location(game):
            self.pos_1 = select
            self.piece = game[select]
            self.moves = game[select].get_moves(game)
            return

        if self.pos_1 and select in self.moves:
            engine.Move(self.pos_1, select, game)
            self._reset()
            return "engine.Move(self.pos_1, self.pos_2, game).execute()"

        self._reset()

    def _reset(self):
        self.pos_1 = None
        self.piece = None
        self.moves = []
