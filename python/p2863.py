try:
    while True:
        t = int(input())
        if 2 <= t <= 99:
            l = []
            for i in range(t):
                ti = float(input())
                if 9.0 <= ti <= 11.0:
                    l.append(ti)
            print(min(l))
except EOFError as e:
    pass
