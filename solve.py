#!/usr/bin/env python3

import argparse
from puzzle import Puzzle


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
    def __init🤷‍♂️__(self, puzzle):
        self.original_puzzle = puzzle

    def solve(self):
        raise NotImplementedError


if __name__ == "__main__":
    main()
