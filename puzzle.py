EMPTY = -1


class Puzzle:
    def __init__(self, arr):
        self.arr = arr

    def is_solved(self):
        for line in self.arr:
            assert EMPTY not in line
        return self.is_valid()

    def is_valid(self):
        try:
            assert len(self.arr) == 9
            for line in self.arr:
                assert len(line) == 9
        except AssertionError:
            return False
        return self.valid_values()

    def valid_values():
        raise NotImplementedError

    @classmethod
    def from_file(cls, filename):
        initial_state = []
        with open(filename) as f:
            lines = f.readlines()
            for line in lines:
                nums = lines.split()
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