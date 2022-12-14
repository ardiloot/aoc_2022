import numpy as np

g = np.zeros((1000, 1000), dtype=bool)
for line in open("input.txt"):
    points = [tuple(map(int, p.split(","))) for p in line.strip().split(" -> ")]
    for i in range(1, len(points)):
        (x1, y1), (x2, y2) = points[i - 1], points[i]
        g[min(y1, y2):max(y1, y2) + 1, min(x1, x2):max(x1, x2) + 1] = True


full = False
sand_units = 0
while not full:
    sx, sy = 500, 0
    while True:
        new_pos = None
        for dx, dy in [(0, 1), (-1, 1), (1, 1)]:
            nx, ny = sx + dx, sy + dy
            if ny >= g.shape[0]:
                full = True
                break
            if g[ny, nx]:
                continue
            new_pos = (nx, ny)
            break

        if full:
            break

        if new_pos is None:
            g[sy, sx] = True
            sand_units += 1
            break
        else:
            sx, sy = new_pos
print(sand_units)