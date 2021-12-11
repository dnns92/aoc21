import sys
sys.path.append("..\\")
from aoc21.utils import read_lines_as_text

TESTING = False

if TESTING:
    in_file = "11/test_input.txt"
else:
    in_file = "11/input.txt"

blink_counter = 0

def walk_blink(mat, x, y):
    if y >= len(mat):
        return mat
    if x >= len(mat[0]):
        return mat
    if mat[y][x] < 10:
        return mat
    if x < 0 or y < 0:
        return mat
    global blink_counter
    blink_counter += 1
    for i in range(-1, 2):
        for j in range(-1, 2):
            if y + i < 0 or x + j < 0 or y + i >= len(mat) or x +j >= len(mat[0]):
                continue
            mat[y+i][x+j] += 1

    mat[y][x] = -10000
    for i in range(-1, 2):
        for j in range(-1, 2):
            if y + i < 0 or x + j < 0:
                continue
            mat = walk_blink(mat, y+i, x+j)
    return mat

def inrease(mat):
    for idy, row in enumerate(mat):
        for idx, _ in enumerate(row):
            mat[idy][idx] += 1
    return mat

def walk(mat):
    for y, row in enumerate(mat):
        for x, _ in enumerate(row):
            mat = walk_blink(mat, x, y)
    return mat


if __name__ == "__main__":
    levels = [list(map(int, line.strip())) for line in read_lines_as_text(in_file)]
    for i in range(100):
        levels = inrease(levels)
        for i in range(1000):
            levels = walk(levels)
        for idy, row in enumerate(levels):
            for idx, entry in enumerate(row):
                if levels[idy][idx] < 0:
                    levels[idy][idx] = 0
        print("11-1", blink_counter)