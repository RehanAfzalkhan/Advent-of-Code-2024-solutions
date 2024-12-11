def simulate_blinks(stones, num_blinks):
    for _ in range(num_blinks):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:  # Even number of digits
                stone_str = str(stone)
                mid = len(stone_str) // 2
                left = int(stone_str[:mid])
                right = int(stone_str[mid:])
                new_stones.extend([left, right])
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
    return stones


def main():
    # Read initial stones from input.txt
    file_path = "inputs/d11input.txt"
    with open(file_path, "r") as file:
        content = file.read().strip()

    # Extract initial stones (assume they are space-separated integers)
    initial_stones = list(map(int, content.split()))

    # Simulate blinks
    num_blinks = 25
    final_stones = simulate_blinks(initial_stones, num_blinks)

    # Output the number of stones
    print("Number of stones after 25 blinks:", len(final_stones))


if __name__ == "__main__":
    main()
