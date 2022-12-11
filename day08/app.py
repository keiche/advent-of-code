#!/usr/bin/env python3
"""https://adventofcode.com/2022/day/8"""


def is_visible(tree: int, *lines) -> bool:
    hidden = 0
    for line in lines:
        # Hidden
        if any([True for x in line if x >= tree]):
            hidden += 1
    return hidden != len(lines)


def scenic_score(tree:int, *lines) -> int:
    scores = []
    for line in lines:
        line_score = 0
        for x in line:
            if x >= tree:
                line_score += 1
                break
            line_score += 1
        scores.append(line_score)

    total = 1
    for s in scores:
        total = total * s
    return total


# Parse the input
forest = []
with open("8.txt", "r") as f:
    for line in f.readlines():
        forest.append([int(x) for x in line.rstrip()])

# Check only the inner trees
visible_trees = (len(forest[0]) * 2) + ((len(forest) - 2) * 2)
for r_idx, row in enumerate(forest[1:-1]):
    for c_idx, cell in enumerate(row[1:-1]):
        above = list(reversed([x[c_idx + 1] for x in forest[0:r_idx + 1]]))
        below = [x[c_idx + 1] for x in forest[r_idx + 2:]]
        left = list(reversed([x for x in row[0:c_idx + 1]]))
        right = [x for x in row[c_idx + 2:]]

        visible = is_visible(cell, above, below, left, right)
        if visible:
            visible_trees += 1

# Check the whole forest
max_score = 0
for r_idx, row in enumerate(forest):
    for c_idx, cell in enumerate(row):
        above = list(reversed([x[c_idx] for x in forest[0:r_idx]]))
        below = [x[c_idx] for x in forest[r_idx + 1:]]
        left = list(reversed([x for x in row[0:c_idx]]))
        right = [x for x in row[c_idx + 1:]]

        score = scenic_score(cell, above, below, left, right)
        if score > max_score:
            max_score = score

print(f"Part 1: {visible_trees}")
print(f"Part 2: {max_score}")
