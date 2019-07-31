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

type_num = input('Укажите тип границ диапазона: 1 - целое число, 2 - вещественное число, 3 - символ: ')
num_1 = input("Минимальная граница: ")
num_2 = input("Максимальная граница: ")


def get_int_num(num_1, num_2):
    num_1 = int(num_1)
    num_2 = int(num_2)
    num_int = int(random() * (num_2 - num_1 + 1)) + num_1
    print(f'Cлучайное целое число - {num_int}')
    
    
def get_float_num(num_1, num_2):
    num_1 = float(num_1)
    num_2 = float(num_2)
    num_float = round(random() * (num_2 - num_1) + num_1, 3)
    print(f'Cлучайное вещественное число - {num_float}')


def get_str(num_1, num_2):
    str_random = int(random() * (ord(num_2) - ord(num_1) + 1)) + ord(num_1)
    str_random = chr(str_random)
    print(f'Cлучайный символ - {str_random}')


try:
    if type_num == '1':
        get_int_num(num_1, num_2)
    elif type_num == '2':
        get_float_num(num_1, num_2)
    elif type_num == '3':
        get_str(num_1, num_2)
    else:
        print('Нет такого типа')
except ValueError:
    print('Неверные данные')

