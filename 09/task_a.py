
directions = {
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1),
    "U": (-1, 0),
}

head = [0, 0]
tail = [0, 0]
visited = set()

for line in open("input.txt"):
    direction = directions[line[0]]
    steps = int(line[1:].strip())
    for s in range(steps):
        head[0] += direction[0]
        head[1] += direction[1]
        if max(abs(head[0] - tail[0]), abs(head[1] - tail[1])) > 1:
            if head[0] == tail[0]:
                tail[1] += direction[1]
            elif head[1] == tail[1]:
                tail[0] += direction[0]
            else:
                tail[0] += 1 if head[0] > tail[0] else -1
                tail[1] += 1 if head[1] > tail[1] else -1
        visited.add(tuple(tail))

print(len(visited))

