import pytest

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
    board = Board(player_white=True)

    assert board.player_white is True
    assert board.opponent_white is False
    assert board.white_to_move is True
    assert board.moves == []


def test_board_init_play_black():
    board = Board(player_white=False)

    assert board.player_white is False
    assert board.opponent_white is True
    assert board.white_to_move is True
    assert board.moves == []


def test_board_to_array_white(game_grid_white):
    board = Board(player_white=True)
    assert board.to_array() == game_grid_white


def test_board_to_array_black(game_grid_black):
    board = Board(player_white=False)
    assert board.to_array() == game_grid_black
