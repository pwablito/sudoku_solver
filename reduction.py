from puzzle import EMPTY


class ReductionStrategy:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def reduce(self):
        '''
        @return: (puzzle: Puzzle, updated: bool)
        '''
        raise NotImplementedError("Abstract method")


class LastInBlockReductionStrategy(ReductionStrategy):
    def reduce(self):
        updated = False
        for row_offset in [0, 3, 6]:
            for col_offset in [0, 3, 6]:
                available_values = list(range(1, 10))
                for row in range(row_offset, row_offset + 3):
                    for col in range(col_offset, col_offset + 3):
                        item = self.puzzle.arr[row][col]
                        if item != EMPTY:
                            assert item in available_values
                            available_values.remove(item)
                if len(available_values) == 1:
                    for row in range(row_offset, row_offset + 3):
                        for col in range(col_offset, col_offset + 3):
                            item = self.puzzle.arr[row][col]
                            if item == EMPTY:
                                self.puzzle.arr[row][col] = available_values[0]
                                updated = True
        return self.puzzle, updated


class LastInRowReductionStrategy(ReductionStrategy):
    def reduce(self):
        raise NotImplementedError


class LastInColumnReductionStrategy(ReductionStrategy):
    def reduce(self):
        raise NotImplementedError


class ObviousPairsReductionStrategy(ReductionStrategy):
    def reduce(self):
        raise NotImplementedError


class ObviousTriplesReductionStrategy(ReductionStrategy):
    def reduce(self):
        raise NotImplementedError
