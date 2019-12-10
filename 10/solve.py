import math
import operator
from collections import defaultdict

def reachable(s, d):
    targets = defaultdict(list)
    for t in d:
        if t == s:
            continue
        dx = t[0] - s[0]
        dy = t[1] - s[1]
        l = math.gcd(abs(dx), abs(dy))
        targets[(int(dx / l), int(dy / l))].append((t, l))
    for v in targets.values():
        v.sort(key=operator.itemgetter(1))
    return targets

d = open("input.txt").read()
d = [(x, y) for y, line in enumerate(d.split("\n"))
         for x, c in enumerate(line) if c == "#"]

num_hit = -1
best = None
for s in d:
    r = reachable(s, d)
    if len(r) > num_hit:
        num_hit = len(r)
        best = s
print(num_hit)

# We have more than 200 directions, so not even a full sweep is required.
# We do not have to actually eliminate asteroids since we only shoot in
# each direction once.
angle = lambda x: (math.degrees(math.atan2(x[1], x[0])) + 90) % 360
r = reachable(best, d)
dir_sorted = list(r.keys())
dir_sorted.sort(key=angle)
x, y = r[dir_sorted[199]][0][0]
print(x * 100 + y)
