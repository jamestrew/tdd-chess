import pygame as pg
import os
from chess.constants import *

from chess.board import Board
from chess.controller import Select, gui_coord, check, mate

pg.init()
pg.font.init()
pg.display.set_caption("TDD CHESS")


def load_images():
    """
    Create a dictionary of pieces and their respective png
    Access img by IMAGES['wp'] --> white pawn img
    """
    pieces = ['r', 'n', 'b', 'q', 'k', 'p']
    path = 'chess\\assets'
    for piece in pieces:
        # load black pieces
        img = pg.image.load(os.path.join(path, "b" + piece + ".png"))
        IMAGES['b' + piece] = pg.transform.scale(img, (SQ_SIZE, SQ_SIZE))

        # load white pieces
        img = pg.image.load(os.path.join(path, "w" + piece + ".png"))
        IMAGES['w' + piece] = pg.transform.scale(img, (SQ_SIZE, SQ_SIZE))


def draw_board(screen, white):
    """ Draw the back board grid """

    # Background border
    pg.draw.rect(screen, pg.Color(BORDER),
                 (0, 0, B_WIDTH + 2 * BORD, B_HEIGHT + 2 * BORD))

    # Rank/file labels
    label_font = pg.font.SysFont('arial', 20)
    r_list = ['8', '7', '6', '5', '4', '3', '2', '1']
    f_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    if not white:
        rank_list.reverse()
        file_list.reverse()

    for row, x in enumerate(range(BORD, B_WIDTH, SQ_SIZE)):

        # file label
        f_label = label_font.render(f_list[row], True, pg.Color('black'))
        blit_dest = (x + (SQ_SIZE // 2) - (f_label.get_width() // 2), 810)
        screen.blit(f_label, blit_dest)

        for col, y in enumerate(range(BORD, B_HEIGHT, SQ_SIZE)):
            # rank label
            if row == 0:  # ensures rank labels only draws onces
                r_label = label_font.render(r_list[col], True, pg.Color('black'))
                blit_dest = (810, y + (SQ_SIZE // 2) - (r_label.get_height() // 2))
                screen.blit(r_label, blit_dest)

            # grid
            if x % 200 == BORD and y % 200 == BORD or \
                    x % 200 != BORD and y % 200 != BORD:
                pg.draw.rect(screen, pg.Color(LIGHT_GRID), (x, y, SQ_SIZE, SQ_SIZE))
            else:
                pg.draw.rect(screen, pg.Color(DARK_GRID), (x, y, SQ_SIZE, SQ_SIZE))


def draw_pieces(screen, board):
    """
    Draw the moving of pieces.
    Likely requires the refreshing of draws
    """

    for row, x in enumerate(range(BORD, B_WIDTH, SQ_SIZE)):
        for col, y in enumerate(range(BORD, B_HEIGHT, SQ_SIZE)):
            piece = board[row][col]
            if piece != '--':
                screen.blit(IMAGES[piece], pg.Rect(y, x, SQ_SIZE, SQ_SIZE))


def draw_move(screen, cells, type_=None):
    """
    Highlight move suggestions (all possible moves for selected piece)
    """

    if type_ is None:
        color = SELECT
    elif type_ == 'check':
        color = CHECK
    else:
        color = MATE

    for row, x in enumerate(range(BORD, B_WIDTH, SQ_SIZE)):
        for col, y in enumerate(range(BORD, B_HEIGHT, SQ_SIZE)):
            if type(cells) == list:
                if (col, row) in cells:
                    pg.draw.circle(screen, pg.Color(SUGGEST),
                                   (x + SQ_SIZE // 2, y + SQ_SIZE // 2), S_RADIUS)
            else:
                if (col, row) == cells:
                    pg.draw.rect(screen, pg.Color(color), (x, y, SQ_SIZE, SQ_SIZE))


def draw_last_move(screen, game):
    """
    Draw color indicating last played move.
    """
    if game.moves == []:
        return

    last_move = game.moves[-1]
    start, end = last_move

    for row, x in enumerate(range(BORD, B_WIDTH, SQ_SIZE)):
        for col, y in enumerate(range(BORD, B_HEIGHT, SQ_SIZE)):
            if (col, row) == start:
                pg.draw.rect(screen, pg.Color(START), (x, y, SQ_SIZE, SQ_SIZE))
            if (col, row) == end:
                pg.draw.rect(screen, pg.Color(END), (x, y, SQ_SIZE, SQ_SIZE))


def draw_bg(screen, game):
    draw_board(screen, game.player_white)
    draw_last_move(screen, game)
    draw_pieces(screen, game.to_array())


def main(player, arr, move):
    """
    Handles user inputs and graphics updates
    """
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    screen.fill(pg.Color(BACKGROUND))

    game = Board(player_white=player, array=arr, white_to_move=move)
    select = Select()
    load_images()

    running = True
    while running:
        draw_bg(screen, game)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if not (position := gui_coord(player, pg.mouse.get_pos())):
                    continue
                suggestions = select.make_selection(position, game)

        try:
            if suggestions:
                draw_move(screen, select.pos_1)
                draw_pieces(screen, game.to_array())
                draw_move(screen, suggestions)
        except UnboundLocalError:
            pass

        if (king_loc := check(game)):
            draw_move(screen, king_loc, type_='check')
            draw_pieces(screen, game.to_array())
        if (king_loc := mate(game)):
            draw_move(screen, king_loc, type_='mate')
            draw_pieces(screen, game.to_array())
        clock.tick(MAX_FPS)
        pg.display.flip()


if __name__ == '__main__':
    player = True
    arr = None
    move = True
    main(player, arr, move)
