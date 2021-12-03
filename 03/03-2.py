import sys
sys.path.append("..\\")
from copy import deepcopy

from aoc21.utils import read_lines_as_text

TESTING = False

if TESTING:
    in_file = "03/test_input.txt"
else:
    in_file = "03/input.txt"

# python uses a banking-round method, where round(0.5) = 0
epsilon = 10**-6

def binary2decimal(bits):
    idx = 0
    number = 0
    for bit in reversed(bits):
        number += 2**idx * int(bit)
        idx += 1
    return number



def calculate_bit_criterion(bits, position, use_most_common_bit):
    bit_criterion = 0
    for line in bits:
        bit_criterion += int(line[position])
    if use_most_common_bit:
        return str(int(round(epsilon + (bit_criterion / len(bits)))))
    else:
        return str(1 - int(round(epsilon + (bit_criterion / len(bits)))))


def run_through(data, use_most_common_bit=False):
    bit_position = 0
    while len(data) > 1:
        criterion = calculate_bit_criterion(data, bit_position, use_most_common_bit)
        non_fitting_indices = []
        for idx, d in enumerate(data):
            if d[bit_position] != criterion:
                non_fitting_indices.append(idx)
        for idx in reversed(non_fitting_indices):
            del data[idx]
        bit_position += 1
    return data[0]


if __name__ == "__main__":
    data = read_lines_as_text(in_file)
    bitlength = len(data[0])
    bit_position = 0

    gamma = binary2decimal(
        run_through(deepcopy(data), True)
    )

    epsilon = binary2decimal(
        run_through(deepcopy(data), False)
    )

    print("3-2:", gamma * epsilon)