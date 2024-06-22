"""Beecrowd exercise 1134.

See: https://judge.beecrowd.com/es/problems/view/1134
"""


def main():
    """Main function."""
    alcohol = gasolina = diesel = 0

    while True:
        fuel = int(input())

        match fuel:
            case 1:
                alcohol += 1
            case 2:
                gasolina += 1
            case 3:
                diesel += 1
            case 4:
                break
            case _:
                continue

    print("MUITO OBRIGADO")
    print(f"Alcool: {alcohol}")
    print(f"Gasolina: {gasolina}")
    print(f"Diesel: {diesel}")


if __name__ == "__main__":
    main()
