#!/usr/local/env python3
"""
https://adventofcode.com/2024/day/6
keiche
"""

from copy import deepcopy
from typing import Union

grid = []
locations = set()
facing = "up"
directions = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}
next_dir = {"up": "right", "right": "down", "down": "left", "left": "up"}
symbols = {"up": "^", "right": ">", "down": "v", "left": "<"}


def move_guard(curr: tuple[int, int]) -> Union[tuple[int, int], None]:
    global facing
    move_dir = directions[facing]
    next_cell = (curr[0] + move_dir[0], curr[1] + move_dir[1])
    # Move would be out of bounds
    if next_cell[0] > len(grid) - 1 or next_cell[0] < 0 or next_cell[1] > len(grid[0]) - 1 or next_cell[1] < 0:
        return None
    # Hit a wall - turn 90
    if grid[next_cell[0]][next_cell[1]] in ("#", "O"):
        facing = next_dir[facing]
        grid[curr[0]][curr[1]] = symbols[facing]
        return curr

    # No wall - move
    # Update grid
    grid[curr[0]][curr[1]] = "X"
    grid[next_cell[0]][next_cell[1]] = symbols[facing]
    # Update location
    locations.add(next_cell)
    return next_cell


def check_looping(starting: tuple[int, int], obstacle: tuple[int, int]) -> bool:
    position = starting
    part2_location = set()  # y, x, dir

    # Set obstacle
    grid[obstacle[0]][obstacle[1]] = "O"

    while True:
        # Guard left map - no cycle
        if not (position := move_guard(position)):
            return False
        # Next move received
        if position and isinstance(position, tuple):
            new_location = (position[0], position[1], facing)
            # Guard hit the same location/direction - cycle
            if new_location in part2_location:
                return True
            part2_location.add(new_location)
        # print_grid()


def print_grid():
    for y in grid:
        print("".join(y))
    print("")


def main():
    global grid
    global facing
    global locations
    position = (0, 0)
    starting = (0, 0)
    obstacle_possibilities = []

    with open("input.txt", "r") as f:
        for i, line in enumerate(f):
            cells = [x for x in line.strip()]
            grid.append(cells)
            if "^" in cells:
                # Starting position
                position = (i, cells.index("^"))
                starting = position
                locations.add(position)
            # Part 2 - get open cells
            open_cells = [(i, j) for j, cell in enumerate(cells) if cell == "."]
            obstacle_possibilities.extend(open_cells)

    # Set a clean copy aside for part 2
    og_grid = deepcopy(grid)

    # Part 1
    guard_on_map = True
    while guard_on_map:
        if not (position := move_guard(position)):
            guard_on_map = False
        # print_grid()

    print(f"Part 1: {len(locations)}")

    # Part 2
    part2_total = 0
    for obstacle in obstacle_possibilities:
        # Reset grid
        grid = deepcopy(og_grid)
        facing = "up"
        locations = set()

        # Check for loop
        if check_looping(starting, obstacle):
            part2_total += 1

    print(f"Part 2: {part2_total}")


if __name__ == "__main__":
    main()
