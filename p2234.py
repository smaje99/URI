m, p = input().split()
m = int(m)
p = int(p)
if (1 <= m <= 1000 and 1 <= p <= 1000):
    print("{:0.2f}".format(m / p))
