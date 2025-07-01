"""Beecrowd exercise 1168.
LED.
Beginner.
String.

See: https://judge.beecrowd.com/es/problems/view/1168
"""


def main():
    """Main function to read input and calculate LED segments."""
    led_count = {
        '0': 6, '1': 2, '2': 5, '3': 5, '4': 4,
        '5': 5, '6': 6, '7': 3, '8': 7, '9': 6
    }

    n = int(input())
    if not (1 <= n <= 2000):
        return

    for _ in range(n):
        number = input()
        if not (1 <= len(number) <= 10**100):
            continue

        total_leds = sum(led_count[digit] for digit in number)
        print(f'{total_leds} leds')


if __name__ == '__main__':
    main()
