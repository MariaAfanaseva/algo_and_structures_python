"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""


def is_equality(number, a, b):
    # print(number, a, b)
    if a == b:
        return True
    else:
        a += number
        number -= 1
        if number >= 0:
            return is_equality(number, a, b)


def is_equality_1(number, a, b):
    for i in range(number):
        a += number
        number -= 1
    if a == b:
        return True


def main():
    try:
        n = int(input('Введите число: '))
        b = n * (n + 1) / 2
        if is_equality_1(n, 0, b):
            print('Равенство 1+2+...+n = n(n+1)/2 выполняеться')
        else:
            print('Равенство 1+2+...+n = n(n+1)/2 невыполняеться')
    except ValueError:
        print('Вы ввели не число')


if __name__ == '__main__':
    main()
