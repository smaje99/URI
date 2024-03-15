def children():
    while True:
        l, r = map(int, input().split(' '))
        if 1 <= l <= 5 and 1 <= r <= 5:
            yield l + r
        elif l == 0 and r == 0:
            break


if __name__ == '__main__':
    for child in children():
        print(child)

