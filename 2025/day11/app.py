"""
https://adventofcode.com/2025/day/11
keiche
"""

from aoc_utils import DirectedGraph


def main():
    filename = "input.txt"
    dg = DirectedGraph(filename)
    dg.parse_file(filename)
    part1_paths = dg.find_all_paths("you", "out")

    part2_total = dg.count_paths("svr", "fft") * dg.count_paths("fft", "dac") * dg.count_paths("dac", "out")
    part2_total += dg.count_paths("svr", "dac") * dg.count_paths("dac", "fft") * dg.count_paths("fft", "out")

    part1_total = len(part1_paths)
    print(f"Part 1: {part1_total}")
    print(f"Part 2: {part2_total}")


if __name__ == "__main__":
    main()
