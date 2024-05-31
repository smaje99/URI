'''Beecrowd exercise 1019.

See: https://judge.beecrowd.com/es/problems/view/1019
'''

s = int(input())
print(repr((s // 60) // 60) + ":" + repr((s // 60) % 60) + ":" + repr(s % 60))
