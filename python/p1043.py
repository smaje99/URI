'''Beecrowd exercise 1043.

See: https://judge.beecrowd.com/es/problems/view/1043
'''


def main():
    '''Main function.'''
    a, b, c = map(float, input().split())

    if a + b > c and a + c > b and b + c > a:
        print(f'Perimetro = {a + b + c}')
    else:
        print(f'Area = {(a + b) * c / 2}')


if __name__ == '__main__':
    main()
