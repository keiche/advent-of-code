#!/usr/bin/env python3
"""https://adventofcode.com/2022/day/7"""

from copy import deepcopy
from uuid import uuid4

# Flat tracking of directories
dirs = {}

# Track which directory hierarchy per directory
dir_membership = []

# Track previous and current directory for "cd"
prev_dir = ""
curr_dir = ""

# Parse input
with open("7.txt", "r") as f:
    for line in f.readlines():
        line = line.rstrip()
        # Change into a directory
        if "cd " in line and ".." not in line:
            line_dir = line.split(" ")[2]
            # Track the previous dir before go into the next one
            prev_dir = curr_dir
            if prev_dir:
                dir_membership.append(prev_dir)
            # Track the current directory (use unique name to handle repeats)
            curr_dir = uuid4() if line_dir != "/" else "/"
            # Directory stats
            dirs[curr_dir] = {"membership": deepcopy(dir_membership), "size": 0}
        # Change out of a directory
        elif "cd .." in line:
            curr_dir = dir_membership.pop()
            prev_dir = dir_membership[-1] if dir_membership else ""
        # File listings
        elif line[0].isdigit():
            dirs[curr_dir]["size"] += int(line.split(" ")[0])

part_1 = 0
part_2 = 0
total_dir_sizes = []
root_size = 0

# Determine the total directory sizes
for name, d in dirs.items():
    local_size = d["size"]
    child_size = sum([x["size"] for _, x in dirs.items() if name in x["membership"]])
    total_size = local_size + child_size
    total_dir_sizes.append(total_size)

    # Get root's size (Part 2)
    if name == "/":
        root_size = total_size

    # Part 1 answer - sum of dirs under 100k
    if total_size <= 100000:
        part_1 += total_size

# Part 2
space_needed = 30000000 - (70000000 - root_size)
for ds in sorted(total_dir_sizes):
    if ds > space_needed:
        part_2 = ds
        break

print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
