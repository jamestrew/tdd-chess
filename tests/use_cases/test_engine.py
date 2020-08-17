from chess.engine import Move
from unittest import mock


def test_move_init():
    game = mock.Mock()
    move = Move((1, 5), (3, 5), game)

    assert move.from_row == 1
    assert move.from_col == 5
    assert move.dest_row == 3
    assert move.dest_col == 5
