#!/usr/local/env python3
"""
https://adventofcode.com/2024/day/12
keiche
"""

import networkx as nx

cardinal_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class Region:
    def __init__(self, symbol: str, nodes: list[tuple[int, int]]):
        self.symbol = symbol
        self.nodes = nodes

    def calculate_perimeter(self) -> int:
        perimeter_nodes = []
        for node in self.nodes:
            ny, nx = node
            # Surrounding area
            for d in cardinal_directions:
                dy, dx = d
                perimeter_node = (ny + dy, nx + dx)
                if perimeter_node not in self.nodes:
                    perimeter_nodes.append(perimeter_node)

        return len(perimeter_nodes)

    def calculate_area(self) -> int:
        return len(self.nodes)


def build_region_map(grid) -> list[Region]:
    # Combine symbols into specific regions
    tmp_regions = {}
    regions = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            value = grid[y][x]
            if value not in tmp_regions:
                tmp_regions[value] = []
            tmp_regions[value].append((x, y))

    # Create graphs for each symbol region
    for tr, nodes in tmp_regions.items():
        G = nx.Graph()
        G.add_nodes_from(nodes)
        # Add edges between all touching nodes
        for gn in G.nodes():
            gny, gnx = gn
            for node in nodes:
                for dy, dx in cardinal_directions:
                    if (gny + dy, gnx + dx) == node:
                        G.add_edge(gn, node)

        # Split the graph into connected regions using edges
        for component in nx.connected_components(G):
            regions.append(Region(tr, list(component)))

    return regions


def main():
    grid = []
    with open("input.txt", "r") as f:
        for line in f:
            grid.append(list(line.strip()))

    part1_total = 0
    regions = build_region_map(grid)
    for r in regions:
        part1_total += r.calculate_perimeter() * r.calculate_area()

    print(f"Part 1: {part1_total}")


if __name__ == "__main__":
    main()
