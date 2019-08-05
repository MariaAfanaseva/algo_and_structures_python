"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""


def get_sum(number, sum=0):
    if number == 0:
        return sum
    else:
        return get_sum(number // 10, sum + (number % 10))


def max_sum():
    try:
        numbers = input('Ввудите числа через пробел: ').split()
        max = 0
        result = 0
        for num in numbers:
            sum = get_sum(int(num))
            if max < sum:
                max = sum
                result = num
        return max, result
    except ValueError:
        print('Неверные данные')


def max_sum_1():
    try:
        numbers = input('Ввудите числа через пробел: ').split()
        max = 0
        result = 0
        for num in numbers:
            sum = 0
            num_copy = int(num)
            for _ in range(len(num)):
                n = num_copy % 10
                sum += n
                num_copy //= 10
            if max < sum:
                max = sum
                result = num
        return max, result
    except ValueError:
        print('Неверные данные')


def main():
    # max, result = max_sum_1()
    max, result = max_sum()
    print(f'Число {result} с суммой {max} максимально.')


if __name__ == '__main__':
    main()