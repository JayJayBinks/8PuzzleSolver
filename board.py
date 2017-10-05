board_size=3

class board:
    board = [[i + j for i in range(board_size)] for j in range(board_size)]
    finishedBoard = [[i + (j * board_size) for i in range(board_size)] for j in range(board_size)]



    def __init__(self, position):
        self.position = position
        self.neighbors = self.findNeighbours()

    def switch(self, row_and_column, with_row_and_column):
        if self.isFinished():
            return True, board

        row = row_and_column[0]
        column = row_and_column[1]

        with_row = with_row_and_column[0]
        with_column = with_row_and_column[1]

        value = board[row][column]
        with_value = board[with_row][with_column]

        if value != 0 and with_value != 0:
            raise ValueError('Only the 0 field can be switched')

        board[row][column] = with_value
        board[with_row][with_column] = value

        return self.isFinished(), board

    def isFinished(self):
        return self.board == self.finishedBoard

    class zeroTile:

        def __init__(self, position):
            self.position = position
            self.neighbors = self.findNeighbours()

        def findNeighbours(self):

            # always visit child nodes in the "Up Down Left Right" order
            row = self.position[0]
            column = self.position[1]

            up = [row, column - 1] if column - 1 >= 0 else None
            down = [row, column + 1] if column + 1 <= board_size else None
            left = [row - 1, column] if row - 1 >= 0 else None
            right = [row + 1, column] if row + 1 <= board_size else None

            return up, down, left, right
