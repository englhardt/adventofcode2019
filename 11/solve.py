import itertools
import operator
from queue import SimpleQueue

class VM():
    def __init__(self, d, start_color=None):
        self.d = d.copy()
        self.d += [0] * 10000
        self.i = 0
        self.base = 0
        self.io = SimpleQueue()
        self.pos = [0, 0]
        self.dir = 0
        self.dir_v = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        self.img = {} if start_color is None else {(0, 0): start_color}

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
        o_paint = True
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
                d[get_addr(imm_a, i+1)] = self.img.get(tuple(self.pos), 0)
                i += 2
            elif instr == 4:
                output = get_val(imm_a, i+1)
                i += 2
                self.i = i
                if o_paint:
                    self.img[tuple(self.pos)] = output
                    o_paint = False
                else:
                    self.dir = (self.dir + 1) % 4 if output else (self.dir - 1) % 4
                    o_paint = True
                    self.pos[0] += self.dir_v[self.dir][0]
                    self.pos[1] += self.dir_v[self.dir][1]
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
                return self.img
        self.i = i
        return output

d = list(map(int, open("input.txt").read().split(",")))
img = VM(d).run()
print(len(img.keys()))

img = VM(d, 1).run()
x_max = max(map(operator.itemgetter(0), img.keys()))
y_max = max(map(operator.itemgetter(1), img.keys()))
for y in range(y_max+1):
    s = ""
    for x in range(x_max+1):
        v = str(img.get((x, y), " "))
        s += "#" if v == "1" else " "
    print(s)

