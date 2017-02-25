class Game:
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    # board = [
    #     ['X', 'X', 'X'],
    #     ['O', 'X', 'X'],
    #     ['X', 'O', 'X']
    # ]
    board_size = 3

    def __init__(self, *,
                 player1,
                 player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = self.player1

    def end_of_turn(self):
        self.current_player = self.player1 if self.current_player is self.player2 else self.player2

    def __check_cell(self, *, row, column):

        if row < 1 or row > self.board_size:
            raise Exception('Row must be between 1 and 3')

        if column < 1 or column > self.board_size:
            raise Exception('Column must be between 1 and 3')

        if self.board[row - 1][column - 1] is not ' ':
            raise Exception('This cell is already taken.')

        self.board[row - 1][column - 1] = self.current_player.sign

    def check(self, *, row, column):
        self.__check_cell(row=row, column=column)
        self.end_of_turn()

    def __current_player_wins(self):
        for row in self.board:
            if ''.join(row) == self.current_player.sign * 3:
                    return True

        columns = [[row[i] for row in self.board] for i in range(0, self.board_size)]
        for column in self.board:
            if ''.join(column) == self.current_player.sign * 3:
                    return True

        return False

    def is_end(self):
        return self.__current_player_wins()

    def __repr__(self):
        return """
        -------------
        | {0} | {1} | {2} |
        -------------
        | {3} | {4} | {5} |
        -------------
        | {6} | {7} | {8} |
        -------------
        """.format(*self.board[0], *self.board[1], *self.board[2])

    def __str__(self):
        return self.__repr__()
