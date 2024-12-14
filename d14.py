res = 1
robots = []

with open("inputs/d14input.txt") as f:
    for line in f:
        line = line.strip().split(" ")
        cur_coord = (int(line[0].split(",")[0][2:]), int(line[0].split(",")[1]))
        velocity = (int(line[1].split(",")[0][2:]), int(line[1].split(",")[1]))
        robots.append((cur_coord, velocity))

p2_robots = robots.copy()
for i in range(100):
    for j, robot in enumerate(robots):
        cur_coord, velocity = robot
        robots[j] = (
            ((cur_coord[0] + velocity[0]) % 101, (cur_coord[1] + velocity[1]) % 103),
            velocity,
        )

quads = [0, 0, 0, 0]
# count quadrants
for robot in robots:
    cur_coord, velocity = robot
    if cur_coord[0] < 50 and cur_coord[1] < 51:
        quads[0] += 1
    elif cur_coord[0] > 50 and cur_coord[1] < 51:
        quads[1] += 1
    elif cur_coord[0] < 50 and cur_coord[1] > 51:
        quads[2] += 1
    elif cur_coord[0] > 50 and cur_coord[1] > 51:
        quads[3] += 1

for quad in quads:
    res *= quad

print(res)

seconds = 1
while True:
    visited = set()
    for j, robot in enumerate(p2_robots):
        cur_coord, velocity = robot
        p2_robots[j] = (
            ((cur_coord[0] + velocity[0]) % 101, (cur_coord[1] + velocity[1]) % 103),
            velocity,
        )
        visited.add(p2_robots[j][0])

    if len(visited) == len(p2_robots):
        res = seconds
        break

    seconds += 1

print(res)
