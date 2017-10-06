from board import Board

class BoardSet(set):
    def __contains__(self, board):
        for element in self:
            if board.values == element.values:
                return True
        return False

if __name__ == "__main__":
    initList = [[5, 0, 7], [2, 6, 4], [3, 1, 8]]

    board1 = Board(initList, [0, 1])
    board2 = Board(initList, [0, 1])

    boardset1 = BoardSet()
    boardset1.add(board1)
    board2 = board2.switch([0,0])
    print(board2 not in boardset1)