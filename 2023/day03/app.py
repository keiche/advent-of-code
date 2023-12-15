#!/usr/local/env python3
"""
https://adventofcode.com/2023/day/3
keiche
"""

grid = []
part1_total = 0

gears = {}
part2_total = 0


def check(y_idx: int, x_idx_start: int, x_idx_end: int) -> bool:
    """
    Part 1 - Check the surroundings of a number for parts

    Args:
        y_idx: y-coordinate of the number
        x_idx_start: x-coordinate of the start of the number
        x_idx_end: x-coordinate of the end of the number

    Returns:
        True if a part is touching the number

    """
    min_y = y_idx - 1 if not y_idx - 1 < 0 else 0
    max_y = y_idx + 1 if not y_idx + 1 > len(grid) - 1 else len(grid) - 1

    min_x = x_idx_start - 1 if not x_idx_start - 1 < 0 else 0
    max_x = x_idx_end + 1 if not x_idx_end + 1 > len(grid[0]) + 1 else len(grid[0]) + 1

    for line in grid[min_y:max_y + 1]:
        for cell in line[min_x:max_x + 1]:
            if not cell.isdigit() and cell != ".":
                return True
    return False


def check_gear(value: int, y_idx: int, x_idx_start: int, x_idx_end: int) -> None:
    """
    Part 2 - take a number and check if a gear exists around it
    Record numbers that are touching a gear
    Save the gear name as the location of the gear, so we can later see when 2 numbers are touching the same gear

    Args:
        y_idx: y-coordinate of the number
        x_idx_start: x-coordinate of the start of the number
        x_idx_end: x-coordinate of the end of the number

    """
    min_y = y_idx - 1 if not y_idx - 1 < 0 else 0
    max_y = y_idx + 1 if not y_idx + 1 > len(grid) - 1 else len(grid) - 1

    min_x = x_idx_start - 1 if not x_idx_start - 1 < 0 else 0
    max_x = x_idx_end + 1 if not x_idx_end + 1 > len(grid[0]) + 1 else len(grid[0]) + 1

    for rel_y, line in enumerate(grid[min_y:max_y + 1]):
        for rel_x, cell in enumerate(line[min_x:max_x + 1]):
            if cell == "*":
                gear_name = f"{min_y - 1 + rel_y}_{min_x - 1 + rel_x}"
                if gear_name not in gears:
                    gears[gear_name] = [value]
                else:
                    gears[gear_name].append(value)


with open("input.txt", "r") as f:
    for line in f.readlines():
        grid.append(line.rstrip())

for y, line in enumerate(grid):
    cell_idx_start = 0
    cell_idx_end = 0
    number = ""
    for x, cell in enumerate(line):
        # Cell is a digit - track it as part of a number
        if cell.isdigit():
            if not number:
                cell_idx_start = x
            number += cell
        # Cell isn't a digit, or it's the end of the row - time to count it!
        if number and (not cell.isdigit() or x + 1 == len(line)):
            # Part 1
            cell_idx_end = x - 1
            if check(y, cell_idx_start, cell_idx_end):
                part1_total += int(number)

            # Part 2
            check_gear(number, y, cell_idx_start, cell_idx_end)

            # Reset tracked number
            number = ""

# Part 2 - get gear ratio if 2 gears are connected
for _, gear in gears.items():
    if len(gear) == 2:
        part2_total += int(gear[0]) * int(gear[1])

print(f"Part 1: {part1_total}")
print(f"Part 2: {part2_total}")
