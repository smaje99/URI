dia1 = int(input().split()[1])
h1, m1, s1, = map(int, input().split(':'))
dia2 = int(input().split()[1])
h2, m2, s2, = map(int, input().split(':'))
dia = dia2 - dia1
h = h2 - h1
if h < 0:
    h += 24
    dia -= 1
m = m2 - m1
if m < 0:
    m += 60
    h -= 1
s = s2 - s1
if s < 0:
    s += 60
    m -= 1
if dia <= 0:
    dia = 0
print('{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)'.format(dia, h, m, s))
