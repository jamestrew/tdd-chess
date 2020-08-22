from chess.engine import *
from chess.board import Board

import pytest


def test_safe_start(start_board):
    piece = start_board[(6, 0)]
    moves = piece.get_moves(start_board)
    valid_moves = get_valid_moves(start_board, piece)

    assert piece.name == 'wp'
    assert set(valid_moves) == set(moves)


def test_safe_ish_non_king_move(test_game, test_arr):
    piece = test_game[(6, 4)]
    moves = piece.get_moves(test_game)
    valid_moves = get_valid_moves(test_game, piece)

    assert piece.name == 'wp'
    assert set(valid_moves) == set(moves)
    assert test_game.to_array() == test_arr


def test_danger_non_king_move(test_game, test_arr):
    piece = test_game[(6, 5)]
    valid_moves = get_valid_moves(test_game, piece)

    assert piece.name == 'wp'
    assert set(valid_moves) == set([])
    assert test_game.to_array() == test_arr


def test_danger_king(test_king_game, test_king_arr):
    king = test_king_game[(2, 4)]
    king.first_move = False
    valid_moves = get_valid_moves(test_king_game, king)

    assert king.name == 'wk'
    assert set(valid_moves) == set([(3, 3), (3, 5)])


def test_valid_moves_with_castling(white_castle):
    king = white_castle[(7, 4)]
    moves = get_valid_moves(white_castle, king)
    result = [(7, 3), (7, 5), (7, 2), (7, 6)]
    assert set(moves) == set(result)


@pytest.fixture
def test_arr():
    return [["br", "bn", "--", "--", "bk", "bb", "bn", "br"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "bq", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "bb"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]]


@pytest.fixture
def test_game(test_arr):
    return Board(array=test_arr)


@pytest.fixture
def test_king_arr():
    return [
        ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
        ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
        ["--", "--", "--", "--", "wk", "--", "--", "--"],
        ["--", "--", "--", "--", "wp", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["wp", "wp", "wp", "wp", "--", "wp", "wp", "wp"],
        ["wr", "wn", "wb", "wq", "--", "wb", "wn", "wr"]
    ]


@pytest.fixture
def test_king_game(test_king_arr):
    return Board(array=test_king_arr)


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
