#!/usr/bin/env python3

def full_range(range_str: str) -> list:
    a, b = range_str.split("-")
    return list(range(int(a), int(b) + 1))


total_contains = 0
total_partial = 0
with open("4.txt", "r") as f:
    for line in f.readlines():
        left, right = line.rstrip().split(",")
        left_range = full_range(left)
        right_range = full_range(right)
        overlap_len = len(set(left_range) & set(right_range))
        if overlap_len in [len(left_range), len(right_range)]:
            total_contains += 1
        if overlap_len:
            total_partial += 1

print(f"Part 1: {total_contains}")
print(f"Part 2: {total_partial}")
