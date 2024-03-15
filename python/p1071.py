x = int(input())
y = int(input())
x = max(x, y)
y = min(x, y)
n = 0
b = False
for i in range(y, x):
    if b and i % 2 != 0:
        n += i
    b = True
print(n)
