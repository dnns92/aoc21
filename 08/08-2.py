import sys
sys.path.append("..\\")
from utils import read_lines_as_text_raw

TESTING = False

if TESTING:
    in_file = "F:\\aoc21/08/test_input.txt"
else:
    in_file = "F:\\aoc21/08/input.txt"

all_segments = "abcdefg"


def missing(a, b):
    d = 0
    for x in a:
        if x not in b:
            d += 1
    return d


def merge(a, b):
    return str("".join(list({*a, *b})))


def subtract(a, b):
    return "".join([x if x not in b else "" for x in a])


def is_in(a, b):
    return all([i in b for i in a])


if __name__ == "__main__":
    data = read_lines_as_text_raw(in_file)
    lines = data.split("\n")
    int_number = 0
    for line in lines:
        input_data, output_data = line.split(" | ")
        input_numbers = input_data.split(" ")
        output_numbers = output_data.split(" ")

        mapping = {}
        mapping[8] = "abcdefg"
        del_idx = []
        idx = 0
        for number in input_numbers:
            if len(number) == 3:
                mapping[7] = number
                del_idx.append(idx)
            if len(number) == 2:
                mapping[1] = number
                del_idx.append(idx)
            if len(number) == 4:
                mapping[4] = number
                del_idx.append(idx)
            idx += 1
        for i in reversed(del_idx):
            del input_numbers[i]

        del_idx = []
        idx = 0
        for number in input_numbers:
            if "".join(sorted(number)) == "abcdefg":
                del_idx.append(idx)
            idx += 1
        for i in reversed(del_idx):
            del input_numbers[i]

        del_idx = []
        idx = 0
        for number in input_numbers:
            if missing(number, subtract(mapping[8], mapping[4])) == 2:
                mapping[2] = number
                del_idx.append(idx)
            idx += 1

        for i in reversed(del_idx):
            del input_numbers[i]

        del_idx = []
        idx = 0
        for number in input_numbers:
            if is_in(mapping[4], number) and len(number) == 6:
                mapping[9] = number
                del_idx.append(idx)
            idx += 1
        for i in reversed(del_idx):
            del input_numbers[i]

        del_idx = []
        idx = 0
        for number in input_numbers:
            if len(number) == 6 and not is_in(mapping[1], number):
                mapping[6] = number
                del_idx.append(idx)
            idx += 1
        for i in reversed(del_idx):
            del input_numbers[i]

        del_idx = []
        idx = 0
        for number in input_numbers:
            if len(number) == 6:
                mapping[0] = number
                del_idx.append(idx)
            idx += 1
        for i in reversed(del_idx):
            del input_numbers[i]

        del_idx = []
        idx = 0
        for number in input_numbers:
            if is_in(mapping[1], number):
                mapping[3] = number
                del_idx.append(idx)
            idx += 1
        for i in reversed(del_idx):
            del input_numbers[i]
        mapping[5] = input_numbers[0]

        number = ""
        for output_number in output_numbers:
            for key in mapping:
                if sorted(mapping[key]) == sorted(output_number):
                    number += str(key)
        int_number += int(number)
    print("8-2", int_number)
