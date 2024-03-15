from fractions import Fraction as frac

p = []
n = int(input())
if 1 <= n <= 1 * (10 ** 4):
    while n != 0:
        l = input().split()
        a, b, c, d = int(l[0]), int(l[2]), int(l[4]), int(l[6])
        sign = str(l[3])
        if sign == '+':
            p.append(repr(a * d + b * c) + "/" + repr(b * d) + " = " + str(frac(a, b) + frac(c, d)))
        elif sign == '-':
            p.append(repr(a * d - b * c) + "/" + repr(b * d) + " = " + str(frac(a, b) - frac(c, d)))
        elif sign == '*':
            p.append(repr(a * c) + "/" + repr(b * d) + " = " + str(frac(a, b) * frac(c, d)))
        elif sign == '/':
            p.append(repr(a * d) + "/" + repr(b * c) + " = " + str(frac(a, b) / frac(c, d)))
        n -= 1
    for i in p:
        print(i)
