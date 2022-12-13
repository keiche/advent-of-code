#!/usr/bin/env python3
"""https://adventofcode.com/2022/day/12"""

from collections import deque
from copy import deepcopy

grid = []


def translate_letter(letter) -> int:
    """
    Translate the letter into the height
    :param letter: letter
    :return: height number
    """
    if letter == "S":
        letter = "a"
    elif letter == "E":
        letter = "z"
    letters = "abcdefghijklmnopqrstuvwxyz"
    return list(letters).index(letter)


def neighbors(cell: tuple) -> list:
    """
    Find the surrounding cells that have the same or 1 higher height
    :param cell: cell
    :return: cells
    """
    nodes = []

    yi, xi = cell
    v = grid[yi][xi]

    # Check up, down, left, right
    paths = [(yi - 1, xi), (yi + 1, xi), (yi, xi - 1), (yi, xi + 1)]
    for p in paths:
        # Exclude out of bounds
        if p[0] < 0 or p[0] > len(grid) - 1 or p[1] < 0 or p[1] > len(grid[0]) - 1:
            continue
        # Check if any neighbors are the same or one higher
        if grid[p[0]][p[1]] <= v + 1:
            nodes.append(p)

    return nodes


def bfs(root: tuple, finish: tuple) -> int:
    """
    Breadth-First Search
    :param root: Starting position
    :param finish: Ending position
    :return: Number of steps from start to end or -1 if no possible solution
    """
    queue = deque()
    queue.append(root)
    visited = {root: None}
    while queue:
        node = queue.popleft()
        if node == finish:
            break
        for neighbor in neighbors(node):
            if neighbor not in visited:
                # Used to traverse backwards
                visited[neighbor] = node
                queue.append(neighbor)

    # Work backwards to find the shortest path
    curr = deepcopy(finish)
    path = []
    while curr != root:
        path.append(curr)
        try:
            curr = visited[curr]
        # No possible solution
        except KeyError:
            return -1

    return len(path)


def main() -> None:
    global grid
    starting_coord = None
    ending_coord = None
    with open("12.txt", "r") as f:
        for ix, line in enumerate(f.readlines()):
            row = []
            for iy, c in enumerate(line.rstrip()):
                if c == "S":
                    starting_coord = (ix, iy)
                if c == "E":
                    ending_coord = (ix, iy)
                row.append(translate_letter(c))
            grid.append(row)

    # Part 1
    part_1 = bfs(starting_coord, ending_coord)

    # Part 2
    lowest = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            # Only evaluate the lowest height starting spots
            if grid[y][x] == 0:
                result = bfs((y, x), ending_coord)
                if result != -1:
                    lowest.append(result)
    part_2 = sorted(lowest)[0]

    print(f"Part 1: {part_1}")
    print(f"Part 1: {part_2}")


if __name__ == "__main__":
    main()
