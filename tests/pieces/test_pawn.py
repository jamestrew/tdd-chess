from chess.pieces import Pawn


def test_pawn_init():
    pawn = Pawn(1, 0, False)

    assert pawn.row == 1
    assert pawn.col == 0
    assert pawn.white is False
    assert pawn.first_move is True


def test_pawn_unit():
    pawn = Pawn(1, 0, False)
    assert pawn.unit == 'p'


def test_pawn_name():
    pawn = Pawn(1, 0, False)
    assert pawn.name == 'bp'


def test_pawn_repr():
    pawn = Pawn(1, 0, False)
    rep = pawn.__repr__()
    assert rep == "Pawn(1, 0, white=False)"
