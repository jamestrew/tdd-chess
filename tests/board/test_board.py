import pytest
from unittest import mock

from chess.board import Board


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


@pytest.fixture
def game_grid_black():
    return [
        ["wr", "wn", "wb", "wk", "wq", "wb", "wn", "wr"],
        ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
        ["br", "bn", "bb", "bk", "bq", "bb", "bn", "br"]
    ]


def test_board_init_play_white():
    board = Board(player_white=True, array=None, white_to_move=True)

    assert board.player_white is True
    assert board.opponent_white is False
    assert board.white_to_move is True
    assert board.moves == []


def test_board_init_play_black():
    board = Board(player_white=False, array=None, white_to_move=True)

    assert board.player_white is False
    assert board.opponent_white is True
    assert board.white_to_move is True
    assert board.moves == []


def test_board_to_array_white(game_grid_white):
    board = Board(player_white=True, array=None, white_to_move=True)
    assert board.to_array() == game_grid_white


def test_board_to_array_black(game_grid_black):
    board = Board(player_white=False, array=None, white_to_move=True)
    assert board.to_array() == game_grid_black


def test_board_init_from_array():
    test_board = [
        ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
        ["--", "--", "--", "bp", "--", "bp", "bp", "--"],
        ["--", "--", "bp", "--", "bp", "--", "--", "--"],
        ["bp", "bp", "--", "--", "--", "--", "--", "bp"],
        ["wp", "wp", "--", "--", "--", "--", "--", "wp"],
        ["--", "--", "wp", "--", "wp", "--", "--", "--"],
        ["--", "wp", "--", "wp", "--", "wp", "wp", "--"],
        ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]
    ]

    board = Board(player_white=True, array=test_board, white_to_move=True)
    assert board.to_array() == test_board
    assert board[(3, 1)].first_move is False
    assert board[(1, 5)].name == 'bp'


def test_board_print_white():
    board = Board(player_white=True, white_to_move=True)
    board_str = "br bn bb bq bk bb bn br 8\n" + \
                "bp bp bp bp bp bp bp bp 7\n" + \
                "-- -- -- -- -- -- -- -- 6\n" + \
                "-- -- -- -- -- -- -- -- 5\n" + \
                "-- -- -- -- -- -- -- -- 4\n" + \
                "-- -- -- -- -- -- -- -- 3\n" + \
                "wp wp wp wp wp wp wp wp 2\n" + \
                "wr wn wb wq wk wb wn wr 1\n" + \
                "-a -b -c -d -e -f -g -h"

    assert board.__str__() == board_str


def test_board_print_black():
    board = Board(player_white=False, white_to_move=True)
    board_str = "wr wn wb wk wq wb wn wr 1\n" + \
                "wp wp wp wp wp wp wp wp 2\n" + \
                "-- -- -- -- -- -- -- -- 3\n" + \
                "-- -- -- -- -- -- -- -- 4\n" + \
                "-- -- -- -- -- -- -- -- 5\n" + \
                "-- -- -- -- -- -- -- -- 6\n" + \
                "bp bp bp bp bp bp bp bp 7\n" + \
                "br bn bb bk bq bb bn br 8\n" + \
                "-h -g -f -e -d -c -b -a"

    assert board.__str__() == board_str
