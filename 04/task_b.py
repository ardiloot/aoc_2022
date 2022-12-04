import re

res = 0
for line in open("input.txt"):
    i1, i2, j1, j2 = map(int, re.match("(\d*)-(\d*),(\d*)-(\d*)", line).groups())
    if i1 <= j1 <= i2 or i1 <= j2 <= i2 or j1 <= i1 <= j2 or j1 <= i2 <= j2:
        res += 1
print(res)