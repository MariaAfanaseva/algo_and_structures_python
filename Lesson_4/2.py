"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""
import timeit


def get_simple(num):
    if num == 1:
        return 2
    numbers = [i for i in range(num * 10)]
    # print(numbers)
    simple = [2]
    for inx in range(3, len(numbers) - 1):
        inx_simply = True
        for el in simple:
            if inx % el == 0:
                inx_simply = False
        if inx_simply:
            simple.append(inx)
            if len(simple) == num:
                # print(simple)
                return inx


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


def get_simple_2(i):
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


def main():
    num = int(input('Введите номер по счёту простого числа: '))
    print(get_simple(num))
    print(get_simple_1(num))
    print(get_simple_2(num))


def test():
    for num in range(15, 20):
        a = timeit.timeit('get_simple(' + str(num) + ')', setup='from __main__ import get_simple')
        b = timeit.timeit('get_simple_1(' + str(num) + ')', setup='from __main__ import get_simple_1')
        if a >= b:
            print(num)
            print(a, b)
            break


main()
# test()

'''
Начиная с числа 17 «Решето Эратосфена» работает быстрее
'''
