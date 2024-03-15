from math import log10


for i in range(int(input())):
    n , m = map(int, input().split())
    if 1 <= n <= 100 and 1 <= m <= 100:
        print(int(log10(n ** m)) + 1)
