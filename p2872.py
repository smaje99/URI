try:
    while True:
        l = []
        while True:
            i = input()
            if i == '0': break
            elif i == '1': continue
            p=input().split()
            if 1<= (int)p[1] <=999: l.append(p[0]+p[1])
        l.sort()
        for n in l: print(n)
        print()
except EOFError as e:
    pass
