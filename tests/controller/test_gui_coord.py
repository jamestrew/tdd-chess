from chess.controller import gui_coord

import pytest


@pytest.mark.parametrize(
    "coord, cell", [
        ((87, 48), (0, 0)),
        ((167, 66), (0, 1)),
        ((0, 0), False),         # top-right OOB
        ((3, 100), False),       # left OOB
        ((100, 2), False),       # top OOB
        ((805, 0), False),       # right OOB
        ((100, 1000), False),    # top OOB
        ((436, 460), (4, 4)),
        ((266, 624), (6, 2)),
        ((167, 752), (7, 1)),
        ((59, 757), (7, 0)),
        ((677, 760), (7, 6)),
        ((663, 172), (1, 6)),
        ((567, 161), (1, 5)),
        ((306, 347), (3, 3)),
        ((361, 349), (3, 3))
    ]
)
def test_gui_coord_player_white(coord, cell):
    test_cell = gui_coord(player=True, coord=coord)
    assert test_cell == cell


@pytest.mark.parametrize(
    "coord, cell", [
        ((87, 48), (7, 7)),
        ((167, 66), (7, 6)),
        ((0, 0), False),         # top-right OOB
        ((3, 100), False),       # left OOB
        ((100, 2), False),       # top OOB
        ((805, 0), False),       # right OOB
        ((100, 1000), False),    # top OOB
        ((436, 460), (3, 3)),
        ((266, 624), (1, 5)),
        ((167, 752), (0, 6)),
        ((59, 757), (0, 7)),
        ((677, 760), (0, 1)),
        ((663, 172), (6, 1)),
        ((567, 161), (6, 2)),
        ((306, 347), (4, 4)),
        ((361, 349), (4, 4))
    ]
)
def test_gui_coord_player_white(coord, cell):
    test_cell = gui_coord(player=False, coord=coord)
    assert test_cell == cell
