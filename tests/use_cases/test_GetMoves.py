from chess.engine import GetMoves
from chess.board import Board


def test_start_get_all_moves():
    # bad incomplete
    board = Board(player_white=True, white_to_move=True)
    moves = GetMoves().get_all_moves(board)

    assert moves == set([(2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
                         (2, 7), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5),
                         (3, 6), (3, 7), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4),
                         (4, 5), (4, 6), (4, 7), (5, 0), (5, 1), (5, 2), (5, 3),
                         (5, 4), (5, 5), (5, 6), (5, 7)])
