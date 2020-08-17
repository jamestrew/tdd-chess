from chess.pieces import Pawn

import pytest


def test_pawn_init():
    pawn = Pawn(1, 0, False)

    assert pawn.row == 1
    assert pawn.col == 0
    assert pawn.is_white is False
    assert pawn.first_move is True


def test_pawn_unit():
    pawn = Pawn(1, 0, False)
    assert pawn.unit == 'p'


def test_pawn_name():
    pawn = Pawn(1, 0, False)
    assert pawn.name == 'bp'


def test_pawn_repr():
    pawn = Pawn(1, 0, False)
    rep = pawn.__repr__()
    assert rep == "Pawn(1, 0, is_white=False)"


@pytest.fixture
def board_basic():
    return [
        ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
        ["--", "--", "--", "bp", "--", "bp", "bp", "--"],
        ["--", "--", "bp", "--", "bp", "--", "--", "--"],
        ["bp", "bp", "--", "--", "--", "--", "--", "bp"],
        ["wp", "wp", "--", "--", "--", "--", "--", "wp"],
        ["--", "--", "wp", "--", "wp", "--", "--", "--"],
        ["--", "wp", "--", "wp", "--", "wp", "wp", "--"],
        ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]
    ]


def test_pawn_get_moves_first_white(board_basic):
    pawn = Pawn(6, 3, True)
    assert pawn.get_moves(board_basic) == [(5, 3), (4, 3)]


def test_pawn_get_moves_first_black(board_basic):
    pawn = Pawn(1, 3, False)
    assert pawn.get_moves(board_basic) == [(2, 3), (3, 3)]


def test_pawn_get_moves_second_white(board_basic):
    pawn = Pawn(5, 4, True, False)
    assert pawn.get_moves(board_basic) == [(4, 4)]


def test_pawn_get_moves_second_black(board_basic):
    pawn = Pawn(2, 4, False, False)
    assert pawn.get_moves(board_basic) == [(3, 4)]


def test_pawn_blocked_white(board_basic):
    pawn = Pawn(4, 7, True)
    assert pawn.get_moves(board_basic) == []


def test_pawn_blocked_black(board_basic):
    pawn = Pawn(3, 7, False)
    assert pawn.get_moves(board_basic) == []


def test_pawn_capt_white(board_basic):
    pawn = Pawn(4, 1, True, False)
    assert pawn.get_moves(board_basic) == [(3, 0)]


def test_pawn_capt_black(board_basic):
    pawn = Pawn(3, 1, False, False)
    assert pawn.get_moves(board_basic) == [(4, 0)]
