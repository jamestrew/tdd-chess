from chess.engine import Move, get_location
from chess.board import Board

import pytest


def test_start_config(start_board):
    lst = get_location(start_board)

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


@pytest.mark.parametrize(
    "white, coord", [
        (True, (7, 4)),
        (False, (0, 4))
    ]
)
def test_find_king(start_board, white, coord):
    loc = get_location(start_board, turn_white=white, find_king=True)
    assert loc == coord
