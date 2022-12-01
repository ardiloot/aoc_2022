
elves = []
with open("input.txt", "r") as file:
    items = []
    for line in file.readlines() + ["\n"]:
        if line != "\n":
            items.append(int(line.strip()))
        else:
            elves.append(sum(items))
            items = []
            
print(sum(sorted(elves)[-3:]))
