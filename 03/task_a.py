
priority = [chr(ord('a') + i) for i in range(26)] + [chr(ord('A') + i) for i in range(26)]
res = 0
for line in open("input.txt"):
    line = line.strip()
    m = len(line) // 2
    c = (set(line[:m]) & set(line[m:])).pop()
    res += priority.index(c) + 1
print(res)