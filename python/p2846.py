def fib(n):
    ant = 1
    actual = 2
    termo = 0
    while True:
        termo = ant + actual
        ant = actual
        actual = termo
        if n == termo:
            return False
        elif n < termo:
            return True


x = int(input())
cont = 0
i = 4
while True:
    if fib(i):
        cont += 1
        if x == cont:
            print(i)
            break
    i += 1
