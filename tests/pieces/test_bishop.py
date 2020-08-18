from chess.pieces import Bishop
from chess.board import Board

import pytest


@pytest.fixture
def board():
    return [
        ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
        ["bp", "--", "bp", "--", "bp", "bp", "bp", "bp"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
        ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]
    ]


def test_bbishop_move(board):
    board = Board(player_white=True, white_to_move=False, array=board)
    bishop = board[(0, 2)]
    assert bishop.name == 'bb'
    assert bishop.get_moves(board) == [(1, 1), (2, 0), (1, 3), (2, 4), (3, 5),
                                       (4, 6), (5, 7)]


def test_bbishop_move_blocked(board):
    board = Board(player_white=True, white_to_move=False, array=board)
    bishop = board[(0, 5)]
    assert bishop.name == 'bb'
    assert bishop.get_moves(board) == []


@pytest.fixture
def test_board():
    return [
        ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
        ["bp", "--", "bp", "--", "bp", "bp", "bp", "bp"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "wb", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
        ["wr", "wn", "wb", "wq", "wk", "--", "wn", "wr"]
    ]


def test_wbishop_move_wide(test_board):
    board = Board(player_white=True, white_to_move=True, array=test_board)
    bishop = board[(3, 5)]
    assert bishop.name == 'wb'
    assert bishop.get_moves(board) == [(2, 4), (1, 3), (0, 2),
                                       (2, 6), (1, 7),
                                       (4, 4), (5, 3),
                                       (4, 6), (5, 7)]
