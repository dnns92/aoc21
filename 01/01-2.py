import sys
sys.path.append("..\\")
from aoc21.utils import read_lines_as_int

window_size = 3

if __name__ == "__main__":
    integers = read_lines_as_int("01/input.txt")

    increments = 0
    prev = sum(integers[0:window_size])
    rest = integers[1:]
    for idx, integer in enumerate(rest[:-2]):
        sum_ = sum(rest[idx:idx+window_size])
        if (prev < sum_):
            increments += 1
        prev = sum_
    print("1-2:", increments)
