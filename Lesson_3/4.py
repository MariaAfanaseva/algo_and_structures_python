# 4.	Определить, какое число в массиве встречается чаще всего.
from random import randint
count = int(input('Колличество элементов в массиве: '))

lst = []

for i in range(count):
    lst.append(randint(1, 5))
# print(lst)

max_count = 0
el_max_count = []

for inx, el in enumerate(lst):
    if el not in lst[:inx]:
        count = 0
        for num in lst[inx:]:
            if el == num:
                count += 1
        if count > max_count:
            max_count = count
            el_max_count = [el]
        elif count == max_count:
            el_max_count.append(el)

print('Массив случайных чисел')
for num in lst:
    print(num, end=' ')
print(f'\nМаксимальное колличество {max_count} раз встречаеьтся число{*el_max_count,}')


