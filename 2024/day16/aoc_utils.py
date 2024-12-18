from typing import Union

import networkx as nx


class Grid:
    def __init__(self, filename: str, integers: bool = False):
        # Grid
        self.grid = self.initialize(filename, integers)

        # Directions
        self.cardinal_directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]  # u, d, l, r
        self.diagonal_directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]  # se, sw, ne, nw
        self.all_directions = self.cardinal_directions + self.diagonal_directions

    @property
    def height(self) -> int:
        return len(self.grid)

    @property
    def width(self) -> int:
        return len(self.grid[0])

    @staticmethod
    def initialize(filename, integers: bool = False) -> list[list[str]]:
        grid = []
        with open(filename, "r") as f:
            for line in f:
                if integers:
                    grid.append([int(x) for x in line.strip()])
                else:
                    grid.append([x for x in line.strip()])
        return grid

    def print_grid_str(self):
        for row in self.grid:
            print("".join(row))

    def print_grid(self):
        for row in self.grid:
            print(row)

    def create_cardinal_graph(self, characters: list[str]):
        """
        Create a graph of nodes and edges with exact characters (no node weight)
        """
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

    def create_weighted_graph(self, characters: list[str]):
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
