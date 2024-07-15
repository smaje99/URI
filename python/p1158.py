"""Beecrowd exercise 1158.

See: https://judge.beecrowd.com/es/problems/view/1158
"""


def main():
    """Main function."""
    n = int(input())

    for _ in range(n):
        x, y = map(int, input().split())

        odds = range(x + 1 if x % 2 == 0 else x, x + 2 * y, 2)
        print(sum(odds))


if __name__ == "__main__":
    main()
