# 3.	По введенным пользователем координатам двух точек вывести
# уравнение прямой вида y = kx + b, проходящей через эти точки.

date = input('Ведите координаты двух точек (x1, y1, x2, y2) через пробел: ').split()
try:
    x1 = int(date[0])
    y1 = int(date[1])
    x2 = int(date[2])
    y2 = int(date[3])
    # x1, y1, x2, y2 = list(map(int, date))
except ValueError:
    print('Неверно введены значения')
    quit()
except TypeError:
    print('Введены не цифры')
    quit()

k = (y1 - y2) / (x1 - x2)
b = y1 - ((y1 - y2) / (x1 - x2)) * x2
print(f'y = {k}x + {b}')
