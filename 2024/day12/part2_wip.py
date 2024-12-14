#!/usr/local/env python3
"""
https://adventofcode.com/2024/day/12
keiche
"""

import networkx as nx

cardinal_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
diagonals = [(-1, 1), (1, 1), (1, -1), (-1, -1)]


class Region:
    def __init__(self, symbol: str, nodes: list[tuple[int, int]]):
        self.symbol = symbol
        self.nodes = nodes
        self.perimeter_map = {"up": [], "down": [], "left": [], "right": []}
        self.perimeter_nodes = self.determine_perimeter()
        self.corner_nodes = self.determine_corners()

    @property
    def perimeter(self) -> int:
        return len(self.perimeter_nodes)

    @property
    def area(self) -> int:
        return len(self.nodes)

    @property
    def corners(self) -> int:
        return len(self.corner_nodes)

    def determine_perimeter(self) -> list[tuple[int, int]]:
        perimeter_nodes = []
        for node in self.nodes:
            noy, nox = node
            # Check surrounding area
            for d in cardinal_directions:
                dy, dx = d
                perimeter_node = (noy + dy, nox + dx)
                if perimeter_node not in self.nodes:
                    perimeter_nodes.append(perimeter_node)
        return perimeter_nodes

    def determine_corners(self):
        left = (0, -1)
        right = (0, 1)
        up = (-1, 0)
        down = (1, 0)
        nw = (-1, -1)
        sw = (1, -1)
        ne = (-1, 1)
        se = (1, 1)
        convex_combos = [
            (up, right, ne),
            (right, down, se),
            (down, left, sw),
            (left, up, nw),
        ]
        concave_combos = [
            (left, down, sw),
            (up, left, nw),
            (up, right, ne),
            (down, right, se),
        ]
        min_y = min([y for y, _ in self.perimeter_nodes])
        max_y = max([y for y, _ in self.perimeter_nodes])
        min_x = min([x for _, x in self.perimeter_nodes])
        max_x = max([x for _, x in self.perimeter_nodes])
        concave_corners = []
        convex_corners = []
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                # Convex
                if (y, x) not in self.nodes:
                    for cc in convex_combos:
                        cc1, cc2, cc3 = cc
                        cc1y, cc1x = cc1
                        cc2y, cc2x = cc2
                        cc3y, cc3x = cc3
                        if (
                            (y + cc1y, x + cc1x) in self.perimeter_nodes
                            and (y + cc2y, x + cc2x) in self.perimeter_nodes
                            and (y + cc3y, x + cc3x) in self.nodes
                        ):
                            convex_corners.append((y, x))

                # Concave
                if (y, x) in self.perimeter_nodes:
                    for cc in concave_combos:
                        cc1, cc2, cc3 = cc
                        cc1y, cc1x = cc1
                        cc2y, cc2x = cc2
                        cc3y, cc3x = cc3
                        if (
                            (y + cc1y, x + cc1x) in self.nodes
                            and (y + cc2y, x + cc2x) in self.nodes
                            and (y + cc3y, x + cc3x) in self.nodes
                        ):
                            concave_corners.append((y, x))

        # print(f"concave: {concave_corners}")
        # print(f"convex: {convex_corners}")
        return concave_corners + convex_corners


def build_region_map(grid) -> list[Region]:
    # Combine symbols into specific regions
    tmp_regions = {}
    regions = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            value = grid[y][x]
            if value not in tmp_regions:
                tmp_regions[value] = []
            tmp_regions[value].append((y, x))

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
    part2_total = 0
    regions = build_region_map(grid)
    for r in regions:
        part1_total += r.perimeter * r.area
        part2_total += r.corners * r.area

    print(f"Part 1: {part1_total}")
    print(f"Part 2: {part2_total}")


if __name__ == "__main__":
    main()
