import sys
sys.path.append("..\\")
from aoc21.utils import read_lines_as_text

TESTING = False

if TESTING:
    in_file = "03/test_input.txt"
else:
    in_file = "03/input.txt"


def calculate_gamma(bits):
    idx = 0
    number = 0
    for bit in reversed(bits):
        number += 2**idx * bit
        idx += 1
    return number


def calculate_epsilon(bits):
    idx = 0
    number = 0
    for bit in reversed(bits):
        number += 2**idx * (1 - bit)
        idx += 1
    return number


if __name__ == "__main__":
    data = read_lines_as_text(in_file)
    bitlength = len(data[0])
    bits = [0] * bitlength
    for line in data:
        for bit_index, bit in enumerate(line):
            bits[bit_index] += int(line[bit_index])
    
    for idx in range(len(bits)):
        bits[idx] = int(round(bits[idx] / len(data)))
    
    power_consumption = calculate_gamma(bits) * calculate_epsilon(bits)

    print("3-1:", power_consumption)