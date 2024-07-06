"""Beecrowd exercise 1154.

See: https://judge.beecrowd.com/es/problems/view/1154
"""


def main():
    """Main function."""
    ages: list[int] = []

    while True:
        age = int(input())

        if age < 0:
            break

        ages.append(age)

    print(f'{sum(ages) / len(ages):.2f}')


if __name__ == "__main__":
    main()
