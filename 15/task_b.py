import re
import numpy as np

def solve():
    maxv = 4000000
    for y in range(maxv + 1):
        edges = []
        for i, (sx, sy) in enumerate(sensors):
            dx = min_dist[i] - abs(sy - y)
            if dx < 0:
                continue
            edges.append((sx - dx, False))
            edges.append((sx + dx, True))
        edges.sort()
        if len(edges) <= 0:
            continue

        if edges[0][0] > 0 or edges[-1][0] < maxv:
            raise NotImplementedError()

        num_active = 0
        for ex, is_end in edges:
            num_active += -1 if is_end else 1
            if num_active == 0 and ex <= maxv:
                return int(ex + 1) * maxv + y


sensors = []
beacons = []
for line in open("input.txt"):
    sx, sy, bx, by = map(int, 
        re.match("Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)", line.strip()).groups())
    sensors.append((sx, sy))
    beacons.append((bx, by))
sensors = np.array(sensors, dtype=int)
beacons = np.array(beacons, dtype=int)
min_dist = np.abs(sensors[:, 0] - beacons[:, 0]) + np.abs(sensors[:, 1] - beacons[:, 1])

solve()

