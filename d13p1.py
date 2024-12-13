lines = [l.split() for l in open("inputs/d13input.txt")]

# make groups of claw machines
groups = []
for i in range(int((len(lines) + 1) / 4)):
    groups.append([lines[4 * i], lines[4 * i + 1], lines[4 * i + 2]])

# get interesting values from the input
data = [
    [
        int(a[2][2:-1]),
        int(a[3][2:]),
        int(b[2][2:-1]),
        int(b[3][2:]),
        int(p[1][2:-1]),
        int(p[2][2:]),
    ]
    for [a, b, p] in groups
]

res = 0
for [ax, ay, bx, by, x, y] in data:
    # solved the 2 equations system (i * ax + j * bx = x and i * ay + j * by = y)
    i = (bx * y - by * x) / (ay * bx - ax * by)
    j = (x - i * ax) / bx
    # check if i and j are integers
    if (x - i * ax) % bx == 0 and (bx * y - by * x) % (ay * bx - ax * by) == 0:
        res += 3 * int(i) + int(j)
print(res)
