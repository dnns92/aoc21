import sys
sys.path.append("..\\")
from utils import read_lines_as_text_raw

TESTING = False

if TESTING:
    in_file = "F:\\aoc21/08/test_input.txt"
else:
    in_file = "F:\\aoc21/08/input.txt"

if __name__ == "__main__":
    data = read_lines_as_text_raw(in_file)
    lines = data.split("\n")
    ctr = 0
    for line in lines:
        input_data, output_data = line.split(" | ")
        for out in output_data.split(" "):
            if len(out) in [2, 4, 3, 7]:
                ctr += 1
    print("8-1", ctr)
