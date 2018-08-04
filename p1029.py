

def chamadas(x):
    if x > 1:
        return x ** 2 - 3 * x + 4


n = int(input())
for i in range(n):
    x = int(input())
    if 1 <= x <= 39:
        print("fib({}) = {} calls = {}".format(x, chamadas(x), ))