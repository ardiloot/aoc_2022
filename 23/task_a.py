import numpy as np

dirs = [
    (-1, 0), # North
    (1, 0),  # South
    (0, -1), # west
    (0, 1),  # East
]

surroundings = [
    [(-1, -1), (-1, 0), (-1, 1)],
    [(1, -1), (1, 0), (1, 1)],
    [(-1, -1), (0, -1), (1, -1)],
    [(-1, 1), (0, 1), (1, 1)],
]

def elf_nearby(i, j):
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue
            if (i + di, j + dj) in elves:
                return True
    return False

def is_direction_free(i, j, direction):
    for di, dj in surroundings[direction]:
        if (i + di, j + dj) in elves:
            return False
    return True


elves = set()
for i, line in enumerate(open("input.txt")):
    for j, char in enumerate(line.strip()):
        if char == "#":
            elves.add((i, j))


for round_nr in range(10):
    direction_start = round_nr % 4

    # Propose moving
    planned_moves = {} # [to] = from
    duplicates = set()
    for elf in elves:
        ci, cj = elf
        if not elf_nearby(ci, cj):
            continue
        for dir_nr in range(4):
            direction = (direction_start + dir_nr) % 4
            if is_direction_free(ci, cj, direction):
                di, dj = dirs[direction]
                ni, nj = ci + di, cj + dj
                if (ni, nj) in planned_moves:
                    duplicates.add((ni, nj))
                planned_moves[(ni, nj)] = elf
                break
        
    # Move
    for pos_to, pos_from in planned_moves.items():
        if pos_to in duplicates:
            continue
        elves.remove(pos_from)
        elves.add(pos_to)

positions = np.array(list(elves))
area = np.prod(positions.max(axis=0) - positions.min(axis=0) + 1)
print(area - len(elves))
