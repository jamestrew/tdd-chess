from chess.board import Board
from chess.engine import *

import pytest


@pytest.mark.parametrize(
    "white, result", [
        (True, False),   # white not checked
        (False, False)   # black not checked
    ]
)
def test_no_checks(start_board, white, result):
    assert king_checked(start_board, turn_white=white) is result


@pytest.fixture
def check_board():
    arr = [
        ["br", "bn", "bb", "--", "bk", "bb", "bn", "br"],
        ["bp", "bp", "--", "bp", "bp", "--", "bp", "bp"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["bq", "--", "bp", "--", "--", "bp", "--", "wq"],
        ["--", "--", "--", "wp", "wp", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["wp", "wp", "wp", "--", "--", "--", "wp", "wp"],
        ["wr", "wn", "wb", "--", "wk", "wb", "wn", "wr"]
    ]
    return Board(array=arr)


@pytest.mark.parametrize(
    "white, result", [
        (True, True),   # white checked
        (False, True)   # black checked
    ]
)
def test_checks(check_board, white, result):
    assert king_checked(check_board, turn_white=white) is result
