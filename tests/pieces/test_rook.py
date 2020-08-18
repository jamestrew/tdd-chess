from chess.pieces import Rook
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


def test_rook_move_stuck_white(basic_board):
    board = Board(player_white=True, white_to_move=True, array=basic_board)
    rook = board[(7, 0)]

    assert rook.name == 'wr'
    assert set(rook.get_moves(board)) == set([])


@pytest.fixture
def wide_board():
    return [
        ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
        ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "wr", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
        ["--", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]
    ]


def test_rook_move_wide_white(wide_board):
    board = Board(player_white=True, white_to_move=True, array=wide_board)
    rook = board[(4, 2)]

    assert rook.name == 'wr'
    assert set(rook.get_moves(board)) == set([(4, 1), (4, 0),
                                              (3, 2), (2, 2), (1, 2),
                                              (4, 3), (4, 4), (4, 5),
                                              (4, 6), (4, 7), (5, 2)
                                              ])
