l = []
while True:
    n = int(input())
    if n == 0:
        break
    elif n % 2 == 0:
        m = n
        for i in range(4):
            m += 2
            n += m
    else:
        n += 1
        m = n
        for i in range(4):
            m += 2
            n += m
    l.append(n)

for i in l:
    print(i)
