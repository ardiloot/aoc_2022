
line = open("input.txt").readline().strip()
n = 14
for i in range(0, len(line) - n):
    if len(set(line[i:i+n])) >= n:
        print(i + n)
        break