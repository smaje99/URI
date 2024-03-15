while True:
    d, n = map(int, input().split())
    if d == n == 0:
        break
    else:
        m = str(n).replace(str(d), '')
        print(int(m) if len(m) != 0 else 0)
