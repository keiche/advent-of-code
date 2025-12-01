#!/usr/local/env python3
"""
https://adventofcode.com/2025/day/1
keiche
"""
from math import floor


def count_clicks(dial: int, spin: int, dir: str) -> int:
    if dir == "R":
        return floor(spin / 100)
    elif dir == "L":
        if spin <= 0:
            # Don't recount 0 if that's where we started
            return floor(abs(spin) / 100) + 1 if dial != 0 else floor(abs(spin) / 100)
    return 0


def main():
    dial = 50
    part1 = 0
    part2 = 0
    with open("input.txt", "r") as f:
        for line in f:
            d = line[0]
            rot = int(line[1:])

            if d == "L":
                spin = dial - rot
            elif d == "R":
                spin = dial + rot

            part2 += count_clicks(dial, spin, d)

            dial = spin % 100
            if dial == 0:
                part1 += 1

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
