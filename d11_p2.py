def simulate_blinks_count(stones, num_blinks):
    """
    Simulate the evolution of stones by counting their behavior.
    """
    from collections import Counter

    # Count the initial stones
    stone_counts = Counter(stones)  # {stone_value: count}

    for _ in range(num_blinks):
        new_counts = Counter()
        for stone, count in stone_counts.items():
            if stone == 0:
                new_counts[1] += count
            elif len(str(stone)) % 2 == 0:  # Even number of digits
                stone_str = str(stone)
                mid = len(stone_str) // 2
                left = int(stone_str[:mid])
                right = int(stone_str[mid:])
                new_counts[left] += count
                new_counts[right] += count
            else:
                new_counts[stone * 2024] += count
        stone_counts = new_counts

    # Total number of stones
    return sum(stone_counts.values())


def main():
    # Read initial stones from input.txt
    file_path = "inputs/d11input.txt"
    with open(file_path, "r") as file:
        content = file.read().strip()

    # Extract initial stones (assume they are space-separated integers)
    initial_stones = list(map(int, content.split()))

    # Simulate blinks
    num_blinks = 75
    total_stones = simulate_blinks_count(initial_stones, num_blinks)

    # Output the number of stones
    print("Number of stones after 75 blinks:", total_stones)


if __name__ == "__main__":
    main()
