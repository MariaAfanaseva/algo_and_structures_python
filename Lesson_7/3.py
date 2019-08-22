"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""
import timeit
from random import randint


def cocktail_sort(array):
    left = 0
    right = len(array) - 1
    while left <= right:
        for i in range(left, right):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        right -= 1
        for i in range(right, left, -1):
            if array[i-1] > array[i]:
                array[i], array[i-1] = array[i-1], array[i]
        left += 1
    return array


def main():
    m = int(input('Введите натуральное число: '))
    array = [randint(0, 100) for _ in range(2 * m + 1)]
    print(array)
    print(cocktail_sort(array))
    print(f'Медиана: {array[len(array) // 2]}')
    print(timeit.timeit("cocktail_sort(" + str(array) + ")", setup="from __main__ import cocktail_sort", number=100))


main()
