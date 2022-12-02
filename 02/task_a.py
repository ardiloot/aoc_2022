
win = {"🪨✀", "🧻🪨", "✀🧻"}
amap = {"A": "🪨", "B": "🧻", "C": "✀"}
bmap = {"X": "🪨", "Y": "🧻", "Z": "✀"}

total_score = 0
for line in open("input.txt"):
    a, b = line.strip().split(" ")
    a = amap[a]
    b = bmap[b]
    score = {"🪨": 1, "🧻": 2, "✀": 3}[b]
    if a == b:
        score += 3
    elif b + a in win:
        score += 6
    total_score += score
print(total_score)