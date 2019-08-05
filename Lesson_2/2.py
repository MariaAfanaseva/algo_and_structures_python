"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""


def count_type(num, even, uneven):
    if num == 0:
        return even, uneven
    if (num % 10) % 2 == 0:
        even.append(num % 10)
        return count_type(num // 10, even, uneven)
    else:
        uneven.append(num % 10)
        return count_type(num // 10, even, uneven)


def main():
    try:
        num = int(input('Введите число: '))
        even, uneven = count_type(num, [], [])
        print(f'В числе {len(even)} {*even,} четных и {len(uneven)} {*uneven,} не четных чисел')
    except ValueError:
        print('Вы введи не число')


main()
