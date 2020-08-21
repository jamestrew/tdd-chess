from chess.board import Board
from chess.engine import *

import pytest

[
    ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
    ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
    ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]
]


def test_no_check_white():
    game = Board()
    assert check_check(game, turn_white=True) is False


def test_no_check_black():
    game = Board()
    assert check_check(game, turn_white=False) is False


@pytest.fixture
def check_board():
    return [
        ["br", "bn", "bb", "--", "bk", "bb", "bn", "br"],
        ["bp", "bp", "--", "bp", "bp", "--", "bp", "bp"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["bq", "--", "bp", "--", "--", "bp", "--", "wq"],
        ["--", "--", "--", "wp", "wp", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["wp", "wp", "wp", "--", "--", "--", "wp", "wp"],
        ["wr", "wn", "wb", "--", "wk", "wb", "wn", "wr"]
    ]


def test_check_white(check_board):
    game = Board(array=check_board)

    assert check_check(game, turn_white=True) is True


def test_check_black(check_board):
    game = Board(array=check_board)
    assert check_check(game, turn_white=False) is True
