c = int(input())
if 2 <= c <= 99:
    for i in range(c):
        n = input()
        m = ""
        for j in range(len(n)):
            if 'a' <= n[j] <= 'z':
                m = n[j] + m
        print(m)