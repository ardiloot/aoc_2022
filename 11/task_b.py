
monkeys = []
with open("input.txt") as file:
    while True:
        line = file.readline() # Monkey ...
        if line == "":
            break
        # nr = int(line.strip()[7:-1])
        items = list(map(int, file.readline().strip()[16:].split(", ")))
        operation = file.readline().strip()[17:]
        divisable = int(file.readline().strip()[19:])
        target_true = int(file.readline().strip()[25:])
        target_false = int(file.readline().strip()[26:])
        file.readline()

        monkeys.append({
            "items": items,
            "operation": operation,
            "divisable": divisable,
            "target_true": target_true,
            "target_false": target_false,
        })
        

max_div = 1
for monkey in monkeys:
    max_div *= monkey["divisable"]

inpection_counts = [0] * len(monkeys)
for round_nr in range(10000):
    for i, monkey in enumerate(monkeys):
        inpection_counts[i] += len(monkey["items"])
        for item in monkey["items"]:
            new = eval(monkey["operation"].replace("old", str(item))) % max_div
            target = monkey["target_true"] if new % monkey["divisable"] == 0 else monkey["target_false"]
            monkeys[target]["items"].append(new)
        monkey["items"] = []

top = sorted(inpection_counts)[-2:]
print(top[0] * top[1])
