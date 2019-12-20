import math
from collections import defaultdict

def calc(d, f):
    need = {"FUEL": f}
    have = defaultdict(int)
    while list(need.keys()) != ["ORE"]:
        for x in d:
            a, c = x[-1]
            if c in need and c != "ORE":
                required_reactions = math.ceil(need[c] / a)
                if a * required_reactions < need[c]:
                    need[c] -= a * required_reactions
                else:
                    have[c] += max(0, (a * required_reactions) - need[c])
                    del need[c]
                for (a_y, c_y) in x[:-1]:
                    if a_y * required_reactions <= have[c_y]:
                        have[c_y] -= a_y * required_reactions
                    else:
                        req_amount = a_y * required_reactions - have[c_y]
                        have[c_y] = 0
                        need[c_y] = need.get(c_y, 0) + req_amount
    return need["ORE"]

d = [x.replace(" => ", ", ").split(", ") for x in open("input.txt").read().splitlines()]
d_react = [[y.split(" ")[1] for y in x] for x in d]
d = [[y.split(" ") for y in x] for x in d]
d = [[[int(y[0]), y[1]] for y in x] for x in d]

print(calc(d, 1))

a, b = 1, 10**12
while b - a >= 2:
    mid = a + (b - a) // 2
    if calc(d, mid) > 10**12:
        b = mid
    else:
        a = mid
print(a)
