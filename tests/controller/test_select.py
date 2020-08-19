from chess.controller import Select
from chess.board import Board
from chess import engine

import pytest
from unittest import mock


@pytest.fixture
def game_grid():
    return [
        ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
        ["bp", "bp", "bp", "bp", "--", "bp", "bp", "bp"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "bp", "--", "--", "--"],
        ["--", "--", "--", "wp", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["wp", "wp", "wp", "--", "wp", "wp", "wp", "wp"],
        ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]
    ]


def test_select_init():
    select = Select()

    assert select.pos_1 is None
    assert select.moves == []


def test_select_first_valid():
    game = Board()
    select = Select()

    select.make_selection((6, 3), game)

    assert select.pos_1 == (6, 3)
    assert set(select.moves) == set([(5, 3), (4, 3)])


def test_select_first_invalid_black():
    game = Board()
    select = Select()

    select.make_selection((1, 0), game)

    assert select.pos_1 is None
    assert select.moves == []


def test_select_first_empty():
    game = Board()
    select = Select()

    select.make_selection((3, 3), game)

    assert select.pos_1 is None
    assert select.moves == []


# --- First move valid --- #

def test_select_second_empty():
    game = Board()
    select = Select()

    select.make_selection((6, 3), game)
    select.make_selection((3, 3), game)

    assert select.pos_1 is None
    assert select.moves == []


def test_select_second_valid():
    game = Board()
    select = Select()

    select.make_selection((6, 3), game)
    move = select.make_selection((4, 3), game)

    assert select.pos_1 is None
    assert select.moves == []
    assert move == "engine.Move(self.pos_1, select, game).execute()"


def test_select_second_same():
    game = Board()
    select = Select()

    select.make_selection((6, 3), game)
    select.make_selection((6, 3), game)

    assert select.pos_1 == (6, 3)
    assert set(select.moves) == set([(5, 3), (4, 3)])


def test_select_second_new():
    game = Board()
    select = Select()

    select.make_selection((6, 3), game)
    select.make_selection((6, 2), game)

    assert select.pos_1 == (6, 2)
    assert set(select.moves) == set([(5, 2), (4, 2)])

# --- Capture --- #


def test_select_precapture_black(game_grid):
    game = Board(array=game_grid)
    select = Select()

    select.make_selection((4, 3), game)

    assert select.pos_1 == (4, 3)
    assert set(select.moves) == set([(3, 3), (3, 4)])


def test_select_capture_black(game_grid):
    game = Board(array=game_grid)
    select = Select()

    select.make_selection((4, 3), game)
    move = select.make_selection((3, 4), game)

    assert select.pos_1 is None
    assert select.moves == []
    assert move == "engine.Move(self.pos_1, select, game).execute()"
