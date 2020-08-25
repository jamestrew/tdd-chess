from chess.engine import Move
from chess.board import Board
from chess.pieces import *

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


# --------------------------- En Passant Config Test --------------------------- #
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


def test_enpassant_capture(game_enpassant):
    Move((1, 0), (3, 0), game_enpassant).execute()
    Move((3, 1), (2, 0), game_enpassant).execute()
    Move((6, 7), (4, 7), game_enpassant).execute()
    Move((4, 6), (5, 7), game_enpassant).execute()

    post_move = [
        ["br", "bn", "bb", "bq", "bk", "bb", "wp", "br"],
        ["--", "--", "--", "bp", "--", "bp", "--", "--"],
        ["wp", "--", "bp", "--", "bp", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["wp", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "wp", "--", "wp", "--", "--", "bp"],
        ["--", "wp", "--", "wp", "--", "wp", "--", "--"],
        ["wr", "wn", "wb", "wq", "wk", "wb", "bp", "wr"]
    ]

    assert game_enpassant.to_array() == post_move


# -------------------------------- Castling -------------------------------- # noqa
@pytest.mark.parametrize(
    "kpos, pos_2, rdest, name", [
        ((7, 4), (7, 2), (7, 3), ('wk', 'wr')),  # white-white, queen side castle
        ((7, 4), (7, 6), (7, 5), ('wk', 'wr')),  # white-white, king side caslte
        ((0, 4), (0, 2), (0, 3), ('bk', 'br')),  # white-black, queen side castle
        ((0, 4), (0, 6), (0, 5), ('bk', 'br'))   # white-black, king side castle
    ]
)
def test_white_board_castle(white_castle, kpos, pos_2, rdest, name):
    Move(kpos, pos_2, white_castle).execute()

    king = white_castle[pos_2]
    rook = white_castle[rdest]
    assert king.name == name[0]
    assert king.first_move is False
    assert rook.name == name[1]
    assert rook.first_move is False


# ------------------------------- PROMOTION ------------------------------- #
@pytest.mark.parametrize(
    "pos_1, pos_2, piece, name", [
        ((1, 2), (0, 2), Queen, 'wq'),
        ((6, 2), (7, 2), Queen, 'bq'),
        ((6, 2), (7, 2), Rook, 'br')
    ]
)
def test_pawn_promotion(promotion, pos_1, pos_2, piece, name):
    move = Move(pos_1, pos_2, promotion)
    move.promote = piece
    move.execute()

    assert promotion[pos_2].name == name


# ------------------------------- FIXTURES ------------------------------- # noqa
@pytest.fixture  # noqa
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


@pytest.fixture
def game_enpassant():
    arr = [
        ["br", "bn", "bb", "bq", "bk", "bb", "wp", "br"],
        ["bp", "--", "--", "bp", "--", "bp", "--", "--"],
        ["--", "--", "bp", "--", "bp", "--", "--", "--"],
        ["--", "wp", "--", "--", "--", "--", "--", "--"],
        ["wp", "--", "--", "--", "--", "--", "bp", "--"],
        ["--", "--", "wp", "--", "wp", "--", "--", "--"],
        ["--", "wp", "--", "wp", "--", "wp", "--", "wp"],
        ["wr", "wn", "wb", "wq", "wk", "wb", "bp", "wr"]
    ]
    return Board(array=arr, white_to_move=False)


@pytest.fixture
def white_castle():
    arr = [["br", "--", "--", "--", "bk", "--", "--", "br"],
           ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
           ["--", "--", "--", "--", "--", "--", "--", "--"],
           ["--", "--", "--", "--", "--", "--", "--", "--"],
           ["--", "--", "--", "--", "--", "--", "--", "--"],
           ["--", "--", "--", "--", "--", "--", "--", "--"],
           ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
           ["wr", "--", "--", "--", "wk", "--", "--", "wr"]]
    return Board(array=arr)


@pytest.fixture
def promotion():
    arr = [["br", "--", "--", "--", "bk", "--", "--", "br"],
           ["bp", "bp", "wp", "bp", "bp", "bp", "bp", "bp"],
           ["--", "--", "--", "--", "--", "--", "--", "--"],
           ["--", "--", "--", "--", "--", "--", "--", "--"],
           ["--", "--", "--", "--", "--", "--", "--", "--"],
           ["--", "--", "--", "--", "--", "--", "--", "--"],
           ["wp", "wp", "bp", "wp", "wp", "wp", "wp", "wp"],
           ["wr", "--", "--", "--", "wk", "--", "--", "wr"]]
    return Board(array=arr)
