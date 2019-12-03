d = list(map(int, open("input.txt").read().splitlines()))
print(sum(x // 3 - 2 for x in d))
print(sum([d.append(x // 3 - 2) or x // 3 - 2 for x in d if (x // 3 - 2) > 0]))
