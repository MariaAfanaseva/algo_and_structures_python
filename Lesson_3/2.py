"""
2.	Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
надо заполнить значениями 1, 4, 5, 6
(или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""
count = input('Введите список чисел через пробел: ').split()
result = []
inx = 0
for el in count:
    if int(el) % 2 == 0:
        result.append(inx)
    inx += 1

for inx in result:
    print(inx, end=' ')
