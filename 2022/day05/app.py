#!/usr/bin/env python3
"""https://adventofcode.com/2022/day/5"""


import re
from copy import deepcopy

# Setup a list of lists to hold the contents of the stacks
stacks = [[] for x in range(10)]

# Create a mapping of which character to check, and what stack it's part of
# We'll skip brackets and spaces, which means every 4th character is part of a stack
# Pre-build this mapping so we can just check those parts of the line
# Format: [(char_check: stack_num)]
check_stacks = [(1, 0)]
for x in range(1, 9):
    # Character check position: Get the previous character position and add 4
    # Stack number: iterate
    check_stacks.append((check_stacks[-1][0] + 4, x))

flag_build_stacks = True
with open("5.txt", "r") as f:
    for line in f.readlines():
        line = line.rstrip()

        # Check if stack reading is complete
        if line.startswith(" 1 "):
            flag_build_stacks = False
            stacks_pt2 = deepcopy(stacks)

        # Parse the stacks input (first part of the input)
        if flag_build_stacks:
            for check, stack_num in check_stacks:
                # Ensure we stay inbounds
                if check >= len(line) - 1:
                    break
                c = line[check]
                if re.match(r"[A-Z]", c):
                    stacks[stack_num].append(c)

        # Crane logic
        if line.startswith("move"):
            _, crates, _, start_stack, _, end_stack = line.split(" ")
            crates = int(crates)
            start_stack = int(start_stack)
            end_stack = int(end_stack)
            pt2_crates = []
            for x in range(crates):
                # Part 1
                crate = stacks[start_stack - 1].pop(0)
                stacks[end_stack - 1].insert(0, crate)

                # Part 2 - create a temporary stack when crates multiple are pulled up simultaneously
                pt2_crates.append(stacks_pt2[start_stack - 1].pop(0))
            # Part 2 - reverse the temporary stack and add it to the stack
            for crate in reversed(pt2_crates):
                stacks_pt2[end_stack - 1].insert(0, crate)

print(f"Part 1: {''.join([s[0] for s in stacks if s])}")
print(f"Part 2: {''.join([s[0] for s in stacks_pt2 if s])}")
