""" Engine module (Use Cases) """

class Move:

    def __init__(self, p1, p2, game):
        self.from_row, self.from_col = p1
        self.dest_row, self.dest_col = p2
        self.game = game

        self.from_piece = game.get_piece(self.from_row, self.from_col)
        self.dest_piece = game.get_piece(self.dest_row, self.dest_col)

        self.moves = self.from_piece.get_moves(self.game)
