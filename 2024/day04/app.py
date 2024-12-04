#!/usr/local/env python3
"""
https://adventofcode.com/2024/day/4
keiche
"""

puzzle = []
height = 0
width = 0


def check_xmas(y: int, x: int) -> int:
    word_count = 0
    # Each direction multiplier coords
    for coord in [
        # Diagonals
        (-1, -1), (-1, 1), (1, 1), (1, -1),
        # Cardinal
        (0, 1), (0, -1), (1, 0), (-1, 0),
    ]:
        if 0 <= y + coord[0] * 3 < height and 0 <= x + coord[1] * 3 < width:
            word = "".join(
                [
                    puzzle[y][x],
                    puzzle[y + coord[0]][x + coord[1]],
                    puzzle[y + coord[0] * 2][x + coord[1] * 2],
                    puzzle[y + coord[0] * 3][x + coord[1] * 3],
                ]
            )
            if word == "XMAS":
                word_count += 1
    return word_count


def check_mas(y: int, x: int) -> int:
    word_count = 0
    # Diagonals only
    for coord in [(-1, -1), (-1, 1), (1, 1), (1, -1)]:
        if (
            0 <= y + coord[0] < height
            and 0 <= y - coord[0] < height
            and 0 <= x + coord[1] < width
            and 0 <= x - coord[1] < width
        ):
            word = "".join(
                [
                    puzzle[y + coord[0]][x + coord[1]],
                    puzzle[y][x],
                    puzzle[y - coord[0]][x - coord[1]],
                ]
            )
            if word == "MAS":
                word_count += 1
    if word_count >= 2:
        return 1
    return 0


def main():
    part1_total = 0
    part2_total = 0

    with open("input.txt", "r") as f:
        for line in f.readlines():
            puzzle.append([c for c in line.strip()])

    global height
    global width
    height = len(puzzle)
    width = len(puzzle[0])

    for y in range(height):
        for x in range(width):
            if puzzle[y][x] == "X":
                part1_total += check_xmas(y, x)
            if puzzle[y][x] == "A":
                part2_total += check_mas(y, x)

    print(f"Part 1: {part1_total}")
    print(f"Part 2: {part2_total}")


if __name__ == "__main__":
    main()
