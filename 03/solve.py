d = open("input.txt").read().splitlines()
a, b = [[(s[0], int(s[1:])) for s in x.split(",")] for x in d]
dx = {'R': 1, 'L': -1, 'U': 0, 'D': 0}
dy = {'R': 0, 'L': 0, 'U': 1, 'D': -1}
def run(x):
    i = 0
    p = [0, 0]
    v = {} 
    for (d, n) in x:
        for _ in range(n):
            p[0] += dx[d]
            p[1] += dy[d]
            i += 1
            if tuple(p) not in v:
                v[tuple(p)] = i
    return v
v1, v2 = run(a), run(b)
v = set(v1.keys() & v2.keys())
print(min(abs(x) + abs(y) for x, y in v))
print(min(v1[(x, y)] + v2[(x, y)] for x, y in v))
