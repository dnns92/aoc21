import sys
sys.path.append("..\\")
from aoc21.utils import read_lines_as_text_raw
import re


TESTING = False

if TESTING:
    in_file = "04/test_input.txt"
else:
    in_file = "04/input.txt"


bingo_pattern = [
    r"X X X X X",
    r"X [X\d]+ [X\d]+ [X\d]+ [X\d]+\nX [X\d]+ [X\d]+ [X\d]+ [X\d]+\nX [X\d]+ [X\d]+ [X\d]+ [X\d]+\nX [X\d]+ [X\d]+ [X\d]+ [X\d]+\nX [X\d]+ [X\d]+ [X\d]+ [X\d]+",
    r"[X\d]+ X [X\d]+ [X\d]+ [X\d]+\n[X\d]+ X [X\d]+ [X\d]+ [X\d]+\n[X\d]+ X [X\d]+ [X\d]+ [X\d]+\n[X\d]+ X [X\d]+ [X\d]+ [X\d]+\n[X\d]+ X [X\d]+ [X\d]+ [X\d]+",
    r"[X\d]+ [X\d]+ X [X\d]+ [X\d]+\n[X\d]+ [X\d]+ X [X\d]+ [X\d]+\n[X\d]+ [X\d]+ X [X\d]+ [X\d]+\n[X\d]+ [X\d]+ X [X\d]+ [X\d]+\n[X\d]+ [X\d]+ X [X\d]+ [X\d]+",
    r"[X\d]+ [X\d]+ [X\d]+ X [X\d]+\n[X\d]+ [X\d]+ [X\d]+ X [X\d]+\n[X\d]+ [X\d]+ [X\d]+ X [X\d]+\n[X\d]+ [X\d]+ [X\d]+ X [X\d]+\n[X\d]+ [X\d]+ [X\d]+ X [X\d]+",
    r"[X\d]+ [X\d]+ [X\d]+ [X\d]+ X\n[X\d]+ [X\d]+ [X\d]+ [X\d]+ X\n[X\d]+ [X\d]+ [X\d]+ [X\d]+ X\n[X\d]+ [X\d]+ [X\d]+ [X\d]+ X\n[X\d]+ [X\d]+ [X\d]+ [X\d]+ X"
]


def check_for_bingo(board):
    bingo = False
    for idx, pattern in enumerate(bingo_pattern):
        findings = re.findall(pattern, board)
        if len(findings) > 0:
            bingo = True
            break
    return bingo, idx


if __name__ == "__main__":
    text = read_lines_as_text_raw(in_file)
    text = text.replace("  ", " ")
    text = text.replace("\n ", "\n")

    text = text.split("\n\n")
    bingo_numbers = [i for i in text[0].split(",")]
    boards = text[1:]
    boards = ["\n" + i + "\n" for i in boards]
    original_boards = boards.copy()

    for num_iters, drawn_number in enumerate(bingo_numbers):
        for idx, board in enumerate(boards):
            findings = re.findall(fr"[\n ^]{drawn_number}[\n ]", board)
            if findings:
                for finding in findings:
                    board = re.sub(finding, finding[0] + "X" + finding[-1], board)
                boards[idx] = board
            BINGO, pattern_index = check_for_bingo(board)
            if BINGO:
                bingo_board = board
                board_index = idx
                break
        if BINGO:
            break
    findings = re.findall("\d+", bingo_board)
    print(bingo_board)
    print("4-1:", sum([int(i) for i in findings]) * int(drawn_number))
