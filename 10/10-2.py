from utils import read_lines_as_text

TESTING = False

if TESTING:
    in_file = "test_input.txt"
else:
    in_file = "input.txt"


closing_map = {")": "(", "]": "[", "}": "{", ">": "<"}
values = {"(": 1, "[": 2, "{": 3, "<": 4}
GlobalString = ""


def run_bracket(arr, pos, latest_to_close=""):
    if pos >= len(arr):
        global GlobalString
        GlobalString = GlobalString + " " + latest_to_close
        return
    if arr[pos] in "[(<{":
        latest_to_close += arr[pos]
        run_bracket(arr, pos + 1, latest_to_close)
    else:
        if latest_to_close[-1] != closing_map[arr[pos]]:
            return
        else:
            latest_to_close = latest_to_close[0:-1]
            run_bracket(arr, pos + 1, latest_to_close)
    return


def calc_score(string):
    score = 0
    for idx, s in enumerate(string):
        score = score * 5 + values[s]
    return score


if __name__ == "__main__":
    lines = read_lines_as_text(in_file)
    for line in lines:
        run_bracket(line, 0, "")
    x = "".join(list(reversed(GlobalString)))
    scores = sorted([calc_score(i) for i in x.split(" ")])
    print("10-2", scores[len(scores)//2])
