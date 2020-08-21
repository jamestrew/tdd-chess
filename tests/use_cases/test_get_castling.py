from chess.engine import *
from chess.board import Board

import pytest


def test_start_white(start_board):
    assert get_castling(start_board, turn_white=True) == []

# --- Facing white --- #  noqa


@pytest.mark.parametrize(
    "qside_first, kside_first, soln", [
        (True, True, [(7, 2), (7, 6)]),  # both sides possible
        (True, False, [(7, 2)]),         # queen side possible
        (False, True, [(7, 6)]),         # king side possible
        (False, False, [])               # neither possible
    ]
)
def test_white_castle_side_white(safe_board_white, qside_first, kside_first, soln):
    safe_board_white[(7, 0)].first_move = qside_first
    safe_board_white[(7, 7)].first_move = kside_first
    moves = get_castling(safe_board_white, turn_white=True)
    assert set(moves) == set(soln)


@pytest.mark.parametrize(
    "qside_first, kside_first, soln", [
        (True, True, [(0, 2), (0, 6)]),  # both sides possible
        (True, False, [(0, 2)]),         # queen side possible
        (False, True, [(0, 6)]),         # king side possible
        (False, False, [])               # neither possible
    ]
)
def test_black_castle_side_white(safe_board_white, qside_first, kside_first, soln):
    safe_board_white[(0, 0)].first_move = qside_first
    safe_board_white[(0, 7)].first_move = kside_first
    moves = get_castling(safe_board_white, turn_white=False)
    assert set(moves) == set(soln)


# --- Facing Black --- #  noqa
@pytest.mark.parametrize(
    "qside_first, kside_first, soln", [
        (True, True, [(0, 1), (0, 5)]),  # both sides possible
        (True, False, [(0, 1)]),         # king side possible
        (False, True, [(0, 5)]),         # queen side possible
        (False, False, [])               # neither possible
    ]
)
def test_white_castle_side_black(safe_board_black, qside_first, kside_first, soln):
    safe_board_black[(0, 0)].first_move = kside_first
    safe_board_black[(0, 7)].first_move = qside_first
    moves = get_castling(safe_board_black, turn_white=True)
    assert set(moves) == set(soln)


@pytest.mark.parametrize(
    "qside_first, kside_first, soln", [
        (True, True, [(7, 1), (7, 5)]),  # both sides possible
        (True, False, [(7, 1)]),         # king side possible
        (False, True, [(7, 5)]),         # queen side possible
        (False, False, [])               # neither possible
    ]
)
def test_black_castle_side_black(safe_board_black, qside_first, kside_first, soln):
    safe_board_black[(7, 0)].first_move = kside_first
    safe_board_black[(7, 7)].first_move = qside_first
    moves = get_castling(safe_board_black, turn_white=False)
    assert set(moves) == set(soln)


@pytest.fixture
def safe_board_white():
    arr = [["br", "--", "--", "--", "bk", "--", "--", "br"],
           ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
           ["--", "--", "--", "--", "--", "--", "--", "--"],
           ["--", "--", "--", "--", "--", "--", "--", "--"],
           ["--", "--", "--", "--", "--", "--", "--", "--"],
           ["--", "--", "--", "--", "--", "--", "--", "--"],
           ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
           ["wr", "--", "--", "--", "wk", "--", "--", "wr"]]
    return Board(array=arr)


@pytest.fixture
def safe_board_black():
    arr = [["wr", "--", "--", "wk", "--", "--", "--", "wr"],
           ["qp", "qp", "qp", "qp", "qp", "qp", "qp", "qp"],
           ["--", "--", "--", "--", "--", "--", "--", "--"],
           ["--", "--", "--", "--", "--", "--", "--", "--"],
           ["--", "--", "--", "--", "--", "--", "--", "--"],
           ["--", "--", "--", "--", "--", "--", "--", "--"],
           ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
           ["br", "--", "--", "bk", "--", "--", "--", "br"]]
    return Board(player_white=False, array=arr)
