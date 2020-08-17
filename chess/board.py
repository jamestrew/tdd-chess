""" Board module (entity) """

from chess.pieces import *
import numpy as np
from chess.constants import *


class Board:

    def __init__(self, player_white=True):
        self.player_white = True if player_white is True else False
        self.opponent_white = not self.player_white
        self.moves = []

        self.board = np.full((DIM, DIM), Null(), dtype=object)

        self.board[0][0] = Rook(0, 0, self.opponent_white)
        self.board[0][1] = Night(0, 1, self.opponent_white)
        self.board[0][2] = Bishop(0, 2, self.opponent_white)
        self.board[0][5] = Bishop(0, 5, self.opponent_white)
        self.board[0][6] = Night(0, 6, self.opponent_white)
        self.board[0][7] = Rook(0, 7, self.opponent_white)

        for i in range(DIM):
            self.board[1][i] = Pawn(1, i, self.opponent_white)
            self.board[6][i] = Pawn(6, i, self.player_white)

        self.board[7][0] = Rook(7, 0, self.player_white)
        self.board[7][1] = Night(7, 1, self.player_white)
        self.board[7][2] = Bishop(7, 2, self.player_white)
        self.board[7][5] = Bishop(7, 5, self.player_white)
        self.board[7][6] = Night(7, 6, self.player_white)
        self.board[7][7] = Rook(7, 7, self.player_white)

        # flip the King/Queen depending on the player_white
        if self.player_white:
            q_col = 3
            k_col = 4
        else:
            q_col = 4
            k_col = 3

        self.board[0][q_col] = Queen(0, q_col, self.opponent_white)
        self.board[0][k_col] = King(0, k_col, self.opponent_white)
        self.board[7][q_col] = Queen(7, q_col, self.player_white)
        self.board[7][k_col] = King(7, k_col, self.player_white)
