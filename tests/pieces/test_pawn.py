from chess.pieces import Pawn
from chess.board import Board

import pytest


def test_pawn_init():
    pawn = Pawn(1, 0, False)

    assert pawn.row == 1
    assert pawn.col == 0
    assert pawn.is_white is False
    assert pawn.first_move is True
    assert pawn.unit == 'p'
    assert pawn.name == 'bp'

    rep = pawn.__repr__()
    assert rep == "Pawn(1, 0, is_white=False)"


def test_pawn_init_not_first_move():
    pawn = Pawn(3, 1, False, False)

    assert pawn.first_move is False


@pytest.fixture
def board():
    arr = [
        ["br", "bn", "bb", "bq", "bk", "bb", "wp", "br"],
        ["--", "--", "--", "bp", "--", "bp", "--", "--"],
        ["--", "--", "bp", "--", "bp", "--", "--", "--"],
        ["bp", "bp", "--", "--", "--", "--", "--", "bp"],
        ["wp", "wp", "--", "--", "--", "--", "--", "wp"],
        ["--", "--", "wp", "--", "wp", "--", "--", "--"],
        ["--", "wp", "--", "wp", "--", "wp", "--", "--"],
        ["wr", "wn", "wb", "wq", "wk", "wb", "bp", "wr"]
    ]
    return Board(array=arr)


@pytest.mark.parametrize(
    "coord, piece_name, moves", [
        ((6, 3), 'wp', [(5, 3), (4, 3)]),  # white first move
        ((1, 3), 'bp', [(2, 3), (3, 3)]),  # black first move
        ((5, 4), 'wp', [(4, 4)]),          # white second move
        ((2, 4), 'bp', [(3, 4)]),          # black second move
        ((4, 7), 'wp', []),                # white blocked
        ((3, 7), 'bp', []),                # black blocked
        ((4, 1), 'wp', [(3, 0)]),          # white capture
        ((3, 1), 'bp', [(4, 0)]),          # black capture
        ((4, 0), 'wp', [(3, 1)]),          # white capture on board edge
        ((3, 0), 'bp', [(4, 1)])           # black capture on board edge
    ]
)
def test_pawn_get_moves(board, coord, piece_name, moves):
    pawn = board[coord]
    assert pawn.name == piece_name
    assert pawn.get_moves(board) == moves
