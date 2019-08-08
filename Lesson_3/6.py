"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

from random import randint

count = int(input('Колличество элементов в массиве: '))
lst = [0] * count

for i in range(count):
    lst[i] = randint(1, 100)

min_num, max_num = lst[0], lst[0]
min_inx, max_inx = 0, 0
inx = 0
for el in lst:
    if el > max_num:
        max_num = el
        max_inx = inx
    if el < min_num:
        min_num = el
        min_inx = inx
    inx += 1

result_sum = 0

if max_inx < min_inx:
    a, b = max_inx, min_inx
else:
    a, b = min_inx, max_inx

for el in range(a + 1, b):
    result_sum += lst[el]

print('Массив случайных чисел')
for num in lst:
    print(num, end=' ')
print(f'\nСуммa элементов, находящихся между минимальным и максимальным элементами {result_sum}')
