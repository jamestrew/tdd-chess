from chess.pieces import Piece


def test_piece_init():
    piece = Piece(0, 0, True)

    assert piece.row == 0
    assert piece.col == 0
    assert piece.white is True
