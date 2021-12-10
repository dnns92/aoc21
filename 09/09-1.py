from utils import read_lines_as_text

TESTING = False

if TESTING:
    in_file = r"D:\aoc21\09/test_input.txt"
else:
    in_file = r"D:\aoc21\09/input.txt"

def get_row(mat, x, y):
    x_left = x-1
    x_right = x + 1
    return mat[y][x_left], mat[y][x], mat[y][x_right]

def get_col(mat, x, y):
    y_up = max(0, y - 1)
    y_down = min(y + 1, len(mat))
    return mat[y_up][x], mat[y][x], mat[y_down][x]


if __name__ == "__main__":
    data = read_lines_as_text(in_file)
    data.insert(0, "9" * (2 + len(data[0])))
    for idx, d in enumerate(data):
        data[idx] = "9" + d + "9"
    data.extend(["9" * len(data[0])])
    risk = 0
    pts = []
    for j in range(1, len(data) - 1):
        for i in range(1, len(data[0]) - 3):
            row = get_row(data, i, j)
            col = get_col(data, i, j)
            if row[1] < row[0] and row[1] < row[2] and col[1] < col[0] and col[1] < col[2]:
                pts.append([i - 1, j - 1])
                risk += int(row[1]) + 1
    print("09-1", risk)
    print("pts", pts)
