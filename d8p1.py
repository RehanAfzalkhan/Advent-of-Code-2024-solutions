import numpy as np
import itertools

with open("inputs/d8p1_input.txt") as f:
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


def get_antinodes(coords):
    return {
        (2 * x1 - x2, 2 * y1 - y2)
        for (x1, y1), (x2, y2) in itertools.permutations(coords, 2)
    }


all_antinodes = set()
for coords in freq_coords:
    all_antinodes |= get_antinodes(coords)

valid_antinodes = {
    (i, j) for i, j in all_antinodes if i in range(shapex) and j in range(shapey)
}
answer = len(valid_antinodes)
print(answer)
