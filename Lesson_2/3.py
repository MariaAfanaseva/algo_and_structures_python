"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""


def reverse_num(num):
    if num == 0:
        return
    else:
        print(num % 10, end='')
        reverse_num(num // 10)


def main():
    try:
        num = int(input('Введите число: '))
        reverse_num(num)
    except ValueError:
        print('Вы введи не число')


main()
