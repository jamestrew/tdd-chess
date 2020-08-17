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
def board_basic():
    return [
        ["br", "bn", "bb", "bq", "bk", "bb", "wp", "br"],
        ["--", "--", "--", "bp", "--", "bp", "--", "--"],
        ["--", "--", "bp", "--", "bp", "--", "--", "--"],
        ["bp", "bp", "--", "--", "--", "--", "--", "bp"],
        ["wp", "wp", "--", "--", "--", "--", "--", "wp"],
        ["--", "--", "wp", "--", "wp", "--", "--", "--"],
        ["--", "wp", "--", "wp", "--", "wp", "--", "--"],
        ["wr", "wn", "wb", "wq", "wk", "wb", "bp", "wr"]
    ]


def test_pawn_get_moves_first_white(board_basic):
    pawn = Pawn(6, 3, True)
    board = Board(player_white=True, array=board_basic, white_to_move=True)
    assert pawn.get_moves(board) == [(5, 3), (4, 3)]


def test_pawn_get_moves_first_black(board_basic):
    pawn = Pawn(1, 3, False)
    board = Board(player_white=True, array=board_basic, white_to_move=True)
    assert pawn.get_moves(board) == [(2, 3), (3, 3)]


def test_pawn_get_moves_second_white(board_basic):
    pawn = Pawn(5, 4, True, False)
    board = Board(player_white=True, array=board_basic, white_to_move=True)
    board = Board(player_white=True, array=board_basic, white_to_move=True)
    assert pawn.get_moves(board) == [(4, 4)]


def test_pawn_get_moves_second_black(board_basic):
    pawn = Pawn(2, 4, False, False)
    board = Board(player_white=True, array=board_basic, white_to_move=True)
    assert pawn.get_moves(board) == [(3, 4)]


def test_pawn_blocked_white(board_basic):
    pawn = Pawn(4, 7, True)
    board = Board(player_white=True, array=board_basic, white_to_move=True)
    assert pawn.get_moves(board) == []


def test_pawn_blocked_black(board_basic):
    pawn = Pawn(3, 7, False)
    board = Board(player_white=True, array=board_basic, white_to_move=True)
    assert pawn.get_moves(board) == []


def test_pawn_capt_white(board_basic):
    pawn = Pawn(4, 1, True, False)
    board = Board(player_white=True, array=board_basic, white_to_move=True)
    assert pawn.get_moves(board) == [(3, 0)]


def test_pawn_capt_black(board_basic):
    pawn = Pawn(3, 1, False, False)
    board = Board(player_white=True, array=board_basic, white_to_move=True)
    assert pawn.get_moves(board) == [(4, 0)]


def test_pawn_capt_white_edge(board_basic):
    pawn = Pawn(4, 0, True, False)
    board = Board(player_white=True, array=board_basic, white_to_move=True)
    assert pawn.get_moves(board) == [(3, 1)]


def test_pawn_capt_black_edge(board_basic):
    pawn = Pawn(3, 0, False, False)
    board = Board(player_white=True, array=board_basic, white_to_move=True)
    assert pawn.get_moves(board) == [(4, 1)]
