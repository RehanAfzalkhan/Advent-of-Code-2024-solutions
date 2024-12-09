import sys
import re
from collections import *
from itertools import *


def count(it):
    return sum(1 for _ in it)


# Change this to read from 'input.txt' instead of stdin
with open("inputs/d9input.txt", "r") as file:
    inp = file.read().strip()

n = len(inp)
table = [(int(x), i // 2 if i % 2 == 0 else -1) for i, x in enumerate(inp)]

result = 0

while True:
    # Find the first gap
    gap_index = -1
    for i, r in enumerate(table):
        if r[1] == -1:
            gap_index = i
            break
    if gap_index == -1:
        break
    gap = table[gap_index]

    # Find the next file
    file_index = -1
    for i in range(gap_index + 1, len(table)):
        r = table[i]
        if r[1] != -1:
            file_index = i
            # break
    if file_index == -1:
        break
    file = table[file_index]

    if file[0] > gap[0]:
        table[gap_index] = (gap[0], file[1])
        table[file_index] = (file[0] - gap[0], file[1])
        table.insert(file_index + 1, (gap[0], -1))
    elif file[0] == gap[0]:
        table[gap_index] = (gap[0], file[1])
        table[file_index] = (gap[0], -1)
    else:
        table[file_index] = (file[0], -1)
        table[gap_index] = (file[0], file[1])
        table.insert(gap_index + 1, (gap[0] - file[0], -1))
    # print(table)

print("Done!")
curr_idx = 0
for entry in table:
    next_idx = curr_idx + entry[0]
    if entry[1] == -1:
        curr_idx = next_idx
        continue
    while curr_idx < next_idx:
        result += curr_idx * entry[1]
        curr_idx += 1

print(table)
print(result)
