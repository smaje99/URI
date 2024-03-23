'''Beecrowd exercise 1040.

See: https://judge.beecrowd.com/es/problems/view/1040
'''


def main():
    '''Main function.'''
    n1, n2, n3, n4 = map(float, input().split())

    average = (n1 * 2 + n2 * 3 + n3 * 4 + n4) / 10

    print(f'Media: {average:.1f}')

    if average >= 7.0:
        print('Aluno aprovado.')
    elif average < 5.0:
        print('Aluno reprovado.')
    else:
        print('Aluno em exame.')
        exam_score = float(input())
        print(f'Nota do exame: {exam_score:.1f}')

        average = (average + exam_score) / 2

        if average >= 5.0:
            print('Aluno aprovado.')
        else:
            print('Aluno reprovado.')

        print(f'Media final: {average:.1f}')


if __name__ == '__main__':
    main()
