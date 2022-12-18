import numpy as np

DIRS = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

def is_internal(x, y, z):
    if min(x, y, x) < 0 or max(x, y, z) > 20:
        return False
    if (x, y, z) in internal:
        return internal[x, y, z]
    visited.add((x, y, z))

    res = True
    for dx, dy, dz in DIRS:
        nx, ny, nz = x + dx, y + dy, z + dz
        if (nx, ny, nz) in g or (nx, ny, nz) in visited:
            continue
        if not is_internal(nx, ny, nz):
            res = False
            break
    internal[x, y, z] = res
    return res

scan = np.loadtxt("input.txt", delimiter=",", dtype=int)
g = {}
for x, y, z in scan:
    g[x, y, z] = True
internal = {}

res = 0
for x, y, z in scan:
    for dx, dy, dz in DIRS:
        nx, ny, nz = x + dx, y + dy, z + dz
        visited = set()
        if is_internal(nx, ny, nz):
            continue
        if (nx, ny, nz) not in g:
            res += 1
print(res)