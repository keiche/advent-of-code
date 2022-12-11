#!/usr/bin/env python3
"""https://adventofcode.com/2022/day/4"""


def full_range(range_str: str) -> list:
    """
    Unpack the range
    :param range_str: range string (X-Y)
    :return: list of numbers in the range
    """
    a, b = range_str.split("-")
    return list(range(int(a), int(b) + 1))


total_contains = 0
total_partial = 0
with open("4.txt", "r") as f:
    for line in f.readlines():
        left, right = line.rstrip().split(",")
        left_range = full_range(left)
        right_range = full_range(right)
        # Use set intersection to find overlapping elements
        overlap_len = len(set(left_range) & set(right_range))
        # Part 1 - number of sets that fully overlap (length of set is the number of overlapping elements)
        if overlap_len in [len(left_range), len(right_range)]:
            total_contains += 1
        # Part 2 - number of sets that overlap at all
        if overlap_len:
            total_partial += 1

print(f"Part 1: {total_contains}")
print(f"Part 2: {total_partial}")
