"""
https://adventofcode.com/2025/day/7
keiche
"""

from aoc_utils import Grid


def main():
    part1_total = 0
    part2_total = 0

    g = Grid()
    g.initialize_file("input.txt")

    # Part 1
    for y in range(1, g.height):
        for x in range(g.width):
            current_cell = g.grid[y][x]
            above_cell = g.grid[y - 1][x]
            # Tachyon beam continues down
            if above_cell in ["S", "|"]:
                if current_cell == ".":
                    g.update_cell(y, x, "|")
                # Tachyon beam splits left and right
                elif current_cell == "^":
                    g.update_cell(y, x - 1, "|")
                    g.update_cell(y, x + 1, "|")
                    part1_total += 1

    g.print_grid_str()

    # Part 2 - start with completed beam paths from Part 1
    # At this point there's only one beam / timeline
    path_counts = {g.find_character("S")[1]: 1}

    for y in range(1, g.height):
        # Track distinct paths that reached that column
        #   Key = column where the beam is at that row
        #   Value = number of distinct paths that reached that column
        row_counts = {}
        # We're only following the beam paths
        for x, count in path_counts.items():
            cell = g.grid[y][x]
            if cell in [".", "|"]:
                # Tachyon beam continues down
                row_counts[x] = row_counts.get(x, 0) + count
            elif cell == "^":
                # Timeline splits - count the possible paths to each new column
                row_counts[x - 1] = row_counts.get(x - 1, 0) + count
                row_counts[x + 1] = row_counts.get(x + 1, 0) + count
        path_counts = row_counts
    part2_total = sum(path_counts.values())

    print(f"Part 1: {part1_total}")
    print(f"Part 2: {part2_total}")


if __name__ == "__main__":
    main()
