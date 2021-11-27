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
    # puzzle.solve()
    print(puzzle)


if __name__ == "__main__":
    main()
