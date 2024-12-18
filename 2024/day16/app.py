#!/usr/local/env python3
"""
https://adventofcode.com/2024/day/16
keiche
"""

import networkx as nx

from aoc_utils import Grid


def calculate_score(grid: Grid, path: list[tuple[int, int]]) -> int:
    """Built-in weighted length function may just do this"""
    facing = (0, 1)  # Always start facing east
    score = 0

    dir_map = {(0, 1): ">", (0, -1): "<", (-1, 0): "^", (1, 0): "v"}

    # First step
    step = path[0]
    for next_step in path[1:]:
        sy, sx, _ = step
        nsy, nsx, _ = next_step
        # Step taken - add to score
        score += 1
        # Check facing
        if (nsy - sy, nsx - sx) != facing:
            # Turn! Impose penalty
            score += 1000
            facing = (nsy - sy, nsx - sx)
            grid.grid[sy][sx] = "T"
        else:
            grid.grid[sy][sx] = dir_map[facing]
        step = next_step
    grid.print_grid_str()
    return score


def main():
    facing = (0, 1)
    grid = Grid("input.txt")
    graph = grid.create_weighted_graph([".", "S", "E"])

    start = grid.find_character("S")
    end = grid.find_character("E")

    path = nx.dijkstra_path(graph, (start[0], start[1], facing), (end[0], end[1], (0, 1)))
    part1_total = calculate_score(grid, path)
    print(f"Part 1: {part1_total}")

    paths = nx.all_shortest_paths(graph, (start[0], start[1], facing), (end[0], end[1], (0, 1)), weight="weight")
    unique_visited = set([(y, x) for path in paths for y, x, _ in path])
    print(f"Part 2: {len(unique_visited)}")


if __name__ == "__main__":
    main()
