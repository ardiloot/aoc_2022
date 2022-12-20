import numpy as np

def display():
    index = 0
    for j in range(len(values)):
        print(values[index], end=" ")
        index = next[index]
    print()


values = np.loadtxt("input.txt", dtype=np.int64)
values *= 811589153

# Linked list
next = np.arange(len(values)) + 1
prev = np.arange(len(values)) - 1
next[-1] = 0
prev[0] = len(values) - 1

for iteration in range(10):
    for i, v in enumerate(values):
        
        # Remove i from list
        tmp_next, tmp_prev = next[i], prev[i]
        prev[tmp_next], next[tmp_prev] = tmp_prev, tmp_next
        next[i], prev[i] = -1, -1

        # Find move after location
        if v > 0:
            move_after = tmp_next
            for j in range((v - 1) % (len(values) - 1)):
                move_after = next[move_after]
        else:
            move_after = prev[tmp_prev]
            for j in range((-v - 1) % (len(values) - 1)):
                move_after = prev[move_after]
        
        # Move
        tmp_mt_next = next[move_after]
        prev[i], next[move_after] = move_after, i
        prev[tmp_mt_next], next[i] = i, tmp_mt_next
        # display()

res = 0
index = list(values).index(0)
for i in range(3001):
    if i > 0 and i % 1000 == 0:
        res += int(values[index])
    index = next[index]
print(res)
