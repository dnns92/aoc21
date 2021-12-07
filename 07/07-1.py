import sys
sys.path.append("..\\")
from aoc21.utils import read_line_as_integer_list

def calc_median(x):
    x = sorted(x)
    return (x[len(x)//2 - 1] + x[len(x)//2]) / 2 if len(x) % 2 == 0 else x[(len(x))//2]

TESTING = True

if TESTING:
    in_file = "07/test_input.txt"
else:
    in_file = "07/input.txt"

if __name__ == "__main__":
    data = read_line_as_integer_list(in_file)
    median = calc_median(data)
    print("7-1:", int(sum([abs(i - median) for i in data])))
