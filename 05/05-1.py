import sys
sys.path.append("..\\")
from aoc21.utils import read_lines_as_text
import re

TESTING = False

if TESTING:
    in_file = "05/test_input.txt"
else:
    in_file = "05/input.txt"

if __name__ == "__main__":
    lines = read_lines_as_text(in_file)
    left = []
    right = []
    size = 1000
    max_ = 0
    img = [[0]*size for _ in range(size)]

    for line in  lines:
        left_numbers, right_numbers = line.split(" -> ")
        left_numbers = re.findall("[0-9]+", left_numbers) 
        right_numbers = re.findall("[0-9]+", right_numbers)
        left.append(left_numbers)
        right.append(right_numbers)
    for l, r in zip(left, right):
        if l[0] != r[0] and l[1] != r[1]:
            continue
        if l[1] == r[1]:
            start = min([int(l[0]), int(r[0])])
            end = max([int(l[0]),  int(r[0])])
            for x1 in range(start, end + 1):
                img[int(l[1])][x1] += 1
                if img[int(l[1])][x1] > max_:
                    max_ = img[int(l[1])][x1]
        if l[0] == r[0]:
            start = min([int(l[1]), int(r[1])])
            end = max([int(l[1]),  int(r[1])])
            for x1 in range(start, end + 1):
                img[x1][int(l[0])] += 1
                if img[x1][int(l[0])] > max_:
                    max_ = img[x1][int(l[0])]
    ctr = 0
    for row in img:
        for entry in row:
            if entry > 1:
                ctr += 1
    print(ctr)
