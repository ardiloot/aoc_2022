import re
from collections import defaultdict

stacks = defaultdict(list)
with open("input.txt") as file:
    for line in file:
        if line == "\n":
            break
        if "[" not in line:
            continue
        for i in range(len(line) // 4):
            name = line[4 * i: 4 * (i + 1)].strip("[] \n")
            if name == "":
                continue
            stacks[i + 1].insert(0, name)
  
    for line in file:
        n, fr, to = map(int, re.match("move (\d*) from (\d*) to (\d*)", line).groups())
        stacks[to].extend(stacks[fr][-n:][::-1])
        del stacks[fr][-n:]

    print("".join([stacks[i + 1][-1] for i in range(len(stacks))]))