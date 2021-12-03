import sys
sys.path.append("..\\")
from aoc21.utils import read_lines_as_int

print("1-1")

if __name__ == "__main__":
    distances = read_lines_as_int("01/input.txt")
    print(distances)

    increments = 0
    prev = distances[0]
    for distance in distances[1:]:
        if prev < distance:
            increments += 1
    print("Amount of Increments:", increments)
