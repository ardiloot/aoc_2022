import re
import numpy as np

sensors = []
beacons = []
beacon_set = set()
for line in open("input.txt"):
    sx, sy, bx, by = map(int, 
        re.match("Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)", line.strip()).groups())
    sensors.append((sx, sy))
    beacons.append((bx, by))
    beacon_set.add((bx, by))

sensors = np.array(sensors, dtype=int)
beacons = np.array(beacons, dtype=int)
min_dist = np.abs(sensors[:, 0] - beacons[:, 0]) + np.abs(sensors[:, 1] - beacons[:, 1])

res = 0
target_y = 2000000
for bx, by in beacon_set:
    if by == target_y:
        res -= 1

xs = np.arange(-30000000, 30000000, dtype=int)
t = np.abs(xs[:, np.newaxis] - sensors[:, 0][np.newaxis, :]) + np.abs(sensors[:, 1] - target_y)
res += (t <= min_dist).any(axis=1).sum()
print(res)
