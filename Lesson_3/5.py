#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.
from random import randint

count = int(input('Колличество элементов в массиве: '))
lst = [0] * count

for i in range(count):
    lst[i] = randint(-100, 10)

result = -100
result_inx = 0
inx = 0
for el in lst:
    if result < el < 0:
        result = el
        result_inx = inx
    inx += 1

print('Массив случайных чисел')
for num in lst:
    print(num, end=' ')
print(f'\nМаксимальный отрицательный элемент: {result}, позиция (индекс) {result_inx + 1} в массиве')
