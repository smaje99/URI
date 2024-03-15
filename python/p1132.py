x = int(input())
y = int(input())
j = 0
for i in range(min(x, y), max(x, y) + 1):
    if i % 13 != 0:
        j += i
print(j)
