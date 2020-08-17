from chess.pieces import *


def test_piece_init():
    piece = Piece(0, 0, True)

    assert piece.row == 0
    assert piece.col == 0
    assert piece.is_white is True
    assert piece.name == 'wx'

    rep = piece.__repr__()
    assert rep == "Piece(0, 0, is_white=True)"
