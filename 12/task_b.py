import numpy as np

def bfs(start):
    dist = np.full_like(heightmap, -1)
    dist[start] = 0
    queue = [start]
    while len(queue) > 0:
        f = queue.pop(0)
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            t = (f[0] + di, f[1] + dj)
            if t[0] < 0 or t[1] < 0 or t[0] >= heightmap.shape[0] or t[1] >= heightmap.shape[1]:
                continue
            if dist[t] >= 0:
                continue
            if heightmap[t] > heightmap[f] + 1:
                continue
            dist[t] = dist[f] + 1
            queue.append(t)
    if dist[destination] < 0:
        return 1000000
    return dist[destination]

destination = None
heightmap = []
starts = []
for i, line in enumerate(open("input.txt")):
    heights = []
    for j, s in enumerate(line.strip()):
        if s == "S":
            height = "a"
        elif s == "E":
            destination = (i, j)
            height = "z"
        else:
            height = s
        if height == "a":
            starts.append((i, j))
        heights.append(ord(height) - ord('a'))
    heightmap.append(heights)
heightmap = np.array(heightmap, dtype=int)

print(min(bfs(start) for start in starts))




