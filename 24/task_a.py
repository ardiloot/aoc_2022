from collections import defaultdict

dirs = {
    ">": (0, 1),
    "<": (0, -1),
    "^": (-1, 0),
    "v": (1, 0),
}

def can_be(i, j, steps):

    for dir, pos in row_blizzards[i]:
        new_pos = (((pos - 1) + steps * dirs[dir][1]) % (num_cols - 2)) + 1
        if new_pos == j:
            return False

    for dir, pos in col_blizzards[j]:
        new_pos = (((pos - 1) + steps * dirs[dir][0]) % (num_rows - 2)) + 1
        if new_pos == i:
            return False
    return True


def solve(ci, cj, steps):
    if steps > 500:
        return 100000
    if ci + 1 == num_rows:
        return steps

    cache_key = (ci, cj, steps)
    if cache_key in cache:
        return cache[cache_key]


    res = 100000
    for (di, dj) in dirs.values():
        ni, nj = ci + di, cj + dj
        if wall_map.get((ni, nj), True):
            continue
        if not can_be(ni, nj, steps + 1):
            continue
        res = min(res, solve(ni, nj, steps + 1))
    
    if can_be(ci, cj, steps + 1):
        res = min(res, solve(ci, cj, steps + 1))

    cache[cache_key] = res
    return res


start_j = 0
wall_map = {}
row_blizzards = defaultdict(list) # [dir, row] = []
col_blizzards = defaultdict(list)
num_rows = 0
num_cols = 0
cache = {}

for i, line in enumerate(open("input.txt")):
    num_rows = i + 1
    num_cols = len(line) - 1
    for j, char in enumerate(line.strip()):
        is_wall = False
        if char in [">", "<"]:
            row_blizzards[i].append((char, j))
        elif char in ["^", "v"]:
            col_blizzards[j].append((char, i))
        elif char == "#":
            is_wall = True
        else:
            if i == 0:
                start_j = j
        wall_map[i, j] = is_wall

res = solve(0, start_j, 0)
print(res)
