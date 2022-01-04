#!/usr/bin/env python3

import argparse
from puzzle import Puzzle
from solver import PuzzleSolver
from bruteforce_solver import BruteForcePuzzleSolver
from human_solver import HumanPuzzleSolver


def main():
    parser = argparse.ArgumentParser(description="Solve a sudoku puzzle")
    parser.add_argument(
        "file",
        help="File containing sudoku puzzle",
        type=str,
    )
    parser.add_argument(
        "method",
        help="Method to solve puzzle",
        options=["brute", "human"],
    )
    args = parser.parse_args()
    solver_cls = PuzzleSolver
    if args.method == "brute":
        solver_cls = BruteForcePuzzleSolver
    elif args.method == "human":
        solver_cls = HumanPuzzleSolver
    puzzle = Puzzle.from_file(args.file)
    print("Before:")
    print(puzzle)
    print("Solving...")
    solver = solver_cls(puzzle)
    print("After:")
    print(solver.solve())


if __name__ == "__main__":
    main()
