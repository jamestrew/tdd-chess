from chess.board import Board


def main():
    while True:
        print("CLI CHESS")
        color = input("Choose color:\n (w) White\n (b) Black\n")

        if color in ('b', 'w'):
            print()
            break
        else:
            input("Invalid color.\nPress any key to continue.")

    is_white = True if color == 'w' else False
    game = Board(player_white=is_white)
    print(game)


if __name__ == '__main__':
    main()
