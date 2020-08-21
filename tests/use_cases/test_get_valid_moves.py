from chess.engine import *
from chess.board import Board

import pytest


def test_safe_start(start_board):
    piece = start_board[(6, 0)]
    moves = piece.get_moves(start_board)
    valid_moves = get_valid_moves(start_board, piece)

    assert piece.name == 'wp'
    assert set(valid_moves) == set(moves)
