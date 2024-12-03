def is_safe_report(report):
    """
    Checks if the given report (list of levels) is safe.
    """
    is_increasing = all(
        1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1)
    )
    is_decreasing = all(
        -3 <= report[i + 1] - report[i] <= -1 for i in range(len(report) - 1)
    )
    return is_increasing or is_decreasing


def count_safe_reports_with_dampener(file_path):
    """
    Counts the number of safe reports in the file, considering the Problem Dampener.
    """
    safe_count = 0
    with open(file_path, "r") as file:
        for line in file:
            report = list(map(int, line.split()))

            # Check if the report is safe as is
            if is_safe_report(report):
                safe_count += 1
                continue

            # Check if removing any one level makes it safe
            for i in range(len(report)):
                modified_report = report[:i] + report[i + 1 :]  # Remove the ith level
                if is_safe_report(modified_report):
                    safe_count += 1
                    break
    return safe_count


# Path to the input file
file_path = "day2_prob2_input.txt"

# Count and print the number of safe reports considering the Problem Dampener
safe_reports_with_dampener = count_safe_reports_with_dampener(file_path)
print(f"Number of safe reports with the Problem Dampener: {safe_reports_with_dampener}")
