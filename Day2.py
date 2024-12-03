def is_safe_report(report):
    """
    Checks if the given report (list of levels) is safe.
    """
    # Check if the report is strictly increasing or decreasing
    is_increasing = all(
        1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1)
    )
    is_decreasing = all(
        -3 <= report[i + 1] - report[i] <= -1 for i in range(len(report) - 1)
    )
    return is_increasing or is_decreasing


def count_safe_reports(file_path):
    """
    Counts the number of safe reports in the file.
    """
    safe_count = 0
    with open(file_path, "r") as file:
        for line in file:
            report = list(map(int, line.split()))
            if is_safe_report(report):
                safe_count += 1
    return safe_count


# Path to the input file
file_path = "day2_prob2_input.txt"

# Count and print the number of safe reports
safe_reports = count_safe_reports(file_path)
print(f"Number of safe reports: {safe_reports}")
