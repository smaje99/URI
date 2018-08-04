n = int(input())
l = []
for i in range(n):
    p = input()
    if len(p) == 5:
        l.append(3)
    elif (p[0] == 't' and p[1] == 'w') or (p[0] == 't' and p[2] == 'o') or (p[1] == 'w' and p[2] == 'o'):
        l.append(2)
    else:
        l.append(1)
for i in l:
    print(i)
