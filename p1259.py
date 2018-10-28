n = int(input())
if 1 <= n <= 10 ** 5:
    even, odd = [], []
    for i in range(n):
        e = int(input())
        if e % 2 == 0: even.append(e)
        else: odd.append(e)
    even.sort()
    odd.sort(reverse=True)
    for i in even, odd:
        for u in i:
            print(u)
