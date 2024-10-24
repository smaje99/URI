"""Beecrowd exercise 1094.

See: https://judge.beecrowd.com/es/problems/view/1094
"""


def main():
    """Main function."""
    n = int(input())
    animals = {"C": 0, "R": 0, "S": 0}

    for _ in range(n):
        read = input().split()
        cantidad = int(read[0])
        animal = read[1].upper()

        if 1 <= cantidad <= 15:
            animals[animal] += cantidad

    total = sum(animals.values())
    percentages = {
        key: value * 100 / total
        if total > 0 else 0
        for key, value in animals.items()
    }

    print(f"Total: {total} cobaias")
    print(f'Total de coelhos: {animals["C"]}')
    print(f'Total de ratos: {animals["R"]}')
    print(f'Total de sapos: {animals["S"]}')
    print(f'Percentual de coelhos: {percentages["C"]:.2f} %')
    print(f'Percentual de ratos: {percentages["R"]:.2f} %')
    print(f'Percentual de sapos: {percentages["S"]:.2f} %')


if __name__ == "__main__":
    main()
