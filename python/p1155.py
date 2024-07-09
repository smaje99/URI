"""Beecrowd exercise 1155.

See: https://judge.beecrowd.com/es/problems/view/1155
"""


def main():
    """Main function."""
    s = 1

    for i in range(2, 101):
        s += 1 / i

    print(f"{s:.2f}")


if __name__ == "__main__":
    main()
