
win = {"🪨✀", "🧻🪨", "✀🧻"}
amap = {"A": "🪨", "B": "🧻", "C": "✀"}
wmap = {"🪨": "🧻", "🧻": "✀", "✀": "🪨"}
lmap = {"🪨": "✀", "🧻": "🪨", "✀": "🧻"}

total_score = 0
for line in open("input.txt"):
    a, b = line.strip().split(" ")
    a = amap[a]
    b = {"X": lmap[a], "Y": a, "Z": wmap[a]}[b]
    score = {"🪨": 1, "🧻": 2, "✀": 3}[b]
    if a == b:
        score += 3
    elif b + a in win:
        score += 6
    total_score += score
print(total_score)