#!/usr/local/env python3
"""
https://adventofcode.com/2024/day/19
keiche
"""

from functools import cache

patterns = []


def search(towel: str) -> bool:
    """Find any matching towel patterns"""
    if len(towel) == 0:
        return True

    for pattern in patterns:
        if towel.startswith(pattern):
            if search(towel[len(pattern):]):
                return True

    return False


@cache
def combos(towel: str) -> int:
    """Find all possible combinations of towel patterns"""
    result = 0
    if len(towel) == 0:
        result += 1

    for pattern in patterns:
        if towel.startswith(pattern):
            result += combos(towel[len(pattern):])

    return result


def parse_input(filename: str) -> tuple[list[str], list[str]]:
    global patterns
    towels: list[str] = []
    with open(filename) as f:
        for i, line in enumerate(f):
            line = line.strip()
            if i == 0:
                patterns = line.split(", ")
            elif line == "":
                continue
            else:
                towels.append(line)

    return patterns, towels


def main():
    global patterns
    patterns, towels = parse_input("input.txt")
    part1_total = 0
    part2_total = 0
    for t in towels:
        if search(t):
            part1_total += 1
        if result := combos(t):
            part2_total += result

    print(f"Part 1: {part1_total}")
    print(f"Part 2: {part2_total}")


if __name__ == "__main__":
    main()
