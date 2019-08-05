"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""


def sum_numbers(count, start, sum_num=0):
    if count == 0:
        return sum_num
    # print(start, end=' ')
    if count < 0:
        return sum_numbers(count - 1, start / 2, sum_num + start)
    else:
        return sum_numbers(count - 1, -(start / 2), sum_num + start)


def sum_numbers_1(count, start=1):
    sum_num = start
    for i in range(count - 1):
        start = start / 2
        if i % 2 != 0:
            sum_num += start
        else:
            sum_num -= start
    return sum_num


def main():
    try:
        count = int(input('Введите количество элементов: '))
        print(f'Сумма чисел последовательности {sum_numbers_1(count)}')
        print(f'Сумма чисел последовательности {sum_numbers(count, 1)}')
    except ValueError:
        print('Вы ввели не число')


if __name__ == '__main__':
    main()
