#!/usr/local/env python3
"""
https://adventofcode.com/2023/day/2
keiche
"""

part1_max = {"red": 12, "green": 13, "blue": 14}

part1_total = 0
part2_total = 0


with open("input.txt", "r") as f:
    for line in f.readlines():
        line = line.rstrip()
        part1_possible = True

        game_num = int(line.split(":")[0].split(" ")[1])

        # Part 1
        cube_values = line.split(": ")[1].replace(";", ",").split(", ")
        for cv in cube_values:
            count, color = cv.split(" ")
            if int(count) > part1_max[color]:
                part1_possible = False
                break
        if part1_possible:
            part1_total += game_num

        # Part 2
        min_set = {"blue": 0, "green": 0, "red": 0}
        sets = line.split(": ")[1].split("; ")
        for s in sets:
            for cv in s.split(", "):
                count, color = cv.split(" ")
                if int(count) > min_set[color]:
                    min_set[color] = int(count)

        power = min_set["blue"] * min_set["green"] * min_set["red"]
        part2_total += power


print(f"Part 1: {part1_total}")
print(f"Part 2: {part2_total}")
