import unittest

import solver
from solver import Solver

board1 = [[3,1,2],[0,4,5],[6,7,8]]
board2= [[1,2,5],[3,4,0],[6,7,8]]
long_path_to_goals = [[6,1,8],[4,0,2],[7,3,5]]

class SolverTest(unittest.TestCase):
    def testBFS1(self):
        #self.assertEqual(
        solver.Solver("bfs", board1, [1,0]).solve()

    def testBFS2(self):
        solver.Solver("bfs", board2, [1,2]).solve()

    def testDFS1(self):
         # self.assertEqual(
         solver.Solver("dfs", board1, [1, 0]).solve()

    def testDFS2(self):
        solver.Solver("dfs", board2, [1, 2]).solve()

if __name__ == '__main__':
    unittest.main()