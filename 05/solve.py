def run(d, io):
    def get_val(imm, i):
        return d[i] if imm else d[d[i]]
    i = 0
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
            d[d[i+1]] = io.pop(0)
            i += 2
        elif instr == 4:
            io.append(get_val(imm_a, i+1))
            output = get_val(imm_a, i+1)
            i += 2
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
            break
    return output
d = list(map(int, open("input.txt").read().split(",")))
print(run(d.copy(), [1]))
print(run(d, [5]))
