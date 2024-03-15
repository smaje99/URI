l = []
try:
    while True:
        n = int(input())
        if 1001 <= n <= 9999:
            l.append(n)
except EOFError as error:
    for i in l:
        print(i - 1)
