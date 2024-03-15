try:
    while True:
        l = []
        while True:
            i = input()
            if i == '0': break
            elif i == '1': continue
            l.append(i)
        l.sort()
        for n in l: print(n)
        print()
except EOFError as e:
    pass
