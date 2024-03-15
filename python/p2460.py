n = input()
n_l = input().split()
m = input()
m_l = input().split()

for i in m_l:
    n_l.remove(i)

print(' '.join(n_l))
