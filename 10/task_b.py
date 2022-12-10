import numpy as np

def score():
    x = (cycle - 1) % 40
    y = (cycle - 1) // 40
    if (abs(x - value) <= 1):
        res[y, x] = True

value = 1
cycle = 1
res = np.zeros((6, 40), dtype=bool)

for line in open("input.txt"):
    if line.startswith("noop"):
        score()
        cycle += 1
    else:
        for i in range(2):
            score()
            cycle += 1
        value += int(line[5:].strip())
score()

for r in res:
    print("".join("#" if v else "." for v in r))