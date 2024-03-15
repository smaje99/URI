while True:
    a, b, c, d = input().split()
    if a == b == c == d == '0':
        break
    else:
        print("{:0.5f}".format((((int(a) / 2) + int(b)) * int(c)) / int(d)))