import numpy as np

def can_move(shape, x, y):
    if y < 0:
        return False
    if x < 0 or x + shape.shape[1] > cave.shape[1]:
        return False
    overlap = (cave[y:y + shape.shape[0], x:x + shape.shape[1]] & shape).sum()
    if overlap > 0:
        return False
    return True

shapes = [
    np.array([[True, True, True, True]], dtype=bool),
    np.array([[False, True, False], [True, True, True], [False, True, False]], dtype=bool),
    np.array([[True, True, True], [False, False, True], [False, False, True]], dtype=bool),
    np.array([[True], [True], [True], [True]], dtype=bool),
    np.array([[True, True], [True, True]], dtype=bool),
]

jets = open("input.txt").readline().strip()
cave = np.zeros((10000, 7), dtype=bool)
jet_index = 0
max_y = 0
num_stopped = 0
max_rocks = 2022

while num_stopped < max_rocks:
    for shape in shapes:
        # Begins to fall
        y = max_y + 3
        x = 2

        while True:
            # Moved by jet
            dx = -1 if jets[jet_index % len(jets)] == "<" else 1
            if can_move(shape, x + dx, y):
                x += dx
            jet_index += 1

            # Move downwards
            if can_move(shape, x, y - 1):
                y -= 1
            else:
                cave[y:y + shape.shape[0], x:x + shape.shape[1]] |= shape
                max_y = max(max_y, y + shape.shape[0])
                num_stopped += 1
                break

        if num_stopped >= max_rocks:
            break
        
print(num_stopped, max_y)