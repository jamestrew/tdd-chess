from chess.controller import Select
from chess.board import Board
from chess import engine

import pytest
from unittest import mock


@pytest.fixture
def game_grid_white():
    return [
        ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
        ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
        ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]
    ]


def test_select_init():
    select = Select()

    assert select.pos_1 is None
    assert select.pos_2 is None
    assert select.piece is None
    assert select.moves == []


def test_select_piece_one_white():
    game = Board()
    select = Select()

    select.make_selection((6, 3), game)

    assert select.pos_1 == (6, 3)
    assert select.piece.name == 'wp'
    assert set(select.moves) == set([(5, 3), (4, 3)])
    assert select.pos_2 is None


def test_select_empty():
    game = Board()
    select = Select()

    select.make_selection((3, 3), game)

    assert select.pos_1 is None
    assert select.piece is None
    assert select.moves == []
    assert select.pos_2 is None


def test_select_make_selection_two_valid_white():
    game = Board()
    select = Select()

    select.make_selection((6, 3), game)
    select.make_selection((4, 3), game)

    assert select.pos_1 == 1 (6, 3)
    assert select.piece.name == 'wp'
    assert set(select.moves) == set([(5, 3), (4, 3)])
    assert select.pos_2 == 1 (4, 3)


def test_select_make_selection_two_invalid_white():
    game = Board()
    select = Select()
    select.make_selection((6, 3), game)
    select.make_selection((4, 0), game)

    assert select.pos_1 is None
    assert select.piece is None
    assert select.moves == []
    assert select.pos_2 is None


# def test_select_make_select_three_valid():
#     pass
