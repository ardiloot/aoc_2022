import itertools

symbols = {
    "=": -2,
    "-": -1,
    "0": 0,
    "1": 1,
    "2": 2,
}
symbol_list = list(symbols.keys())

def to_dec(line):
    base = 1
    res = 0
    for i in range(len(line)):
        res += symbols[line[len(line) - i - 1]] * base
        base *= 5
    return res

def to_snafu(dec, place):
    if place < 0:
        if dec == 0:
            print("Solution", "".join(snafu_res).lstrip("0"))
        return

    snafu_res.append("")
    for symbol, value in symbols.items():
        this = value * (5 ** place)

        next_value = dec - this
        next_delta_max = 2 * (5 ** (place)) if place > 0 else 0
        if abs(next_value) > next_delta_max:
            continue
        snafu_res[-1] = symbol
        to_snafu(next_value, place - 1)
    snafu_res.pop(-1)

fuel_needed = 0
for line in open("input.txt"):
    fuel_needed += to_dec(line.strip())
snafu_res = []
to_snafu(fuel_needed, 20)
