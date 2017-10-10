from board import Board

class BoardList(list):
    def __contains__(self, board):
        for element in self:
            if board.values == element.values:
                return True
        return False

if __name__ == "__main__":
    initList = ((5, 0, 7), (2, 6, 4), (3, 1, 8))
    initList2 = [[5, 0, 7], [2, 6, 4], [3, 1, 8]]

    board1 = Board(initList, [0, 1])

    boardset1 = BoardList()

    boardset1.add(board1.values)

    board2 = board1.swap([0, 0])
    boardset1.add(board2.values)

    print(((0, 5, 7), (2, 6, 4), (3, 1, 8)) in boardset1)