from puzzle import Puzzle


def test_check_valid_no_error():
    assert Puzzle([
        [1, -1, -1, 2, -1, -1, 3, -1, -1],
        [4, -1, -1, 5, -1, -1, 6, -1, -1],
        [7, -1, -1, 8, -1, -1, 9, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    ]).is_valid()


def test_check_valid_horizontal_error():
    assert not Puzzle([
        [1, -1, 1, 2, -1, -1, 3, -1, -1],
        [4, -1, -1, 5, -1, -1, 6, -1, -1],
        [7, -1, -1, 8, -1, -1, 9, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    ]).is_valid()


def test_check_valid_vertical_error():
    assert not Puzzle([
        [1, -1, -1, 2, -1, -1, 3, -1, -1],
        [1, -1, -1, 5, -1, -1, 6, -1, -1],
        [7, -1, -1, 8, -1, -1, 9, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    ]).is_valid()


def test_check_valid_3x3_error():
    assert not Puzzle([
        [1, -1, -1, 2, -1, -1, 3, -1, -1],
        [4, -1, -1, 5, -1, -1, 6, -1, -1],
        [7, -1, 1, 8, -1, -1, 9, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    ]).is_valid()


def test_check_solved_incorrect():
    assert not Puzzle([
        [1, -1, -1, 2, -1, -1, 3, -1, -1],
        [4, -1, -1, 5, -1, -1, 6, -1, -1],
        [7, -1, -1, 8, -1, -1, 9, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    ]).is_solved()


def test_check_solved_correct():
    assert Puzzle([
        [4, 3, 5, 2, 6, 9, 7, 8, 1],
        [6, 8, 2, 5, 7, 1, 4, 9, 3],
        [1, 9, 7, 8, 3, 4, 5, 6, 2],
        [8, 2, 6, 1, 9, 5, 3, 4, 7],
        [3, 7, 4, 6, 8, 2, 9, 1, 5],
        [9, 5, 1, 7, 4, 3, 6, 2, 8],
        [5, 1, 9, 3, 2, 6, 8, 7, 4],
        [2, 4, 8, 9, 5, 7, 1, 3, 6],
        [7, 6, 3, 4, 1, 8, 2, 5, 9],
    ]).is_solved()
