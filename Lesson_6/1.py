"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
------
Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
надо заполнить значениями 1, 4, 5, 6
(или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""
from memory_profiler import profile
from random import randint


@profile
def get_lst():
    # count = input('Введите список чисел через пробел: ').split()
    count = []
    for i in range(100000):
        count.append(i)
    result = []
    inx = 0
    for el in count:
        if int(el) % 2 == 0:
            result.append(inx)
        inx += 1
    return result


@profile
def get_lst_1():
    count = [randint(1, 100) for i in range(100000)]
    result = [inx for inx, el in enumerate(count) if el % 2 == 0]
    return result


def main():
    print(get_lst())
    print(get_lst_1())


'''
Реализация через генератор занимает меньше памяти, чем реализация через цикл.

Line #    Mem usage    Increment   Line Contents
================================================
    20     16.2 MiB     16.2 MiB   @profile
    21                             def get_lst():
    22                                 # count = input('Введите список чисел через пробел: ').split()
    23     16.2 MiB      0.0 MiB       count = []
    24     20.6 MiB      0.0 MiB       for i in range(100000):
    25     20.6 MiB      0.4 MiB           count.append(i)
    26     20.6 MiB      0.0 MiB       result = []
    27     20.6 MiB      0.0 MiB       inx = 0
    28     22.2 MiB      0.1 MiB       for el in count:
    29     22.2 MiB      0.0 MiB           if int(el) % 2 == 0:
    30     22.2 MiB      0.0 MiB               result.append(inx)
    31     22.2 MiB      0.0 MiB           inx += 1
    32     22.2 MiB      0.0 MiB       return result
----------------------------------------------------------------------------------------

Line #    Mem usage    Increment   Line Contents
================================================
    35     16.4 MiB     16.4 MiB   @profile
    36                             def get_lst_1():
    37     17.8 MiB      0.5 MiB       count = [randint(1, 100) for i in range(100000)]
    38     19.2 MiB      0.1 MiB       result = [inx for inx, el in enumerate(count) if el % 2 == 0]
    39     19.2 MiB      0.0 MiB       return result

    '''

"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""


@profile
def get_simple(i):
    if i == 1:
        return 2
    simple = [2]
    number = 2
    while len(simple) < i:
        number += 1
        is_simply = True
        for el in simple:
            if number % el == 0:
                is_simply = False
        if is_simply:
            simple.append(number)
    return number


@profile
def get_simple_1(num):
    numbers = [i for i in range(num * 10)]
    # print(numbers)
    numbers[1] = 0
    simple = 0
    inx = 2
    while inx < numbers[-1]:
        if numbers[inx] != 0:
            simple += 1
            if simple == num:
                # print(simple)
                return inx
            n = inx * 2
            while n < numbers[-1]:
                numbers[n] = 0
                n += inx
        inx += 1


def main_1():
    num = int(input('Введите номер по счёту простого числа: '))
    print(get_simple(num))
    print(get_simple_1(num))


'''
Алгоритм «Решето Эратосфена» использует больше памяти чем наивный алгоритм.
input 2000
Line #    Mem usage    Increment   Line Contents
================================================
    83     16.2 MiB     16.2 MiB   @profile
    84                             def get_simple(i):
    85     16.2 MiB      0.0 MiB       if i == 1:
    86                                     return 2
    87     16.2 MiB      0.0 MiB       simple = [2]
    88     16.2 MiB      0.0 MiB       number = 2
    89     16.2 MiB      0.0 MiB       while len(simple) < i:
    90     16.2 MiB      0.0 MiB           number += 1
    91     16.2 MiB      0.0 MiB           is_simply = True
    92     16.2 MiB      0.0 MiB           for el in simple:
    93     16.2 MiB      0.0 MiB               if number % el == 0:
    94     16.2 MiB      0.0 MiB                   is_simply = False
    95     16.2 MiB      0.0 MiB           if is_simply:
    96     16.2 MiB      0.0 MiB               simple.append(number)
    97     16.0 MiB      0.0 MiB       return number


17389
Filename: D:/GeekBrains/Python/Algorithms/HW/algo_and_structures_python/Lesson_6/1.py

Line #    Mem usage    Increment   Line Contents
================================================
   100     16.1 MiB     16.1 MiB   @profile
   101                             def get_simple_1(num):
   102     17.0 MiB      0.1 MiB       numbers = [i for i in range(num * 10)]
   103                                 # print(numbers)
   104     17.0 MiB      0.0 MiB       numbers[1] = 0
   105     17.0 MiB      0.0 MiB       simple = 0
   106     17.0 MiB      0.0 MiB       inx = 2
   107     17.0 MiB      0.0 MiB       while inx < numbers[-1]:
   108     17.0 MiB      0.0 MiB           if numbers[inx] != 0:
   109     17.0 MiB      0.0 MiB               simple += 1
   110     17.0 MiB      0.0 MiB               if simple == num:
   111                                             # print(simple)
   112     17.0 MiB      0.0 MiB                   return inx
   113     17.0 MiB      0.0 MiB               n = inx * 2
   114     17.0 MiB      0.0 MiB               while n < numbers[-1]:
   115     17.0 MiB      0.0 MiB                   numbers[n] = 0
   116     17.0 MiB      0.0 MiB                   n += inx
   117     17.0 MiB      0.0 MiB           inx += 1
'''

"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""


@profile
def count_type(num, even, uneven):
    if num == 0:
        return even, uneven
    if (num % 10) % 2 == 0:
        even.append(num % 10)
        return count_type(num // 10, even, uneven)
    else:
        uneven.append(num % 10)
        return count_type(num // 10, even, uneven)


@profile
def count_type_1(num):
    even, uneven = [], []
    for i in num:
        if int(i) % 2 == 0:
            even.append(i)
        else:
            uneven.append(i)
    return even, uneven


def main_2():
    try:
        num = str(randint(10*100, 10**200))
        even, uneven = count_type(int(num), [], [])
        print(num)
        even_1, uneven_1 = count_type_1(num)
    except ValueError:
        print('Вы введи не число')


@profile
def sum_numbers(count, start, sum_num=0):
    if count == 0:
        return sum_num
    if count < 0:
        return sum_numbers(count - 1, start / 2, sum_num + start)
    else:
        return sum_numbers(count - 1, -(start / 2), sum_num + start)


@profile
def sum_numbers_1(count, start=1):
    sum_num = start
    for i in range(count - 1):
        start = start / 2
        if i % 2 != 0:
            sum_num += start
        else:
            sum_num -= start
    return sum_num


def main_3():
    try:
        count = int(input('Введите количество элементов: '))
        print(f'Сумма чисел последовательности {sum_numbers_1(count)}')
        print(f'Сумма чисел последовательности {sum_numbers(count, 1)}')
    except ValueError:
        print('Вы ввели не число')


if __name__ == '__main__':
    # main()
    # main_1()
    main_2()
    # main_3()

'''
Рекурсия затрачивает больше памяти чем цикл, 
и при больших числах, рекурсия выполняет слишком много рекурсивных вызовов, 
что пиводит к  RecursionError

Введите количество элементов: 100
Filename: D:/GeekBrains/Python/Algorithms/HW/algo_and_structures_python/Lesson_6/1.py

Line #    Mem usage    Increment   Line Contents
================================================
   224     16.3 MiB     16.3 MiB   @profile
   225                             def sum_numbers_1(count, start=1):
   226     16.3 MiB      0.0 MiB       sum_num = start
   227     16.3 MiB      0.0 MiB       for i in range(count - 1):
   228     16.3 MiB      0.0 MiB           start = start / 2
   229     16.3 MiB      0.0 MiB           if i % 2 != 0:
   230     16.3 MiB      0.0 MiB               sum_num += start
   231                                     else:
   232     16.3 MiB      0.0 MiB               sum_num -= start
   233     16.3 MiB      0.0 MiB       return sum_num


Сумма чисел последовательности 0.6666666666666667
Filename: D:/GeekBrains/Python/Algorithms/HW/algo_and_structures_python/Lesson_6/1.py

Line #    Mem usage    Increment   Line Contents
================================================
   214     17.0 MiB     17.0 MiB   @profile
   215                             def sum_numbers(count, start, sum_num=0):
   216     17.0 MiB      0.0 MiB       if count == 0:
   217     17.0 MiB      0.0 MiB           return sum_num
   218                                 if count < 0:
   219                                     return sum_numbers(count - 1, start / 2, sum_num + start)
   220                                 else:
   221                                     return sum_numbers(count - 1, -(start / 2), sum_num + start)'''
