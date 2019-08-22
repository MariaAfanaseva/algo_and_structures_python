"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""

import timeit
import random


def merge_sort(array):
    if len(array) > 1:
        middle = len(array) // 2
        left = array[:middle]
        right = array[middle:]

        merge_sort(left)
        merge_sort(right)

        lft, rgt, arr = 0, 0, 0

        while lft < len(left) and rgt < len(right):
            if left[lft] < right[rgt]:
                array[arr] = left[lft]
                lft += 1
            else:
                array[arr] = right[rgt]
                rgt += 1
            arr += 1

        while lft < len(left):
            array[arr] = left[lft]
            lft += 1
            arr += 1

        while rgt < len(right):
            array[arr] = right[rgt]
            rgt += 1
            arr += 1
        return array


array = [random.randint(0, 50) for _ in range(10)]
print(array)
print(timeit.timeit("merge_sort(array)", setup="from __main__ import merge_sort, array", number=10))
merge_sort(array)
print(array)


'''
Вывод
[4, 12, 3, 43, 31, 29, 40, 2, 36, 20]
0.00032220000000000165
[2, 3, 4, 12, 20, 29, 31, 36, 40, 43]
'''
