bills = [100, 50, 20, 10, 5, 2]


def first(mn):
    for i in bills:
        if mn > i:
            return mn - i
    return -1


def second(mn):
    for i in bills:
        if mn >= i:
            return mn - i
    return -1


while True:
    n, m = map(int, input().split())
    bill = -1
    if n == m == 0:
        break
    elif n < m:
        bill = second(first(m - n))
    print('possible' if bill == 0 else 'impossible')
