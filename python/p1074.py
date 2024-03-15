n = int(input())
if n < 10000:
    for i in range(n):
        x = int(input())
        if -10 ** 7 < x < 10 ** 7:
            if x == 0:
                print("NULL")
            elif x > 0 and x % 2 == 0:
                print("EVEN POSITIVE")
            elif x < 0 and x % 2 == 0:
                print("EVEN NEGATIVE")
            elif x > 0 and x % 2 != 0:
                print("ODD POSITIVE")
            else:
                print("ODD NEGATIVE")
