"""
https://adventofcode.com/2025/day/9
keiche
"""

# lol easy mode
from shapely.geometry import Polygon


def get_area(tile1: tuple[int, int], tile2: tuple[int, int]) -> int:
    # Add 1 to include the edges
    return (abs(tile1[0] - tile2[0]) + 1) * (abs(tile1[1] - tile2[1]) + 1)


def get_sorted_areas(red_tiles: list[tuple[int, int]]) -> list[tuple[int, int, int]]:
    areas = []
    for tile1 in red_tiles:
        for tile2 in red_tiles:
            if tile1 != tile2:
                area = get_area(tile1, tile2)
                areas.append((area, tile1, tile2))
    return list(reversed(sorted(areas, key=lambda x: x[0])))


def get_max_area(red_tiles: list[tuple[int, int]]) -> int:
    areas = []
    for tile1 in red_tiles:
        for tile2 in red_tiles:
            if tile1 != tile2:
                area = get_area(tile1, tile2)
                areas.append(area)
    return max(areas)


def print_grid(red_tiles: list[tuple[int, int]], green_tiles: list[tuple[int, int]]) -> None:
    max_x = max(tile[0] for tile in red_tiles) + 2
    max_y = max(tile[1] for tile in red_tiles) + 2
    grid = [["." for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for tile in red_tiles:
        if grid[tile[1]][tile[0]] == ".":
            grid[tile[1]][tile[0]] = "#"
    for tile in green_tiles:
        if grid[tile[1]][tile[0]] == ".":
            grid[tile[1]][tile[0]] = "X"
    for row in grid:
        print("".join(row))


def main():
    part1_total = 0
    part2_total = 0

    # Input
    red_tiles = []
    with open("input.txt", "r") as f:
        for line in f:
            red_tiles.append(tuple(map(int, line.strip().split(","))))

    # Part 1
    part1_total = get_max_area(red_tiles)

    # Part 2
    sorted_areas = get_sorted_areas(red_tiles)
    polygon = Polygon(red_tiles)
    # Check for the largest area that is contained by the red tile polygon
    for area, tile1, tile2 in sorted_areas:
        y1, x1 = tile1
        y2, x2 = tile2
        rectangle = Polygon([(y1, x1), (y1, x2), (y2, x2), (y2, x1)])
        if polygon.contains(rectangle):
            part2_total = area
            break

    print(f"Part 1: {part1_total}")
    print(f"Part 2: {part2_total}")


if __name__ == "__main__":
    main()
