"""
Reusable helper functions for Advent of Code
keiche
"""
from typing import Union

import networkx as nx


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

    @staticmethod
    def initialize_file(filename, integers: bool = False) -> list[list[str]]:
        grid = []
        with open(filename, "r") as f:
            for line in f:
                if integers:
                    grid.append([int(x) for x in line.strip()])
                else:
                    grid.append([x for x in line.strip()])
        return grid

    def initialize_empty(self, height: int, width: int, character: str = ".") -> list[list[str]]:
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
                    if 0 <= acy < self.height and 0 <= acx < self.width and self.grid[acy][acx] in characters:
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

        up = (-1, 0)
        down = (1, 0)
        left = (0, -1)
        right = (0, 1)
        turn_options = {
            right: [up, down],
            left: [up, down],
            up: [left, right],
            down: [left, right],
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
