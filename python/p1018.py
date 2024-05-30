'''Beecrowd exercise 1018.

See: https://judge.beecrowd.com/es/problems/view/1018
'''

n = int(input())

print(n)

print((n // 100), "nota(s) de R$ 100,00")
n %= 100

print((n // 50), "nota(s) de R$ 50,00")
n %= 50

print((n // 20), "nota(s) de R$ 20,00")
n %= 20

print((n // 10), "nota(s) de R$ 10,00")
n %= 10

print((n // 5), "nota(s) de R$ 5,00")
n %= 5

print((n // 2), "nota(s) de R$ 2,00")
n %= 2

print((n // 1), "nota(s) de R$ 1,00")
