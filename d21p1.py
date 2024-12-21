from functools import cache


def read_input(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()


inputval = ""
posi = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"],
]
arr_pads = [[None, "^", "A"], ["<", "v", ">"]]


def get_pos(arr, code):
    for i, row in enumerate(arr):
        if code in row:
            return (i, row.index(code))


@cache
def shortest(start, end, layers):
    if start == "<" and end == ">":
        pass
    if isinstance(start, str):
        start = get_pos(arr_pads, start)
    if isinstance(end, str):
        end = get_pos(arr_pads, end)

    if layers == 0:
        return 1
    elif layers < 3:
        vert = None
        hori = None
        if end[0] < start[0]:
            vert = "^"
        elif end[0] > start[0]:
            vert = "v"
        if end[1] < start[1]:
            hori = "<"
        elif end[1] > start[1]:
            hori = ">"
        if not hori and not vert:
            return shortest("A", "A", layers - 1)
        elif not hori:
            return (
                shortest("A", vert, layers - 1)
                + (abs(end[0] - start[0]) - 1) * shortest(vert, vert, layers - 1)
                + shortest(vert, "A", layers - 1)
            )
        elif not vert:
            return (
                shortest("A", hori, layers - 1)
                + (abs(end[1] - start[1]) - 1) * shortest(hori, hori, layers - 1)
                + shortest(hori, "A", layers - 1)
            )
        else:
            if start[1] == 0:
                return (
                    shortest("A", hori, layers - 1)
                    + (abs(end[1] - start[1]) - 1) * shortest(hori, hori, layers - 1)
                    + shortest(hori, vert, layers - 1)
                    + (abs(end[0] - start[0]) - 1) * shortest(vert, vert, layers - 1)
                    + shortest(vert, "A", layers - 1)
                )
            elif end[1] == 0:
                return (
                    shortest("A", vert, layers - 1)
                    + (abs(end[0] - start[0]) - 1) * shortest(vert, vert, layers - 1)
                    + shortest(vert, hori, layers - 1)
                    + (abs(end[1] - start[1]) - 1) * shortest(hori, hori, layers - 1)
                    + shortest(hori, "A", layers - 1)
                )
            else:
                return min(
                    shortest("A", hori, layers - 1)
                    + (abs(end[1] - start[1]) - 1) * shortest(hori, hori, layers - 1)
                    + shortest(hori, vert, layers - 1)
                    + (abs(end[0] - start[0]) - 1) * shortest(vert, vert, layers - 1)
                    + shortest(vert, "A", layers - 1),
                    shortest("A", vert, layers - 1)
                    + (abs(end[0] - start[0]) - 1) * shortest(vert, vert, layers - 1)
                    + shortest(vert, hori, layers - 1)
                    + (abs(end[1] - start[1]) - 1) * shortest(hori, hori, layers - 1)
                    + shortest(hori, "A", layers - 1),
                )
    else:
        vert = None
        hori = None
        if end[0] < start[0]:
            vert = "^"
        elif end[0] > start[0]:
            vert = "v"
        if end[1] < start[1]:
            hori = "<"
        elif end[1] > start[1]:
            hori = ">"
        if not hori and not vert:
            return shortest("A", "A", layers - 1)
        elif not hori:
            return (
                shortest("A", vert, layers - 1)
                + (abs(end[0] - start[0]) - 1) * shortest(vert, vert, layers - 1)
                + shortest(vert, "A", layers - 1)
            )
        elif not vert:
            return (
                shortest("A", hori, layers - 1)
                + (abs(end[1] - start[1]) - 1) * shortest(hori, hori, layers - 1)
                + shortest(hori, "A", layers - 1)
            )
        else:
            if start[1] == 0 and end[0] == 3:
                return (
                    shortest("A", hori, layers - 1)
                    + (abs(end[1] - start[1]) - 1) * shortest(hori, hori, layers - 1)
                    + shortest(hori, vert, layers - 1)
                    + (abs(end[0] - start[0]) - 1) * shortest(vert, vert, layers - 1)
                    + shortest(vert, "A", layers - 1)
                )
            elif end[1] == 0 and start[0] == 3:
                return (
                    shortest("A", vert, layers - 1)
                    + (abs(end[0] - start[0]) - 1) * shortest(vert, vert, layers - 1)
                    + shortest(vert, hori, layers - 1)
                    + (abs(end[1] - start[1]) - 1) * shortest(hori, hori, layers - 1)
                    + shortest(hori, "A", layers - 1)
                )
            else:
                return min(
                    shortest("A", hori, layers - 1)
                    + (abs(end[1] - start[1]) - 1) * shortest(hori, hori, layers - 1)
                    + shortest(hori, vert, layers - 1)
                    + (abs(end[0] - start[0]) - 1) * shortest(vert, vert, layers - 1)
                    + shortest(vert, "A", layers - 1),
                    shortest("A", vert, layers - 1)
                    + (abs(end[0] - start[0]) - 1) * shortest(vert, vert, layers - 1)
                    + shortest(vert, hori, layers - 1)
                    + (abs(end[1] - start[1]) - 1) * shortest(hori, hori, layers - 1)
                    + shortest(hori, "A", layers - 1),
                )


def main():
    inputval = read_input("inputs/d21input.txt").strip().split("\n")
    score = 0
    for line in inputval:
        intval = int(line[:3])
        total = 0
        for startp, endp in zip("A" + line[:3], line):
            total += shortest(get_pos(posi, startp), get_pos(posi, endp), 3)
        print(intval, total)
        score += intval * total
    print(score)


if __name__ == "__main__":
    main()
