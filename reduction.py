class ReductionStrategy:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def reduce(self):
        '''
        @return: (puzzle: Puzzle, updated: bool)
        '''
        raise NotImplementedError("Abstract method")


class BlockReductionStrategy(ReductionStrategy):
    def reduce(self):
        raise NotImplementedError


class RowReductionStrategy(ReductionStrategy):
    def reduce(self):
        raise NotImplementedError


class ColumnReductionStrategy(ReductionStrategy):
    def reduce(self):
        raise NotImplementedError


class ObviousPairsReductionStrategy(ReductionStrategy):
    def reduce(self):
        raise NotImplementedError


class ObviousTriplesReductionStrategy(ReductionStrategy):
    def reduce(self):
        raise NotImplementedError
