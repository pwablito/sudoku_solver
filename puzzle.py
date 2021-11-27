EMPTY = -1


class Puzzle:
    def __init__(self, arr):
        self.arr = arr

    def is_solved(self):
        try:
            for line in self.arr:
                assert EMPTY not in line
        except AssertionError:
            return False
        return self.is_valid()

    def is_valid(self):
        try:
            assert len(self.arr) == 9
            for line in self.arr:
                assert len(line) == 9
        except AssertionError:
            return False
        return self.valid_values()

    def valid_values(self):
        try:
            for i in range(9):
                available_values = list(range(1, 10))
                for item in self.arr[i]:
                    if item is not EMPTY:
                        assert item in available_values
                        available_values.remove(item)
            for i in range(9):
                available_values = list(range(1, 10))
                for item in self.arr[:][i]:
                    if item is not EMPTY:
                        assert item in available_values
                        available_values.remove(item)
            for row_offset in [0, 3, 6]:
                for col_offset in [0, 3, 6]:
                    available_values = list(range(1, 10))
                    for row in range(row_offset, row_offset + 3):
                        for col in range(col_offset, col_offset + 3):
                            if item is not EMPTY:
                                assert item in available_values
                                available_values.remove(item)
        except AssertionError:
            return False
        return True

    @classmethod
    def from_file(cls, filename):
        initial_state = []
        with open(filename) as f:
            lines = f.readlines()
            for line in lines:
                nums = line.split()
                state_line = []
                for digit in nums:
                    if digit.isdigit():
                        state_line.append(int(digit))
                    else:
                        state_line.append(EMPTY)
                initial_state.append(state_line)
        obj = cls(initial_state)
        if not obj.is_valid():
            raise ValueError("Invalid initial state")
        return obj

    def solve(self):
        raise NotImplementedError

    def __str__(self):
        str_array = [
            [
                str(item) if item is not EMPTY
                else " " for item in line
            ]
            for line in self.arr
        ]
        return "\n".join([" ".join(line) for line in str_array])
