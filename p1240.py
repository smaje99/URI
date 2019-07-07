n = int(input())
for i in range(n):
    a, b = input().split()
    if 1 <= int(a) <= 2 ** 31 and 1 <= int(b) <= 2 ** 31:
        print('encaixa' if a.endswith(b) else 'nao encaixa')
