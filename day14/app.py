#!/usr/bin/env python3
"""https://adventofcode.com/2022/day/14"""

from copy import deepcopy

grid = []


def print_grid() -> None:
    """Print top of grid (Debugging)"""
    for row in grid[0:32]:
        print("".join(row[450:550]))
    print()


def next_move(y: int, x: int) -> tuple:
    """
    Move the piece of sand
    :param y: current y-coord
    :param x: current x-coord
    :return: updated y and x coords
    """
    solid_space = ["#", "o"]

    d_value = grid[y + 1][x]
    # Nothing below - move down
    if d_value not in solid_space:
        return y + 1, x
    # Something below
    if d_value in solid_space:
        # Try diagonal left
        ld_value = grid[y + 1][x - 1]
        if ld_value not in solid_space:
            return y + 1, x - 1
        # Try diagonal right
        rd_value = grid[y + 1][x + 1]
        if rd_value not in solid_space:
            return y + 1, x + 1
    return y, x


def falling_sand() -> int:
    """Simulate falling sand"""
    sand_units = 0
    while True:
        new_sand = (0, 500)
        sand_resting = False
        while not sand_resting:
            try:
                move = next_move(new_sand[0], new_sand[1])
            except IndexError:
                return sand_units

            # Move
            if move != new_sand:
                new_sand = move
            # Move can't happen - sand is resting
            else:
                # New sand made it all the way to the top - end counting
                if grid[new_sand[0]][new_sand[1]] == "o":
                    return sand_units - 1

                # Sand is resting
                grid[new_sand[0]][new_sand[1]] = "o"
                sand_units += 1
                sand_resting = True


def add_floor(height: int) -> None:
    """Add a floor to the grid (Part 2)"""
    for x in range(len(grid[height])):
        grid[height][x] = "#"


def main() -> None:
    # Initialize grid
    global grid
    # Make a very large grid so that sand doesn't fall off before it reaches the top
    for y in range(200):
        row = []
        for x in range(-1000, 1000):
            row.append("+" if y == 0 and x == 500 else ".")
        grid.append(row)

    lowest_y = 0
    with open("14.txt", "r") as f:
        for line in f.readlines():
            paths = line.rstrip().split(" -> ")
            for i, p in enumerate(paths):
                # Last element already processed
                if i == len(paths) - 1:
                    continue

                # Get the paths
                x1, y1 = p.split(",")
                x2, y2 = paths[i + 1].split(",")
                xs = [int(x1), int(x2)]
                ys = [int(y1), int(y2)]

                # Part 2 - Find the lowest Y (thinking upside down)
                if max(ys) > lowest_y:
                    lowest_y = max(ys)

                # Draw the paths in the grid
                for j in range(min(ys), max(ys) + 1):
                    for k in range(min(xs), max(xs) + 1):
                        grid[j][k] = "#"

    clean_grid = deepcopy(grid)
    part_1 = falling_sand()

    # Part 2
    grid = deepcopy(clean_grid)
    add_floor(lowest_y + 2)
    part_2 = falling_sand()
    print_grid()

    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")


if __name__ == "__main__":
    main()
