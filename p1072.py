n = int(input())
if n < 10000:
    inte = 0
    ninte = 0
    for i in range(n):
        x = int(input())
        if (-10 ** 7) <= x <= (10 ** 7):
            if 10 <= x <= 20:
                inte += 1
            else:
                ninte += 1
    print(inte, 'in\n' + repr(ninte), 'out')
