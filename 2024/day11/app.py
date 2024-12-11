#!/usr/local/env python3
"""
https://adventofcode.com/2024/day/11
keiche
"""


def blink(stones: dict[int, int]) -> dict[int, int]:
    """A full blink iteration"""
    stone_queue = {}
    for num, count in stones.items():
        for sb in stone_blink(num):
            if sb not in stone_queue:
                stone_queue[sb] = 0
            stone_queue[sb] += count

    return stone_queue


def stone_blink(num: int) -> list[int]:
    """Process a single digit at a time, so it can be cached"""
    # Blink conditions
    num_str = str(num)
    if num == 0:
        return [1]
    elif len(num_str) % 2 == 0:
        half = int(len(num_str) / 2)
        return [int(num_str[0:half]), int(num_str[half:])]
    else:
        return [num * 2024]


def main():
    stones = {}  # {value: occurrences, ...}
    with open("input.txt", "r") as f:
        line = f.read()
        # Store stones
        for stone in list(map(int, line.split(" "))):
            if stone not in stones:
                stones[stone] = 0
            stones[stone] += 1

    # Blinks
    result = stones
    for i in range(75):
        result = blink(result)
        if i + 1 == 25:
            print(f"Part 1: {sum(result.values())}")
        elif i + 1 == 75:
            print(f"Part 2: {sum(result.values())}")


if __name__ == "__main__":
    main()
