from board import Board

class BoardStack(list):
    def empty(self):
        return len(self) == 0


if __name__ == "__main__":
    initList = [[5, 0, 7], [2, 6, 4], [3, 1, 8]]

    board1 = Board(initList, [0, 1])

    frontier = BoardStack()
    frontier.append(board1)
    board2 = board1.swap([0, 0])
    if not frontier.empty() and not board2 in frontier:
        frontier.append(board2)

    print(frontier.pop().values)