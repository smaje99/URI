"""Beecrowd exercise 1161.
Factorial Sum.
Math, factorial.

See: https://judge.beecrowd.com/es/problems/view/1161
"""



def main():
    """Main function."""
    import contextlib
    from math import factorial

    fact = [factorial(i) for i in range(21)]

    with contextlib.suppress(EOFError):
        while True:
            a, b = map(int, input().split())
            print(fact[a] + fact[b])


if __name__ == "__main__":
    main()
