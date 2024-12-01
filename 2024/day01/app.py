#!/usr/local/env python3
"""
https://adventofcode.com/2024/day/1
keiche
"""


def parse_input(infile: str = "input.txt") -> tuple:
    left_list = []
    right_list = []
    with open(infile, "r") as f:
        for line in f.readlines():
            left_num, right_num = line.split("   ")
            left_list.append(int(left_num))
            right_list.append(int(right_num))
    return sorted(left_list), sorted(right_list)


# Left and right lists
ll, rl = parse_input()

# Part 1
part1_total = 0
for ln, rn in zip(ll, rl):
    # Sum the difference
    part1_total += abs(ln - rn)

# Part 2
similarity_map = {}
part2_total = 0
for ln in ll:
    if ln not in similarity_map:
        similarity_map[ln] = rl.count(ln)
    part2_total += ln * similarity_map[ln]


print(f"Part 1: {part1_total}")
print(f"Part 2: {part2_total}")
