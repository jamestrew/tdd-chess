from chess.board import Board

import pytest


@pytest.fixture
def board():
    arr = [
        ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
        ["bp", "--", "bp", "--", "bp", "bp", "bp", "bp"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "wb", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
        ["wr", "wn", "wb", "wq", "wk", "--", "wn", "wr"]
    ]
    return Board(array=arr)


@pytest.mark.parametrize(
    "coord, piece_name, moves", [
        # black first move
        ((0, 2), 'bb', [(1, 1), (2, 0), (1, 3), (2, 4), (3, 5)]),
        # black blocked
        ((0, 5), 'bb', []),
        # white wide
        ((3, 5), 'wb', [(2, 4), (1, 3), (0, 2), (2, 6), (1, 7),
                        (4, 4), (5, 3), (4, 6), (5, 7)])
    ]
)
def test_bishop_move(board, coord, piece_name, moves):
    bishop = board[coord]
    assert bishop.name == piece_name
    assert bishop.get_moves(board) == moves
