from structures import Game, Player


def main():
    player1 = Player('first', 'Z')
    player2 = Player('second', 'O')
    game = Game(player1=player1, player2=player2)
    game.check(row=1, column=2)
    game.check(row=2, column=2)
    game.check(row=1, column=1)
    game.check(row=2, column=1)
    game.check(row=1, column=3)
    print(game)
    print(game.current_player)
    # game.check()
    print(game.is_end())
    # print('Tic tac toe')


if __name__ == '__main__':
    main()
