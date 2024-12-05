import re


def calculate_conditional_multiplications(file_path):
    # Define regex patterns
    mul_pattern = r"mul\((\d+),(\d+)\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    total_sum = 0
    is_enabled = True  # Start with mul instructions enabled

    with open(file_path, "r") as file:
        for line in file:
            # Split the line into tokens to process sequentially
            tokens = re.split(r"(\bdo\(\)|\bdon't\(\)|mul\(\d+,\d+\))", line)
            for token in tokens:
                token = token.strip()
                if not token:
                    continue

                if re.match(do_pattern, token):
                    is_enabled = True  # Enable mul instructions
                elif re.match(dont_pattern, token):
                    is_enabled = False  # Disable mul instructions
                elif re.match(mul_pattern, token) and is_enabled:
                    # Extract numbers and compute product
                    x, y = map(int, re.findall(r"\d+", token))
                    total_sum += x * y

    return total_sum


# Path to the input file
file_path = "inputs/day3_prob2_input.txt"

# Calculate and print the result
result = calculate_conditional_multiplications(file_path)
print(f"The sum of all enabled multiplications is: {result}")
