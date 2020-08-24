import pytest

from chess.board import Board


def test_board_init_play_white(start_board):

    assert start_board.player_white is True
    assert start_board.white_to_move is True
    assert start_board.moves == []


def test_board_to_array_white(start_board, game_grid_white):
    assert start_board.to_array() == game_grid_white
    assert start_board.to_array() == game_grid_white


def test_board_to_array_black(game_grid_black):
    board = Board(player_white=False)
    assert board.to_array() == game_grid_black
    assert board.to_array() == game_grid_black


def test_board_init_from_array():
    test_board = [
        ["br", "bn", "bb", "bq", "--", "bb", "bn", "br"],
        ["--", "--", "--", "bp", "bk", "bp", "bp", "--"],
        ["--", "--", "bp", "--", "bp", "--", "--", "--"],
        ["bp", "bp", "--", "--", "--", "--", "--", "bp"],
        ["wp", "wp", "--", "--", "--", "--", "--", "wp"],
        ["--", "--", "wp", "--", "wp", "--", "--", "--"],
        ["--", "wp", "--", "wp", "--", "wp", "wp", "wr"],
        ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "--"]
    ]

    board = Board(player_white=True, array=test_board, white_to_move=True)
    assert board.to_array() == test_board
    assert board[(3, 1)].first_move is False
    assert board[(1, 5)].name == 'bp'

    assert board[6, 7].name == 'wr'
    assert board[6, 7].first_move is False

    assert board[1, 4].name == 'bk'
    assert board[1, 4].first_move is False


def test_board_print_white(start_board):
    board_str = "br bn bb bq bk bb bn br 8\n" + \
                "bp bp bp bp bp bp bp bp 7\n" + \
                "-- -- -- -- -- -- -- -- 6\n" + \
                "-- -- -- -- -- -- -- -- 5\n" + \
                "-- -- -- -- -- -- -- -- 4\n" + \
                "-- -- -- -- -- -- -- -- 3\n" + \
                "wp wp wp wp wp wp wp wp 2\n" + \
                "wr wn wb wq wk wb wn wr 1\n" + \
                "-a -b -c -d -e -f -g -h"

    assert start_board.__str__() == board_str


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
