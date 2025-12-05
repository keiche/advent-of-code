"""
https://adventofcode.com/2025/day/5
keiche
"""


def range_overlap_correcter(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Merge overlapping ranges into a single range so we can count without brute force"""
    # Sort ranges by start so that we can always just focus on the last range
    sorted_ranges = sorted(ranges)
    new_ranges = [sorted_ranges[0]]

    for start, end in sorted_ranges[1:]:
        last_start, last_end = new_ranges[-1]
        # Ranges overlap, merge them
        if start <= last_end:
            new_ranges[-1] = (last_start, max(last_end, end))
        else:
            new_ranges.append((start, end))

    return new_ranges


def main():
    part1_total = 0
    part2_total = 0

    ranges = []
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            # Fresh ID range
            if "-" in line:
                start, end = line.split("-")
                ranges.append((int(start), int(end)))
            # Ingredients
            elif line.isdigit():
                ingredient = int(line)
                for start, end in ranges:
                    if start <= ingredient <= end:
                        part1_total += 1
                        break

    # Part 2
    updated_ranges = range_overlap_correcter(ranges)
    for r in updated_ranges:
        part2_total += int(r[1] - r[0] + 1)

    print(f"Part 1: {part1_total}")
    print(f"Part 2: {part2_total}")


if __name__ == "__main__":
    main()
