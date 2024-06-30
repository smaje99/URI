"""Beecrowd exercise 1150.

See: https://judge.beecrowd.com/es/problems/view/1150
"""


def main():
    """Main function."""
    x = int(input())

    while True:
        z = int(input())
        if z > x:
            break

    count = 1
    total = x
    while total <= z:
        total += x + count
        count += 1

    print(count)


if __name__ == "__main__":
    main()
