""" Board module (entity) """

from chess.pieces import *
import numpy as np
from chess.constants import *


class Board:

    unit_dict = {
        'p': Pawn,
        'r': Rook,
        'n': Night,
        'b': Bishop,
        'q': Queen,
        'k': King
    }

    def __init__(self, player_white, white_to_move=True, array=None):
        self.player_white = True if player_white is True else False
        self.opponent_white = not self.player_white
        self.white_to_move = white_to_move
        self.moves = []

        self.board = np.full((DIM, DIM), Null(), dtype=object)
        if array is None:
            self._init_board_start()
        else:
            self._init_from_array(array)

    def _init_board_start(self):
        """ Inits the board according to basic chess start config """
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
        q_col, k_col = (3, 4) if self.player_white else (4, 3)

        self.board[0][q_col] = Queen(0, q_col, self.opponent_white)
        self.board[0][k_col] = King(0, k_col, self.opponent_white)
        self.board[7][q_col] = Queen(7, q_col, self.player_white)
        self.board[7][k_col] = King(7, k_col, self.player_white)

    def _init_from_array(self, array):
        for j in range(DIM):
            for i in range(DIM):
                if array[i][j] == '--':
                    continue
                is_white = True if array[i][j].startswith('w') else False
                unit = self.unit_dict[array[i][j][-1]]
                if unit == Pawn and i not in (1, 6):
                    # pawn has committed their first move
                    self.board[i][j] = unit(i, j, is_white, first_move=False)
                else:
                    self.board[i][j] = unit(i, j, is_white)

    def to_array(self):
        array = []
        for i in range(DIM):
            row = []
            for j in range(DIM):
                row.append(self.board[i][j].name)
            array.append(row)
        return array

    def get_piece(self, row, col):
        return self.board[row][col]
