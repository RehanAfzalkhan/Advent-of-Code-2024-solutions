import numpy as np
from queue import Queue


def bfs_shortest_path(grid, start, goal):
    rows, cols = grid.shape
    queue = Queue()
    queue.put((start, [start]))
    visited = set()
    visited.add(start)

    while not queue.empty():
        (current, path) = queue.get()
        x, y = current

        if current == goal:
            return path

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < rows
                and 0 <= ny < cols
                and grid[nx, ny] == 0
                and (nx, ny) not in visited
            ):
                queue.put(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))

    return None


grid = np.zeros((71, 71), dtype=int)

with open("inputs/d18input.txt") as f:
    for i, line in enumerate(f):
        x, y = map(int, line.strip().split(","))
        grid[x, y] = 1

        if i > 1024:
            path = bfs_shortest_path(grid, (0, 0), (70, 70))
            if i == 1025:
                print(len(path) - 1)
            if not path:
                print(x, y)
                break
