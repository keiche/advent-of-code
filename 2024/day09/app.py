#!/usr/local/env python3
"""
https://adventofcode.com/2024/day/9
keiche
"""

from copy import deepcopy


class Disk:
    def __init__(self, disk_map: list[int]) -> None:
        self.disk_map = disk_map
        self.free_space_map = []  # [(raw_disk_index, size), ...]
        self.file_list = []  # [(id, raw_disk_index, size), ...]
        self.raw_disk = []
        idn = 0
        for i, x in enumerate(disk_map):
            raw_disk_idx = len(self.raw_disk)
            # Blocks
            if i % 2 == 0:
                self.file_list.append((idn, raw_disk_idx, x))
                self.raw_disk.extend([idn for _ in range(x)])
                idn += 1
            # Free space
            if i % 2 == 1:
                self.free_space_map.append((raw_disk_idx, x))
                self.raw_disk.extend(["." for i in range(x)])

    def compact_disk(self):
        data_blocks = list(reversed([d for d in self.raw_disk if isinstance(d, int)]))
        total_replacements = 0
        for idx, size in self.free_space_map:
            for c, i in enumerate(range(idx, idx + size)):
                self.raw_disk[i] = data_blocks.pop(0)
                total_replacements += 1
        self.raw_disk[-total_replacements:] = ["." for _ in range(total_replacements)]

    def compact_disk2(self):
        for file_idx, file_raw_idx, file_size in list(reversed(self.file_list)):
            for c, (free_raw_idx, free_size) in enumerate(self.free_space_map):
                # File fits and is moving left
                if file_size <= free_size and free_raw_idx < file_raw_idx:
                    # Place file in free space
                    self.raw_disk[free_raw_idx: free_raw_idx + file_size] = [file_idx for _ in range(file_size)]
                    # Reclaim file space
                    self.raw_disk[file_raw_idx: file_raw_idx + file_size] = ["." for _ in range(file_size)]
                    # No more free space - remove
                    if free_size - file_size == 0:
                        self.free_space_map.pop(c)
                    # Update remaining free space
                    else:
                        self.free_space_map[c] = (free_raw_idx + file_size, free_size - file_size)
                    break

    def checksum(self) -> int:
        cs = 0
        for i, b in enumerate(self.raw_disk):
            if isinstance(b, int):
                cs += i * b
        return cs


def main():
    with open("input.txt", "r") as f:
        for line in f:
            disk1 = Disk(list(map(int, (line.strip()))))
    disk2 = deepcopy(disk1)

    # Part 1
    disk1.compact_disk()
    print(f"Part 1: {disk1.checksum()}")

    # Part 2
    disk2.compact_disk2()
    print(f"Part 2: {disk2.checksum()}")


if __name__ == "__main__":
    main()
