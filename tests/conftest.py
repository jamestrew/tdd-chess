import pytest

from chess.board import Board


@pytest.fixture
def start_board():
    return Board()
