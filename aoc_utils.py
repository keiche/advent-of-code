"""
Reusable helper functions for Advent of Code
keiche
"""

from typing import Union

import networkx as nx
from functools import cache


class Grid:
    def __init__(self, filename: str = "", integers: bool = False) -> None:
        # Grid
        self.grid = []
        if filename:
            self.initialize_file(filename, integers)

        # Directions
        self.up = (-1, 0)
        self.down = (1, 0)
        self.left = (0, -1)
        self.right = (0, 1)
        self.nw = (-1, -1)
        self.sw = (1, -1)
        self.ne = (-1, 1)
        self.se = (1, 1)
        self.cardinal_directions = [self.up, self.down, self.left, self.right]
        self.diagonal_directions = [self.nw, self.sw, self.ne, self.se]
        self.all_directions = self.cardinal_directions + self.diagonal_directions

    @property
    def height(self) -> int:
        return len(self.grid)

    @property
    def width(self) -> int:
        return len(self.grid[0])

    def initialize_file(self, filename, integers: bool = False) -> list[list[str]]:
        grid = []
        with open(filename, "r") as f:
            for line in f:
                if integers:
                    grid.append([int(x) for x in line.strip()])
                else:
                    grid.append([x for x in line.strip()])
        self.grid = grid
        return grid

    def initialize_empty(
        self, height: int, width: int, character: str = "."
    ) -> list[list[str]]:
        grid = []
        for y in range(height):
            grid.append([character for _ in range(width)])
        self.grid = grid
        return grid

    def update_cell(self, y: int, x: int, value: str = ".") -> None:
        self.grid[y][x] = value

    def print_grid_str(self) -> None:
        for row in self.grid:
            print("".join(row))

    def print_grid(self) -> None:
        for row in self.grid:
            print(row)

    def create_cardinal_graph(self, characters: list[str]) -> nx.Graph:
        """Create a graph of nodes and edges with exact characters (no node weight)"""
        G = nx.Graph()
        for y in range(self.height):
            for x in range(self.width):
                v = self.grid[y][x]
                if v not in characters:
                    continue
                node = (y, x)
                G.add_node(node)
                for d in self.cardinal_directions:
                    dy, dx = d
                    adjacent_cell = (y + dy, x + dx)
                    acy, acx = adjacent_cell
                    if (
                        0 <= acy < self.height
                        and 0 <= acx < self.width
                        and self.grid[acy][acx] in characters
                    ):
                        G.add_edge(node, adjacent_cell)

        return G

    def find_character(self, character: Union[str, int]) -> tuple[int, int]:
        """
        Find first instance of a character in grid
        Useful for finding start / end locations
        """
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == character:
                    return y, x
        raise ValueError(f"No such character: {character}")

    def create_weighted_graph(self, characters: list[str]) -> nx.DiGraph:
        """
        2024 Day 16
        Create a graph of nodes and edges with exact characters - weights are when there are multiple options
        """
        G = nx.DiGraph()

        turn_options = {
            self.right: [self.up, self.down],
            self.left: [self.up, self.down],
            self.up: [self.left, self.right],
            self.down: [self.left, self.right],
        }

        for y in range(self.height):
            for x in range(self.width):
                # Make sure this is not a wall
                if self.grid[y][x] not in characters:
                    continue
                # Direction we're checking
                for d in self.cardinal_directions:
                    dy, dx = d
                    G.add_node((y, x, d))
                    # Make sure this not a wall
                    if 0 <= y + dy < self.height and 0 <= x + dx < self.width:
                        if self.grid[y + dy][x + dx] in characters:
                            G.add_edge((y, x, d), (y + dy, x + dx, d), weight=1)

                    # Turn direction
                    for od in turn_options[d]:
                        ody, odx = od
                        if 0 <= y + ody < self.height and 0 <= x + odx < self.width:
                            # Make sure this not a wall
                            if not self.grid[y + ody][x + odx] in characters:
                                continue
                            G.add_edge((y, x, d), (y + ody, x + odx, od), weight=1000)

        return G

    def get_surrounding_cell_values(self, y: int, x: int) -> list[str]:
        """Get the values of the surrounding cells"""
        values = []
        for dy, dx in self.all_directions:
            if 0 <= y + dy < self.height and 0 <= x + dx < self.width:
                values.append(self.grid[y + dy][x + dx])
        return values


class DirectedGraph:
    def __init__(self, filename: str = "input.txt"):
        self.graph = nx.DiGraph()
        self._successors = {}

    def parse_file(self, filename: str = "input.txt"):
        """Assuming each line is 'node: edge1 edge2 ...'"""
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                node, edges = line.split(":")
                self.graph.add_node(node)
                for edge in edges.strip().split(" "):
                    self.graph.add_edge(node, edge)
        # Pre-compute successors as tuples for caching
        self._successors = {node: tuple(self.graph.successors(node)) for node in self.graph.nodes()}

    def find_all_paths(self, start: str, end: str) -> list[list[str]]:
        """Find all simple paths from start to end - not cached"""
        return list(nx.all_simple_paths(self.graph, start, end))

    @cache
    def count_paths(self, start: str, end: str) -> int:
        """Count all simple paths from start to end using memoized DFS"""
        if start == end:
            return 1
        
        total = 0
        for neighbor in self._successors.get(start, ()):
            total += self.count_paths(neighbor, end)
        return total


def manhattan_distance(node1: tuple[int, int], node2: tuple[int, int]) -> int:
    n1y, n1x = node1
    n2y, n2x = node2
    return abs(n1x - n2x) + abs(n1y - n2y)
