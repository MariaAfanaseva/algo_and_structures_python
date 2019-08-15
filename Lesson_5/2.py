"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
import collections


def get_result():
    input_num = input('Введите два числа в шестнадцатеричном формате через пробел: ').split()
    numbers = collections.defaultdict(list)
    for num in input_num:
        numbers[num] = list(num)
    sum_num = 0
    mul_num = 1
    for num in numbers.keys():
        num = int(num, 16)
        sum_num += num
        mul_num *= num
    sum_num = list(hex(sum_num).upper())[2:]
    mul_num = list(hex(mul_num).upper())[2:]
    return sum_num, mul_num


def main():
    try:
        sum_num, mul_num = get_result()
        print(f'Сумма чисел {sum_num}, поизведение {mul_num}')
    except ValueError:
        print('Неверный формат')


# OR


class OperationsNum:
    def __init__(self, num_1, num_2):
        self.num_first = num_1
        self.num_second = num_2

    def numbers_sum(self):
        return list(hex(int(self.num_first, 16) + int(self.num_second, 16)).upper())[2:]

    def numbers_mul(self):
        return list(hex(int(self.num_first, 16) * int(self.num_second, 16)).upper())[2:]


def main_1():
    try:
        num_1, num_2 = input('Введите два числа в шестнадцатеричном формате через пробел: ').split()
        result = OperationsNum(num_1, num_2)
        print(f'Сумма чисел {result.numbers_sum()}, поизведение {result.numbers_mul()}')
    except ValueError:
        print('Неверный формат')


# OR


class OperationsNumUpd:
    def __init__(self, num_1, num_2):
        self.num_first = num_1
        self.num_second = num_2

    def __add__(self, other):
        return list(hex(int(self.num_first, 16) + int(self.num_second, 16)).upper())[2:]

    def __mul__(self, other):
        return list(hex(int(self.num_first, 16) * int(self.num_second, 16)).upper())[2:]


def main_2():
    try:
        num_1, num_2 = input('Введите два числа в шестнадцатеричном формате через пробел: ').split()
        result = OperationsNumUpd(num_1, num_2)
        print(f'Сумма чисел {result + result}, поизведение {result * result}')
    except ValueError:
        print('Неверный формат')


if __name__ == '__main__':
    main()
    main_1()
    main_2()
