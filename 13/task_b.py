from functools import cmp_to_key

def compare(left, right):
    if isinstance(left, list) and isinstance(right, list):
        if len(left) == 0 and len(right) == 0:
            return 0
        elif len(left) == 0:
            return -1
        elif len(right) == 0:
            return 1
        if (res := compare(left[0], right[0])) != 0:
            return res
        return compare(left[1:], right[1:])
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    else:
        if left == right:
            return 0
        else:
            return -1 if left < right else 1
        

packets = [
    [[2]],
    [[6]],
]
for line in open("input.txt"):
    if line == "\n":
        continue
    packets.append(eval(line.strip()))
packets.sort(key=cmp_to_key(compare))

i1 = packets.index([[2]]) + 1
i2 = packets.index([[6]]) + 1
print(i1 * i2)