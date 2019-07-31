"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""

from random import random

type_date = input('Укажите тип границ диапазона: 1 - целое число, 2 - вещественное число, 3 - символ: ')
date_1 = input("Минимальная граница: ")
date_2 = input("Максимальная граница: ")

try:
    if type_date == '1':
        date_1 = int(date_1)
        date_2 = int(date_2)
        date_int = int(random() * (date_2 - date_1 + 1)) + date_1
        print(f'Cлучайное целое число - {date_int}')
    elif type_date == '2':
        date_1 = float(date_1)
        date_2 = float(date_2)
        date_float = round(random() * (date_2 - date_1) + date_1, 3)
        print(f'Cлучайное вещественное число - {date_float}')
    elif type_date == '3':
        str_random = int(random() * (ord(date_2) - ord(date_1) + 1)) + ord(date_1)
        str_random = chr(str_random)
        print(f'Cлучайный символ - {str_random}')
    else:
        print('Нет такого типа')
except ValueError:
    print('Неверные данные')

