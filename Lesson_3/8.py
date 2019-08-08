"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""
from random import randint

matrix = [[0] * 4 for i in range(5)]

for i in range(5):
    sum_line = 0
    for j in range(4):
        num = randint(1, 10)
        matrix[i][j] = num
        sum_line += num
    matrix[i].append(sum_line)

for line in matrix:
    for num in line:
        print(f'{num:<3}', end=' ')
    print()
