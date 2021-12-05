import sys
sys.path.append("..\\")
from aoc21.utils import read_lines_as_text
import re

TESTING = False

if TESTING:
    in_file = "05/test_input.txt"
    size = 10
else:
    in_file = "05/input.txt"
    size = 1000

epsilon = 10**-8

def plotLine(img, x0, y0, x1, y1):
    dx =  abs(x1-x0)
    dy = -abs(y1-y0);
    err = dx+dy
    while (True):
        img[x0][y0] += 1
        if (x0 == x1 and y0 == y1):
            break
        e2 = 2*err
        if (e2 >= dy):
            err += dy;
            x0 += 1 if x0<x1 else -1;
        if (e2 <= dx):
            err += dx;
            y0 += 1 if y0<y1 else -1;
    return img

if __name__ == "__main__":
    lines = read_lines_as_text(in_file)    
    img = [[0]*size for _ in range(size)]

    for line in lines:
        left_numbers, right_numbers = line.split(" -> ")
        left_numbers = re.findall("[0-9]+", left_numbers) 
        right_numbers = re.findall("[0-9]+", right_numbers)
        img = plotLine(img, int(left_numbers[1]), int(left_numbers[0]), int(right_numbers[1]), int(right_numbers[0]))

    overlaps = 0
    for row in img:
        for entry in row:
            if entry > 1:
                overlaps += 1
    print("5-2", overlaps)