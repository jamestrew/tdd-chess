""" Controller module (adapter for UIs) """
from chess.constants import *
from chess.pieces import Null
from chess import engine


class Select:
    """ Select piece, shows suggestions and prepares piece for move """

    def __init__(self):
        self.pos_1 = None
        self.pos_2 = None
        self.piece = None
        self.moves = []

    def make_selection(self, select, game):
        if self.pos_1 is None:
            self.pos_1 = select
        else:
            self.pos_2 = select

        if self.piece is None:
            self.piece = game[(select)]
        if not self.moves and not isinstance(self.piece, Null):
            self.moves = self.piece.get_moves(game)

        if isinstance(self.piece, Null):
            if self.pos_2 in self.moves:
                engine.Move(self.pos_1, self.pos_2, game).execute()
            self.pos_1 = None
            self.pos_2 = None
            self.piece = None
            self.moves = []
