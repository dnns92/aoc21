import sys
sys.path.append("/mnt/wsl/")
from aoc21.utils import read_line_as_comma_list

TESTING = False

class FishList:
    def __init__(self):
        self.fishes = {i:0 for i in range(-1, 9)}

    def initialize(self, init_list):
        for l in init_list:
            self.fishes[l] += 1

    def new_day(self):
        for remaining_days in range(9):
            self.fishes[remaining_days - 1] = self.fishes[remaining_days]     
        self.fishes[8] = self.fishes[-1]
        self.fishes[6] += self.fishes[-1]
        del self.fishes[-1]

    def solve(self):
        sum_ = 0
        for i in range(9):
            sum_ += self.fishes[i]
        return sum_
    
    def __repr__(self):
        return ", ".join([f"{i}:" + str(self.fishes[i]) for i in self.fishes])


if TESTING:
    in_file = "/mnt/wsl/aoc21/06/test_input.txt"
else:
    in_file = "/mnt/wsl/aoc21/06/input.txt"

if __name__ == "__main__":
    txt = read_line_as_comma_list(in_file)

    fl = FishList()
    fl.initialize(txt)
    for i in range(256):
        fl.new_day()
    print("6-2", fl.solve())
    