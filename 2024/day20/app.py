#!/usr/local/env python3
"""
https://adventofcode.com/2024/day/20
keiche
"""
from copy import deepcopy
from typing import Union

import networkx as nx

from aoc_utils import Grid


def find_cheat_path(
    node1: tuple[int, int], node2: tuple[int, int], cheat_len: int = 2
) -> Union[set[tuple[int, int]], None]:
    """Find cheat path from node1 to node2. Only useful for Part 1"""
    y1, x1 = node1
    y2, x2 = node2

    # Check vertical
    if 1 <= abs(y2 - y1) <= cheat_len and x2 == x1:
        step = 1 if (dist := y2 - y1) > 0 else -1
        cheat_paths = set()
        for i in range(0, dist, step):
            cheat_path = (y1 + i, x1)
            if cheat_path != node1 and cheat_path != node2:
                cheat_paths.add(cheat_path)
        return cheat_paths

    # Check horizontal
    if 1 <= abs(x2 - x1) <= cheat_len and y2 == y1:
        step = 1 if (dist := x2 - x1) > 0 else -1
        cheat_paths = set()
        for i in range(0, dist, step):
            cheat_path = (y1, x1 + i)
            if cheat_path != node1 and cheat_path != node2:
                cheat_paths.add(cheat_path)
        return cheat_paths

    return None


def find_all_cheats(grid: Grid, path: list[tuple[int, int]], cheat_len: int = 2) -> list[set[tuple[int, int]]]:
    """See if a position is within X cells of the path, and contains a wall"""
    all_cheats = []
    for node in path:
        for node2 in path:
            # Skip if the same node
            if node == node2:
                continue
            if cheats := find_cheat_path(node, node2, cheat_len):
                # Ensure the path at least has 1 wall... otherwise it's not really cheating
                if any([True for cy, cx in cheats if grid.grid[cy][cx] == "#"]):
                    # Unique
                    if cheats not in all_cheats:
                        all_cheats.append(cheats)

    return all_cheats


def activate_cheat(grid: Grid, start: tuple[int, int], end: tuple[int, int], cheat: set[tuple[int, int]]) -> int:
    """Add the cheat and return the new total path length"""
    # Make a new grid / graph with the cheat activated
    new_grid = deepcopy(grid)
    cheat_nums = []
    for i, (y, x) in enumerate(cheat):
        new_grid.grid[y][x] = "."
        cheat_nums.append(i)
    new_graph = new_grid.create_cardinal_graph(["S", "E", "."] + cheat_nums)
    new_path = nx.shortest_path(new_graph, start, end)
    # Don't count the starting node in the total time / length
    return len(new_path) - 1


def main():
    grid = Grid(filename="input.txt")
    graph = grid.create_cardinal_graph(["S", "E", "."])
    start = grid.find_character("S")
    end = grid.find_character("E")

    path = nx.shortest_path(graph, start, end)
    # Don't count the starting node in the total time / length
    original_time = len(path) - 1
    # Use the fastest path as the starting point for inserting cheats
    possible_cheats = find_all_cheats(grid, path, 2)

    part1_total = 0
    for cheat in possible_cheats:
        # Make a new grid / graph with the cheat activated
        new_time = activate_cheat(grid, start, end, cheat)
        time_saved = original_time - new_time
        if time_saved >= 100:
            part1_total += 1
        print(f"Path length: {new_time}, Time Saved: {time_saved}, Cheat: {cheat}")

    print(f"Part 1: {part1_total}")


if __name__ == "__main__":
    main()
