"""Beecrowd exercise 1113.

See: https://judge.beecrowd.com/es/problems/view/1113
"""


def main():
    """Main function."""
    while True:
        x, y = map(int, input().split())

        if x == y:
            break

        if x > y:
            print("Decrescente")
        else:
            print("Crescente")


if __name__ == "__main__":
    main()
