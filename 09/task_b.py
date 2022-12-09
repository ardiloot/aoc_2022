
directions = {
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1),
    "U": (-1, 0),
}

knots = [[0, 0] for _ in range(10)]
visited = set()

for line in open("input.txt"):
    direction = directions[line[0]]
    steps = int(line[1:].strip())
    for s in range(steps):
        head = knots[0]
        head[0] += direction[0]
        head[1] += direction[1]
        for k in range(1, len(knots)):
            h = knots[k - 1]
            t = knots[k]
            if max(abs(h[0] - t[0]), abs(h[1] - t[1])) > 1:
                if h[0] == t[0]:
                    t[1] += 1 if h[1] > t[1] else -1
                elif h[1] == t[1]:
                    t[0] += 1 if h[0] > t[0] else -1
                else:
                    t[0] += 1 if h[0] > t[0] else -1
                    t[1] += 1 if h[1] > t[1] else -1
        visited.add(tuple(knots[-1]))

print(len(visited))

