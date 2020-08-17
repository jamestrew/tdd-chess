from chess.engine import Move
from chess.board import Board

import pytest
from unittest import mock


@pytest.fixture
def board_basic():
    return [
        ["br", "bn", "bb", "bq", "bk", "bb", "wp", "br"],
        ["--", "--", "--", "bp", "--", "bp", "--", "--"],
        ["--", "--", "bp", "--", "bp", "--", "--", "--"],
        ["bp", "bp", "--", "--", "--", "--", "--", "bp"],
        ["wp", "wp", "--", "--", "--", "--", "--", "wp"],
        ["--", "--", "wp", "--", "wp", "--", "--", "--"],
        ["--", "wp", "--", "wp", "--", "wp", "--", "--"],
        ["wr", "wn", "wb", "wq", "wk", "wb", "bp", "wr"]
    ]


def test_pawn_move_init(board_basic):
    game = Board(player_white=True, array=board_basic, white_to_move=True)
    move = Move((1, 5), (3, 5), game)

    assert move.from_row == 1
    assert move.from_col == 5
    assert move.from_piece.name == 'bp'
    assert move.dest_row == 3
    assert move.dest_col == 5
    assert move.dest_piece.name == '--'


def test_pawn_move_execute(board_basic):
    game = Board(player_white=True, array=board_basic, white_to_move=False)
    move = Move((1, 5), (3, 5), game)

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

    assert game.to_array() == new_board
    assert game.white_to_move is True
    assert game.moves == ['f5']
    assert move.from_piece.first_move is False


def test_rook_move_execute(board_basic):
    game = Board(player_white=True, array=board_basic, white_to_move=False)
    move = Move((0, 0), (2, 0), game)

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

    assert game.to_array() == new_board
    assert game.white_to_move is True
    assert game.moves == ['a6']
