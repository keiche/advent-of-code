#!/usr/bin/env python3
"""https://adventofcode.com/2022/day/6"""


def find_start_seq(seq: str, marker_len: int) -> int:
    """
    Find the first unique set of characters of a certain length
    :param seq: input message
    :param marker_len: how long the unique starting sequence is
    :return: the end index of the unique starting sequence
    """
    for idx, c in enumerate(seq):
        check_seq = set(list(seq[idx:idx + marker_len]))
        if len(check_seq) == marker_len:
            return idx + marker_len


with open("6.txt", "r") as f:
    line = f.readline().rstrip()
    print(f"Part 1: {find_start_seq(line, 4)}")
    print(f"Part 2: {find_start_seq(line, 14)}")
