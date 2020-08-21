from chess.engine import Move
from chess.board import Board

import pytest


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


def test_multiple_moves(start_board):

    Move((6, 3), (4, 3), start_board).execute()
    Move((1, 4), (3, 4), start_board).execute()

    new_board_1 = [["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
                   ["bp", "bp", "bp", "bp", "--", "bp", "bp", "bp"],
                   ["--", "--", "--", "--", "--", "--", "--", "--"],
                   ["--", "--", "--", "--", "bp", "--", "--", "--"],
                   ["--", "--", "--", "wp", "--", "--", "--", "--"],
                   ["--", "--", "--", "--", "--", "--", "--", "--"],
                   ["wp", "wp", "wp", "--", "wp", "wp", "wp", "wp"],
                   ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]]

    assert start_board.to_array() == new_board_1
    assert start_board.white_to_move is True
    assert start_board.moves == ['d4', 'e5']

    Move((4, 3), (3, 4), start_board).execute()

    new_board_2 = [["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
                   ["bp", "bp", "bp", "bp", "--", "bp", "bp", "bp"],
                   ["--", "--", "--", "--", "--", "--", "--", "--"],
                   ["--", "--", "--", "--", "wp", "--", "--", "--"],
                   ["--", "--", "--", "--", "--", "--", "--", "--"],
                   ["--", "--", "--", "--", "--", "--", "--", "--"],
                   ["wp", "wp", "wp", "--", "wp", "wp", "wp", "wp"],
                   ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]]

    assert start_board.to_array() == new_board_2
    assert start_board.white_to_move is False
    assert start_board.moves == ['d4', 'e5', 'e5']


# --- En Passant Config Test ---#
@pytest.mark.parametrize(
    "pos_2, enpass", [
        ((5, 0), False),  # single step move, not en passantable
        ((4, 0), True)    # double step move, en passantable
    ]
)
def test_enpassant_config(start_board, pos_2, enpass):
    pawn = start_board[(6, 0)]
    Move((6, 0), pos_2, start_board).execute()

    assert pawn.first_move is False
    assert pawn.enpassantable is enpass


# --- FIXTURES --- # noqa
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
