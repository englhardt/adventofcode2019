from collections import Counter
w, h = (25, 6)
im = list(map(int, open("input.txt").read().replace("\n", "")))
num_layer = int(len(im)/(w*h))
num_z = w*h
out = None
for l in range(num_layer):
    c = Counter(im[w*h*l:w*h*(l+1)])
    if c[0] < num_z:
        num_z = c[0]
        out = c[1] * c[2]
print(out)

out = im[:w*h]
for i in range(len(out)):
    l = 0
    while out[i] == 2 and l < num_layer:
        if im[w*h*l+i] < 2:
            out[i] = im[w*h*l+i]
        l += 1

for y in range(h):
    print("".join(map(lambda x: str(x).replace("0", " "), out[w*y:w*(y+1)])))
