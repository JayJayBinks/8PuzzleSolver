import copy

board_size=3
finishedBoard = [[i + (j * board_size) for i in range(board_size)] for j in range(board_size)]


class board:

    def __init__(self, instance, zero_tile_position):
        self.instance = instance
        if self.instance[zero_tile_position[0]][zero_tile_position[1]] != 0:
            raise ValueError("zero tile value must be 0!")
        self.zeroTile = self.zeroTile(zero_tile_position)

    def switch(self, with_row_and_column):

        zero_row = self.zeroTile.position[0]
        zero_column = self.zeroTile.position[1]

        with_row = with_row_and_column[0]
        with_column = with_row_and_column[1]

        with_value = self.instance[with_row][with_column]

        instance = self.instance
        instance[zero_row][zero_column] = with_value
        instance[with_row][with_column] = 0

        new_board = board(instance, [with_row, with_column])

        return new_board

    def isFinished(self):
        return self.instance == finishedBoard

    class zeroTile:

        def __init__(self, position):
            self.position = position
            self.neighbors = self.findNeighbours()

        def findNeighbours(self):

            # always visit child nodes in the "Up Down Left Right" order
            row = self.position[0]
            column = self.position[1]

            up = [row - 1, column] if row - 1 >= 0 else None
            down = [row + 1, column] if row + 1 <= board_size else None
            left = [row, column - 1] if column - 1 >= 0 else None
            right = [row, column + 1] if column + 1 <= board_size else None

            return up, down, left, right
