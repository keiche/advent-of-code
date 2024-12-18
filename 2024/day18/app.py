#!/usr/local/env python3
"""
https://adventofcode.com/2024/day/18
keiche
"""

import sys

import networkx as nx

from aoc_utils import Grid


def main():
    # Config
    dimensions_max = 71
    filename = "input.txt"
    steps = 1024
    if "-t" in sys.argv[1:]:
        dimensions_max = 7
        filename = "test.txt"
        steps = 12

    # Input
    grid = Grid()
    grid.initialize_empty(dimensions_max, dimensions_max)
    input_pairs = []
    with open(filename, "r") as f:
        for line in f:
            x, y = map(int, line.strip().split(","))
            input_pairs.append((x, y))

    # Part 1 - specific steps
    for i, (x, y) in enumerate(input_pairs):
        if i >= steps:
            break
        grid.update_cell(y=y, x=x, value="#")

    start = (0, 0)
    end = (dimensions_max - 1, dimensions_max - 1)
    graph = grid.create_cardinal_graph(["."])
    path = nx.shortest_path(graph, start, end)
    print(f"Part 1: {len(path) - 1}")

    # Part 2 - when does it break
    for x, y in input_pairs[steps:]:
        grid.update_cell(y=y, x=x, value="#")
        graph = grid.create_cardinal_graph(["."])
        fail_cell = (x, y)
        try:
            nx.shortest_path(graph, start, end)
        except nx.exception.NetworkXNoPath:
            print(f"Part 2: {fail_cell[0]},{fail_cell[1]}")
            break


if __name__ == "__main__":
    main()
