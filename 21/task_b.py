
class Monkey:

    def __init__(self, name):
        self.name = name
        self.value = None
        self.op = None
        self.children = []
        self.parent = None

    def get_value(self):
        if self.name == "humn":
            raise ValueError()
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

    def get_reverse_value(self, from_name):
        if self.value is not None:
            return self.value

        v_parent = monkeys[self.parent].get_reverse_value(self.name)
        if len(self.children) == 0:
            return v_parent

        v_other_child = monkeys[self.children[1 if from_name == self.children[0] else 0]].get_value()
        if self.op == "+":
            res = v_parent - v_other_child
        elif self.op == "*":
            res = v_parent // v_other_child
        elif self.op == "-":
            if from_name == self.children[0]:
                res = v_parent + v_other_child
            else:
                res = -v_parent + v_other_child
        elif self.op == "/":
            if from_name == self.children[0]:
                res = v_parent * v_other_child
            else:
                res = v_parent // v_other_child
        else:
            raise NotImplementedError()
        return res

monkeys = {}
for line in open("input.txt"):
    name, formula = line.strip().split(": ")
    monkey = Monkey(name)
    if " + " in formula or " - " in formula or " * " in formula or " / " in formula:
        child1, op, child2 = formula.split(" ")
        monkey.op = op
        monkey.children = [child1, child2]
    else:
        monkey.value = int(formula)
    monkeys[name] = monkey


# Update parents
for m in monkeys.values():
    for ch in m.children:
        monkeys[ch].parent = m.name

desired_value = monkeys[monkeys["root"].children[1]].get_value()
monkeys["root"].value = desired_value
monkeys["humn"].value = None
print(monkeys["humn"].get_reverse_value(""))

