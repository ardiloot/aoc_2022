
priority = [chr(ord('a') + i) for i in range(26)] + [chr(ord('A') + i) for i in range(26)]
res = 0
lines = list(map(str.strip, open("input.txt").readlines()))
for i in range(0, len(lines), 3):
    c = (set(lines[i]) & set(lines[i + 1]) & set(lines[i + 2])).pop()
    res += priority.index(c) + 1
print(res)