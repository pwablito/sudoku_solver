#!/usr/bin/env python3

import argparse
from puzzle import Puzzle, EMPTY


def main():
    parser = argparse.ArgumentParser(description="Solve a sudoku puzzle")
    parser.add_argument(
        "file",
        help="File containing sudoku puzzle",
        type=str
    )
    args = parser.parse_args()
    puzzle = Puzzle.from_file(args.file)
    solver = PuzzleSolver(puzzle)
    solver.solve()


class PuzzleSolver:
    def __init__(self, puzzle):
        self.puzzle = puzzle

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


if __name__ == "__main__":
    main()
