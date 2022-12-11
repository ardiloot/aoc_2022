
monkeys = []
with open("input.txt") as file:
    while True:
        line = file.readline()
        if line == "":
            break
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
        

inpection_counts = [0] * len(monkeys)
for round_nr in range(20):
    for i, monkey in enumerate(monkeys):
        inpection_counts[i] += len(monkey["items"])
        for item in monkey["items"]:
            new = eval(monkey["operation"].replace("old", str(item))) // 3
            target = monkey["target_true"] if new % monkey["divisable"] == 0 else monkey["target_false"]
            monkeys[target]["items"].append(new)
        monkey["items"] = []

top = sorted(inpection_counts)[-2:]
print(top[0] * top[1])