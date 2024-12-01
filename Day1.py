def read_input(file_path):
    left_list = []
    right_list = []
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Split each line into two numbers
                left, right = map(int, line.strip().split())
                left_list.append(left)
                right_list.append(right)
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
        return None, None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None, None
    
    return left_list, right_list

def calculate_total_distance(left_list, right_list):
    # Sort both lists
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    
    total_distance = 0
    
    # Calculate distance between corresponding pairs
    for left, right in zip(left_sorted, right_sorted):
        distance = abs(left - right)
        total_distance += distance
    
    return total_distance

def main():
    # Read input file
    file_path = "input.txt"
    left_list, right_list = read_input(file_path)
    
    if left_list is None or right_list is None:
        return
    
    # Calculate and print the result
    result = calculate_total_distance(left_list, right_list)
    print(f"The total distance between the lists is: {result}")

if __name__ == "_main_":
    main()