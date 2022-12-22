import numpy as np

OPEN = 1
WALL = 2
DIRS = [
    (0, 1),     # Right
    (1, 0),     # Down
    (0, -1),    # Left
    (-1, 0),    # Up
]

# TODO: find values automatically
CELL_GRID_ROWS = 4
CELL_GRID_COLS = 3
CUBE_SIZE = 50
CELL_MAP = {
    1: (slice(0, CUBE_SIZE), slice(CUBE_SIZE, 2 * CUBE_SIZE)),
    2: (slice(0, CUBE_SIZE), slice(2 * CUBE_SIZE, 3 * CUBE_SIZE)),
    3: (slice(CUBE_SIZE, 2 * CUBE_SIZE), slice(CUBE_SIZE, 2 * CUBE_SIZE)),
    4: (slice(2 * CUBE_SIZE, 3 * CUBE_SIZE), slice(0, CUBE_SIZE)),
    5: (slice(2 * CUBE_SIZE, 3 * CUBE_SIZE), slice(CUBE_SIZE, 2 * CUBE_SIZE)),
    6: (slice(3 * CUBE_SIZE, 4 * CUBE_SIZE), slice(0, CUBE_SIZE)),
}
WRAPING = {
    1: [(2, 0), (3, 0), (4, 2), (6, 3)], # cell: [(new_cell, new_cell_direction), ...]
    2: [(5, 2), (3, 3), (1, 0), (6, 0)],
    3: [(2, 1), (5, 0), (4, 1), (1, 0)],
    4: [(5, 0), (6, 0), (1, 2), (3, 3)],
    5: [(2, 2), (6, 3), (4, 0), (3, 0)],
    6: [(5, 1), (2, 0), (1, 1), (4, 0)],
}


class Cell:
    def __init__(self, rownr, colnr, values):
        self.rownr = rownr
        self.colnr = colnr
        self.values = values

class Location:

    def __init__(self):
        self.cell = 0
        self.row = 0
        self.col = 0
        self.dir = 0

    def turn_right(self):
        self.dir = (self.dir + 1) % 4
    
    def turn_left(self):
        self.dir = (self.dir + 4 - 1) % 4

    def next_pos(self):
        drow, dcol = DIRS[self.dir]
        return self.row + drow, self.col + dcol


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
    g = np.zeros((CELL_GRID_ROWS * CUBE_SIZE, CELL_GRID_COLS * CUBE_SIZE), dtype=np.int32)
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

    g_rows, g_cols = np.meshgrid(range(g.shape[0]), range(g.shape[1]), indexing="ij")
    cells = {}
    for cell_nr, mask in CELL_MAP.items():
        cells[cell_nr] = Cell(g_rows[mask], g_cols[mask], g[mask])
    instructions = parse_instructions(instruction_line)

    return cells, instructions


if __name__ == "__main__":
    cells, instructions = read_input()
    loc = Location()
    loc.cell, loc.row, loc.col = 1, 0, 0 # TODO: find automatically

    for cmd in instructions:
        if cmd == "R":
            loc.turn_right()
        elif cmd == "L":
            loc.turn_left()
        else:
            for _ in range(cmd):
                new_cell, new_dir = loc.cell, loc.dir
                new_row, new_col = loc.next_pos()

                out_of_cell = min(new_col, new_row) < 0 or max(new_col, new_row) >= CUBE_SIZE
                if out_of_cell:
                    new_cell, new_cell_dir = WRAPING[loc.cell][loc.dir]
                    if loc.dir == 0:
                        if new_cell_dir == 0:
                            new_col = 0
                        elif new_cell_dir == 1:
                            new_col = loc.row
                            new_row = CUBE_SIZE - 1
                            new_dir = 3
                        elif new_cell_dir == 2:
                            new_row = CUBE_SIZE - 1 - loc.row
                            new_col = CUBE_SIZE - 1
                            new_dir = 2
                        else:
                            raise NotImplementedError()
                    elif loc.dir == 1:
                        if new_cell_dir == 0:
                            new_row = 0
                        elif new_cell_dir == 3:
                            new_col = CUBE_SIZE - 1
                            new_row = loc.col
                            new_dir = 2
                        else:
                            raise NotImplementedError()
                    elif loc.dir == 2:
                        if new_cell_dir == 0:
                            new_col = CUBE_SIZE - 1
                        elif new_cell_dir == 1:
                            new_row = 0
                            new_col = loc.row
                            new_dir = 1
                        elif new_cell_dir == 2:
                            new_col = 0
                            new_row = CUBE_SIZE - 1 - loc.row
                            new_dir = 0
                        else:
                            raise NotImplementedError()
                    elif loc.dir == 3:
                        if new_cell_dir == 0:
                            new_row = CUBE_SIZE - 1
                        elif new_cell_dir == 3:
                            new_row = loc.col
                            new_col = 0
                            new_dir = 0
                        else:
                            raise NotImplementedError()
    
                if cells[new_cell].values[new_row, new_col] == WALL:
                    break
                loc.row, loc.col = new_row, new_col
                loc.cell, loc.dir = new_cell, new_dir


cell = cells[loc.cell]
row = cell.rownr[loc.row, loc.col]
col = cell.colnr[loc.row, loc.col]
res = 1000 * (row + 1) + 4 * (col + 1) + loc.dir
print(res)
