from chess.engine import *
from chess.board import Board

import pytest


def test_start_white(start_board):
    king = start_board[(7, 4)]
    moves = get_castling(start_board, king)
    assert moves.get(King) == [(), ()]


# -------------------------------- SAFE CASTLE -------------------------------- #
@pytest.mark.parametrize(  # noqa
    "q_first, k_first, k_soln, r_soln", [
        (True, True, [(7, 2), (7, 6)], [(7, 3), (7, 5)]),  # both sides possible
        (True, False, [(), (7, 2)], [(), (7, 3)]),         # queen side possible
        (False, True, [(7, 6), ()], [(7, 5), ()]),         # king side possible
        (False, False, [(), ()], [(), ()])                 # neither possible
    ]
)
def test_safe_castle(safe, q_first, k_first, k_soln, r_soln):
    safe[(7, 0)].first_move = q_first
    safe[(7, 7)].first_move = k_first
    king = safe[(7, 4)]
    moves = get_castling(safe, king)
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
def test_safe_black_castle(safe, q_first, k_first, k_soln, r_soln):
    safe[(0, 0)].first_move = q_first
    safe[(0, 7)].first_move = k_first
    king = safe[(0, 4)]
    moves = get_castling(safe, king)
    assert set(moves.get(King)) == set(k_soln)
    assert set(moves.get(Rook)) == set(r_soln)


# -------------------------------- NOW CHECKED ------------------------------ #
def test_now_checked_castle(now_checked):  # noqa
    wking = now_checked[7, 4]
    wmoves = get_castling(now_checked, wking)
    assert wmoves.get(King) == [(), ()]

    bking = now_checked[0, 4]
    now_checked.white_to_move = False
    bmoves = get_castling(now_checked, bking)
    assert bmoves.get(King) == [(), ()]


# ------------------------------- PATH CHECKED ------------------------------- #
def test_path_checked_castle(path_checked):
    wking = path_checked[7, 4]
    wmoves = get_castling(path_checked, wking)
    assert wmoves.get(King) == [(), ()]

    bking = path_checked[0, 4]
    path_checked.white_to_move = False
    bmoves = get_castling(path_checked, bking)
    assert bmoves.get(King) == [(), ()]


# ------------------------------- END CHECKED ------------------------------- #
def test_end_checked_castle(end_checked):
    wking = end_checked[7, 4]
    wmoves = get_castling(end_checked, wking)
    assert wmoves.get(King) == [(), ()]

    bking = end_checked[0, 4]
    end_checked.white_to_move = False
    bmoves = get_castling(end_checked, bking)
    assert bmoves.get(King) == [(), ()]


@pytest.fixture
def safe():
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
def now_checked():
    arr = [["br", "--", "--", "--", "bk", "--", "--", "br"],
           ["bp", "bp", "bp", "bp", "bp", "--", "bp", "bp"],
           ["--", "--", "--", "--", "--", "--", "--", "--"],
           ["--", "--", "--", "--", "--", "--", "--", "wq"],
           ["--", "--", "--", "--", "--", "--", "--", "bq"],
           ["--", "--", "--", "--", "--", "--", "--", "--"],
           ["wp", "wp", "wp", "wp", "wp", "--", "wp", "wp"],
           ["wr", "--", "--", "--", "wk", "--", "--", "wr"]]
    return Board(array=arr)


@pytest.fixture
def path_checked():
    arr = [["br", "--", "--", "--", "bk", "--", "--", "br"],
           ["--", "--", "--", "--", "--", "--", "--", "--"],
           ["--", "--", "wn", "--", "--", "--", "wn", "--"],
           ["--", "--", "--", "--", "--", "--", "--", "--"],
           ["--", "--", "--", "--", "--", "--", "--", "--"],
           ["--", "--", "bn", "--", "--", "--", "bn", "--"],
           ["--", "--", "--", "--", "--", "--", "--", "--"],
           ["wr", "--", "--", "--", "wk", "--", "--", "wr"]]
    return Board(array=arr)


@pytest.fixture
def end_checked():
    arr = [["br", "--", "--", "--", "bk", "--", "--", "br"],
           ["--", "--", "--", "--", "--", "--", "--", "--"],
           ["--", "--", "--", "--", "wb", "--", "--", "--"],
           ["--", "--", "--", "--", "--", "--", "--", "--"],
           ["--", "--", "--", "--", "--", "--", "--", "--"],
           ["--", "--", "--", "--", "bb", "--", "--", "--"],
           ["--", "--", "--", "--", "--", "--", "--", "--"],
           ["wr", "--", "--", "--", "wk", "--", "--", "wr"]]
    return Board(array=arr)
