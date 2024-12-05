#!/usr/local/env python3
"""
https://adventofcode.com/2024/day/5
keiche
"""

from math import ceil

ordering_rules = []
update_order = []


def parse_input(infile: str = "input.txt") -> None:
    with open(infile, "r") as f:
        switch_inputs = False
        for line in f:
            line = line.strip()
            if not line:
                switch_inputs = True
                continue

            if not switch_inputs:
                ordering_rules.append(tuple(list(map(int, line.split("|")))))
            else:
                update_order.append(list(map(int, line.split(","))))


def check_order(line: list, value: int) -> bool:
    # Only check rules where both pages exist in the update line
    rules = [x for x in ordering_rules if x[0] == value and x[1] in line]
    for rule in rules:
        if line.index(rule[0]) > line.index(rule[1]):
            return False
    return True


def reorder_update(line: list) -> int:
    for page in line:
        rules = [x for x in ordering_rules if x[0] == page and x[1] in line]
        for rule in rules:
            # Only reorder failed rules
            if not check_order(line, page):
                # Remove page
                page_index = line.index(rule[0])
                line.pop(page_index)

                # Place page before to fit the rule
                before_index = line.index(rule[1])
                line.insert(before_index, page)

    mid = ceil((len(line) - 1) / 2)
    return line[mid]


def main():
    part1_total = 0
    part2_total = 0

    parse_input()
    for line in update_order:
        valid_update = True
        for c in line:
            if not check_order(line, c):
                valid_update = False
                break
        # Part 1
        if valid_update:
            # Get middle element
            mid = ceil((len(line) - 1) / 2)
            part1_total += line[mid]
        # Part 2
        else:
            part2_total += reorder_update(line)

    print(f"Part 1: {part1_total}")
    print(f"Part 2: {part2_total}")


if __name__ == "__main__":
    main()
