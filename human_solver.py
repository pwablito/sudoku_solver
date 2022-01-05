from solver import PuzzleSolver
import reduction


class HumanPuzzleSolver(PuzzleSolver):
    strategies = [
        reduction.LastInBlockReductionStrategy,
        reduction.LastInRowReductionStrategy,
        reduction.LastInColumnReductionStrategy,
        reduction.ObviousPairsReductionStrategy,
        reduction.ObviousTriplesReductionStrategy,
    ]

    def solve(self):
        '''
        @return puzzle: Puzzle
        '''
        while True:
            for strategy in self.strategies:
                self.puzzle, updated = strategy(self.puzzle).reduce()
                if updated:
                    break
            if self.puzzle.is_solved():
                break
        return self.puzzle
