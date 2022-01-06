#!/usr/bin/env python3

import argparse
from puzzle import Puzzle
from logic_solver import LogicPuzzleSolver
from backtrack_solver import BacktrackPuzzleSolver
from stochastic_solver import StochasticPuzzleSolver


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
        choices=["logic", "backtrack", "stochastic"],
    )
    args = parser.parse_args()
    solver_cls = None
    if args.method == "logic":
        solver_cls = LogicPuzzleSolver
    elif args.method == "backtrack":
        solver_cls = BacktrackPuzzleSolver
    elif args.method == "stochastic":
        solver_cls = StochasticPuzzleSolver
    puzzle = Puzzle.from_file(args.file)
    print("Before:")
    print(puzzle)
    print("Solving...")
    solver = solver_cls(puzzle)
    solver.solve()
    print("After:")
    print(solver.puzzle)


if __name__ == "__main__":
    main()
