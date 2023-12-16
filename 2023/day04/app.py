#!/usr/local/env python3
"""
https://adventofcode.com/2023/day/4
keiche
"""

part1_total = 0


with open("input.txt", "r") as f:
    for line in f.readlines():
        line = line.rstrip()

        # Parse
        card_no = line.split(":")[0].split(" ")[1]
        win_list = line.split(" | ")[0].split(": ")[1].split()
        num_list = line.split(" | ")[1].split()

        # Inner join
        winners = list(set(win_list) & set(num_list))

        if winners:
            card_value = 2 ** (len(winners) - 1)
            part1_total += card_value

print(f"Part 1: {part1_total}")
