import sys
sys.path.append("..\\")
from aoc21.utils import read_lines_as_text_raw
import re

TESTING = False

if TESTING:
    in_file = "13/test_input.txt"
else:
    in_file = "13/input.txt"

if __name__ == "__main__":
    txt = read_lines_as_text_raw(in_file)
    dots, instructions = txt.split("\n\n")
    instruction = instructions.split("\n")[0]
    axis, line = re.findall("[xy]=[0-9]+", instruction)[0].split("=")
    line = int(line)
    print(axis, line)
    dots = [[int (y) for y in d.split(",")] for d in dots.split("\n")]
    print("dots", dots)

    new_dots = []
    x_dots = [x[0] for x in dots]
    y_dots = [x[1] for x in dots]
    len_of_paper = max(x_dots), max(y_dots)

    if axis == "x":
        tmp = x_dots
        x_dots = y_dots
        y_dots = tmp
    len_of_paper = max(x_dots), max(y_dots)


    for x, y in zip(x_dots, y_dots):
        if y > line:
            y = len_of_paper[1] - y
        elif y == line:
            pass
        new_dots.append([x, y])
    
    print(len(new_dots))
    unique_dots = []
    for x in new_dots:
        if x not in unique_dots:
            unique_dots.append(x)
    print(len(unique_dots))



