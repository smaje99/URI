"""Beecrowd exercise 1170.
Blobs.
Mathematics.
Simple Math.

See: https://judge.beecrowd.com/es/problems/view/1170
"""


def main():
    """Main function to read input and calculate days until extinction."""
    import math

    n = int(input())
    if not (1 <= n <= 1000):
        return

    results = []
    for _ in range(n):
        x = float(input())
        if not (1 <= x <= 1000):
            continue

        days = math.ceil(math.log2(x))
        results.append(f"{days} dias")

    print('\n'.join(results))


if __name__ == '__main__':
    main()
