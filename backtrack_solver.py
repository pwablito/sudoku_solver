from puzzle import EMPTY, Puzzle
from solver import PuzzleSolver


class BacktrackPuzzleSolver(PuzzleSolver):
    @staticmethod
    def first_empty_coords(arr):
        for i in range(9):
            for j in range(9):
                if arr[i][j] == EMPTY:
                    return i, j
        raise ValueError("No empty cells")

    def solve(self):
        state = self.puzzle.arr.copy()
        solution = BacktrackPuzzleSolver.rec_solve(state)
        self.puzzle = Puzzle(solution)

    @staticmethod
    def rec_solve(state):
        '''
        @return 2D array or False
        '''
        i, j = BacktrackPuzzleSolver.first_empty_coords(state)
        for test_val in range(1, 10):  # Numbes 1-9
            state[i][j] = test_val
            if Puzzle(state).is_valid():
                if Puzzle(state).is_solved():
                    return state
                solution_or_false = BacktrackPuzzleSolver.rec_solve(state)
                if solution_or_false:
                    return solution_or_false
        state[i][j] = EMPTY
        return False
