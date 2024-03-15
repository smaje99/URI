a = []
pas = []
for i in range(31):
    b = []
    for j in range(i + 1):
        if j == 0 or j == i:
            b.append(1)
        else:
            b.append(a[j] + a[j - 1])
    pas.append(b)
    a = b

n = int(input())
for i in range(n):
    t = int(input())
    if 1 <= t <= 31:
        kn = 0
        for j in range(t):
            for k in pas[j]:
                kn += k
        print(kn)
