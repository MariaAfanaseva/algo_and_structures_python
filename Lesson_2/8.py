"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""


def cont_number_1(search, numbers):
    count = 0
    for num in numbers:
        count += num.count(search)
    return count


def main():
    try:
        search = input('Ввкдите число которое нужно найти: ')
        numbers = input('Введите последовательность чисел: ').split()
        print(f'Количество {search} в последовательности равно {cont_number_1(search, numbers)}')
    except ValueError:
        print('Вы ввели не число')


if __name__ == '__main__':
    main()
