from chess.board import Board
from chess.constants import *


def test_board_init_play_white():
    board = Board(player_white=True)

    test_game = [
        ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
        ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
        ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]
    ]

    game = [[0 for _ in range(DIM)] for _ in range(DIM)]
    for i in range(DIM):
        for j in range(DIM):
            game[i][j] = board.board[i][j].name

    assert board.player_white is True
    assert board.opponent_white is False
    assert board.moves == []
    assert game == test_game


def test_board_init_play_black():
    board = Board(player_white=False)

    test_game = [
        ["wr", "wn", "wb", "wk", "wq", "wb", "wn", "wr"],
        ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
        ["br", "bn", "bb", "bk", "bq", "bb", "bn", "br"]
    ]

    game = [[0 for _ in range(DIM)] for _ in range(DIM)]
    for i in range(DIM):
        for j in range(DIM):
            game[i][j] = board.board[i][j].name

    assert board.player_white is False
    assert board.opponent_white is True
    assert board.moves == []
    assert game == test_game
