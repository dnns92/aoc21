import sys
sys.path.append("..\\")
from aoc21.utils import read_line_as_integer_list

TESTING = False

if TESTING:
    in_file = "07/test_input.txt"
else:
    in_file = "07/input.txt"


def calc_oil_usage(pos, target):
    return (abs(target-pos) * (abs(target-pos) + 1)) / 2
    

if __name__ == "__main__":
    data = read_line_as_integer_list(in_file)
    positions = max(data)
    smallest = -1
    for target_position in range(positions):
        sum_ = 0
        for position in data:
            sum_+= calc_oil_usage(position, target_position)
        if smallest == -1 or sum_ < smallest:
            smallest = sum_
    print("7-2", int(smallest))