#!/usr/bin/env python3

import argparse
from puzzle import Puzzle


def main():
    parser = argparse.ArgumentParser(description="Solve a sudoku puzzle")
    parser.add_argument(
        "-f", "--file",
        help="File containing sudoku puzzle",
        type=str, required=True
    )
    args = parser.parse_args()
    puzzle = Puzzle(args.file)
    print(puzzle.is_solved())


if __name__ == "__main__":
    main()
