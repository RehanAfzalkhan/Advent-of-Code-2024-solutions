def read_input(file):
    with open(file, "r") as f:
        data = f.read().splitlines()
    return data


# Convert lock/key schematics to height arrays
def schematic_to_heights(schematic):
    cols = list(zip(*schematic))  # Transpose to process columns
    heights = []
    for col in cols:
        if "#" in col:
            height = len(col) - col[::-1].index("#") - 1  # Pin height
        else:
            height = 0
        heights.append(height)
    return heights


# Check if key fits into lock without overlapping
def fits(lock, key):
    return all(lock[i] + key[i] <= len(lock) for i in range(len(lock)))


# Process the schematics and compute pairs
def count_fitting_pairs(data):
    schematics = []
    current_schematic = []
    for line in data:
        if line == "":  # Empty line signifies new schematic
            if current_schematic:
                schematics.append(current_schematic)
                current_schematic = []
        else:
            current_schematic.append(line)
    if current_schematic:
        schematics.append(current_schematic)

    locks, keys = [], []
    for schematic in schematics:
        if schematic[0].count("#") == len(schematic[0]):  # Lock schematic
            locks.append(schematic_to_heights(schematic))
        else:  # Key schematic
            keys.append(schematic_to_heights(schematic[::-1]))  # Flip for key

    count = 0
    for lock in locks:
        for key in keys:
            if fits(lock, key):
                count += 1

    return count


# Part Two: Count stars and check if enough places are visited
def count_stars(data):
    star_count = sum(line.count("*") for line in data)
    return star_count >= 50


if __name__ == "__main__":
    input_data = read_input("inputs/d25input.txt")
    result = count_fitting_pairs(input_data)
    print(f"Number of fitting lock/key pairs: {result}")

    if count_stars(input_data):
        print("Enough stars collected to complete the chronicle!")
    else:
        print("Not enough stars collected, continue visiting places.")
