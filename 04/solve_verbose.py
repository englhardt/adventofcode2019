r = range(146810, 612564)

def check(x, p1=False):
    d = list(map(int, str(x)))
    dbl = False
    i = 0
    while i < len(d) - 1:
        if d[i] > d[i+1]:
            return False
        if d[i] == d[i+1]:
            if p1:
                dbl = True
            else:
                c = 2
                while i + c < len(d) and d[i + c] == d[i]:
                    c += 1
                if c == 2:
                    dbl = True
                i += c - 2
        i += 1
    return dbl

print(sum(map(lambda x: check(x, True), r)))
print(sum(map(check, r)))
