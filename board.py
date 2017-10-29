size=3
finished_board = ((0, 1, 2), (3, 4, 5), (6, 7, 8))

# a 3*3 sized board looks like this
# (1, 2, 5)
# (3, 4, 0)
# (6, 7, 8)


class Board:

    def __init__(self, values, zero_tile_position):
        self.values = tuple(values)
        self.zero_tile = Board.ZeroTile(zero_tile_position)

    # only the zero tile can be swapped
    def swap(self, with_row_and_column):
        zero_row = self.zero_tile.position[0]
        zero_column = self.zero_tile.position[1]

        with_row = with_row_and_column[0]
        with_column = with_row_and_column[1]
        with_value = self.values[with_row][with_column]

        # need to cast to list for swapping
        instance = [list(e) for e in self.values]
        instance[zero_row][zero_column] = with_value
        instance[with_row][with_column] = 0
        instance = [tuple(e) for e in instance]

        return Board(instance, [with_row, with_column])

    def is_finished(self):
        return self.values == finished_board

    def draw(self):
        print(self.values[0][0:3])
        print(self.values[1][0:3])
        print(self.values[2][0:3])
        print("-----------")

    class ZeroTile:

        def __init__(self, position):
            self.position = position
            self.neighbors = self.find_neighbours()

        def find_neighbours(self):

            # always visit child nodes in the "Up Down Left Right" order
            row = self.position[0]
            column = self.position[1]

            up = [row - 1, column] if row - 1 >= 0 else None
            down = [row + 1, column] if row + 1 < size else None
            left = [row, column - 1] if column - 1 >= 0 else None
            right = [row, column + 1] if column + 1 < size else None

            return [up, down, left, right]
