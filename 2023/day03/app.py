#!/usr/local/env python3
"""
https://adventofcode.com/2023/day/2
keiche
"""

grid = []
part1_total = 0


def check(y_idx: int, x_idx_start: int, x_idx_end: int) -> bool:
    min_y = y_idx - 1 if not y_idx - 1 < 0 else 0
    max_y = y_idx + 1 if not y_idx + 1 > len(grid) - 1 else len(grid) - 1

    min_x = x_idx_start - 1 if not x_idx_start - 1 < 0 else 0
    max_x = x_idx_end + 1 if not x_idx_end + 1 > len(grid[0]) + 1 else len(grid[0]) + 1

    for line in grid[min_y:max_y + 1]:
        for cell in line[min_x:max_x + 1]:
            if not cell.isdigit() and cell != ".":
                return True
    return False


with open("input.txt", "r") as f:
    for line in f.readlines():
        grid.append(line.rstrip())

for y, line in enumerate(grid):
    cell_idx_start = 0
    cell_idx_end = 0
    number = ""
    for x, cell in enumerate(line):
        if cell.isdigit():
            if not number:
                cell_idx_start = x
            number += cell
        # Cell isn't a digit, or it's the end of the row - time to count it!
        if number and (not cell.isdigit() or x + 1 == len(line)):
            cell_idx_end = x - 1
            if check(y, cell_idx_start, cell_idx_end):
                part1_total += int(number)
                print(number)
            number = ""

print(f"Part 1: {part1_total}")
