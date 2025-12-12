"""
https://adventofcode.com/2025/day/12
keiche
"""


class Region:
    def __init__(self, id: int, width: int, length: int, quantity: list[int]):
        self.id = id
        self.width = width
        self.length = length
        self.area = width * length
        self.quantity = quantity
        self.total_quantity = sum(quantity)


class Box:
    def __init__(self):
        self.dimensions = []

    def add_dimension(self, dimension: str):
        self.dimensions.append(dimension)

    @property
    def area(self) -> int:
        return "".join(self.dimensions).count("#")


def main():
    part1_total = 0
    boxes = {}
    regions = []
    box_id = None
    region_id = 0
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            # Box creation
            if line and line[0].isdigit() and line[1] == ":":
                box_id = int(line[0])
                boxes[box_id] = Box()
            elif "#" in line:
                boxes[box_id].add_dimension(line.strip())
            elif "x" in line:
                region_size, region_quantity = line.split(":")
                width, length = tuple(map(int, region_size.split("x")))
                region = Region(region_id, width, length, list(map(int, region_quantity.strip().split(" "))))
                regions.append(region)
                region_id += 1

    # Start rejecting regions
    remaining_regions = [r.id for r in regions]
    # print(f"Starting regions: {remaining_regions}")

    for region in regions:
        # print(f"Checking region {region.id}: {region.width}x{region.length} with quantity {region.quantity}")
        # Check if the region area is too small if all boxes perfectly fit
        min_area_needed = 0
        for bid, bqty in enumerate(region.quantity):
            min_area_needed += boxes[bid].area * bqty
        if min_area_needed > region.area:
            # print(f"Rejecting region {region.id} because it's area is too small")
            remaining_regions.remove(region.id)
            continue

        # Rough check if region can fit in the amount of 3x3 boxes
        rough_needed_width = region.width / 3
        rough_needed_length = region.length / 3
        rough_max_boxes = rough_needed_width * rough_needed_length
        if rough_max_boxes < region.total_quantity:
            # print(f"Rejecting region {region.id} because it can't fit in the amount of 3x3 boxes")
            remaining_regions.remove(region.id)
            continue

    # print(f"\nRemaining regions: {remaining_regions}")
    part1_total = len(remaining_regions)
    print(f"Part 1: {part1_total}")


if __name__ == "__main__":
    main()
