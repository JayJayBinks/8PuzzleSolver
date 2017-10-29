import sys, board
import solver


def read_board_values(tiles):
    values = [[0 for row in range(0, board.size)] for col in range(0, board.size)]
    row = 0
    column = 0
    zero_position = None
    for tile in range(0, len(tiles)):
        if tile != 0 and (tile % board.size == 0):
            row += 1
            column = 0
        tile_value = int(tiles[tile])
        values[row][column] = tile_value
        if tile_value == 0:
            zero_position = [row, column]
        column += 1
    values = [tuple(e) for e in values]
    return values, zero_position;


def read_script_arguments(argv):
    algorithm = argv[0]
    tiles = argv[1]
    tiles = str.replace(tiles, ',', '')
    tiles = tuple(tiles)
    return algorithm, tiles


if __name__ == "__main__":
    algorithm, tiles = read_script_arguments(sys.argv[1:])
    values, zero_position = read_board_values(tiles)
    solver = solver.Solver(algorithm, values, zero_position)
    solver.solve()
