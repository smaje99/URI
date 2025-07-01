"""Beecrowd exercise 1165.
Prime Number.
Beginner.
Repetition.

See: https://judge.beecrowd.com/es/problems/view/1165
"""

from math import isqrt


def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = isqrt(n) + 1
    return all(n % i != 0 for i in range(3, limit, 2))

def main():
    """Main function to read input and check for prime numbers."""
    n = int(input())
    if not (1 <= n <= 100):
        return

    for _ in range(n):
        number = int(input())
        if not (1 <= number <= 10**7):
            continue

        result = 'eh primo' if is_prime(number) else 'nao eh primo'
        print(f'{number} {result}')


if __name__ == '__main__':
    main()
