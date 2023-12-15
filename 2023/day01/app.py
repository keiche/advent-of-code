#!/usr/local/env python3
"""
https://adventofcode.com/2023/day/1
keiche
"""

import re

part1_total = 0
part2_total = 0

num_replace = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


with open("input.txt", "r") as f:
    for line in f.readlines():
        line = line.rstrip()

        # Part 1
        nums_only = [x for x in line if x.isdigit()]
        part1_total += int(nums_only[0] + nums_only[-1])

        # Part 2 - replace words with numbers

        # Array of tuples (index, value)
        num_indices = []

        # Get index location of the numbers
        for i, char in enumerate(line):
            if char.isdigit():
                num_indices.append((i, int(char)))

        # Get index location of the word numbers
        for k, v in num_replace.items():
            for m in re.finditer(k, line):
                num_indices.append((m.start(0), v))

        num_indices = sorted(num_indices)
        # Find the lowest and highest index numbers with corresponding value
        part2_total += int(str(num_indices[0][1]) + str(num_indices[-1][1]))


print(f"Part 1: {part1_total}")
print(f"Part 2: {part2_total}")
