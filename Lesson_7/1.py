"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

from random import randint
import timeit


def bubble_sort(array):
    for i in range(1, len(array)):
        for j in range(len(array) - i):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


# arr = [randint(-100, 100) for _ in range(10)]
arr = [-64, -10, 36, -94, -21, 53, -15, -7, -54, -10]
print(arr)
bubble_sort(arr)
print(arr)


# print(timeit.timeit("bubble_sort(arr)", setup="from __main__ import bubble_sort, arr", number=10))
'''
[-64, -10, 36, -94, -21, 53, -15, -7, -54, -10]
[53, 36, -7, -10, -10, -15, -21, -54, -64, -94]
'''