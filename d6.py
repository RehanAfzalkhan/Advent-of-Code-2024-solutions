#!/bin/python3

import sys
from typing import List

FILE = sys.argv[1] if len(sys.argv) > 1 else "inputs/d6p2_input.txt"


def read_lines_to_maze() -> List[str]:
    lines: List[str] = []
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            lines.append(list(line))

    return lines


def part_one():
    lines = read_lines_to_maze()
    answer = 0

    maze = {}
    visited = set()
    curr = None

    height = len(lines)
    width = len(lines[0])

    for row, line in enumerate(lines):
        for col, cell in enumerate(line):
            maze[(row, col)] = cell
            if cell == "^":
                curr = (row, col)

    direction = "up"
    visited.add(curr)
    while True:
        if direction == "up":
            if curr[0] - 1 < 0:
                break
            elif maze[(curr[0] - 1, curr[1])] == "#":
                direction = "right"
            else:
                maze[curr] = "."
                curr = (curr[0] - 1, curr[1])
                maze[curr] = "^"
                visited.add(curr)
        elif direction == "down":
            if curr[0] + 1 >= height:
                break
            elif maze[(curr[0] + 1, curr[1])] == "#":
                direction = "left"
            else:
                maze[curr] = "."
                curr = (curr[0] + 1, curr[1])
                maze[curr] = "^"
                visited.add(curr)
        elif direction == "right":
            if curr[1] + 1 >= width:
                break
            elif maze[(curr[0], curr[1] + 1)] == "#":
                direction = "down"
            else:
                maze[curr] = "."
                curr = (curr[0], curr[1] + 1)
                maze[curr] = "^"
                visited.add(curr)
        elif direction == "left":
            if curr[1] - 1 < 0:
                break
            elif maze[(curr[0], curr[1] - 1)] == "#":
                direction = "up"
            else:
                maze[curr] = "."
                curr = (curr[0], curr[1] - 1)
                maze[curr] = "^"
                visited.add(curr)

    answer = len(visited)
    print(f"Part 1: {answer}")


def part_two():
    lines = read_lines_to_maze()
    answer = 0

    maze = {}
    start = None

    height = len(lines)
    width = len(lines[0])

    for row, line in enumerate(lines):
        for col, cell in enumerate(line):
            maze[(row, col)] = cell
            if cell == "^":
                start = (row, col)

    for m in maze.keys():
        if maze[m] != ".":
            continue

        maze[m] = "#"

        curr = start
        direction = "up"
        visited = set()
        visited.add((curr, direction))
        while True:
            if direction == "up":
                if curr[0] - 1 < 0:
                    break
                elif maze[(curr[0] - 1, curr[1])] == "#":
                    direction = "right"
                else:
                    maze[curr] = "."
                    curr = (curr[0] - 1, curr[1])
                    maze[curr] = "^"
                    if (curr, direction) in visited:
                        answer += 1
                        break
                    else:
                        visited.add((curr, direction))
            elif direction == "down":
                if curr[0] + 1 >= height:
                    break
                elif maze[(curr[0] + 1, curr[1])] == "#":
                    direction = "left"
                else:
                    maze[curr] = "."
                    curr = (curr[0] + 1, curr[1])
                    maze[curr] = "^"
                    if (curr, direction) in visited:
                        answer += 1
                        break
                    else:
                        visited.add((curr, direction))
            elif direction == "right":
                if curr[1] + 1 >= width:
                    break
                elif maze[(curr[0], curr[1] + 1)] == "#":
                    direction = "down"
                else:
                    maze[curr] = "."
                    curr = (curr[0], curr[1] + 1)
                    maze[curr] = "^"
                    if (curr, direction) in visited:
                        answer += 1
                        break
                    else:
                        visited.add((curr, direction))
            elif direction == "left":
                if curr[1] - 1 < 0:
                    break
                elif maze[(curr[0], curr[1] - 1)] == "#":
                    direction = "up"
                else:
                    maze[curr] = "."
                    curr = (curr[0], curr[1] - 1)
                    maze[curr] = "^"
                    if (curr, direction) in visited:
                        answer += 1
                        break
                    else:
                        visited.add((curr, direction))

        maze[curr] = "."
        maze[start] = "^"
        maze[m] = "."

    print(f"Part 2: {answer}")


part_one()
part_two()
