DIM = 8

# Helper boards
"""
  -0 -1 -2 -3 -4 -5 -6 -7
0 br bn bb bq bk bb bn br 0
1 bp bp bp bp bp bp bp bp 1
2 -- -- -- -- -- -- -- -- 2
3 -- -- -- -- -- -- -- -- 3
4 -- -- -- -- -- -- -- -- 4
5 -- -- -- -- -- -- -- -- 5
6 wp wp wp wp wp wp wp wp 6
7 wr wn wb wq wk wb wn wr 7
  -0 -1 -2 -3 -4 -5 -6 -7

    -0    -1    -2    -3    -4    -5    -6    -7
0 ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"] 0
1 ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"] 1
2 ["--", "--", "--", "--", "--", "--", "--", "--"] 2
3 ["--", "--", "--", "--", "--", "--", "--", "--"] 3
4 ["--", "--", "--", "--", "--", "--", "--", "--"] 4
5 ["--", "--", "--", "--", "--", "--", "--", "--"] 5
6 ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"] 6
7 ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"] 7
    -0    -1    -2    -3    -4    -5    -6    -7
"""

""" --- GUI CONSTANTS --- """

WIDTH = 1200
HEIGHT = 900
B_WIDTH = B_HEIGHT = 800
BORD = 4

SQ_SIZE = B_WIDTH // DIM
S_RADIUS = 15

MAX_FPS = 15
IMAGES = {}


""" COLORS """
BACKGROUND = "#DBE0E2"
BORDER = "#333334"
DARK_GRID = "#C49B5A"
LIGHT_GRID = "#F5E5CA"
SUGGEST = "#44824C"
START = "#8CC45A"
END = "#ADE879"
SELECT = "#7BA74B"
CHECK = "#F08A6A"
MATE = "#F64C4C"
