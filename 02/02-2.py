import sys
sys.path.append("..\\")
from aoc21.utils import read_lines_as_text

TESTING = False


if TESTING:
    in_file = "02/test_input.txt"
else:
    in_file = "02/input.txt"


class Position:
    def __init__(self):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0
    
    def add(self, direction, amount):
        if direction == "forward":
            self.horizontal = self.horizontal + amount
            self.depth = self.depth + (self.aim * amount)
        elif direction == "down":
            self.aim = self.aim + amount
        elif direction == "up":
            self.aim = self.aim - amount
        else:
            raise NotImplementedError("Unknown Command")
    
    def solve(self):
        return self.horizontal * self.depth


if __name__ == "__main__":
    text_input = read_lines_as_text(in_file)
    course = []
    for line in text_input:
        course.append(line.split(" "))
    print(course[0:10])

    pos = Position()
    for instruction in course:
        pos.add(instruction[0], int(instruction[1]))
    print(pos.solve())