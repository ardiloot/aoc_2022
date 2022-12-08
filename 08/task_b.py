import numpy as np

lines = map(str.strip, open("input.txt").readlines())
m = np.array(list(map(list, lines)), dtype=int)
max_score = 0

for (i1, i2), v in np.ndenumerate(m):
    distances = []
    for d1, d2 in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        dist = 0
        for d in range(1, max(m.shape) + 1):
            j1 = i1 + d * d1
            j2 = i2 + d * d2
            if j1 < 0 or j1 >= m.shape[0] or j2 < 0 or j2 >= m.shape[1]:
                break
            dist += 1
            if m[j1, j2] >= v:
                break
        distances.append(dist)

    score = 1
    for dist in distances:
        score *= dist
    max_score = max(max_score, score)
    
print(max_score)