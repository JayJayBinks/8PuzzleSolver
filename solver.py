from time import time
import os
import psutil
import board
from boardqueue import BoardQueue
from boardstack import BoardStack

meta = dict()

class Solver:

    nodes_expanded = 0
    search_depth = "implement this"
    max_search_depth = "implement this"
    running_time = 0
    max_ram_usage = 0

    def __init__(self , algo, init_list, zero_position):
        self.algo = algo
        self.board_state = board.Board(init_list, zero_position)
        self.explored = set()
        self.frontier_set = set()

    def enqueue_new_states(self):
        neighbours = self.board_state.zero_tile.neighbors
        if self.algo == "dfs":
            #stack is lifo so put "up" last
            neighbours = neighbours.__reversed__()
        for neighbour in neighbours:
            if neighbour is not None:
                new_board = self.board_state.swap(neighbour)
                if new_board.values not in self.explored and new_board.values not in self.frontier_set:
                    #print("frotnier board")
                    #new_board.draw()
                    self.frontier_set.add(new_board.values)
                    self.frontier.append(new_board)

    def solve(self):
        switcher = {
            "bfs": self._bfs,
            "dfs": self._dfs,
            "ast": self._ast
        }
        #find and execute algo
        switcher.get(self.algo, "not implemented")()

    def _print_stats(self):
        print("path to goal:", self.board_state.list_of_moves)
        print("cost_of_path:", len(self.board_state.list_of_moves))
        print("nodes_expanded:", self.nodes_expanded)
        print("search_depth", self.max_search_depth)
        print("running_time", time() - self.t0, "seconds")
        print("max_ram_usage", self.process.memory_info().rss / float(2 ** 20), "Mbit")

    def _bfs_or_dfs(self, frontier):
        self.frontier = frontier
        self.t0 = time()
        self.process = psutil.Process(os.getpid())
        # frontier init

        print("init board")
        self.board_state.draw()

        self.explored.add(self.board_state.values)
        self.enqueue_new_states()

        while not self.frontier.empty():
            self.board_state = self.frontier.pop()
            #print("search board")
            #self.board_state.draw()
            self.explored.add(self.board_state.values)
            self.frontier_set.remove(self.board_state.values)
            self.nodes_expanded += 1

            if self.board_state.isFinished():
                #heureka found the path!
                self._print_stats()
                break

            self.enqueue_new_states()

    def _bfs(self):
        self._bfs_or_dfs(BoardQueue())

    def _dfs(self):
        self._bfs_or_dfs(BoardStack())

    def _ast(self):
        raise NotImplementedError()
