from chess.board import Board

import pytest


@pytest.fixture
def board():
    arr = [
        ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
        ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
        ["--", "--", "--", "--", "wk", "--", "--", "--"],
        ["--", "--", "--", "--", "wp", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["wp", "wp", "wp", "wp", "--", "wp", "wp", "wp"],
        ["wr", "wn", "wb", "wq", "--", "wb", "wn", "wr"]
    ]
    return Board(array=arr)


@pytest.mark.parametrize(
    "coord, piece, moves", [
        ((0, 4), 'bk', []),  # black blocked
        # white wide
        ((2, 4), 'wk', [(2, 3), (1, 3), (1, 4), (1, 5), (2, 5), (3, 5), (3, 3)])
    ]
)
def test_king_moves(board, coord, piece, moves):
    king = board[coord]

    assert king.name == piece
    assert set(king.get_moves(board)) == set(moves)
