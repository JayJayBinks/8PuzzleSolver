from time import time
import os
import psutil

from board import Board
from boardqueue import BoardQueue
from boardset import BoardSet

initList = [[1, 2, 5], [3, 4, 0], [6, 7, 8]]
frontier = BoardQueue()
explored = BoardSet()

nodes_expanded = 0
search_depth = "implement this"
max_search_depth= "implement this"
running_time = 0
max_ram_usage = 0

def enqueue_new_states(board_state):
    for neighbour in board_state.zero_tile.neighbors:
        if neighbour is not None:
            new_board = board_state.switch(neighbour)
            if new_board not in explored and new_board not in frontier:
                frontier.put_nowait(new_board)



if __name__ == "__main__":
    t0 = time()
    process = psutil.Process(os.getpid())


    #frontier init
    enqueue_new_states(Board(initList, [1,2]))

    while not frontier.empty():
        boardState = frontier.get_nowait()

        explored.add(boardState)

        if boardState.isFinished():
            print("path to goal:" , boardState.list_of_moves)
            print("cost_of_path:", len(boardState.list_of_moves))
            print("nodes_expanded:", nodes_expanded)
            print("search_depth", max_search_depth)
            print("running_time", time() - t0)
            print("max_ram_usage", process.memory_info().rss / float(2 ** 20), "Mbit")

            break

        nodes_expanded += 1
        enqueue_new_states(boardState)
