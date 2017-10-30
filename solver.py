import os
from queue import PriorityQueue
from time import time

import psutil

import board
from boardqueue import BoardQueue
from boardstack import BoardStack

# keep track of the swapping history etc. to report the goal path when finished
meta = dict()


class Solver:

    nodes_expanded = 0
    search_depth = 0
    max_search_depth = 0
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
            # stack is lifo so put "up" last
            neighbours = neighbours.__reversed__()
        for neighbour in neighbours:
            if neighbour is not None:
                new_board = self.board_state.swap(neighbour)
                if new_board.values not in self.explored and new_board.values not in self.frontier_set:
                    # print("frotnier board")
                    # new_board.draw()
                    Solver._update_moves_list(self.board_state, new_board, neighbour)
                    self.frontier_set.add(new_board.values)
                    self.frontier.append(new_board)

    def solve(self):
        self.t0 = time()
        self.process = psutil.Process(os.getpid())
        switcher = {
            "bfs": self._bfs,
            "dfs": self._dfs,
            "ast": self._ast
        }
        # find and execute algo
        print("board to solve")
        self.board_state.draw()
        meta[self.board_state.values] = [None, None]

        switcher.get(self.algo, "not implemented")()

    def _print_stats(self):
        goal_path = self._gen_goal_path()
        print("path to goal:", goal_path)
        print("cost_of_path:", len(goal_path))
        print("nodes_expanded:", self.nodes_expanded)
        print("search_depth", self.search_depth)
        print("max_search_depth", self.max_search_depth)
        print("running_time", time() - self.t0, "seconds")
        print("max_ram_usage", self.process.memory_info().rss / float(2 ** 20), "Mbit")

    # frontier needs to be queue or stack
    def _bfs_or_dfs(self, frontier):
        self.frontier = frontier

        self.explored.add(self.board_state.values)
        self.enqueue_new_states()

        while not self.frontier.empty():
            self.board_state = self.frontier.pop()
            # print("search board")
            # self.board_state.draw()
            self.explored.add(self.board_state.values)
            self.frontier_set.remove(self.board_state.values)
            self.nodes_expanded += 1

            if self.board_state.is_finished():
                # found the path!
                self._print_stats()
                break

            self.enqueue_new_states()

    def _bfs(self):
        self._bfs_or_dfs(BoardQueue())

    def _dfs(self):
        self._bfs_or_dfs(BoardStack())

    def _ast(self):
        self.frontier = PriorityQueue()
        self.frontier.put(self.board_state, 0)
        self.frontier_set = set()

        gscore = dict()
        gscore[self.board_state.values] = 0

        fscore = dict()
        fscore[self.board_state.values] = gscore[self.board_state.values] + self.board_state.manhattan_distance

        while not self.frontier.empty():
            self.board_state = self.frontier.get()
            # print("search board")
            # self.board_state.draw()
            self.explored.add(self.board_state.values)

            if self.board_state.is_finished():
                # found the path!
                self._print_stats()
                break

            neighbours = self.board_state.zero_tile.neighbors
            for neighbour in neighbours:
                if neighbour is not None:
                    new_board = self.board_state.swap(neighbour)
                    self.nodes_expanded += 1
                    if new_board.values in self.explored or new_board.values in self.frontier_set:
                        continue

                    gscore[new_board.values] = gscore[self.board_state.values] + self.board_state.cost(neighbour)
                    fscore[new_board.values] = gscore[new_board.values] + new_board.manhattan_distance

                    # print("frontier board")
                    # print("manhattan distance: ", new_board.manhattan_distance)
                    # new_board.draw()
                    self.frontier.put(new_board, fscore[new_board.values])
                    self.frontier_set.add(new_board.values)
                    Solver._update_moves_list(self.board_state, new_board, neighbour)

    @staticmethod
    def _update_moves_list(old_board, new_board, neighbour):
        zero_row = old_board.zero_tile.position[0]
        zero_column = old_board.zero_tile.position[1]
        with_row = neighbour[0]
        with_column = neighbour[1]

        move = None
        if zero_row > with_row and zero_column == with_column:
            move = "Up"
        if zero_row < with_row and zero_column == with_column:
            move = "Down"
        if zero_row == with_row and zero_column > with_column:
            move = "Left"
        if zero_row == with_row and zero_column < with_column:
            move = "Right"

        meta[new_board.values] = (old_board.values, move)

    def _gen_goal_path(self):
        state = self.board_state.values
        action_list = []
        while True:
            self.max_search_depth += 1
            row = meta[state]
            state = row[0]
            action = row[1]
            if state is None:
                break
            action_list.append(action)
            self.search_depth += 1
        return list(reversed(action_list))