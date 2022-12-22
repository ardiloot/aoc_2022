import numpy as np

VOID = 0
OPEN = 1
WALL = 2
DIRS = [
    (0, 1),     # Right
    (1, 0),     # Down
    (0, -1),    # Left
    (-1, 0),    # Up
]

def parse_instructions(instruction_line):
    cur_instruction = ""
    instructions = []
    for char in instruction_line + ".":
        if char in ["R", "L", "."]:
            if cur_instruction != "":
                instructions.append(int(cur_instruction))
                cur_instruction = ""
            if char == ".":
                break
            instructions.append(char)
        else:
            cur_instruction += char
    return instructions

def read_input():
    g = np.zeros((201, 201), dtype=np.int32)
    with open("input.txt") as file:
        for i, line in enumerate(file):
            for j, char in enumerate(line[:-1]):
                if char == "#":
                    g[i, j] = WALL
                elif char == ".":
                    g[i, j] = OPEN
            if line == "\n":
                break
        instruction_line = file.readline().strip()

    instructions = parse_instructions(instruction_line)

    # Find starting pos
    loc = [0, 0, 0] # (row, col, dir)
    for i in range(g.shape[1]):
        if g[0, i] == OPEN:
            loc[1] = i
            break

    return g, instructions, loc


if __name__ == "__main__":
    g, instructions, loc = read_input()

    for cmd in instructions:
        if cmd == "R":
            loc[2] = (loc[2] + 1) % 4
            continue
        elif cmd == "L":
            loc[2] = (loc[2] + 4 - 1) % 4
            continue
        else:
            for _ in range(cmd):
                drow, dcol = DIRS[loc[2]]
                new_row = loc[0] + drow
                new_col = loc[1] + dcol
                if g[new_row, new_col] == VOID:
                    if dcol == 0:
                        # Moving up - down
                        values = np.nonzero(g[:, new_col] != VOID)[0]
                        new_row = values[0] if drow > 0 else values[-1]
                    else:
                        # Moving left - right
                        values = np.nonzero(g[new_row, :] != VOID)[0]
                        new_col = values[0] if dcol > 0 else values[-1]

                if g[new_row, new_col] == WALL:
                    break
                loc[0], loc[1] = new_row, new_col

res = 1000 * (loc[0] + 1) + 4 * (loc[1] + 1) + loc[2]
print(res)
