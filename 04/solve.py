from collections import Counter
r = range(146810, 612564)
p1 = lambda x: list(x) == sorted(x) and any(x >= 2 for x in Counter(x).values())
p2 = lambda x: list(x) == sorted(x) and any(x == 2 for x in Counter(x).values())
print(sum(map(lambda x: p1(str(x)), r)))
print(sum(map(lambda x: p2(str(x)), r)))
