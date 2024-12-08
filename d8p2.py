import numpy as np
import itertools

with open("inputs/d8p2_input.txt") as f:
    rawgrid = f.read()

grid = np.array([list(line) for line in rawgrid.splitlines()])
shapex, shapey = grid.shape

frequencies = set(rawgrid) - {"\n", "."}
freq_coords = [
    {
        (i, j)
        for i, line in enumerate(grid)
        for j, char in enumerate(line)
        if char == freq
    }
    for freq in frequencies
]


def get_antinodes(coords1, coords2):
    x1, y1 = coords1
    x2, y2 = coords2
    dx, dy = x2 - x1, y2 - y1
    output = set()
    xa, ya = x1, y1
    while xa in range(shapex) and ya in range(shapey):
        output.add((xa, ya))
        xa, ya = xa + dx, ya + dy
    xa, ya = x1, y1
    while xa in range(shapex) and ya in range(shapey):
        output.add((xa, ya))
        xa, ya = xa - dx, ya - dy
    return output


all_antinodes = set()
for coords in freq_coords:
    for coords1, coords2 in itertools.combinations(coords, 2):
        all_antinodes |= get_antinodes(coords1, coords2)

answer = len(all_antinodes)
print(answer)
