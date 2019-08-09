"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Задание
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""
import timeit
import cProfile

# Изначальный мой вариант


def sum_numbers(count, start, sum_num=0):
    if count == 0:
        return sum_num
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


# Варианты после небольшой оптимизации


def sum_numbers_2(count, start, sum_num=0):
    if count == 0:
        return sum_num
    return sum_numbers_2(count - 1, start / -2, sum_num + start)


def sum_numbers_3(count, start=1):
    sum_num = start
    for _ in range(count - 1):
        start /= -2
        sum_num += start
    return sum_num


def sum_numbers_4(count):
    num = 1
    i = 0
    sum_num = 0
    while i < count:
        sum_num += num
        num /= -2
        i += 1
    return sum_num


# Результаты испытаний timeit
count = int(input('Введите количество элементов: '))
start = 1
print(timeit.timeit('sum_numbers(count, start)', setup='from __main__ import sum_numbers, count, start'))
print(timeit.timeit('sum_numbers_1(count)', setup='from __main__ import sum_numbers_1, count'))
print(timeit.timeit('sum_numbers_2(count, start)', setup='from __main__ import sum_numbers_2, count, start'))
print(timeit.timeit('sum_numbers_3(count)', setup='from __main__ import sum_numbers_3, count'))
print(timeit.timeit('sum_numbers_4(count)', setup='from __main__ import sum_numbers_4, count'))

'''
Введите количество элементов: 15
6.483470700000001
3.9131237999999993
5.5825444
2.762092599999999
3.461309800000002

Введите количество элементов: 20
7.7225166000000005
4.9614167999999985
6.961654199999998
3.246098800000002
4.155226499999998

Введите количество элементов: 30
12.651390000000006
6.795468299999996
7.2959022999999945
3.3903772999999973
5.9224894000000035
'''

# Результаты испытаний cProfile показали все 0

cProfile.run('sum_numbers(count, start)')
cProfile.run('sum_numbers_1(count)')
cProfile.run('sum_numbers_2(count, start)')
cProfile.run('sum_numbers_3(count)')

'''

Сложность всех вариантов O(N).
Но после проведенных испытаний можно сделать вывод,
что функция sum_numbers_3 самый оптимальный вариант,
т.к время выполнения наименьшее.
 
 '''
