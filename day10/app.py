#!/usr/bin/env python3
"""https://adventofcode.com/2022/day/10"""

instructions = []
with open("10.txt", "r") as f:
    for line in f.readlines():
        instructions.append(line.rstrip())

check = 20
check_cycle_pt1 = [check] + list(range(20, 260, 40))
check_cycle_pt2 = list(range(40, 280, 40))

cycle = 1
x = 1
op = []
total_signal = 0
output = []
row = "#"
while cycle <= check_cycle_pt2[-1]:
    # Part 1
    if cycle in check_cycle_pt1:
        signal_strength = cycle * x
        total_signal += signal_strength

    # Part 2 - next CRT line
    if cycle in check_cycle_pt2:
        output.append(row)
        row = ""

    # Handle instructions
    if not op:
        instruction = instructions.pop(0)
        if "addx" in instruction:
            op.append(instruction)
    else:
        x += int(instruction.split(" ")[1])
        op.pop()

    # Part 2 pixel
    cycle_pos = cycle % 40
    row += "#" if x in [cycle_pos - 1, cycle_pos, cycle_pos + 1] else "."

    # Increment cycle
    cycle += 1

print(f"Part 1: {total_signal}")
print(f"Part 2:")
for r in output:
    print(r)
