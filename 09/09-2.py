from utils import read_lines_as_text

TESTING = False

if TESTING:
    in_file = r"D:\aoc21\09\test_input.txt"
else:
    in_file = r"D:\aoc21\09\input.txt"


def get_row(mat, x, y):
    x_left = x-1
    x_right = x + 1
    return mat[y][x_left], mat[y][x], mat[y][x_right]


def get_col(mat, x, y):
    y_up = max(0, y - 1)
    y_down = min(y + 1, len(mat))
    return mat[y_up][x], mat[y][x], mat[y_down][x]

# copied from part 1
def find_low_points(data):
    pts = []
    for j in range(1, len(data) - 1):
        for i in range(1, len(data[0]) - 3):
            row = get_row(data, i, j)
            col = get_col(data, i, j)
            if row[1] < row[0] and row[1] < row[2] and col[1] < col[0] and col[1] < col[2]:
                pts.append([i - 1, j - 1])
    return pts


def walk_basin(mat, x: int, y: int, prev=-1, points=None):
    # every point is part of >exactly< one basin!
    try:
        if prev == -1:
            prev = mat[y][x]
        points = points if points else []
        # found hill
        if mat[y][x] == "9":
            return points

        # i was already here
        if any([x == p[0] and y == p[1] for p in points]):
            return points

        # entering next basin
        if int(prev) > int(mat[y][x]):
            return points

        points.append([x, y])
        walk_basin(mat, x + 1, y, mat[y][x], points)  # go right
        walk_basin(mat, x - 1, y, mat[y][x], points)  # go left
        walk_basin(mat, x, y + 1, mat[y][x], points)  # go down
        walk_basin(mat, x, y - 1, mat[y][x], points)  # go down
        return points

    except IndexError:
        return points


def pad_data(data, value):
    data.insert(0, value * (2 + len(data[0])))
    for idx, d in enumerate(data):
        data[idx] = value + d + value
    data.extend([value * len(data[0])])
    return data


if __name__ == "__main__":
    data = read_lines_as_text(in_file)
    data = pad_data(data, "9")
    pts = find_low_points(data)

    basins = []
    for pt in pts:
        basins.append(
            len(walk_basin(data, pt[0] + 1, pt[1] + 1, -1, None))
        )

    l = sorted(basins, reverse=True)
    print("9-2", l[0] * l[1] * l[2])

