from chess.pieces import Night
from chess.board import Board

import pytest


@pytest.fixture
def board():
    return [
        ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
        ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
        ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]
    ]


def test_night_move_start_white(board):
    board = Board(player_white=True, white_to_move=True, array=board)
    night = board[(7, 1)]

    assert night.name == 'wn'
    assert set(night.get_moves(board)) == set([(5, 0), (5, 2)])
