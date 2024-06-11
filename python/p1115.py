"""Beecrowd exercise 1115.

See: https://judge.beecrowd.com/es/problems/view/1115
"""


def main():
    """Main function."""
    while True:
        x, y = map(int, input().split())

        if x == 0 or y == 0:
            break

        if x > 0 and y > 0:
            print("primeiro")
        elif x < 0 and y > 0:
            print("segundo")
        elif x < 0 and y < 0:
            print("terceiro")
        else:
            print("quarto")


if __name__ == "__main__":
    main()
