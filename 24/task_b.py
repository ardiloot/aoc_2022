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


def solve(ci, cj, steps, to_dest):
    # print(ci, cj, steps)
    if steps > 900:
        return 100000

    if to_dest and ci + 1 == num_rows:
        return steps
    if not to_dest and ci == 0:
        return steps

    cache_key = (ci, cj, steps, to_dest)
    if cache_key in cache:
        return cache[cache_key]


    res = 100000
    for (di, dj) in dirs.values():
        ni, nj = ci + di, cj + dj
        if wall_map.get((ni, nj), True):
            continue
        if not can_be(ni, nj, steps + 1):
            continue
        res = min(res, solve(ni, nj, steps + 1, to_dest))
    
    if can_be(ci, cj, steps + 1):
        res = min(res, solve(ci, cj, steps + 1, to_dest))

    cache[cache_key] = res
    return res


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
        wall_map[i, j] = is_wall

dest_j = [j for j in range(num_cols) if not wall_map[num_rows - 1, j]][0]
start_j = [j for j in range(num_cols) if not wall_map[0, j]][0]

steps1 = solve(0, start_j, 0, True)
steps2 = solve(num_rows - 1, dest_j, steps1, False)
steps3 = solve(0, start_j, steps2, True)
print(steps1, steps2, steps3)
