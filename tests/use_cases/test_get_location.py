from chess.engine import Move, get_location
from chess.board import Board
from chess.pieces import *

import pytest


def test_start_config_white(start_board):
    lst = get_location(start_board)

    assert lst == set([(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5),
                       (6, 6), (6, 7), (7, 0), (7, 1), (7, 2), (7, 3),
                       (7, 4), (7, 5), (7, 6), (7, 7)])


def test_start_config_black():
    game = Board(player_white=False)
    lst = get_location(game)

    assert lst == set([(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5),
                       (6, 6), (6, 7), (7, 0), (7, 1), (7, 2), (7, 3),
                       (7, 4), (7, 5), (7, 6), (7, 7)])


def test_start_midgame_config():
    board = [["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
             ["bp", "bp", "bp", "bp", "--", "bp", "bp", "bp"],
             ["--", "--", "--", "--", "--", "--", "--", "--"],
             ["--", "--", "--", "--", "wp", "--", "--", "--"],
             ["--", "--", "--", "--", "--", "--", "--", "--"],
             ["--", "--", "--", "--", "--", "--", "--", "--"],
             ["wp", "wp", "wp", "--", "wp", "wp", "wp", "wp"],
             ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]]

    game = Board(array=board)
    lst = get_location(game)
    assert lst == set([(6, 0), (6, 1), (6, 2), (3, 4), (6, 4), (6, 5),
                       (6, 6), (6, 7), (7, 0), (7, 1), (7, 2), (7, 3),
                       (7, 4), (7, 5), (7, 6), (7, 7)])


def test_after_move():
    game = Board()

    Move((6, 3), (4, 3), game).execute()
    Move((1, 4), (3, 4), game).execute()

    lst = get_location(game)

    assert game[(4, 3)].name == 'wp'
    assert lst == set([(6, 0), (6, 1), (6, 2), (4, 3), (6, 4), (6, 5),
                       (6, 6), (6, 7), (7, 0), (7, 1), (7, 2), (7, 3),
                       (7, 4), (7, 5), (7, 6), (7, 7)])


#  --- Find Pieces ---  # noqa
@pytest.mark.parametrize(
    "white, coord", [
        (True, (7, 4)),
        (False, (0, 4))
    ]
)
def test_find_king(start_board, white, coord):
    loc = get_location(start_board, turn_white=white, find_piece=King)
    assert loc == coord


@pytest.mark.parametrize(
    "white, piece, coord", [
        (True, Rook, set([(7, 0), (7, 7)])),  # white rooks, both alive
        (False, Night, (0, 6)),               # black night, one alive
        (True, King, (7, 4)),                 # white king
        (False, King, (0, 4)),                # black king
        (False, Bishop, [])                 # black bishop, none alive
    ]
)
def test_find_others(game, white, piece, coord):
    loc = get_location(game, turn_white=white, find_piece=piece)

    assert loc == coord


@ pytest.fixture
def game():
    board = [["br", "--", "--", "bq", "bk", "--", "bn", "br"],
             ["bp", "bp", "bp", "bp", "--", "bp", "bp", "bp"],
             ["--", "--", "--", "--", "--", "--", "--", "--"],
             ["--", "--", "--", "--", "wp", "--", "--", "--"],
             ["--", "--", "--", "--", "--", "--", "--", "--"],
             ["--", "--", "--", "--", "--", "--", "--", "--"],
             ["wp", "wp", "wp", "--", "wp", "wp", "wp", "wp"],
             ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]]
    return Board(array=board)
