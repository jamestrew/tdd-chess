from chess.board import Board

import pytest


@pytest.fixture
def board():
    arr = [
        ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
        ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "wq", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
        ["wr", "wn", "wb", "--", "wk", "wb", "wn", "wr"]
    ]
    return Board(array=arr)


@pytest.mark.parametrize(
    "coord, piece, moves", [
        ((0, 3), 'bq', []),  # black blocked
        ((4, 2), 'wq', [(4, 1), (4, 0), (3, 2), (2, 2), (1, 2), (4, 3), (4, 4),
                        (4, 5), (4, 6), (4, 7), (5, 2), (3, 1), (2, 0), (3, 3),
                        (2, 4), (1, 5), (5, 1), (6, 0), (5, 3)])
    ]
)
def test_queen_moves(board, coord, piece, moves):
    queen = board[coord]
    assert queen.name == piece
    assert set(queen.get_moves(board)) == set(moves)
