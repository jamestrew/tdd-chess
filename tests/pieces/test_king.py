from chess.pieces import King
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


def test_king_move_stuck_white(basic_board):
    board = Board(player_white=True, white_to_move=True, array=basic_board)
    king = board[(7, 4)]

    assert king.name == 'wk'
    assert set(king.get_moves(board)) == set([])


@pytest.fixture
def wide_board():
    return [
        ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
        ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
        ["--", "--", "--", "--", "wk", "--", "--", "--"],
        ["--", "--", "--", "--", "wp", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["wp", "wp", "wp", "wp", "--", "wp", "wp", "wp"],
        ["wr", "wn", "wb", "wq", "--", "wb", "wn", "wr"]
    ]


def test_king_move_wide_white(wide_board):
    board = Board(player_white=True, white_to_move=True, array=wide_board)
    king = board[(2, 4)]

    assert king.name == 'wk'
    assert set(king.get_moves(board)) == set([(2, 3), (1, 3), (1, 4), (1, 5),
                                              (2, 5), (3, 5), (3, 3)])
