"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""

from random import randint

count = int(input('Колличество элементов в массиве: '))
lst = [0] * count

for i in range(count):
    lst[i] = randint(-2, 100)

min_1 = lst[0]
min_2 = lst[1]
for el in lst[2:]:
    if el < min_1:
        if min_1 < min_2:
            min_2 = min_1
        min_1 = el
    else:
        if el < min_2:
            min_2 = el

print('Массив случайных чисел')
for num in lst:
    print(num, end=' ')
print(f'\nДва наименьших элемента {min_1} и {min_2}')
