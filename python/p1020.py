'''Beecrowd exercise 1020.

See: https://judge.beecrowd.com/es/problems/view/1020
'''

a = int(input())

print((a // 365), "ano(s)")
print(((a % 365) // 30), "mes(es)")
print(((a % 365) % 30), "dia(s)")
