from utils import read_lines_as_text

TESTING = False

if TESTING:
    in_file = "test_input.txt"
else:
    in_file = "input.txt"


closing_map = {")": "(", "]": "[", "}": "{", ">": "<"}

values = {")": 3, "]": 57, "}": 1197, ">": 25137}


def run_bracket(arr, pos, latest_to_close=""):
    if pos >= len(arr):
        return -1
    if arr[pos] in "[(<{":
        latest_to_close += arr[pos]
        err = run_bracket(arr, pos + 1, latest_to_close)
    else:
        if latest_to_close[-1] != closing_map[arr[pos]]:
            return pos
        else:
            latest_to_close = latest_to_close[0:-1]
            err = run_bracket(arr, pos + 1, latest_to_close)
    return err


if __name__ == "__main__":
    lines = read_lines_as_text(in_file)

    pts = 0
    for line in lines:
        ret = run_bracket(line, 0, "")
        if ret > -1:
            pts += values[line[ret]]
    print("10-1", pts)
