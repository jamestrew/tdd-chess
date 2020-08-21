from chess.board import Board

import pytest


@pytest.fixture
def board():
    arr = [
        ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
        ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "wr", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
        ["--", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]
    ]
    return Board(array=arr)


@pytest.mark.parametrize(
    "coord, piece, moves", [
        ((0, 0), 'br', []),  # black blocked
        ((4, 2), 'wr', [(4, 1), (4, 0), (3, 2), (2, 2), (1, 2),
                        (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (5, 2)])
    ]
)
def test_rook_moves(board, coord, piece, moves):
    rook = board[coord]

    assert rook.name == piece
    assert set(rook.get_moves(board)) == set(moves)
