import itertools
from queue import SimpleQueue

class Amp():
    def __init__(self, d):
        self.d = d.copy()
        self.i = 0
        self.io = SimpleQueue()

    def run(self):
        i = self.i
        io = self.io
        d = self.d
        def get_val(imm, i):
            return d[i] if imm else d[d[i]]
        output = None
        while True:
            instr = d[i] % 100
            imm_a, imm_b = d[i] // 100 % 10 == 1, d[i] // 1000 == 1
            if instr == 1:
                d[d[i+3]] = get_val(imm_a, i+1) + get_val(imm_b, i+2)
                i += 4
            elif instr == 2:
                d[d[i+3]] = get_val(imm_a, i+1) * get_val(imm_b, i+2)
                i += 4
            elif instr == 3:
                d[d[i+1]] = io.get()
                i += 2
            elif instr == 4:
                output = get_val(imm_a, i+1)
                i += 2
                self.i = i
                return output
            elif instr == 5:
                if get_val(imm_a, i+1) != 0:
                    i = get_val(imm_b, i+2)
                else:
                    i += 3
            elif instr == 6:
                if get_val(imm_a, i+1) == 0:
                    i = get_val(imm_b, i+2)
                else:
                    i += 3
            elif instr == 7:
                d[d[i+3]] = int(get_val(imm_a, i+1) < get_val(imm_b, i+2))
                i += 4
            elif instr == 8:
                d[d[i+3]] = int(get_val(imm_a, i+1) == get_val(imm_b, i+2))
                i += 4
            else:
                assert d[i] == 99
                raise Exception()
        self.i = i
        return output

def run(d, r):
    output = -9999999
    for config in itertools.permutations(r):
        a = []
        for i in range(len(config)):
            a.append(Amp(d))
            a[i].io.put(config[i])
        x = 0
        while True:
            try:
                for i in range(len(config)):
                    a[i].io.put(x)
                    x = a[i].run()
            except Exception:
                break
        output = max(output, x)
    return output

d = list(map(int, open("input.txt").read().split(",")))
print(run(d, range(5)))
print(run(d, range(5, 10)))
