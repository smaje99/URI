"""Beecrowd exercise 1099.

See: https://judge.beecrowd.com/es/problems/view/1099
"""


def main():
    """Main function."""
    n = int(input())

    for _ in range(n):
        x, y = map(int, input().split())

        if x == y:
            print(0)
            continue

        if x > y:
            x, y = y, x

        x += 1
        y -= 1

        if x % 2 == 0:
            x += 1

        if y % 2 == 0:
            y -= 1

        print(sum(range(x, y + 1, 2)))


if __name__ == "__main__":
    main()
