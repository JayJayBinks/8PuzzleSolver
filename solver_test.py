import unittest
import solver

board1 = ((3,1,2),(0,4,5),(6,7,8))
board2= ((1,2,5),(3,4,0),(6,7,8))
board3 = ((1,2,5),(3,4,8),(0,6,7))
long_path_to_goals = ((6,1,8),(4,0,2),(7,3,5))
long_path_to_goals2 = ((8,6,4),(2,1,3),(5,7,0))


class SolverTest(unittest.TestCase):
    def testBFS1(self):
        solver.Solver("bfs", board1, [1, 0]).solve()

    def testBFS2(self):
        solver.Solver("bfs", board2, [1, 2]).solve()

    def testBFS3(self):
        solver.Solver("bfs", long_path_to_goals, [1, 1]).solve()

    def testBFS4(self):
        solver.Solver("bfs", long_path_to_goals2, [2, 2]).solve()

    def testDFS1(self):
         solver.Solver("dfs", board1, [1, 0]).solve()

    def testDFS2(self):
        solver.Solver("dfs", board2, [1, 2]).solve()

    def testDFS3(self):
        solver.Solver("dfs", long_path_to_goals, [1, 1]).solve()

    def testDFS4(self):
        solver.Solver("dfs", long_path_to_goals2, [2, 2]).solve()

    def testAST1(self):
        solver.Solver("ast", board1, [1, 0]).solve()

    def testAST2(self):
        solver.Solver("ast", board2, [1, 2]).solve()

    def testAST3(self):
         solver.Solver("ast", long_path_to_goals, [1, 1]).solve()

    def testAST4(self):
        solver.Solver("ast", long_path_to_goals2, [2, 2]).solve()

    def testAST5(self):
        solver.Solver("ast", board3, [2, 0]).solve()

if __name__ == '__main__':
    unittest.main()