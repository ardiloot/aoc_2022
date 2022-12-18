import numpy as np

scan = np.loadtxt("input.txt", delimiter=",", dtype=int)

g = {}
for x, y, z in scan:
    g[x, y, z] = True

res = 0
for x, y, z in scan:
    for dx, dy, dz in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
        if (x + dx, y + dy, z + dz) not in g:
            res += 1
print(res)