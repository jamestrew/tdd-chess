from chess.engine import Move
from chess.board import Board

import pytest


@pytest.fixture
def game_white():
    arr = [
        ["br", "bn", "bb", "bq", "bk", "bb", "wp", "br"],
        ["--", "--", "--", "bp", "--", "bp", "--", "--"],
        ["--", "--", "bp", "--", "bp", "--", "--", "--"],
        ["bp", "bp", "--", "--", "--", "--", "--", "bp"],
        ["wp", "wp", "--", "--", "--", "--", "--", "wp"],
        ["--", "--", "wp", "--", "wp", "--", "--", "--"],
        ["--", "wp", "--", "wp", "--", "wp", "--", "--"],
        ["wr", "wn", "wb", "wq", "wk", "wb", "bp", "wr"]
    ]
    return Board(array=arr)


@pytest.fixture
def game_black():
    arr = [
        ["br", "bn", "bb", "bq", "bk", "bb", "wp", "br"],
        ["--", "--", "--", "bp", "--", "bp", "--", "--"],
        ["--", "--", "bp", "--", "bp", "--", "--", "--"],
        ["bp", "bp", "--", "--", "--", "--", "--", "bp"],
        ["wp", "wp", "--", "--", "--", "--", "--", "wp"],
        ["--", "--", "wp", "--", "wp", "--", "--", "--"],
        ["--", "wp", "--", "wp", "--", "wp", "--", "--"],
        ["wr", "wn", "wb", "wq", "wk", "wb", "bp", "wr"]
    ]
    return Board(array=arr, white_to_move=False)


def test_pawn_move_init(game_white):
    move = Move((1, 5), (3, 5), game_white)

    assert move.pos_1 == (1, 5)
    assert move.from_piece.name == 'bp'
    assert move.pos_2 == (3, 5)
    assert move.dest_piece.name == '--'


def test_pawn_move_execute(game_black):
    move = Move((1, 5), (3, 5), game_black)

    move.execute()
    new_board = [
        ["br", "bn", "bb", "bq", "bk", "bb", "wp", "br"],
        ["--", "--", "--", "bp", "--", "--", "--", "--"],
        ["--", "--", "bp", "--", "bp", "--", "--", "--"],
        ["bp", "bp", "--", "--", "--", "bp", "--", "bp"],
        ["wp", "wp", "--", "--", "--", "--", "--", "wp"],
        ["--", "--", "wp", "--", "wp", "--", "--", "--"],
        ["--", "wp", "--", "wp", "--", "wp", "--", "--"],
        ["wr", "wn", "wb", "wq", "wk", "wb", "bp", "wr"]
    ]

    assert game_black.to_array() == new_board
    assert game_black.white_to_move is True
    assert game_black.moves == ['f5']
    assert move.from_piece.first_move is False


def test_rook_move_execute(game_black):
    move = Move((0, 0), (2, 0), game_black)

    move.execute()
    new_board = [
        ["--", "bn", "bb", "bq", "bk", "bb", "wp", "br"],
        ["--", "--", "--", "bp", "--", "bp", "--", "--"],
        ["br", "--", "bp", "--", "bp", "--", "--", "--"],
        ["bp", "bp", "--", "--", "--", "--", "--", "bp"],
        ["wp", "wp", "--", "--", "--", "--", "--", "wp"],
        ["--", "--", "wp", "--", "wp", "--", "--", "--"],
        ["--", "wp", "--", "wp", "--", "wp", "--", "--"],
        ["wr", "wn", "wb", "wq", "wk", "wb", "bp", "wr"]
    ]

    assert game_black.to_array() == new_board
    assert game_black.white_to_move is True
    assert game_black.moves == ['a6']


def test_multiple_moves():
    game = Board()

    Move((6, 3), (4, 3), game).execute()
    Move((1, 4), (3, 4), game).execute()

    new_board_1 = [["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
                   ["bp", "bp", "bp", "bp", "--", "bp", "bp", "bp"],
                   ["--", "--", "--", "--", "--", "--", "--", "--"],
                   ["--", "--", "--", "--", "bp", "--", "--", "--"],
                   ["--", "--", "--", "wp", "--", "--", "--", "--"],
                   ["--", "--", "--", "--", "--", "--", "--", "--"],
                   ["wp", "wp", "wp", "--", "wp", "wp", "wp", "wp"],
                   ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]]

    assert game.to_array() == new_board_1
    assert game.white_to_move is True
    assert game.moves == ['d4', 'e5']

    Move((4, 3), (3, 4), game).execute()

    new_board_2 = [["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
                   ["bp", "bp", "bp", "bp", "--", "bp", "bp", "bp"],
                   ["--", "--", "--", "--", "--", "--", "--", "--"],
                   ["--", "--", "--", "--", "wp", "--", "--", "--"],
                   ["--", "--", "--", "--", "--", "--", "--", "--"],
                   ["--", "--", "--", "--", "--", "--", "--", "--"],
                   ["wp", "wp", "wp", "--", "wp", "wp", "wp", "wp"],
                   ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]]

    assert game.to_array() == new_board_2
    assert game.white_to_move is False
    assert game.moves == ['d4', 'e5', 'e5']
