import sys
from copy import deepcopy
sys.path.append("..\\")
from aoc21.utils import read_lines_as_text

TESTING = False

if TESTING:
    in_file = "12/test_input.txt"
else:
    in_file = "12/input.txt"


class AllPaths:
    def __init__(self):
        self.paths = []
        self.final = []

    def append(self, item):
        self.paths.append(item)


all_paths = AllPaths()


def walk(current_node, walked_path, mapping):
    walked_path.append(current_node)
    if current_node == "end":
        global all_paths
        all_paths.append(walked_path)
        return
    if "end" in walked_path:
        return
    next_nodes = mapping[current_node]
    available_nodes = []
    for name in next_nodes:
        if name == name.lower():
            if name not in walked_path:
                available_nodes.append(name)
        else:
            available_nodes.append(name)
    if available_nodes == []:
        return
    for node in available_nodes:
        walked_path_cp = deepcopy(walked_path)
        walk(node, walked_path_cp, mapping)


def generate_mapping(data):
    cave_map = {}
    for d in data:
        if not d[0] in cave_map.keys():
            cave_map[d[0]] = []
        if not d[1] in cave_map.keys():  
            cave_map[d[1]] = []
        cave_map[d[0]].append(d[1])
        cave_map[d[1]].append(d[0])
    cave_map["end"] = []
    return cave_map


if __name__ == "__main__":
    data = read_lines_as_text(in_file)
    data = [i.split("-") for i in data]
    cave_map = generate_mapping(data)

    for node in cave_map["start"]:
        walk(node, ["start"], cave_map)
    print("12-1", len(all_paths.paths))
