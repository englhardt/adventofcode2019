import itertools
from queue import SimpleQueue

class VM():
    def __init__(self, d, io=None):
        self.d = d.copy()
        self.d += [0] * 10000
        self.i = 0
        self.base = 0
        self.io = SimpleQueue()
        if io is not None:
            self.io.put(io)

    def run(self):
        i = self.i
        io = self.io
        d = self.d
        def get_val(imm, i):
            return d[get_addr(imm, i)]
        def get_addr(imm, i):
            if imm == 1:
                return i
            elif imm == 2:
                return self.base + d[i]
            else:
                return d[i]
        output = None
        while True:
            instr = d[i] % 100
            imm_a, imm_b, imm_c = d[i] // 100 % 10, d[i] // 1000 % 10, d[i] // 10000
            if instr == 1:
                d[get_addr(imm_c, i+3)] = get_val(imm_a, i+1) + get_val(imm_b, i+2)
                i += 4
            elif instr == 2:
                d[get_addr(imm_c, i+3)] = get_val(imm_a, i+1) * get_val(imm_b, i+2)
                i += 4
            elif instr == 3:
                d[get_addr(imm_a, i+1)] = io.get()
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
                d[get_addr(imm_c, i+3)] = int(get_val(imm_a, i+1) < get_val(imm_b, i+2))
                i += 4
            elif instr == 8:
                d[get_addr(imm_c, i+3)] = int(get_val(imm_a, i+1) == get_val(imm_b, i+2))
                i += 4
            elif instr == 9:
                self.base += get_val(imm_a, i+1)
                i += 2
            else:
                assert d[i] == 99
                raise Exception()
        self.i = i
        return output

d = list(map(int, open("input.txt").read().split(",")))
print(VM(d, 1).run())
print(VM(d, 2).run())
