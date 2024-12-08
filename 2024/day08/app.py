#!/usr/local/env python3
"""
https://adventofcode.com/2024/day/8
keiche
"""

from itertools import combinations

grid = []
nodes = {}
all_antinodes = set()
width = 0
height = 0


def print_grid():
    for y in range(len(grid)):
        print("".join(grid[y]))


def check_bounds(coords: tuple[int, int]) -> bool:
    if 0 <= coords[0] < height and 0 <= coords[1] < width:
        return True
    return False


def find_antinodes(node_list: list[str], name: str, repeat: bool = False) -> int:
    antinode_count = 0
    all_other_nodes = [v2 for k, v in nodes.items() for v2 in nodes if k != name]

    # Part 2 - include the nodes themselves if not already counted
    if repeat:
        if len(node_list) > 1:
            for n in node_list:
                if n not in all_antinodes:
                    antinode_count += 1
            all_antinodes.update(node_list)

    # Part 1 & 2 - loop through all node pair combos
    for pair in combinations(node_list, 2):
        count = 1
        keep_looping = True
        while keep_looping:
            y_dist = (pair[1][0] * count) - (pair[0][0] * count)
            x_dist = (pair[1][1] * count) - (pair[0][1] * count)

            antinode_1 = (pair[0][0] - y_dist, pair[0][1] - x_dist)
            antinode_2 = (pair[1][0] + y_dist, pair[1][1] + x_dist)
            out_of_bounds = 0
            for an in [antinode_1, antinode_2]:
                if check_bounds(an):
                    if an not in all_other_nodes and an not in all_antinodes:
                        antinode_count += 1
                        grid[an[0]][an[1]] = "#"
                        all_antinodes.add(an)
                else:
                    out_of_bounds += 1
            # print(pair, y_dist, x_dist, antinode_1, antinode_2, antinode_count, out_of_bounds)

            # Part 1 only needs to run once (no resonant harmonics)
            if not repeat:
                keep_looping = False
            # Part 2 - both points are out of bounds, no more harmonics to check
            if out_of_bounds == 2:
                keep_looping = False
            count += 1
    return antinode_count


def main():
    global width
    global height
    global all_antinodes
    # Input
    with open("input.txt", "r") as f:
        for y, line in enumerate(f):
            line = line.strip()
            # Build the grid
            grid.append(list(line))
            # Capture all nodes
            for x, c in enumerate(line):
                if c != ".":
                    if c not in nodes:
                        nodes[c] = []
                    nodes[c].append((y, x))

    width = len(grid[0])
    height = len(grid)

    part1_total = 0
    for node_name, node_list in nodes.items():
        part1_total += find_antinodes(node_list, node_name)

    part2_total = 0
    all_antinodes = set()
    for node_name, node_list in nodes.items():
        part2_total += find_antinodes(node_list, node_name, repeat=True)

    # print_grid()
    print(f"Part 1: {part1_total}")
    print(f"Part 2: {part2_total}")


if __name__ == "__main__":
    main()
