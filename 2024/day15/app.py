#!/usr/local/env python3
"""
https://adventofcode.com/2024/day/15
keiche
"""

grid = []
move_queue = []
move_map = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


class Robot:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def update_position(self, new_position: tuple[int, int]):
        self.y, self.x = new_position


def parse_input(filename: str) -> tuple[int, int]:
    robot_position = (0, 0)
    switch_input = False
    with open(filename, "r") as f:
        for y, line in enumerate(f):
            row = list(line.strip())
            if not row:
                switch_input = True
                continue

            # Create grid
            if not switch_input:
                grid.append(row)
                # Get starting position
                for x, cell in enumerate(row):
                    if cell == "@":
                        robot_position = (y, x)
            else:
                # Create move queue
                for cell in row:
                    move_queue.append(cell)
    return robot_position


def print_grid():
    for y in grid:
        print("".join(y))


def calculate_gps():
    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "O":
                total += (100 * y) + x
    return total


def main():
    robot = Robot(*parse_input("input.txt"))

    for m in move_queue:
        my, mx = move_map[m]
        next_cell = (robot.y + my, robot.x + mx)
        ncy, ncx = next_cell
        # Wall - do nothing
        if grid[ncy][ncx] == "#":
            continue
        # Empty - just move
        elif grid[ncy][ncx] == ".":
            grid[robot.y][robot.x] = "."
            grid[ncy][ncx] = "@"
            robot.update_position(next_cell)
            continue
        # Box - can we move it
        elif grid[ncy][ncx] == "O":
            next_open_square = None
            check_cell = (ncy, ncx)
            # See if there's a queue of boxes and an open space
            while True:
                check_cell = (check_cell[0] + my, check_cell[1] + mx)
                checky, checkx = check_cell
                # Another box to push
                if grid[checky][checkx] == "O":
                    continue
                # Open space - we can move the queue!
                elif grid[checky][checkx] == ".":
                    next_open_square = (checky, checkx)
                    break
                elif grid[checky][checkx] == "#":
                    break

            if next_open_square:
                # Move the last box
                nosy, nosx = next_open_square
                grid[nosy][nosx] = "O"
                # First box position will now have the robot
                grid[robot.y][robot.x] = "."
                grid[ncy][ncx] = "@"
                robot.update_position(next_cell)
                continue

    print(f"Part 1: {calculate_gps()}")


if __name__ == "__main__":
    main()
