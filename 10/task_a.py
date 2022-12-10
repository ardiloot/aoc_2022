

def score():
    global res
    if (cycle - 20) % 40 == 0:
        res += cycle * value

value = 1
cycle = 1
res = 0
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
print(res)