import numpy as np

def can_move(shape, cave, x, y):
    if y < 0:
        return False
    if x < 0 or x + shape.shape[1] > cave.shape[1]:
        return False
    overlap = (cave[y:y + shape.shape[0], x:x + shape.shape[1]] & shape).sum()
    return overlap == 0

def solve():

    cave = np.zeros((100000, 7), dtype=bool)
    jet_index = 0
    max_y = 0
    num_stopped = 0
    max_rocks = 1000000000000
    dp = {}

    while True:
        for si, shape in enumerate(shapes):
            # Begins to fall
            y = max_y + 3
            x = 2

            while True:
                # Moved by jet
                dx = -1 if jets[jet_index % len(jets)] == "<" else 1
                if can_move(shape, cave, x + dx, y):
                    x += dx
                jet_index += 1
                if jet_index >= len(jets):
                    jet_index = 0

                # Move downwards
                if can_move(shape, cave, x, y - 1):
                    y -= 1
                else:
                    cave[y:y + shape.shape[0], x:x + shape.shape[1]] |= shape
                    max_y = max(max_y, y + shape.shape[0])
                    num_stopped += 1

                    # Save state
                    top = []
                    for r in cave[max(0, max_y - 100):max_y][::-1]:
                        top.append("".join("#" if v else "." for v in r))
                    top = "\n".join(top)
        
                    state = (top, si, jet_index)
                    if state in dp:
                        t_period = num_stopped - dp[state][0]
                        h_period = max_y - dp[state][1]
                        if (max_rocks - num_stopped) % t_period == 0:
                            n = (max_rocks - num_stopped) // t_period
                            return max_y + n * h_period
                    dp[state] = num_stopped, max_y
                    break

shapes = [
    np.array([[True, True, True, True]], dtype=bool),
    np.array([[False, True, False], [True, True, True], [False, True, False]], dtype=bool),
    np.array([[True, True, True], [False, False, True], [False, False, True]], dtype=bool),
    np.array([[True], [True], [True], [True]], dtype=bool),
    np.array([[True, True], [True, True]], dtype=bool),
]

jets = open("input.txt").readline().strip()
res = solve()
print(res)
