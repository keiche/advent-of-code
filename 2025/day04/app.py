"""
https://adventofcode.com/2025/day/4
keiche
"""

from aoc_utils import Grid


def main():
    part1_total = 0
    part2_total = 0

    grid = Grid()
    grid.initialize_file("input.txt")

    part1_check = True
    while True:
        cells_to_remove = []
        for y in range(grid.height):
            for x in range(grid.width):
                if grid.grid[y][x] == "@":
                    surrounding_cells = grid.get_surrounding_cell_values(y, x)
                    if len([x for x in surrounding_cells if x == "@"]) < 4:
                        if part1_check:
                            part1_total += 1
                        part2_total += 1
                        cells_to_remove.append((y, x))

        # Only need the first pass for part 1
        part1_check = False

        # Remove cells
        for y, x in cells_to_remove:
            grid.update_cell(y, x, "x")

        # Check if there are no more cells to remove
        if not cells_to_remove:
            break

    print(f"Part 1: {part1_total}")
    print(f"Part 2: {part2_total}")


if __name__ == "__main__":
    main()
