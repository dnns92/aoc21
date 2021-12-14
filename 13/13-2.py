import sys
sys.path.append("..\\")
from aoc21.utils import read_lines_as_text_raw, print_list_pretty
import re

TESTING = False

if TESTING:
    in_file = "13/test_input.txt"
else:
    in_file = "13/input.txt"

if __name__ == "__main__":
    txt = read_lines_as_text_raw(in_file)
    dots, instructions = txt.split("\n\n")
    dots = [[int (y) for y in d.split(",")] for d in dots.split("\n")]
    x_dots = [x[0] for x in dots]
    y_dots = [x[1] for x in dots]

    for instruction in instructions.split("\n"):
        axis, line = re.findall("[xy]=[0-9]+", instruction)[0].split("=")
        line = int(line)
        new_dots = []
        if axis == "x":
            tmp = x_dots
            x_dots = y_dots
            y_dots = tmp
        len_of_paper = max(x_dots), max(y_dots)

        for x, y in zip(x_dots, y_dots):
            if y > line:
                y = 2 * line - y
            new_dots.append([x, y])
        
        unique_dots = []
        for x in new_dots:
            if x not in unique_dots:
                unique_dots.append(x)
        x_dots = [x[0] for x in unique_dots]
        y_dots = [x[1] for x in unique_dots]
        if axis == "x":
            tmp = x_dots
            x_dots = y_dots
            y_dots = tmp
    
    len_of_paper = len_of_paper[1]+1, len_of_paper[0]+1
    paper = [[0]*len_of_paper[0] for i in range(len_of_paper[1])]
    for x, y in zip(x_dots, y_dots):
        paper[x][y] = 1
    print_list_pretty(paper)
