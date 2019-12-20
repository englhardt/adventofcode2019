import math
import numpy as np
import re

def sim(mp, mv, axis=None, n=None):
    mp_start = mp.copy()
    mv_start = mv.copy()
    s = 0
    while True:
        v_change = []
        for i in range(len(mp)):
            c = np.zeros(3, dtype=int)
            for j in range(len(mp)):
                if i != j:
                    x = np.array([int(x) or -1 for x in mp[i] < mp[j]])
                    x[mp[i] == mp[j]] = 0
                    c += x
            v_change.append(c)
        mv += v_change
        mp += mv
        s += 1
        if axis is not None and (mp[:, axis] == mp_start[:, axis]).all() \
            and (mv[:, axis] == mv_start[:, axis]).all():
            return s
        if n is not None and s == n:
            return mp, mv
mp = np.array([list(map(int, re.findall(r'-?\d+', x))) for x in open("input.txt").read().splitlines()])
mv = np.array([[0, 0, 0] for _ in range(len(mp))])

mp_sim, mv_sim = sim(mp.copy(), mv.copy(), n=1000)
print(sum(abs(mp_sim).sum(axis=1) * abs(mv_sim).sum(axis=1)))

x_cycle = sim(mp.copy(), mv.copy(), 0)
y_cycle = sim(mp.copy(), mv.copy(), 1)
z_cycle = sim(mp.copy(), mv.copy(), 2)
a = (x_cycle * y_cycle) // math.gcd(x_cycle, y_cycle)
print((z_cycle * a) // math.gcd(z_cycle, a))
