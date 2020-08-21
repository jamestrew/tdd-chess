""" Controller module (adapter for UIs) """
from chess.constants import *
from chess.pieces import Null
from chess import engine


class Select:
    """ Select piece, shows suggestions and prepares piece for move """

    def __init__(self):
        self.pos_1 = None
        self.moves = []

    def make_selection(self, select, game):
        if select in engine.get_location(game):
            self.pos_1 = select
            self.moves = game[select].get_moves(game)
            return self.moves

        if self.pos_1 and select in self.moves:
            engine.Move(self.pos_1, select, game).execute()
            self._reset()

        self._reset()

    def _reset(self):
        self.pos_1 = None
        self.moves = []
