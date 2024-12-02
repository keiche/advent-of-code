#!/usr/local/env python3
"""
https://adventofcode.com/2024/day/2
keiche
"""

from copy import deepcopy


def check_safe(levels: list) -> bool:
    """Check for safe levels"""
    direction = None
    prev_dir = None
    prev_level = 0
    safe = True
    for level in levels:
        if prev_level:
            d = abs(prev_level - level)
            direction = "inc" if level - prev_level > 0 else "dec"
            if (d < 1 or d > 3) or (prev_dir and direction != prev_dir):
                safe = False
        prev_level = level
        prev_dir = direction
    return safe


def check_part2(levels: list) -> bool:
    """Check for a safe condition when removing 1 element"""
    for i in range(len(levels)):
        new_levels = deepcopy(levels)
        new_levels.pop(i)
        if check_safe(new_levels):
            return True
    return False


def main():
    part1_total = 0
    part2_total = 0

    with open("input.txt", "r") as f:
        for line in f.readlines():
            line = line.strip()
            sl = list(map(int, line.split(" ")))

            # Part 1 and partially part 2
            if check_safe(sl):
                part1_total += 1
                part2_total += 1
            else:
                # Part 2 check
                if check_part2(sl):
                    part2_total += 1

    print(f"Part 1: {part1_total}")
    print(f"Part 2: {part2_total}")


if __name__ == "__main__":
    main()
