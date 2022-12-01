
max_calories = 0
with open("input_test.txt", "r") as file:
    items = []
    for line in file.readlines() + ["\n"]:
        if line != "\n":
            items.append(int(line.strip()))
        else:
            max_calories = max(max_calories, sum(items))
            items = []
            
print(max_calories)
