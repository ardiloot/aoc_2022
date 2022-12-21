
class Monkey:

    def __init__(self):
        self.value = None
        self.op = None
        self.children = []

    def get_value(self):
        if self.value is not None:
            return self.value
        
        v1 = monkeys[self.children[0]].get_value()
        v2 = monkeys[self.children[1]].get_value()
        if self.op == "+":
            return v1 + v2
        elif self.op == "-":
            return v1 - v2
        elif self.op == "*":
            return v1 * v2
        elif self.op == "/":
            return v1 // v2
        else:
            raise NotImplementedError()

monkeys = {}
for line in open("input.txt"):
    name, formula = line.strip().split(": ")
    monkey = Monkey()
    if " + " in formula or " - " in formula or " * " in formula or " / " in formula:
        child1, op, child2 = formula.split(" ")
        monkey.op = op
        monkey.children = [child1, child2]
    else:
        monkey.value = int(formula)
    monkeys[name] = monkey

print(monkeys["root"].get_value())