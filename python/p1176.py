"""Beecrowd exercise 1176.
Arreglo de Fibonacci.
Beginner.
Array.

See: https://judge.beecrowd.com/es/problems/view/1176
"""


def main():
    """Main function."""

    # Fibonacci serie via dynamic programming.
    # Precompute Fibonacci numbers up to Fib(60).
    fib = [0, 1]
    fib.extend(fib[i - 1] + fib[i - 2] for i in range(2, 61))

    t = int(input())
    for _ in range(t):
        n = int(input())
        print(f"Fib({n}) = {fib[n]}")


if __name__ == "__main__":
    main()
