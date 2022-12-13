
def compare(left, right):
    if isinstance(left, list) and isinstance(right, list):
        if len(left) == 0 and len(right) == 0:
            return None
        elif len(left) == 0:
            return True
        elif len(right) == 0:
            return False

        if (res := compare(left[0], right[0])) is not None:
            return res
        return compare(left[1:], right[1:])
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    else:
        if left == right:
            return None
        else:
            return left < right

res = 0
number = 1
with open("input.txt") as file:
    while True:
        left = eval(file.readline().strip())
        right = eval(file.readline().strip())

        value = compare(left, right)
        if value:
            res += number

        line = file.readline()
        number += 1
        if line == "":
            break
print(res)