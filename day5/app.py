#!/usr/bin/env python3

import re
from copy import deepcopy

stacks = [[] for x in range(10)]
# Format: [{char_check: stack_num}]
check_stacks = [{1: 0}]
for x in range(2, 10):
    check_stacks.append({list(check_stacks[-1].keys())[0] + 4: x - 1})

flag_build_stacks = True
with open("5.txt", "r") as f:
    for line in f.readlines():
        line = line.rstrip()

        # Check if stack reading is complete
        if line.startswith(" 1 "):
            flag_build_stacks = False
            stacks_pt2 = deepcopy(stacks)

        # Read in the stacks
        if flag_build_stacks:
            for cs in check_stacks:
                for check, stack_num in cs.items():
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

                # Part 2
                pt2_crates.append(stacks_pt2[start_stack - 1].pop(0))
            # Also for Part 2 only
            for crate in reversed(pt2_crates):
                stacks_pt2[end_stack - 1].insert(0, crate)

print(f"Part 1: {''.join([s[0] for s in stacks if s])}")
print(f"Part 2: {''.join([s[0] for s in stacks_pt2 if s])}")
