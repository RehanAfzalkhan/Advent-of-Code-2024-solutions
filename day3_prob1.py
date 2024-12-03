import re


def calculate_sum_of_multiplications(file_path):
    # Define regex pattern to match valid mul(X,Y)
    pattern = r"mul\((\d+),(\d+)\)"
    total_sum = 0

    with open(file_path, "r") as file:
        for line in file:
            # Find all matches of the pattern in the line
            matches = re.findall(pattern, line)
            for x, y in matches:
                # Convert extracted strings to integers and calculate the product
                total_sum += int(x) * int(y)

    return total_sum


# Path to the input file
file_path = "day3_prob1_input.txt"

# Calculate and print the result
result = calculate_sum_of_multiplications(file_path)
print(f"The sum of all valid multiplications is: {result}")
