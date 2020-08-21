from chess.engine import get_all_moves

import pytest


@pytest.mark.parametrize(
    "white, moves", [
        (True, [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6),
                (4, 7), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5),
                (5, 6), (5, 7)]),
        (False, [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
                 (2, 7), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5),
                 (3, 6), (3, 7)])
    ]
)
def test_start_get_all_moves(start_board, white, moves):
    assert set(get_all_moves(start_board, for_white=white)) == set(moves)
