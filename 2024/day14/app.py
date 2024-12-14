#!/usr/local/env python3
"""
https://adventofcode.com/2024/day/14
keiche
"""

import sys
from copy import deepcopy
from math import prod
from os import mkdir

import matplotlib.pyplot as plt
import numpy as np

height = 0
width = 0


class Robot:
    def __init__(self, position: tuple[int, int], velocity: tuple[int, int]):
        self.px, self.py = position
        self.vx, self.vy = velocity

    def move(self):
        self.px += self.vx
        if self.px < 0:
            self.px += width
        elif self.px >= width:
            self.px -= width

        self.py += self.vy
        if self.py < 0:
            self.py += height
        elif self.py >= height:
            self.py -= height


def build_grid(robots: list[Robot]) -> list[list[int]]:
    grid = []
    for y in range(height):
        row = []
        for x in range(width):
            if robot_count := sum([1 for r in robots if (y, x) == (r.py, r.px)]):
                row.append(robot_count)
            else:
                row.append(0)
        grid.append(row)
    return grid


def possible_easter_egg(robots: list[Robot], long_chain_size: int = 10) -> bool:
    """Look for long chains of digits"""
    for y in range(height):
        row = []
        for x in range(width):
            if any([True for r in robots if (y, x) == (r.py, r.px)]):
                row.append("#")
            else:
                row.append(".")
        if "".join(["#" for _ in range(long_chain_size)]) in "".join(row):
            return True
    return False


def print_grid(grid: list[list[str]]) -> None:
    for y in grid:
        print("".join(list(map(str, y))))
    print()


def determine_quadrant(y, x) -> int:
    # Quadrant numbering
    # 0 1
    # 2 3
    if y > int(height / 2):
        if x > int(width / 2):
            return 3
        return 2
    if x > int(width / 2):
        return 1
    return 0


def count_robot_in_quad(robots: list[Robot]) -> int:
    robot_cells = {0: [], 1: [], 2: [], 3: []}
    for y in range(height):
        for x in range(width):
            # Skip the middle lines
            if y == int(height / 2) or x == int(width / 2):
                continue
            robot_cell = sum([1 for r in robots if (y, x) == (r.py, r.px)])
            if robot_cell:
                robot_quad = determine_quadrant(y, x)
                robot_cells[robot_quad].append(robot_cell)

    return prod([sum(rc) for rc in robot_cells.values()])


def parse_input(filename: str) -> list[Robot]:
    robots = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            position = tuple(map(int, line.split(" ")[0].split("=")[1].split(",")))
            velocity = tuple(map(int, line.split(" ")[1].split("=")[1].split(",")))
            robots.append(Robot(position, velocity))
    return robots


def main():
    global height, width
    is_test = True if "-t" in sys.argv[1:] else False
    height, width = (103, 101) if not is_test else (7, 11)

    # Get input
    filename = "input.txt" if not is_test else "test.txt"
    robots = parse_input(filename)
    original_robots = deepcopy(robots)

    # Part 1
    for i in range(100):
        # Move all the robots
        for r in robots:
            r.move()
    print(f"Part 1: {count_robot_in_quad(robots)}")

    # Part 2
    robots = deepcopy(original_robots)
    # Make output directory
    out_dir = "./images"
    try:
        mkdir(out_dir)
    except FileExistsError:
        pass

    for i in range(10000):
        # Move all the robots
        for r in robots:
            r.move()

        if possible_easter_egg(robots, 10):
            print(f"Possible easter egg: Move {i + 1}")

            # Make image
            np_grid = np.array(build_grid(robots))
            plt.imshow(np_grid, cmap="viridis")
            plt.colorbar()

            # Save image to review output
            plt.savefig(f"{out_dir}/{str(i + 1).zfill(4)}.png")
            plt.clf()
            plt.close()

        if i % 100 == 0:
            print(f"Status update: Move {i}")


if __name__ == "__main__":
    main()
