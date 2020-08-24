from chess.engine import *
from chess.board import Board

import pytest


def test_start_white(start_board):
    king = start_board[(7, 4)]
    moves = get_castling(start_board, king)
    assert moves.get(King) == [(), ()]


# --- Facing white --- #
@pytest.mark.parametrize(  # noqa
    "q_first, k_first, k_soln, r_soln", [
        (True, True, [(7, 2), (7, 6)], [(7, 3), (7, 5)]),  # both sides possible
        (True, False, [(), (7, 2)], [(), (7, 3)]),         # queen side possible
        (False, True, [(7, 6), ()], [(7, 5), ()]),         # king side possible
        (False, False, [(), ()], [(), ()])                 # neither possible
    ]
)
def test_white_castle_side_white(safe_white, q_first, k_first, k_soln, r_soln):
    safe_white[(7, 0)].first_move = q_first
    safe_white[(7, 7)].first_move = k_first
    king = safe_white[(7, 4)]
    moves = get_castling(safe_white, king)
    assert set(moves.get(King)) == set(k_soln)
    assert set(moves.get(Rook)) == set(r_soln)


@pytest.mark.parametrize(
    "q_first, k_first, k_soln, r_soln", [
        (True, True, [(0, 2), (0, 6)], [(0, 3), (0, 5)]),  # both sides possible
        (True, False, [(), (0, 2)], [(), (0, 3)]),         # queen side possible
        (False, True, [(0, 6), ()], [(0, 5), ()]),         # king side possible
        (False, False, [(), ()], [(), ()])                 # neither possible
    ]
)
def test_black_castle_side_white(safe_white, q_first, k_first, k_soln, r_soln):
    safe_white[(0, 0)].first_move = q_first
    safe_white[(0, 7)].first_move = k_first
    king = safe_white[(0, 4)]
    moves = get_castling(safe_white, king)
    assert set(moves.get(King)) == set(k_soln)
    assert set(moves.get(Rook)) == set(r_soln)


@pytest.fixture
def safe_white():
    arr = [["br", "--", "--", "--", "bk", "--", "--", "br"],
           ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
           ["--", "--", "--", "--", "--", "--", "--", "--"],
           ["--", "--", "--", "--", "--", "--", "--", "--"],
           ["--", "--", "--", "--", "--", "--", "--", "--"],
           ["--", "--", "--", "--", "--", "--", "--", "--"],
           ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
           ["wr", "--", "--", "--", "wk", "--", "--", "wr"]]
    return Board(array=arr)
