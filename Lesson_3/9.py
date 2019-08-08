# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import randint

matrix = [[0] * 4 for i in range(5)]

for i in range(5):
    for j in range(4):
        matrix[i][j] = randint(1, 100)

lst_min = []
for i in range(4):
    min_el = matrix[0][i]
    for j in range(5):
        if matrix[j][i] < min_el:
            min_el = matrix[j][i]
    lst_min.append(min_el)

min_el = lst_min[0]
for el in lst_min:
    if el < min_el:
        min_el = el

print('Mатрица случайных чисел')
for line in matrix:
    for num in line:
        print(f'{num:<4}', end=' ')
    print()

print('Минимальные числа столбцов')
for el in lst_min:
    print(f'{el:<4}', end=' ')

print('\nМинимальный элемент')
print(min_el)