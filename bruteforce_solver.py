from solver import PuzzleSolver
from puzzle import EMPTY


class BruteForcePuzzleSolver(PuzzleSolver):
    def solve(self):
        while True:
            for i in range(9):
                for j in range(9):
                    test_puzzle = self.puzzle.copy()
                    if test_puzzle[i][j] != EMPTY:
                        for k in range(9):
                            test_puzzle[i][j] = k
                            if test_puzzle.is_solved():
                                self.puzzle = test_puzzle
                                return
                            if test_puzzle.is_valid():
                                break
        raise NotImplementedError
