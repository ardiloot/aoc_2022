import numpy as np

def is_visible(mm):
    top = np.maximum.accumulate(mm, axis=0)
    left = np.maximum.accumulate(mm, axis=1)
    visible = np.zeros(mm.shape, dtype=bool)
    visible[0, :] = visible[:, 0] = True
    visible[1:, :] |= mm[1:, :] > top[:-1, :]
    visible[:, 1:] |= mm[:, 1:] > left[:, :-1]
    return visible

lines = map(str.strip, open("input.txt").readlines())
m = np.array(list(map(list, lines)), dtype=int)
visible = (is_visible(m)) | (is_visible(m[::-1, ::-1])[::-1, ::-1])
print(visible.sum())
