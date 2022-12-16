import re


def solve(node, minutes, opened):
    key = (node, minutes, tuple(opened))
    if key in dp:
        return dp[key]

    if minutes <= 0:
        return 0
    
    # Try to open valve
    res = 0
    if valves[node]["flowrate"] > 0 and node not in opened:
        res = solve(node, minutes - 1, sorted(opened + [node]))

    # Move to other valve
    for to in valves[node]["links"]:
        res = max(res, solve(to, minutes - 1, opened))

    res += sum(valves[n]["flowrate"] for n in opened)
    dp[key] = res
    return res

valves = {}
for line in open("input.txt"):
    node, rate, links = re.match("Valve (.*) has flow rate=(.*); tunnels? leads? to valves? (.*)", line.strip()).groups()
    valves[node] = {
        "flowrate": int(rate),
        "links": links.split(", "),
    }

dp = {}
res = solve("AA", 30, [])
print(res)