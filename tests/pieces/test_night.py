from chess.board import Board

import pytest


@pytest.fixture
def board():
    arr = [
        ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
        ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "wn", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "wp", "--", "--", "--", "--", "--"],
        ["wp", "wp", "--", "wp", "wp", "wp", "wp", "wp"],
        ["wr", "--", "wb", "wq", "wk", "wb", "wn", "wr"]
    ]
    return Board(array=arr)


@pytest.mark.parametrize(
    "coord, piece_name, moves", [
        ((7, 6), 'wn', [(5, 5), (5, 7)]),
        ((3, 3), 'wn', [(1, 2), (1, 4), (2, 5), (4, 5), (5, 4), (4, 1), (2, 1)])
    ]
)
def test_moves(board, coord, piece_name, moves):
    night = board[coord]
    assert night.name == piece_name
    assert set(night.get_moves(board)) == set(moves)
