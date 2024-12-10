#!/usr/local/env python3
"""
https://adventofcode.com/2024/day/10
keiche
"""

import networkx as nx
from itertools import product


def build_graph(grid: list[list[int]]) -> nx.Graph:
    height = len(grid)
    width = len(grid[0])
    # DiGraph to ensure we only go "up" in slope
    G = nx.DiGraph()
    for y in range(height):
        for x in range(width):
            value = grid[y][x]
            G.add_node((y, x), value=value)
            # Up, Down, Left, Right
            for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                # Check bounds
                if 0 <= y + d[0] < height and 0 <= x + d[1] < width:
                    next_value = grid[y + d[0]][x + d[1]]
                    # Check slope (only rising by 1)
                    if next_value - value == 1:
                        G.add_edge((y, x), (y + d[0], x + d[1]))
    return G


def main():
    grid = []
    with open("input.txt", "r") as f:
        for y, line in enumerate(f):
            int_line = list(map(int, line.strip()))
            grid.append(int_line)

    G = build_graph(grid)
    trail_heads = [n for n, d in G.nodes(data=True) if d["value"] == 0]
    trail_ends = [n for n, d in G.nodes(data=True) if d["value"] == 9]

    # Analyze graph
    all_paths = []
    for start, end in list(product(trail_heads, trail_ends)):
        paths = list(nx.all_simple_paths(G, start, end))
        all_paths.extend(paths)
    # Unique starting / ending locations
    unique_start_end = set([(p[0], p[-1]) for p in all_paths])

    print(f"Part 1: {len(unique_start_end)}")
    print(f"Part 2: {len(all_paths)}")


if __name__ == "__main__":
    main()
