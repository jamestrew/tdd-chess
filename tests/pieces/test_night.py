from chess.pieces import Night
from chess.board import Board

import pytest


@pytest.fixture
def basic_board():
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


def test_night_move_start_white(basic_board):
    board = Board(player_white=True, white_to_move=True, array=basic_board)
    night = board[(7, 1)]

    assert night.name == 'wn'
    assert set(night.get_moves(board)) == set([(5, 0), (5, 2)])


@pytest.fixture
def wide_board():
    return [
        ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
        ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "wn", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "wp", "--", "--", "--", "--", "--"],
        ["wp", "wp", "--", "wp", "wp", "wp", "wp", "wp"],
        ["wr", "--", "wb", "wq", "wk", "wb", "wn", "wr"]
    ]


def test_night_move_wide_white(wide_board):
    board = Board(player_white=True, white_to_move=True, array=wide_board)
    night = board[(3, 3)]

    assert night.name == 'wn'
    assert set(night.get_moves(board)) == set([(1, 2), (1, 4), (2, 5), (4, 5),
                                               (5, 4), (4, 1), (2, 1)])
