import math
import re
from collections import *
from itertools import *


def count(it):
    return sum(1 for _ in it)


# Read input from the file input.txt
with open("inputs/d92input.txt", "r") as file:
    inp = file.read().strip()

n = len(inp)
table = [(int(x), i // 2 if i % 2 == 0 else -1) for i, x in enumerate(inp)]

result = 0

stop = False
while not stop:
    stop = True
    for id in range(math.ceil(len(inp) / 2) - 1, -1, -1):
        # Find the next file
        file_index = -1
        for i in range(0, len(table)):
            r = table[i]
            if r[1] == id:
                file_index = i
                # break
        if file_index == -1:
            continue
        file = table[file_index]

        # Find the first gap
        gap_index = -1
        for i in range(file_index):
            r = table[i]
            if r[1] == -1 and r[0] >= file[0]:
                gap_index = i
                break
        if gap_index == -1:
            continue
        gap = table[gap_index]
        stop = False

        if file[0] == gap[0]:
            table[gap_index] = (gap[0], file[1])
            table[file_index] = (gap[0], -1)
        else:
            table[file_index] = (file[0], -1)
            table[gap_index] = (file[0], file[1])
            table.insert(gap_index + 1, (gap[0] - file[0], -1))

        # Merge consecutive free space blocks
        i = 0
        while i < len(table) - 1:
            if table[i][1] == -1 and table[i + 1][1] == -1:
                table[i] = (table[i][0] + table[i + 1][0], -1)
                del table[i + 1]
            else:
                i += 1

    stop = True

print("Done!")

# Calculate the checksum
curr_idx = 0
for entry in table:
    next_idx = curr_idx + entry[0]
    if entry[1] == -1:
        curr_idx = next_idx
        continue
    while curr_idx < next_idx:
        result += curr_idx * entry[1]
        curr_idx += 1

# Print final table and checksum result
print(
    "".join(
        "".join(repeat(str(t[1]), t[0])) if t[1] != -1 else "".join(repeat(".", t[0]))
        for t in table
    )
)
print(result)
