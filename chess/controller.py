""" Controller module (adapter for UIs) """
from chess import engine


class Select:
    """ Select piece, shows suggestions and prepares piece for move """

    def __init__(self):
        self.pos_1 = None
        self.moves = []

    def make_selection(self, select, game):
        if select in engine.get_location(game):
            self.pos_1 = select
            self.moves = engine.get_valid_moves(game, game[select])
            return self.moves

        if self.pos_1 and select in self.moves:
            engine.Move(self.pos_1, select, game).execute()
            self._reset()

        self._reset()

    def _reset(self):
        self.pos_1 = None
        self.moves = []
