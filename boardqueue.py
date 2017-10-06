import queue
from board import Board

class BoardQueue(queue.Queue): # or OrderedSetQueue
    def __contains__(self, board):
        with self.mutex:
            for element in self.queue:
                if board.values == element.values:
                    return True
            return False


if __name__ == "__main__":
    initList = [[5, 0, 7], [2, 6, 4], [3, 1, 8]]

    board1 = Board(initList, [0, 1])

    frontier = BoardQueue()
    frontier.put_nowait(board1)
    board2 = board1.switch([0,0])
    print(board1 in frontier)