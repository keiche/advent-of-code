#!/usr/local/env python3
"""
https://adventofcode.com/2024/day/20
keiche
"""

import networkx as nx

from aoc_utils import Grid


def manhattan_distance(node1: tuple[int, int], node2: tuple[int, int]) -> int:
    n1y, n1x = node1
    n2y, n2x = node2
    return abs(n1x - n2x) + abs(n1y - n2y)


def find_cheats(path: list[tuple[int, int]], cheat_len: int = 2, min_time_saved: int = 100) -> int:
    savings_count = {}
    for node in path:
        for node2 in path:
            if node == node2:
                continue
            distance = manhattan_distance(node, node2)
            if distance <= cheat_len:
                time_saved = abs(path.index(node) - path.index(node2)) - distance
                if time_saved >= min_time_saved:
                    if time_saved not in savings_count:
                        savings_count[time_saved] = set()
                    # Shenanigans to make sure the start end is unique, no matter the ordering
                    savings_count[time_saved].add(",".join(sorted([str(node), str(node2)])))

    return sum([len(v) for k, v in sorted(savings_count.items())])


def main():
    grid = Grid(filename="input.txt")
    graph = grid.create_cardinal_graph(["S", "E", "."])
    start = grid.find_character("S")
    end = grid.find_character("E")

    path = nx.shortest_path(graph, start, end)
    part1_total = find_cheats(path, cheat_len=2, min_time_saved=100)
    part2_total = find_cheats(path, cheat_len=20, min_time_saved=100)

    print(f"Part 1: {part1_total}")
    print(f"Part 2: {part2_total}")


if __name__ == "__main__":
    main()
