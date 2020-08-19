from chess.engine import get_all_moves
from chess.board import Board

import pytest


def test_start_get_all_moves_white():
    # bad incomplete
    board = Board()
    moves = get_all_moves(board, for_white=True)

    assert moves == set([(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5),
                         (4, 6), (4, 7), (5, 0), (5, 1), (5, 2), (5, 3),
                         (5, 4), (5, 5), (5, 6), (5, 7)])


def test_start_get_all_moves_black():
    # bad incomplete
    board = Board()
    moves = get_all_moves(board, for_white=False)

    assert moves == set([(2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5),
                         (2, 6), (2, 7), (3, 0), (3, 1), (3, 2), (3, 3),
                         (3, 4), (3, 5), (3, 6), (3, 7)])


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


# def test_mid_get_moves_white(check_board):
#     board = Board(array=check_board)
#     moves = get_all_moves(board, for_white=True)

#     assert moves == []


# def test_mid_get_moves_black(check_board):
#     board = Board(array=check_board)
#     moves = get_all_moves(board, for_white=False)

#     assert moves == []
