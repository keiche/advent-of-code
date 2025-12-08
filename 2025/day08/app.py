"""
https://adventofcode.com/2025/day/8
keiche
"""
from math import sqrt


def get_distance(junction1: tuple[int, int, int], junction2: tuple[int, int, int]) -> float:
    # https://en.wikipedia.org/wiki/Euclidean_distance
    x1, y1, z1 = junction1
    x2, y2, z2 = junction2
    return sqrt(abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2 + abs(z2 - z1) ** 2)


def build_circuits(ordered_distances: list[tuple[tuple[int, int, int], float]], connections: int = 0) -> list[list[tuple[int, int, int]]]:
    # Walk through distances and build circuits
    circuits = []
    subset_ordered_distances = (ordered_distances[:connections] if connections > 0 else ordered_distances)
    # Part 2 - Track the last unconnected junction
    last_unconnected_junction = []

    for key, _ in subset_ordered_distances:
        j1, j2 = key

        # Find which circuits contain j1 and j2
        c1_idx = None
        c2_idx = None
        for i, c in enumerate(circuits):
            if j1 in c:
                c1_idx = i
            if j2 in c:
                c2_idx = i

        if c1_idx is not None and c2_idx is not None:
            # Both are in circuits
            if c1_idx != c2_idx:
                # Merge the two circuits
                circuits[c1_idx].extend(circuits[c2_idx])
                del circuits[c2_idx]
        # Only j1 is in a circuit, add j2
        elif c1_idx is not None:
            circuits[c1_idx].append(j2)
            # Part 2 - Keep updating, we only need the last time this is set
            last_unconnected_junction = [j1, j2]
        # Only j2 is in a circuit, add j1
        elif c2_idx is not None:
            circuits[c2_idx].append(j1)
            # Part 2 - Keep updating, we only need the last time this is set
            last_unconnected_junction = [j1, j2]
        # Neither is in a circuit, create a new one
        else:
            circuits.append([j1, j2])

    return circuits, last_unconnected_junction


def main():
    part1_total = 0
    part2_total = 1  # Set to 1 so we're not multiplying by 0

    junctions = []
    filename = "input.txt"
    with open(filename, "r") as f:
        for line in f:
            junctions.append(tuple(map(int, line.strip().split(","))))

    # Get all distances between all junctions
    distances = {}
    for j1 in junctions:
        for j2 in junctions:
            key = tuple(sorted([j1, j2]))
            if j1 != j2 and key not in distances:
                distances[key] = get_distance(j1, j2)

    # Sort distances by distance
    ordered_distances = sorted(distances.items(), key=lambda x: x[1])
    circuits, _ = build_circuits(ordered_distances, connections=1000 if filename == "input.txt" else 10)

    # Part 1 - Length of all circuits
    circuit_lengths = []
    for c in circuits:
        # Make sure to only count each junction once
        circuit_lengths.append(len(set(c)))
    circuit_lengths = list(reversed(sorted(circuit_lengths)))
    part1_total = circuit_lengths[0] * circuit_lengths[1] * circuit_lengths[2]

    # Part 2 - X values of final 2 junctions
    _, last_unconnected_junction = build_circuits(ordered_distances)
    part2_total = last_unconnected_junction[0][0] * last_unconnected_junction[1][0]

    print(f"Part 1: {part1_total}")
    print(f"Part 2: {part2_total}")


if __name__ == "__main__":
    main()
