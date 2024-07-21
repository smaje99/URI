"""Beecrowd exercise 1030.

See: https://judge.beecrowd.com/es/problems/view/1030
"""


def main():
    """Main function.
    Josephus Problem.
    """
    nc = int(input())

    if 1 <= nc <= 30:
        for i in range(1, nc + 1):
            n, k = map(int, input().split())

            if not 1 <= n <= 10_000 or not 1 <= k <= 1_000:
                continue

            """ # Josephus Problem - Method 1
            people = list(range(1, n + 1))
            index = 0

            while len(people) > 1:
                index = (index + k - 1) % len(people)
                people.pop(index)

            print(f"Case {i}: {people[0]}") """

            # Josephus Problem - Method 2
            survivor = 0

            for j in range(2, n + 1):
                survivor = (survivor + k) % j

            print(f"Case {i}: {survivor + 1}")


if __name__ == "__main__":
    main()
