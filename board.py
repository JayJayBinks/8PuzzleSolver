size=3
finishedBoard = ((0,1,2),(3,4,5),(6,7,8))
#[[i + (j * size) for i in range(size)] for j in range(size)]

class Board:

    def __init__(self, values, zero_tile_position, list_of_moves=[]):
        self.list_of_moves = list(list_of_moves)
        self.values = tuple(values)
        if self.values[zero_tile_position[0]][zero_tile_position[1]] != 0:
            raise ValueError("zero tile value must be 0!")
        self.zero_tile = Board.ZeroTile(zero_tile_position)

    def swap(self, with_row_and_column):
        zero_row = self.zero_tile.position[0]
        zero_column = self.zero_tile.position[1]

        with_row = with_row_and_column[0]
        with_column = with_row_and_column[1]
        with_value = self.values[with_row][with_column]

        instance = [list(e) for e in self.values]
        instance[zero_row][zero_column] = with_value
        instance[with_row][with_column] = 0
        instance = [tuple(e) for e in instance]

        new_board = Board(instance, [with_row, with_column], self.list_of_moves)

        self.update_moves_list(new_board, with_column, with_row, zero_column, zero_row)

        return new_board

    def update_moves_list(self, new_board, with_column, with_row, zero_column, zero_row):
        if zero_row > with_row and zero_column == with_column:
            new_board.list_of_moves.append("Up")
        if zero_row < with_row and zero_column == with_column:
            new_board.list_of_moves.append("Down")
        if zero_row == with_row and zero_column > with_column:
            new_board.list_of_moves.append("Left")
        if zero_row == with_row and zero_column < with_column:
            new_board.list_of_moves.append("Right")

    def isFinished(self):
        return self.values == finishedBoard

    def draw(self):
        print(self.values[0][0:3])
        print(self.values[1][0:3])
        print(self.values[2][0:3])
        print("-----------")

    class ZeroTile:

        def __init__(self, position):
            self.position = position
            self.neighbors = self.findNeighbours()

        def findNeighbours(self):

            # always visit child nodes in the "Up Down Left Right" order
            row = self.position[0]
            column = self.position[1]

            up = [row - 1, column] if row - 1 >= 0 else None
            down = [row + 1, column] if row + 1 < size else None
            left = [row, column - 1] if column - 1 >= 0 else None
            right = [row, column + 1] if column + 1 < size else None

            return [up, down, left, right]
