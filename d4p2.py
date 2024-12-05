def rotate90(grid):
    return ["".join(row) for row in zip(*grid[::-1])]


def go(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    for row in range(rows - 2):
        for col in range(cols - 2):
            if (
                grid[row][col] == "M"
                and grid[row][col + 2] == "M"
                and grid[row + 1][col + 1] == "A"
                and grid[row + 2][col] == "S"
                and grid[row + 2][col + 2] == "S"
            ):
                count += 1
    return count


def main():
    grid = [line.strip() for line in open("inputs/D4p2_input.txt")]
    result = 0
    for _ in range(4):
        result += go(grid)
        grid = rotate90(grid)
    print(result)


if __name__ == "__main__":
    main()
