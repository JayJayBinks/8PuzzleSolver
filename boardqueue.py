from board import Board
from collections import deque

initList = ((5, 0, 7), (2, 6, 4), (3, 1, 8))

class BoardQueue(deque):
    def pop(self):
        return self.popleft()

    def empty(self):
        return len(self) == 0

if __name__ == "__main__":

    import timeit

    timeit.timeit("test()", number=1, setup="from boardqueue import test")



    # initList = [[5, 0, 7], [2, 6, 4], [3, 1, 8]]
    #
    # board1 = Board(initList, [0, 1])
    #
    # frontier = BoardQueue()
    # frontier.append(board1)
    # board2 = board1.swap([0, 0])
    # print(board1 in frontier)
    #
    # frontier.append(board2)
    # print(frontier.pop().values)