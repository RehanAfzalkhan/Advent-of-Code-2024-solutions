def find_word_in_grid(grid, word):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1),  # Horizontal right
        (0, -1),  # Horizontal left
        (1, 0),  # Vertical down
        (-1, 0),  # Vertical up
        (1, 1),  # Diagonal down-right
        (1, -1),  # Diagonal down-left
        (-1, 1),  # Diagonal up-right
        (-1, -1),  # Diagonal up-left
    ]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def search(x, y, dx, dy):
        for k in range(word_len):
            nx, ny = x + k * dx, y + k * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[k]:
                return False
        return True

    count = 0
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if search(i, j, dx, dy):
                    count += 1
    return count


# Read the grid from the input file
def read_grid(file_path):
    with open(file_path, "r") as file:
        return [list(line.strip()) for line in file.readlines()]


# Path to the input file
file_path = "inputs/D4p1_input.txt"

# Find and print the total occurrences of "XMAS"
grid = read_grid(file_path)
word = "XMAS"
result = find_word_in_grid(grid, word)
print(f"The word '{word}' appears {result} times in the grid.")
