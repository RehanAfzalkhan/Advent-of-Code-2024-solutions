from itertools import product


def parse_input(file_path):
    """
    Parse the input file to extract target values and sequences of numbers.
    """
    equations = []
    with open(file_path, "r") as f:
        for line in f:
            target, numbers = line.split(":")
            target = int(target.strip())
            numbers = list(map(int, numbers.strip().split()))
            equations.append((target, numbers))
    return equations


def evaluate_expression(numbers, operators, mode):
    """
    Evaluate an expression left-to-right with the given operators.
    Includes concatenation ('||') in mode 2.
    """
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == "+":
            result += numbers[i + 1]
        elif op == "*":
            result *= numbers[i + 1]
        elif op == "||" and mode == 2:
            result = int(str(result) + str(numbers[i + 1]))
    return result


def calculate_total(file_path, mode):
    """
    Determine the total calibration result based on the valid equations.
    """
    equations = parse_input(file_path)
    total = 0

    for target, numbers in equations:
        num_operators = len(numbers) - 1
        valid = False

        # Generate all possible operator combinations
        operators_list = ["+", "*"] + (["||"] if mode == 2 else [])
        for operators in product(operators_list, repeat=num_operators):
            if evaluate_expression(numbers, operators, mode) == target:
                valid = True
                break

        if valid:
            total += target

    return total


if __name__ == "__main__":
    file_path = "inputs/d7_input.txt"  # Replace with your input file path
    print("Day 7: Bridge Repair")
    part1_result = calculate_total(file_path, mode=1)
    print(f"Part 1: {part1_result}")
    part2_result = calculate_total(file_path, mode=2)
    print(f"Part 2: {part2_result}")
