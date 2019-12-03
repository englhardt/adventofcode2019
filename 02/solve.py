import itertools

def run(x, a, b):
    d = x.copy()
    d[1], d[2] = a, b
    i = 0
    while True:
        if d[i] == 1:
            d[d[i+3]] = d[d[i+1]] + d[d[i+2]]
        elif d[i] == 2:
            d[d[i+3]] = d[d[i+1]] * d[d[i+2]]
        else:
            assert d[i] == 99
            break
        i += 4
    return d[0]
d = list(map(int, open("input.txt").read().split(",")))
print(run(d, 12, 2))
for a, b in itertools.product(range(100), range(100)):
    if run(d, a, b) == 19690720:
        print(100 * a + b)
