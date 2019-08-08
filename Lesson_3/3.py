#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

from random import randint

count = int(input('Колличество элементов в массиве: '))
lst = [0] * count

for i in range(count):
    num = randint(1, 100)
    lst[i] = num
    print(num, end=' ')
print()
min_num, max_num = lst[0], lst[0]
min_inx, max_inx = 0, 0

for inx, el in enumerate(lst):
    if el > max_num:
        max_num = el
        max_inx = inx
    if el < min_num:
        min_num = el
        min_inx = inx

lst[max_inx], lst[min_inx] = lst[min_inx], lst[max_inx]
for i in lst:
    print(i, end=' ')
