from chess.controller import Select
from chess.board import Board

import pytest
from unittest.mock import patch


def test_select_init():
    select = Select()

    assert select.pos_1 is None
    assert select.moves == []


# --- First Selection --- # noqa
@pytest.mark.parametrize(
    "sel1, pos1, result", [
        ((6, 3), (6, 3), [(5, 3), (4, 3)]),  # valid selection
        ((1, 0), None, []),                  # invalid, wrong turn
        ((3, 3), None, [])                   # invalid, empty square
    ]
)
def test_first_selection(start_board, sel1, pos1, result):
    select = Select()
    select.make_selection(sel1, start_board)

    assert select.pos_1 == pos1
    assert set(select.moves) == set(result)


def test_first_selection_capture(game):
    select = Select()
    select.make_selection((4, 3), game)

    assert select.pos_1 == (4, 3)
    assert set(select.moves) == set([(3, 3), (3, 4)])


# --- Second Selection --- # noqa
@pytest.mark.parametrize(
    "sel1, sel2, pos1, result", [
        ((6, 3), (3, 3), None, []),                  # invalid, empty square
        ((6, 3), (6, 3), (6, 3), [(5, 3), (4, 3)]),  # valid, same square
        ((6, 3), (6, 2), (6, 2), [(5, 2), (4, 2)])   # valid, new piece
    ]
)
def test_second_selection(start_board, sel1, sel2, pos1, result):
    select = Select()
    select.make_selection(sel1, start_board)
    select.make_selection(sel2, start_board)

    assert select.pos_1 == pos1
    assert set(select.moves) == set(result)


# --- Second Selection (MOVING) --- # noqa
@patch("chess.engine.Move")
def test_second_selection_move(mock_Move, start_board):
    select = Select()

    select.make_selection((6, 3), start_board)
    select.make_selection((4, 3), start_board)

    assert select.pos_1 is None
    assert select.moves == []
    mock_Move.assert_called_with((6, 3), (4, 3), start_board)


@patch("chess.engine.Move")
def test_second_selection_capture(mock_Move, game):
    select = Select()

    select.make_selection((4, 3), game)
    select.make_selection((3, 4), game)

    assert select.pos_1 is None
    assert select.moves == []
    mock_Move.assert_called_with((4, 3), (3, 4), game)


@pytest.fixture
def game():
    arr = [
        ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
        ["bp", "bp", "bp", "bp", "--", "bp", "bp", "bp"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "bp", "--", "--", "--"],
        ["--", "--", "--", "wp", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["wp", "wp", "wp", "--", "wp", "wp", "wp", "wp"],
        ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]
    ]
    return Board(array=arr)
