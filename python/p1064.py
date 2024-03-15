l = []
l.append(float(input()))
l.append(float(input()))
l.append(float(input()))
l.append(float(input()))
l.append(float(input()))
l.append(float(input()))
j = 0
p = 0
for i in l:
    if i >= 0.0:
        j += 1
        p += i
print(repr(j) + " valores positivos")
print("{:0.1f}".format(p / j))
