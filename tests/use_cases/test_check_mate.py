from chess.engine import check_mate
from chess.board import Board


def test_fools_cm_white():
    arr = [["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
           ["bp", "bp", "bp", "bp", "--", "bp", "bp", "bp"],
           ["--", "--", "--", "--", "--", "--", "--", "--"],
           ["--", "--", "--", "--", "bp", "--", "--", "--"],
           ["--", "--", "--", "--", "--", "--", "wp", "bq"],
           ["--", "--", "--", "--", "--", "wp", "--", "--"],
           ["wp", "wp", "wp", "wp", "wp", "--", "--", "wp"],
           ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]]
    game = Board(array=arr)
    assert check_mate(game) is True


def test_double_rook_mate():
    arr = [["--", "bn", "bb", "bq", "bk", "bb", "bn", "--"],
           ["--", "--", "--", "--", "--", "--", "--", "--"],
           ["--", "--", "--", "--", "--", "--", "--", "--"],
           ["--", "--", "--", "--", "--", "--", "--", "--"],
           ["--", "--", "--", "--", "--", "--", "--", "bq"],
           ["--", "--", "--", "--", "--", "--", "--", "--"],
           ["--", "--", "--", "--", "--", "--", "br", "--"],
           ["wk", "--", "--", "--", "--", "--", "--", "br"]]
    game = Board(array=arr)
    assert check_mate(game) is True
