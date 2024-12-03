#!/usr/local/env python3
"""
https://adventofcode.com/2024/day/3
keiche
"""

from re import compile

re_instructions = compile(r"(mul\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don't\(\))")

part1_total = 0
part2_total = 0

with open("input.txt", "r") as f:
    active = True
    for line in f:
        for m in re_instructions.findall(line.strip()):
            if "don't()" in list(m):
                active = False
            elif "do()" in list(m):
                active = True
            if "mul" in m[0]:
                if active:
                    part2_total += int(m[1]) * int(m[2])
                part1_total += int(m[1]) * int(m[2])

print(f"Part 1: {part1_total}")
print(f"Part 2: {part2_total}")
