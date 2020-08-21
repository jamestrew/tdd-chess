from chess.engine import *
from chess.board import Board

import pytest


def test_false_start(start_board):
    piece = start_board[(6, 0)]
    assert piece.name == 'wp'
    assert piece.is_white is True
    assert move_allows_check(start_board, piece) is False


@pytest.mark.parametrize(
    "coord, piece_name, result", [
        ((6, 4), 'wp', False),
        ((6, 5), 'wp', True)
    ]
)
def test_non_king_move(test_game, test_arr, coord, piece_name, result):
    piece = test_game[coord]
    assert piece.name == piece_name
    assert move_allows_check(test_game, piece) is result
    assert test_game.to_array() == test_arr


@pytest.fixture
def test_arr():
    return [["br", "bn", "--", "--", "bk", "bb", "bn", "br"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "bq", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "bb"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]]


@pytest.fixture
def test_game(test_arr):
    return Board(array=test_arr)


@pytest.fixture
def test_king_arr():
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


@pytest.fixture
def test_king_game():
    return Board(array=test_king_arr)
